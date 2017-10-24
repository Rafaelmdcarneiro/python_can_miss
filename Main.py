from Solver import Solver
from State import State, Canoe, MISSIONARY_NUM, CANNIBAL_NUM


class Main:
    right_margin = [CANNIBAL_NUM, MISSIONARY_NUM]
    left_margin = [0, 0]
    canoe = Canoe.RIGHT

    initialState = State(right_margin, left_margin, canoe)
    Solver().search(initialState)