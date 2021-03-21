import typing as ty
from backtracker.backtrackable import Backtrackable

def iterative_search(state: Backtrackable) -> ty.Set[Backtrackable]:
    """Given a state, search all nodes that can be reached from the given state
    that are solutions

    :param state: [description]
    :type state: BackTrackable
    :return: [description]
    :rtype: ty.List[Backtrackable]
    """
    backlog: ty.List[Backtrackable] = [state]
    footprints: ty.Dict[Backtrackable, bool] = dict()
    solutions: ty.Set[Backtrackable] = set()

    while len(backlog) > 0:
        current = backlog.pop()

        if not footprints.get(current, False):
            # If the current node is already in the footprints, then do not 
            # search; otherwise, add it to the footprints, and obtain all of its
            # immediate neighbors, some being solutions, and others being 
            # next node(s) to search
            for next in current.next():
                if next.is_solution() and not next in solutions:
                    solutions.add(next)
                elif not footprints.get(next, False):
                    backlog.insert(0, next)
            footprints[current] = True    
    
    return solutions

def recursive_search(state: Backtrackable) -> ty.Set[Backtrackable]:
    """Given a state, search all nodes that can be reached from the given state
    that are solutions

    :param state: [description]
    :type state: Backtrackable
    :return: [description]
    :rtype: ty.Set[Backtrackable]
    """
    if state.is_solution():
        return {state}
    else:
        solutions = set()
        for next in state.next():
            for sub_solution in recursive_search(next):
                solutions.add(sub_solution)
        return solutions
