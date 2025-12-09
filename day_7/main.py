import sys

START: str = "S"
SPACE: str = "."
SPLIT: str = "^"
BEAM: str = "|"
SPLIT_COUNT: int = 0
BEAM_LOCATIONS: list[int] = []


def main() -> None:
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] | list[list[str]] = [
        line for line in open(file=input_file_path, mode="r")
    ]
    for string in range(len(input)):
        input[string] = list(input[string].strip())

    run_manifold(input)
    print("----- Part One -----")
    print(f"Split count: {SPLIT_COUNT}")


def run_manifold(input: list[list[str]]) -> None:
    global SPLIT_COUNT
    print("\n")
    for i in range(len(input)):
        print(BEAM_LOCATIONS)
        if i == 0:
            start: int = input[i].index("S")
            BEAM_LOCATIONS.append(start)
            continue
        for location in BEAM_LOCATIONS:
            if input[i][location] == SPACE:
                input[i][location] = BEAM
            if input[i][location] == SPLIT:
                print(f"splitting at location: {location}")
                BEAM_LOCATIONS.remove(location)
                if location not in (0, len(input[i])):
                    possible_locations: list[int] = [location - 1, location + 1]
                if location == 0:
                    possible_locations = [location + 1]
                if location == len(input[i]):
                    possible_locations = [location - 1]
                while possible_locations:
                    print(f"{possible_locations = }")
                    new_beam: int = possible_locations.pop()
                    if input[i][new_beam] == SPACE:
                        print(f"new beams at: {new_beam}")
                        input[i][new_beam] = BEAM
                        BEAM_LOCATIONS.append(new_beam)
                SPLIT_COUNT += 1

    for i in input:
        print("".join(i))


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


if __name__ == "__main__":
    main()
