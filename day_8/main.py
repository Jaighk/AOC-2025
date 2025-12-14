import math
import sys


class Coord:
    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.conns: list[Coord] = []

    def __repr__(self):
        string: str = f"""x: {self.x}
y: {self.y}
z: {self.z}
conns: {self.conns}"""
        return string


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


def calculate_distance(point_one: Coord, point_two: Coord) -> float:
    return math.sqrt(
        (point_one.x - point_two.x) ** 2
        + math.sqrt(point_one.y - point_two.y) ** 2
        + math.sqrt(point_one.z - point_two.z) ** 2
    )


# globals
boxes: list[Coord] = []


def main() -> None:
    global boxes
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line.strip() for line in open(file=input_file_path, mode="r")]

    get_boxes(input)


if __name__ == "__main__":
    main()
