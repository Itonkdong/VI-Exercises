from VI.searching_framework import Problem, breadth_first_graph_search


class Atoms(Problem):
    barriers = (
        (0, 1), (1, 1), (3, 1), (6, 1), (4, 2), (6, 2), (1, 3), (6, 3), (7, 3), (2, 5), (8, 5), (3, 6), (5, 6), (7, 6))

    board_size = (8, 6)

    def __init__(self, h1, o, h2):
        initial = (h1, o, h2)
        super().__init__(initial)

    def get_other_atoms(self, state, which_not):
        if which_not == 0:
            return state[1], state[2]
        if which_not == 1:
            return state[0], state[2]
        if which_not == 2:
            return state[0], state[1]

    def move_atom(self, state, which, direction):
        new_state = list(state)
        atom = new_state[which]

        move = None
        if direction == "left":
            move = (-1, 0)
        elif direction == "right":
            move = (1, 0)
        elif direction == "up":
            move = (0, 1)
        elif direction == "down":
            move = (0, -1)

        other_atom1, other_atom2 = self.get_other_atoms(state, which)

        previous_atom_position = atom
        new_atom_position = atom

        while True:
            new_atom_position = (previous_atom_position[0] + move[0], previous_atom_position[1] + move[1])

            if self.is_position_legal(other_atom1, other_atom2, new_atom_position):
                previous_atom_position = new_atom_position
            else:
                new_atom_position = previous_atom_position
                break

        if new_atom_position == atom:
            return None

        new_state[which] = new_atom_position

        return tuple(new_state)

    def is_position_legal(self, other_atom1, other_atom2, position):

        if position in Atoms.barriers:
            return False

        if position == other_atom1 or position == other_atom2:
            return False

        if position[0] < 0 or position[1] < 0:
            return False

        if position[0] > Atoms.board_size[0] or position[1] > Atoms.board_size[1]:
            return False

        return True

    def goal_test(self, state):
        atom_h1 = state[0]
        atom_o = state[1]
        atom_h2 = state[2]
        return atom_h1[0] == atom_o[0] - 1 == atom_h2[0] - 2 and atom_h1[1] == atom_o[1] == atom_h2[1]

    def successor(self, state):

        mappings = {0: "H1", 1: "O", 2: "H2"}
        directions = ("up", "down", "left", "right")
        successor_states = dict()

        for i in range(3):
            for direction in directions:
                new_state = self.move_atom(state, i, direction)
                if new_state is not None:
                    successor_states[direction.capitalize() + mappings[i]] = new_state

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    h1 = tuple(map(int, input().split(" ")))
    o = tuple(map(int, input().split(" ")))
    h2 = tuple(map(int, input().split(" ")))
    atoms_problems = Atoms(h1, o, h2)
    search = breadth_first_graph_search(atoms_problems)
    print(search)
    if search:
        print(search.solution())
'''
2 1
7 2
2 6
'''
