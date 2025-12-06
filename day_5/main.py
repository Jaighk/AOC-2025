from re import A
import sys

def main() -> None:
    input_file_path: str = get_input_file(mode = sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line for line in open(file=input_file_path, mode="r")]
    ranges, ingredients = parse_input(input)
    print(f"Fresh: {count_fresh(ranges, ingredients)}")
    print(f"Total Fresh IDs: {count_fresh_ids(ranges)}")


def parse_input(input: list[str]) -> tuple[list[str], list[str]]:
    ranges: list[str] = []
    ingredients: list[str] = []
    for line in input:
        line: str = line.strip()
        if "-" in line:
            ranges.append(line)
        if len(line) > 0 and "-" not in line:
            ingredients.append(line)

    return ranges, ingredients


def count_fresh(ranges: list[str], ingredients: list[str]) -> int:
    count: int = 0
    found_fresh: list[str] = []
    for ingredient in ingredients:
        for id_range in ranges:
            if ingredient in found_fresh: 
                continue
            range_min: int = int(id_range.split(sep="-")[0])
            range_max: int = int(id_range.split(sep="-")[1])
            if int(ingredient) in range(range_min, range_max + 1):
                found_fresh.append(ingredient)
                count += 1
    return count


def count_fresh_ids(ranges: list[str]) -> int:
    counted: list[int] = []
    for id_range in ranges: 
        range_min: int = int(id_range.split(sep="-")[0])
        range_max: int = int(id_range.split(sep="-")[1])
        for id in range(range_min, range_max + 1):
            if id not in counted:
                counted.append(id)
    return len(counted)


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


if __name__ == "__main__":
    main()
