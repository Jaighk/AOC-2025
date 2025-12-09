import sys
from collections import defaultdict


START: str = "S"
SPACE: str = "."
SPLITTER: str = "^"
BEAM: str = "|"
split_count: int = 0
beam_locations: list[int] = []


def main() -> None:
    global split_count
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] | list[list[str]] = [
        line for line in open(file=input_file_path, mode="r")
    ]
    for string in range(len(input)):
        input[string] = list(input[string].strip())
    
    beams = {input[0].index("S"): 1}

    for i in range(1, len(input)): 
        line = input[i]
        new_beams = defaultdict(int)
        for k, v in beams.items():
            if line[k] == SPACE:
                new_beams[k] += v
            else:
                split_count += 1
                new_beams[k - 1] += v
                new_beams[k + 1] += v
        beams = new_beams

    print(f"{split_count = }")
    print(f"{sum(beams.values())}")



def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


if __name__ == "__main__":
    main()
