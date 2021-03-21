import typing as ty
from backtracker.backtrackable import Backtrackable

class NQueens(Backtrackable):
    @staticmethod 
    def is_safe(qs, nq) -> bool:
        """Return true if and only if the next queen is safe against all 
        existing queens
        
        qs is short for queens, and nq is short for next queen"""
        for q in qs:
            h = q[0] == nq[0]
            v = q[1] == nq[1]
            pd = (nq[1] - q[1]) == (nq[0] - q[0])
            nd = (q[1] - nq[1]) == (nq[0] - q[0])

            if any([h, v, pd, nd]):
                return False
        
        return True

    def __init__(self, n: int, queens: ty.Tuple[ty.Tuple[int, int]]):
        """The state of the N Queens problem consists of the size of the board
        and the current set of queens on the board.
        The queens coordinates need to be sorted for hashing"""
        self.n = n 

        queens = list(queens)
        queens.sort(key=lambda q: q[0] * n + q[1])
        self.queens = tuple(queens)

    def is_solution(self) -> bool:
        """The current state is a solution iff there are as many queens as 
        the problem size"""
        return len(self.queens) == self.n

    def next(self) -> "NQueens":
        """ Iterate through all positions on the board, each time checking if 
        the current position is a safe spot, and if yes, return a new 
        NQueens object with the safe spot added to the set of queens
        """
        for i in range(self.n):
            for j in range(self.n):
                next_queen = (i, j)
                if NQueens.is_safe(self.queens, next_queen):
                    yield NQueens(
                        self.n, tuple([q for q in self.queens] + [next_queen]))

    def __hash__(self) -> int:
        return hash(
            (self.__class__.__name__, self.n, self.queens))

    def __str__(self) -> str:
        return f"<NQueens queens={self.queens}>"
