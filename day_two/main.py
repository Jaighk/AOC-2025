import sys


def main() -> None:
    # collect and clean input
    file: str = sys.argv[1]
    id_ranges: list[str] = [line.split(sep=",") for line in open(file=file, mode="r")][0]
    for string in id_ranges:
        if string == "\n":
            id_ranges.remove(string)
        else:
            id_ranges[id_ranges.index(string)] = string.strip()

    # identify invalid product ids
    invalid_ids: list[int] = get_invalid_ids(id_ranges)
    result: int = calculate_result(ids=invalid_ids)

    # output
    print(f"Test diff: {testing(invalid_ids)}")
    print(f"Result: {result}")


def get_invalid_ids(ranges: list[str]) -> list[int]:
    invalid_ids: list[int] = []

    for r in ranges:
        range_min: int = int(r.split(sep="-")[0])
        range_max: int = int(r.split(sep="-")[1])
        for value in range(range_min, range_max + 1):
            value_string: str = str(value)
            if repeated_sequences(value_string):
                invalid_ids.append(value)
    return invalid_ids


def matches_front_back(id: str) -> bool:
    front: str = id[0:len(id)//2]
    back: str = id[len(id)//2:]
    if front == back:
        return True
    return False


def repeated_sequences(id: str) -> bool:
    possible_sequences: list[str] = get_possible_sequences(id)
    for sequence in possible_sequences:
        if len(id) % len(sequence) != 0:
            continue
        chunked_id: list[str] = [id[i:i + len(sequence)] for i in range(0,len(id),len(sequence))]
        comparison_chunk: str = chunked_id[0]
        comp_checks: list[bool] = []
        for chunk in chunked_id[1:]:
            comp_checks.append((chunk == comparison_chunk))
        if all(comp_checks):
            return True
    return False


def get_possible_sequences(id: str) -> list[str]:
    possible_sequences: list[str] = []
    sequence_length: int = 1
    while sequence_length <= len(id) / 2:
        sequence: str = id[0:sequence_length]
        possible_sequences.append(sequence)
        sequence_length += 1
    return possible_sequences


def calculate_result(ids: list[int]) -> int:
    result: int = 0
    for id in ids:
        result += id
    return result


def testing(ids: list[int]) -> int:
    expected_result: int = 4174379265
    calculated_result: int = calculate_result(ids)
    return expected_result - calculated_result


if __name__ == "__main__":
    main()