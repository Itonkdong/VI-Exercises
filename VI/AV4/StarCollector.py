from VI.searching_framework import Problem, breadth_first_graph_search, astar_search, manhattan_distance


class StarCollector(Problem):
    MAPPER = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (3, 0): 4, (0, 1): 5, (1, 1): 6, (2, 1): 7, (3, 1): 8, (0, 2): 9,
              (1, 2): 10, (2, 2): 11, (3, 2): 12, (0, 3): 13, (1, 3): 14, (2, 3): 15, (3, 3): 16}

    MOVES = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0), "dia1": (1, -1), "dia2": (-1, 1)}

    BOARD = (3, 3)

    def __init__(self, man_position):
        stars = ((3, 0), (0, 3))
        edges = (
            (1, 2), (1, 5), (2, 6), (5, 6), (6, 7), (7, 8), (8, 4), (4, 3), (3, 7), (7, 10), (7, 11), (6, 10), (10, 11),
            (10, 9), (9, 13), (13, 14), (14, 10), (11, 12), (12, 16), (15, 16), (11, 15))

        initial = (man_position, edges, stars)
        super().__init__(initial)

    def goal_test(self, state):
        return len(state[-1]) == 0

    def handle_edge(self, new_state: list, start, finish):
        start_vertex = StarCollector.MAPPER[start]
        end_vertex = StarCollector.MAPPER[finish]
        edge1 = start_vertex, end_vertex
        edge2 = end_vertex, start_vertex

        new_state[1] = list(new_state[1])

        if edge1 in new_state[1]:
            new_state[1].remove(edge1)
            new_state[1] = tuple(new_state[1])
            return new_state

        if edge2 in new_state[1]:
            new_state[1].remove(edge2)
            new_state[1] = tuple(new_state[1])
            return new_state

        return None

    def handle_stars(self, new_state):
        new_man_position = new_state[0]
        if new_man_position in new_state[-1]:
            tmp = list(new_state[-1])
            tmp.remove(new_man_position)
            new_state[-1] = tuple(tmp)

    def is_man_position_legal(self, man):
        if man[0] < 0 or man[1] < 0:
            return False

        if man[0] > StarCollector.BOARD[0] or man[1] > StarCollector.BOARD[1]:
            return False

        return True

    def move(self, state, where):
        new_state = list(state)
        man, edges, stars = new_state
        move_to_make = StarCollector.MOVES[where]
        new_position = man[0] + move_to_make[0], man[1] + move_to_make[1]
        new_state[0] = new_position

        if not self.is_man_position_legal(new_position):
            return None

        new_state = self.handle_edge(new_state, man, new_position)
        if not new_state:
            return None

        self.handle_stars(new_state)

        return tuple(new_state)

    def successor(self, state):
        successor_states = dict()

        new_state = self.move(state, "up")
        if new_state:
            successor_states["up"] = new_state

        new_state = self.move(state, "down")
        if new_state:
            successor_states["down"] = new_state

        new_state = self.move(state, "left")
        if new_state:
            successor_states["left"] = new_state

        new_state = self.move(state, "right")
        if new_state:
            successor_states["right"] = new_state

        new_state = self.move(state, "dia1")
        if new_state:
            successor_states["diagonal_bottom"] = new_state

        new_state = self.move(state, "dia2")
        if new_state:
            successor_states["diagonal_top"] = new_state

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


class StarCollectorInformal(StarCollector):

    def h(self, node):
        state = node.state
        man = state[0]

        total_value = 0

        for star in state[-1]:
            total_value += manhattan_distance(man, star)

        return total_value


if __name__ == '__main__':
    problem = StarCollector((1, 1))
    search = breadth_first_graph_search(problem)
    print(search)
    if search:
        print(search.solution())

    problem2 = StarCollectorInformal((1, 1))
    search2 = astar_search(problem2)
    print(search2)
    if search2:
        print(search2.solution())
