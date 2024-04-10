from VI.searching_framework import Problem, breadth_first_graph_search


class Beaker(Problem):

    def __init__(self, initial, goal, capacity):
        super().__init__(initial, goal)
        self.capacity = capacity

    def spil(self, state, which):
        if state[which] == 0:
            return None

        tmp = list(state)
        tmp[which] -= 1
        return tuple(tmp)

    def pour(self, state, _form, to):
        if state[to] + 1 > self.capacity[to]:
            return None

        if self.initial[_form] == 0:
            return None

        tmp = list(state)
        tmp[_form] -= 1
        tmp[to] += 1
        return tuple(tmp)

    def successor(self, state):
        successor_states = dict()

        state1 = self.pour(state, 0, 1)
        if state1: successor_states["From_0_to_1"] = state1

        state2 = self.pour(state, 1, 0)
        if state2: successor_states["From_1_to_0"] = state2

        state3 = self.spil(state, 0)
        if state3: successor_states["Empty_0"] = state3

        state4 = self.spil(state, 1)
        if state4: successor_states["Empty_1"] = state4

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        successor_states = self.successor(state)
        if action in successor_states:
            return successor_states[action]

        return None


if __name__ == '__main__':
    max_capacities = tuple(map(int, input().split(" ")))
    goal_state = tuple(map(int, input().split(" ")))
    initial_state = tuple(map(int, input().split(" ")))
    beaker_problem = Beaker(initial_state, goal_state, max_capacities)
    search = breadth_first_graph_search(beaker_problem)
    print(search)
    if search:
        print(search.solution())
        print(search.solve())
