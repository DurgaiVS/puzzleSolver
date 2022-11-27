import numpy
from grids import *


# to check whether the puzzle is all filled out
def is_filled(grid: list[list[int]]) -> bool:
    if not grid:
        return False
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False

    return True


# to check whether the number will fit in the specified position
def validator(grid: list[list[int]], row: int, col: int, val: int) -> bool:
    for i in range(9):
        if grid[row][i] == val:
            return False
        elif grid[i][col] == val:
            return False

    startSqRow = (row // 3) * 3
    startSqCol = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[startSqRow+i][startSqCol+j] == val:
                return False

    return True


# will find an empty space in the puzzle
def finder(grid: list[list[int]]) -> tuple:
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)


# puzzle solver recursively
def solver(grid: list[list[int]]) -> list[list[int]]:
    if is_filled(grid):  # checking whether the grid is all filled
        return grid

    row, col = finder(grid)  # finding the next empty space

    for val in range(1, 10):
        if validator(grid, row, col, val):  # validating the value at the position
            grid[row][col] = val
            ret_val = solver(grid)  # recursion call
            if ret_val:  # checking whether the returned value is a true value
                return ret_val

            # if the execution have reached this area, this means the above condition is not met
            # so the above grid is a deadend
            # so undoing the value inserted
            grid[row][col] = 0

    # returning false if there is no possible solution
    return False


def main():
    # printing the output grid in a matrix form using numpy
    print(numpy.matrix(solver(grid)))


if __name__ == "__main__":
    main()
