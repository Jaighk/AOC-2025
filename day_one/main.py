import sys

# get input
input_file: str = sys.argv[1]
input: list[str] = []
with open(file=input_file, mode="r") as file:
    file_lines = file.readlines()
    file.close()
input = [line.strip() for line in file_lines]

position = 50
part1 = 0
part2 = 0

for line in input:
    direction = line[0]
    distance = int(line[1:])

    for _ in range(distance):
        if direction == "L":
            position = (position-1+100)%100
        else:
            position = (position+1)%100
        if position == 0:
            part2 += 1
    if position == 0:
        part1 += 1

print(f"{part1 = }")
print(f"{part2 = }")
