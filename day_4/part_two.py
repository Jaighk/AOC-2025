import sys
from tkinter import W
PAPER: str = "@"
EMPTY: str = "."

def main() -> None:
    file: str = get_file(sys.argv[1])
    input_grid: list[str] = [char for char in [line.strip() for line in open(file=file, mode="r")]]
    grid: Grid = Grid()
    grid.height = len(input_grid)
    grid.width = len(input_grid[0])
    grid.size_grid()

    accessible: int = 0
    removed: int = 0 

    # build cells
    cell_id: int = 0
    for y in range(grid.height):
        for x in range(grid.width):
            # grid.append(build_cell(value=input_grid[y][x], y=y, x=x))
            grid.add_cell(cell=Cell(value=input_grid[y][x], y=y, x=x, id = cell_id))
            cell_id += 1
    
    add_cell_neighbors(grid)
    set_accessible_cells(grid)

    # intial count of accessible cells
    for y in range(grid.height):
        for x in range(grid.width):
            cell: Cell = grid.members[y][x]
            if cell.accessible:
                accessible += 1


    print(grid)
    # remove accessible cells and update the grid
    while grid.has_accessible_cells():
        for y in range(grid.height):
            for x in range(grid.width):
                cell: Cell = grid.members[y][x]
                if cell.accessible:
                    cell.value = EMPTY
                    cell.accessible = False
                    update_neighbors(cell)
                    removed += 1
                    set_accessible_cells(grid)

    print(grid)
    print(f"Accessible: {accessible}")
    print(f"Removed: {removed}")

class Cell:
    def __init__(self, value: str, x: int, y: int, id: int) -> None:
        self.id: int = int()
        self.value: str = value
        self.x: int = x
        self.y: int = y
        self.neighbors: list[Cell] = []
        self.accessible: bool = False
    

    def __repr__(self) -> str:
        return self.value


class Grid:
    def __init__(self) -> None:
        self.members: list[list[Cell]] = []
        self.height: int = int()
        self.width: int = int()

    
    def __repr__(self) -> str:
        return_str: str = ""
        for row in self.members:
            for cell in row: 
                return_str += cell.value
            return_str += "\n"
        return return_str

    
    def size_grid(self) -> None: 
        cell: Cell = Cell("", None, None, None)
        row: list[Cell] = []
        for y in range(self.height):
            for x in range(self.width):
                row.append(cell)
            self.members.append(row)
            row = []

    def has_accessible_cells(self) -> bool: 
        for y in range(self.height):
            for x in range(self.width):
                cell: Cell = self.members[y][x]
                if cell.accessible:
                    return True
        return False


    def add_cell(self, cell: Cell) -> None:
        self.members[cell.y][cell.x] = cell
        
def get_neighbors(grid: Grid, y: int, x: int) -> list[Cell]:
    neighbors: list[Cell] = []

    # get neighbors above
    if y != 0:
        row_above_index= y - 1
        if x != 0:
            neighbors.append(grid.members[row_above_index][x - 1])
        neighbors.append(grid.members[row_above_index][x])
        if x != len(grid.members[y]) - 1:
            neighbors.append(grid.members[row_above_index][x + 1])

    # get neighbors to sides
    if x != 0:
        neighbors.append(grid.members[y][x - 1])
    if x != len(grid.members[y]) - 1:
        neighbors.append(grid.members[y][x + 1])

    # get neighbors below
    if y != len(grid.members) - 1:
        row_below_index = y + 1
        if x != 0:
            neighbors.append(grid.members[row_below_index][x - 1])
        neighbors.append(grid.members[row_below_index][x])
        if x != len(grid.members[y]) - 1:
            neighbors.append(grid.members[row_below_index][x + 1])
    return neighbors

def add_cell_neighbors(grid: Grid) -> None:
    for y in range(grid.height):
        for x in range(grid.width):
            cell: Cell = grid.members[y][x]
            cell.neighbors = get_neighbors(grid=grid, y=cell.y, x=cell.x)


def set_accessible_cells(grid: Grid) -> None:
    for y in range(grid.height):
        for x in range(grid.width):
            cell: Cell = grid.members[y][x]
            if cell.value == PAPER:
                if count_paper_neighbors(cell.neighbors) < 4: 
                    cell.accessible = True
            else:
                cell.accessible = False

            
def count_paper_neighbors(neighbors: list[Cell]) -> int:
    count: int = 0
    for neighbor in neighbors:
        if neighbor.value == PAPER:
            count += 1
    return count


def get_file(mode: str) -> str:
    if mode == "test":
        return "./inputs/test_input.txt"
    if mode == "puzzle":
        return "./inputs/puzzle_input.txt"
    else:
        raise Exception(f"ModeError: Mode {mode} is not valid")


if __name__ == "__main__":
    main()