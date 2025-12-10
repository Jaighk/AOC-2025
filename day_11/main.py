import sys

def main() -> None:
    input_file_path: str = get_input_file(mode = sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line for line in open(file=input_file_path, mode="r")]


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


if __name__ == "__main__":
    main()
