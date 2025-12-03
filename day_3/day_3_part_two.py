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
    batteries_required = 12
    enabled_batteries: str = ""

    # Find highest battery from bank with enough room for all the batteries
    first_battery, first_battery_index = get_first_battery(bank, batteries_required=batteries_required)
    enabled_batteries += first_battery
    enabled_batteries += get_rest_of_batteries(bank[first_battery_index:], batteries_required=batteries_required)
    return int(enabled_batteries)


def get_first_battery(bank: str, batteries_required: int) -> tuple[str, int]:
    first_battery: str = str()
    first_battery_index: int = int()

    # find the highest battery that still leaves room for the other 11
    for battery in bank[:-batteries_required]:
        if not first_battery:
            first_battery = battery
            first_battery_index = bank.index(battery)
            continue
        if int(battery) > int(first_battery):
            first_battery = battery
            first_battery_index = bank.index(battery)

    return first_battery, first_battery_index


def get_rest_of_batteries(battery_pool: str, batteries_required: int, ) -> str:
    remaining_batteries: list[str] = [battery for battery in battery_pool]
    to_turn_off: int = len(battery_pool) - batteries_required

    for i in range(to_turn_off):
        lowest: str = remaining_batteries[0]
        for battery in remaining_batteries[1:]:
            if int(battery) < int(lowest):
                lowest = battery
        remaining_batteries.remove(lowest)
    return "".join(remaining_batteries)


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