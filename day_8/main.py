import cmath
import sys


class Coord:
    def __init__(self, x, y, z):
        self.x: int = int(x)
        self.y: int = int(y)
        self.z: int = int(z)
        self.conns: list[Coord] = []

    def __repr__(self):
        string: str = f"""x: {self.x}
y: {self.y}
z: {self.z}
conns: {self.conns}"""
        return string


# globals
boxes: list[Coord] = []


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


def calculate_distance(point_one: Coord, point_two: Coord):
    # delta_x: float = point_one.x - point_two.x
    # delta_y: float = point_one.y - point_two.y
    # delta_z: float = point_one.z - point_two.z

    return cmath.sqrt(
        abs(
            (point_one.x - point_two.x) ** 2
            + (point_one.y - point_two.y) ** 2
            + (point_one.z - point_two.z) ** 2
        )
    )


def main() -> None:
    global boxes
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line.strip() for line in open(file=input_file_path, mode="r")]

    get_boxes(input)
    for i in range(len(boxes)):
        if i != len(boxes) - 1:
            print(f"Distance: {calculate_distance(boxes[i], boxes[i + 1])}")


if __name__ == "__main__":
    main()
