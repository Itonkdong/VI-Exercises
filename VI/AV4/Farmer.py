from VI.searching_framework import Problem, astar_search, breadth_first_graph_search


class Farmer(Problem):
    GOAL = ("w", "w", "w", "w")
    ENTITY_INDEX = {"farmer": 0, "wolf": 1, "goat": 2, "cab": 3}

    def __init__(self, initial):
        # (farmer, wolf, goat, cabbage)
        # Ex. w ,w ,e, e
        super().__init__(initial)

    def change_direction(self, direction):
        if direction == 'w':
            return "e"

        return "w"

    def is_state_valid(self, new_state):
        wolf = Farmer.ENTITY_INDEX["wolf"]
        goat = Farmer.ENTITY_INDEX["goat"]
        farmer = Farmer.ENTITY_INDEX["farmer"]
        cab = Farmer.ENTITY_INDEX["cab"]

        if new_state[goat] == new_state[cab] and new_state[goat] != new_state[farmer]:
            return False

        if new_state[wolf] == new_state[goat] and new_state[goat] != new_state[farmer]:
            return False

        return True

    def travel(self, state, who):
        new_state = list(state)

        farmer = Farmer.ENTITY_INDEX["farmer"]
        traveller = Farmer.ENTITY_INDEX[who]

        if state[farmer] != state[traveller]:
            return None

        new_side = self.change_direction(new_state[farmer])
        new_state[farmer] = new_side
        new_state[traveller] = new_side

        if not self.is_state_valid(new_state):
            return None

        return tuple(new_state)

    def successor(self, state):

        successor_states = dict()

        new_state = self.travel(state, "farmer")
        if new_state:
            successor_states["farmer_carries_farmer"] = new_state

        new_state = self.travel(state, "goat")
        if new_state:
            successor_states["farmer_carries_goat"] = new_state

        new_state = self.travel(state, "wolf")
        if new_state:
            successor_states["farmer_carries_wolf"] = new_state

        new_state = self.travel(state, "cab")
        if new_state:
            successor_states["farmer_carries_cabbage"] = new_state

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == Farmer.GOAL

    def h(self, node):
        state = node.state

        value = 0
        for position in state:
            if position == "e":
                value += 1

        return value


if __name__ == '__main__':
    problem = Farmer(("e", "e", "e", "e"))
    search = astar_search(problem)
    if search:
        print(search.solution())
