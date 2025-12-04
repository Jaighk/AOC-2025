import sys
from tkinter import W

def main() -> None:
    file: str = get_file(sys.argv[1])
    grid: list[str] = [char for char in [line.strip() for line in open(file=file, mode="r")]]
    for row in grid:
        print(row)

    grid_height: int = len(grid)
    grid_width: int = len(grid[0])

    paper: str = "@"
    empty: str = "."
    accessible: int = 0

    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] == empty:
                continue
            neighbors: list[str] = get_neighbors(grid, y, x)
            if neighbors.count(paper) < 4:
                accessible += 1

    print(f"Accessible: {accessible}")
        

def get_neighbors(grid: list[str], y: int, x: int) -> list[str]:
    neighbors: list[str] = []

    # get neighbors above
    if y != 0:
        row_above_index= y - 1
        if x != 0:
            neighbors.append(grid[row_above_index][x - 1])
        neighbors.append(grid[row_above_index][x])
        if x != len(grid[y]) - 1:
            neighbors.append(grid[row_above_index][x + 1])

    # get neighbors to sides
    if x != 0:
        neighbors.append(grid[y][x - 1])
    if x != len(grid[y]) - 1:
        neighbors.append(grid[y][x + 1])

    # get neighbors below
    if y != len(grid) - 1:
        row_below_index = y + 1
        if x != 0:
            neighbors.append(grid[row_below_index][x - 1])
        neighbors.append(grid[row_below_index][x])
        if x != len(grid[y]) - 1:
            neighbors.append(grid[row_below_index][x + 1])
    return neighbors


def get_file(mode: str) -> str:
    if mode == "test":
        return "./inputs/test_input.txt"
    if mode == "puzzle":
        return "./inputs/puzzle_input.txt"
    else:
        raise Exception(f"ModeError: Mode {mode} is not valid")


if __name__ =="__main__":
    main()