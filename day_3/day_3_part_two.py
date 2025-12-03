import sys

def main() -> None:
    args: list[str] = sys.argv
    mode: str = args[1]
    file: str = get_file(mode)

    banks: list[str] = [line.strip() for line in open(file=file, mode="r")]
    total_output_joltage: int = 0

    for bank in banks:
        max_joltage: int = get_joltage(bank)
        total_output_joltage += max_joltage

    print(f"Total output joltage: {total_output_joltage}")

        

def get_joltage(bank: str) -> int:
    tens_position: str = ""
    tens_index: int = None
    ones_position: str = ""

    # Find highest batter from bank
    for battery in bank[:-1]:
        if not tens_position:
            tens_position = battery
            tens_index = bank.index(battery)
            continue
        if int(battery) > int(tens_position):
            tens_position = battery
            tens_index = bank.index(battery)

    # Find highest battery to the right of the highest battery
    for battery in bank[tens_index+1:]:
        if not ones_position:
            ones_position = battery
            continue
        if int(battery) > int(ones_position):
            ones_position = battery
    return int(tens_position + ones_position)



def get_file(mode:str) -> str:
    file: str = str()
    if not mode:
        print("Mode not specified")
    if mode == "test":
        file: str = "./inputs/test.txt"
    if mode == "puzzle":
        file: str = "./inputs/input.txt"
    return file

if __name__ == "__main__":
    main()