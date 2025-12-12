import sys

from AOC-2025.day_8.coords import Coord


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


def get_boxes(input: list[str]):
    global boxes
    for coord in input:
        x, y, z = coord.split(sep=",")
        box = Coord(x, y, z)
        boxes.append(box)


# globals
boxes: list[Coord] = []


def main() -> None:
    global boxes
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line.strip() for line in open(file=input_file_path, mode="r")]

    get_boxes(input)


if __name__ == "__main__":
    main()
