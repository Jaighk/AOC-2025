import math
import sys

TEST_ANS: int = 4277556


def main() -> None:
    input_file_path: str = get_input_file(mode=sys.argv[1] if len(sys.argv) > 1 else "")
    input: list[str] = [line for line in open(file=input_file_path, mode="r")]
    clean_input(input)
    problem_answers: list[int] = solve_problems(input)
    grand_total: int = sum(problem_answers)

    # Part 1
    print("Part One")
    print(f"Grand Total: {grand_total}")
    print(f"Diff: {TEST_ANS - grand_total}")

    # Part 2
    print("Part Two")
    print(f"{solve_part_two(input)}")


def get_input_file(mode: str) -> str:
    if mode == "puzzle":
        return "./inputs/input.txt"
    else:
        return "./inputs/test.txt"


def clean_input(input: list[str]) -> None:
    for line in input:
        input[input.index(line)] = [item.strip() for item in line.split(" ") if item]


def solve_problems(input: list[str]) -> list[int]:
    answers: list[int] = []
    i: int = 0

    while len(answers) < len(input[0]):
        operator: str = input[-1][i]
        nums: list[str] | list[int] = []

        for col in input[0:-1]:
            nums.append(int(col[i]))

        match operator:
            case "*":
                answers.append(math.prod(nums))
            case "+":
                answers.append(sum(nums))
        i += 1
    return answers


if __name__ == "__main__":
    main()
