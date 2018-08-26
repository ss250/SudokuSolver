from Backtracker import Backtracker
from timeit import default_timer as timer


def test_bad_inputs(bad_puzzle):
    try:
        Backtracker(bad_puzzle)
    except ValueError:
        print("Successfully caught " + str(bad_puzzle))

if __name__ == "__main__":

    # puzzle = Backtracker(
    #    [[8, 5, 0, 0, 0, 2, 4, 0, 0],
    #     [7, 2, 0, 0, 0, 0, 0, 0, 9],
    #     [0, 0, 4, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 7, 0, 0, 2],
    #     [3, 0, 5, 0, 0, 0, 9, 0, 0],
    #     [0, 4, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 0],
    #     [0, 1, 7, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 3, 6, 0, 4, 0]]
    # )

    # puzzle = Backtracker(
    #    [[0, 0, 0, 0, 0, 5, 0, 8, 0],
    #     [0, 0, 0, 6, 0, 1, 0, 4, 3],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 5, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 6, 0, 0, 0],
    #     [3, 0, 0, 0, 0, 0, 0, 0, 5],
    #     [5, 3, 0, 0, 0, 0, 0, 6, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 4],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # )

    # puzzle = Backtracker(
    #    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # )

    start = timer()
    puzzle.solve(debug=True)
    end = timer()
    print(str(puzzle))
    print("Runtime: {:.2f}s".format(end - start))
