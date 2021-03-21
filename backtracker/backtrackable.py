from abc import ABC, abstractmethod
import typing as ty

class Backtrackable(ABC):
    @abstractmethod
    def is_solution(self) -> bool:
        """Return True if and only if the current state itself is a solution
        """
        raise NotImplementedError("Backtrackable.is_solution not implemented")

    @abstractmethod
    def next(self):
        """This method can either explicitly return an iterable of Backtrackable 
        instances, or be implemented as a generator using 'yield' if specifying 
        all possible next states can be expensive or if you don't care about
        finding all solutions
        """
        raise NotImplementedError("Backtrackable.next not implemented")
    
    @abstractmethod 
    def __hash__(self) -> int:
        """The hash of the Backtrackable state, which is used for detecting 
        duplicate states in tracking footprint"""
        raise NotImplementedError("Backtrackable.__hash__ not implemented")

    def __eq__(self, other) -> bool:
        """Two Backtrackable instances are equal iff their hashes are the same
        """
        return self.__hash__() == other.__hash__()
    