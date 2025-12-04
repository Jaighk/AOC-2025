import sys

INPUT_FILE = "inputs/input.txt"

def getmax(string: str, maxlen: int) -> str: 
    result = ""
    win_start, win_stop = 0, len(string) - maxlen + 1

    while len(result) < maxlen:
        substring = string[win_start:win_stop]
        win_start += substring.index(max(substring))
        if win_start == win_stop - 1:
            result += string[win_start:]
            break
        result += string[win_start]
        win_start += 1
        win_stop += 1
    return result

def solve(maxlen):
    total = 0
    with open(INPUT_FILE, "r") as f:
        lines = [line.strip() for line in f]
        for line in lines:
            number = getmax(line, maxlen)
            total += int(number)
    print(total)

solve(2)
solve(12)