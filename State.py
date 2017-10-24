from pyatspi.enum import Enum


class Canoe(Enum):
    RIGHT = "right"
    LEFT = "left"

CANNIBAL_NUM = 3
MISSIONARY_NUM = 3
CANNIBAL = 0
MISSIONARY = 1


class State(object):
    def __init__(self, right_margin, left_margin, canoe, father=None):
        self.right_margin = right_margin
        self.left_margin = left_margin
        self.canoe = canoe
        self.father = father

    def isObjective(self):
        if self.left_margin[CANNIBAL] == CANNIBAL_NUM and self.left_margin[MISSIONARY] == MISSIONARY_NUM:
            return True
        return False

    def isEqual(self, other):
        if other is None:
            return False

        if self.canoe == other.canoe and self.right_margin[CANNIBAL] == other.right_margin[CANNIBAL] \
                and self.right_margin[MISSIONARY] == other.right_margin[MISSIONARY]:
            return True
        return False
