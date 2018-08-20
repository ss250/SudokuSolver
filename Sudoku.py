
class Sudoku(object):
    """
    Base class for various Sudoku solvers. Implements the Constructor, representation 
    and a pretty print method.
    """

    def __init__(self, puzzle):
        """
        Constructer expects a 2 dimensional array of 9x9, representing the 
        grid of numbers that make up a Sudoku puzzle. 0  will be treated as 
        empty boxes to be solved.
        """
        if not isinstance(puzzle, list):
            raise ValueError("Input must be a 2d list.")

        if len(puzzle) != 9:
            raise ValueError("Input must have 9 columns.")

        for row in puzzle:
            if not isinstance(row, list):
                raise ValueError("Input must be a 2d list.")

            if len(row) != 9:
                raise ValueError("Each row must have 9 elements.")

            for element in row:
                if type(element) is not int:
                    raise ValueError("All elements must an integer between 0 and 9.")

                if element < 0 or element > 9: 
                    raise ValueError("All elements must be between 0 and 9.")


        self.puzzle = puzzle
        self.solution = None
        self.solved = False

    def solve(self):
        """
        To be implemented by child classes
        """
        pass

    def grid_repr(self, grid):
        """
        Pretty prints a string of the 2d array provided.
        """
        output = ""

        for i, row in enumerate(self. puzzle):

            if (i % 3) == 0:
                output += "-------------------\n"

            for k, element in enumerate(row):
                if (k % 3) == 0:
                    output += "|"
                    
                output += str(element) if element != 0 else " "

                if ((k + 1) % 3) != 0:
                    output += " "

            output += "|\n"

        output += "-------------------\n"

        return output

    def __repr__(self):
        """
        If puzzle has already been solved, print solution. 
        Otherwise print the unsolved puzzle
        """
        return self.grid_repr(self.solution) if self.solved else self.grid_repr(self.puzzle)