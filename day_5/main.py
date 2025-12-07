import sys


def main() -> None:
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line for line in open(file=input_file_path, mode="r")]
    ranges, ingredients = parse_input(input)
    print("----- Part One -----")
    print(f"Fresh: {count_fresh(ranges, ingredients)}")

    print("----- Part Two -----")
    sort_ranges(ranges)
    correct_overlaps(ranges)
    print(f"Count Fresh IDs: {count_fresh_ids(ranges)}")


def parse_input(input: list[str]) -> tuple[list[list[int]], list[int]]:
    ranges: list[list[int]] = []
    ingredients: list[int] = []
    for line in input:
        line: str = line.strip()
        if "-" in line:
            range_params = line.split(sep="-")
            range: list[int] = [int(range_params[0]), int(range_params[1])]
            ranges.append(range)
        if len(line) > 0 and "-" not in line:
            ingredients.append(int(line))
    return ranges, ingredients


def count_fresh(ranges: list[list[int]], ingredients: list[int]) -> int:
    count: int = 0
    found_fresh: list[int] = []
    for ingredient in ingredients:
        for id_range in ranges:
            if ingredient in found_fresh:
                continue
            range_min: int = id_range[0]
            range_max: int = id_range[1]
            if int(ingredient) in range(range_min, range_max + 1):
                found_fresh.append(ingredient)
                count += 1
    return count


def sort_ranges(ranges: list[list[int]]) -> None:
    ranges.sort(key=lambda r: (r[0], r[1]))


def correct_overlaps(ranges: list[list[int]]) -> None:
    i: int = 0
    while i < len(ranges):
        range_one = ranges[i]
        j = i + 1
        while j < len(ranges):
            range_two = ranges[j]
            if range_two[0] <= range_one[1]:
                range_one = [range_one[0], max(range_one[1], range_two[1])]
                ranges[i] = range_one
                del ranges[j]
            else:
                break
        i += 1


def count_fresh_ids(ranges: list[list[int]]) -> int:
    count: int = 0
    for range in ranges:
        ids = range[1] - range[0] + 1
        count += ids
    return count


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


if __name__ == "__main__":
    main()
