from VI.searching_framework import Problem, astar_search


class Puzzle(Problem):
    END_POSITION = "*12345678"

    def __init__(self, initial):
        super().__init__(initial)

    @staticmethod
    def is_move_valid(index_empty, where):
        if where == "right":
            if index_empty % 3 == 2:
                return False
        elif where == "left":
            if index_empty % 3 == 0:
                return False
        elif where == "up":
            if index_empty < 3:
                return False
        elif where == "down":
            if index_empty > 5:
                return False

        return True

    @staticmethod
    def move_empty_slot(state, where):
        index_empty = state.index("*")
        new_state = list(state)

        if not Puzzle.is_move_valid(index_empty, where):
            return None

        if where == "right":
            new_state[index_empty], new_state[index_empty + 1] = new_state[index_empty + 1], new_state[index_empty]
        elif where == "left":
            new_state[index_empty], new_state[index_empty - 1] = new_state[index_empty - 1], new_state[index_empty]
        elif where == "up":
            new_state[index_empty], new_state[index_empty - 3] = new_state[index_empty - 3], new_state[index_empty]
        else:
            new_state[index_empty], new_state[index_empty + 3] = new_state[index_empty + 3], new_state[index_empty]

        return "".join(new_state)

    def goal_test(self, state):
        return state == Puzzle.END_POSITION

    def successor(self, state):
        successors_states = dict()

        new_state = Puzzle.move_empty_slot(state, "left")
        if new_state:
            successors_states["left"] = new_state

        new_state = Puzzle.move_empty_slot(state, "right")
        if new_state:
            successors_states["right"] = new_state

        new_state = Puzzle.move_empty_slot(state, "up")
        if new_state:
            successors_states["up"] = new_state

        new_state = Puzzle.move_empty_slot(state, "down")
        if new_state:
            successors_states["down"] = new_state

        return successors_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    # With number of mismatched tiles
    def h(self, node):
        state = node.state
        correct_position = Puzzle.END_POSITION
        on_incorrect_position = 0

        for index, tile in enumerate(state):
            correct_index = correct_position.index(tile)
            if correct_index != index:
                on_incorrect_position += 1

        return on_incorrect_position


class Puzzle2(Puzzle):

    # With manhattan_distance
    def h(self, node):
        correct_coordinates = {"*": (0, 2), "1": (1, 2), "2": (2, 2), "3": (0, 1), "4": (1, 1), "5": (2, 1),
                               "6": (0, 0), "7": (1, 0), "8": (2, 0)}

        mapper = {"0": (0, 2), "1": (1, 2), "2": (2, 2), "3": (0, 1), "4": (1, 1), "5": (2, 1),
                  "6": (0, 0), "7": (1, 0), "8": (2, 0)}

        state = node.state
        total_distance = 0

        for index, tile in enumerate(state):
            is_on = mapper[str(index)]
            correct_on = correct_coordinates[tile]

            total_distance += manhattan_distance(is_on, correct_on)

        return total_distance


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == '__main__':
    problem = Puzzle("*32415678")
    search = astar_search(problem)
    if search:
        print(search.solution())

    problem2 = Puzzle2("*32415678")
    search2 = astar_search(problem2)
    if search2:
        print(search.solution())
