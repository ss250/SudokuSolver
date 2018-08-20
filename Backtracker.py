from Sudoku import Sudoku
import math
import time
import sys


class Backtracker(Sudoku):
    """
    Implementation of a backtracking solver for Sudoku.
    """

    def get_constraints(self, row, column, grid=None):
        """
        Gets the set of numbers representing the numbers already
        present in the row, column, and box. Used to determine the
        constraining numbers on a given row and column.

        If no grid is given, the constraints will act on the 
        unsolved puzzle
        """
        check_grid = grid[:] if grid is not None else self.puzzle[:]

        constraints = []

        # slice grid horizontally
        for element in check_grid[row]:
            if element != 0:
                constraints.append(element)

        # slice grid vertically
        vertical_slice = [line[column] for line in check_grid]
        for element in vertical_slice:
            if element != 0:
                constraints.append(element)

        # slice grid blockily
        blockr = int(math.floor(row / 3))
        blockc = int(math.floor(column / 3))
        for i in range(3):
            for j in range(3):
                element = check_grid[blockr*3 + i][blockc*3 + j]
                constraints += [element] if element != 0 else [] 

        return list(set(constraints))

    def is_valid(self, row, column, element, grid=None):
        """ 
        Checks if a given number is valid in the grid given.
        """
        check_grid = grid[:] if grid is not None else self.puzzle[:]
        return element not in self.get_constraints(row, column, grid=check_grid)

    def solve(self, grid=None, debug=False):
        """
        Recursively performs a depth first search for the solution. An example
        of backtracking.

        If this function finds a solution successfully, the solution will be
        saved in self.solution and self.solved will be set to true.

        Cannot determine if there is a solution, I think that's the halting problem.

        If debug is set to true, this function will print out intermediate
        outputs with a small delay so users can observe each step of the 
        depth first search.
        """

        next_grid = grid[:] if grid is not None else self.puzzle[:]

        if(debug):
            print(self.grid_repr(next_grid))
            time.sleep(0.01)

        # check if solved
        if not (any(0 in line for line in next_grid)):
            self.solved = True
            self.solution = next_grid
            return True

        # depth fist search for the solution
        for i, row in enumerate(next_grid):
            for j, element in enumerate(row):
                if element == 0:
                    for attempt in range(1, 10):
                        if self.is_valid(i, j, attempt, grid=next_grid):
                            next_grid[i][j] = attempt
                            if(self.solve(grid=next_grid, debug=debug)):
                                return True
                    else:
                        next_grid[i][j] = 0
                        return False
                        
        # solution not found
        return False