from sets import Set

from Fifo import Fifo
from Node import Node
from State import State, CANNIBAL, MISSIONARY, CANNIBAL_NUM, MISSIONARY_NUM, Canoe


class Solver:
    checked = Set()

    def search(self, initial_state):
        fifo = Fifo()
        root = Node(initial_state)
        fifo.enqueue(root)

        while not fifo.isEmpty():
            node = fifo.dequeue()
            self.checked.add(node.state)
            if node.state.isObjective():
                self.printResult(self.findRootState(node.state))
                return

            sons = self.action(node.state)
            for son in sons:
                if not self.isAlreadyChecked(son) and not fifo.contains(son):
                    son_node = Node(son)
                    fifo.enqueue(son_node)

        print "No result"

    def action(self, current_state):
        expansions = []
        if current_state.canoe == Canoe.RIGHT:
            state = self.sendTwoCannibalsToTheLeft(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneCannibalToTheLeft(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendTwoMissionariesToTheLeft(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneMissionaryToTheLeft(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneFromEachToTheLeft(current_state)
            if self.isValidState(state):
                expansions.append(state)
        else:
            state = self.sendTwoCannibalsToTheRight(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneCannibalToTheRight(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendTwoMissionariesToTheRight(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneMissionaryToTheRight(current_state)
            if self.isValidState(state):
                expansions.append(state)
            state = self.sendOneFromEachToTheRight(current_state)
            if self.isValidState(state):
                expansions.append(state)
        return expansions

    @staticmethod
    def sendTwoCannibalsToTheLeft(current_state):
        m_dir = [current_state.right_margin[CANNIBAL] - 2, current_state.right_margin[MISSIONARY]]
        m_esq = [current_state.left_margin[CANNIBAL] + 2, current_state.left_margin[MISSIONARY]]
        estado_expandido = State(m_dir, m_esq, Canoe.LEFT, current_state)
        return estado_expandido

    def sendOneCannibalToTheLeft(self, current_state):
        m_dir = [current_state.right_margin[CANNIBAL] - 1, current_state.right_margin[MISSIONARY]]
        m_esq = [current_state.left_margin[CANNIBAL] + 1, current_state.left_margin[MISSIONARY]]
        estado_expandido = State(m_dir, m_esq, Canoe.LEFT, current_state)
        return estado_expandido

    def sendTwoMissionariesToTheLeft(self, current_state):
        m_dir = [current_state.right_margin[CANNIBAL], current_state.right_margin[MISSIONARY] - 2]
        m_esq = [current_state.left_margin[CANNIBAL], current_state.left_margin[MISSIONARY] + 2]
        estado_expandido = State(m_dir, m_esq, Canoe.LEFT, current_state)
        return estado_expandido

    def sendOneMissionaryToTheLeft(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL], estado_atual.right_margin[MISSIONARY] - 1]
        m_esq = [estado_atual.left_margin[CANNIBAL], estado_atual.left_margin[MISSIONARY] + 1]
        estado_expandido = State(m_dir, m_esq, Canoe.LEFT, estado_atual)
        return estado_expandido

    def sendOneFromEachToTheLeft(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL] - 1, estado_atual.right_margin[MISSIONARY] - 1]
        m_esq = [estado_atual.left_margin[CANNIBAL] + 1, estado_atual.left_margin[MISSIONARY] + 1]
        estado_expandido = State(m_dir, m_esq, Canoe.LEFT, estado_atual)
        return estado_expandido

    def sendTwoCannibalsToTheRight(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL] + 2, estado_atual.right_margin[MISSIONARY]]
        m_esq = [estado_atual.left_margin[CANNIBAL] - 2, estado_atual.left_margin[MISSIONARY]]
        estado_expandido = State(m_dir, m_esq, Canoe.RIGHT, estado_atual)
        return estado_expandido

    def sendOneCannibalToTheRight(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL] + 1, estado_atual.right_margin[MISSIONARY]]
        m_esq = [estado_atual.left_margin[CANNIBAL] - 1, estado_atual.left_margin[MISSIONARY]]
        estado_expandido = State(m_dir, m_esq, Canoe.RIGHT, estado_atual)
        return estado_expandido

    def sendTwoMissionariesToTheRight(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL], estado_atual.right_margin[MISSIONARY] + 2]
        m_esq = [estado_atual.left_margin[CANNIBAL], estado_atual.left_margin[MISSIONARY] - 2]
        estado_expandido = State(m_dir, m_esq, Canoe.RIGHT, estado_atual)
        return estado_expandido

    def sendOneMissionaryToTheRight(self, estado_atual):
        m_dir = [estado_atual.right_margin[CANNIBAL], estado_atual.right_margin[MISSIONARY] + 1]
        m_esq = [estado_atual.left_margin[CANNIBAL], estado_atual.left_margin[MISSIONARY] - 1]
        estado_expandido = State(m_dir, m_esq, Canoe.RIGHT, estado_atual)
        return estado_expandido

    def sendOneFromEachToTheRight(self, current_state):
        m_dir = [current_state.right_margin[CANNIBAL] + 1, current_state.right_margin[MISSIONARY] + 1]
        m_esq = [current_state.left_margin[CANNIBAL] - 1, current_state.left_margin[MISSIONARY] - 1]
        estado_expandido = State(m_dir, m_esq, Canoe.RIGHT, current_state)
        return estado_expandido

    def isValidState(self, state):
        if 0 <= state.right_margin[CANNIBAL] <= CANNIBAL_NUM and 0 <= state.right_margin[MISSIONARY] <= MISSIONARY_NUM \
                and 0 <= state.left_margin[CANNIBAL] <= CANNIBAL_NUM and 0 <= state.left_margin[MISSIONARY] <= MISSIONARY_NUM \
                and (state.right_margin[MISSIONARY] == 0 or state.right_margin[CANNIBAL] <= state.right_margin[
                    MISSIONARY]) \
                and (state.left_margin[MISSIONARY] == 0 or state.left_margin[CANNIBAL] <= state.left_margin[
                    MISSIONARY]):
            return True
        return False

    def isAlreadyChecked(self, state):
        for check in self.checked:
            if state.isEqual(check):
                return True
        return False

    def printResult(self, solution):
        for state in solution:
            print "C = %d |     | %d = Cannibal" % (state.left_margin[CANNIBAL], state.right_margin[CANNIBAL])
            if state.canoe == Canoe.RIGHT:
                print "      |   ->|    "
            else:
                print "      |<-   |    "
            print "M = %d |     | %d = Missionary" % (state.left_margin[MISSIONARY], state.right_margin[MISSIONARY])
            print "---------------------"

    def findRootState(self, node_objective):
        solution = []
        while node_objective.father is not None:
            solution.insert(0, node_objective)
            node_objective = node_objective.father

        # insert root
        solution.insert(0, node_objective)
        return solution
