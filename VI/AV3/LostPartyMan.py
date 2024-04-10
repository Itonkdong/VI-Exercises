from VI.searching_framework import Problem, breadth_first_graph_search


class LostPartyMan(Problem):

    def __init__(self, man_position, house_position):
        block1 = (0, -1)
        block2 = (5, 1)
        self.block1_j = 2
        self.block2_j = 5
        self.dimensions = (5, 7)
        initial_state = (
            man_position[0], man_position[1], block1[0], block1[1], block2[0],
            block2[1])
        super().__init__(initial_state, house_position)

    def hande_crates(self, state):
        block1_i = state[2]
        block1_direction = state[3]
        block2_i = state[4]
        block2_direction = state[5]

        if block1_i == 5 and block1_direction == -1:
            block1_i = 4
            block1_direction = 1
        elif block1_i == 0 and block1_direction == 1:
            block1_i = 1
            block1_direction = -1
        elif block1_direction == 1:
            block1_i -= 1
        else:
            block1_i += 1

        if block2_i == 5 and block2_direction == -1:
            block2_i = 4
            block2_direction = 1
        elif block2_i == 0 and block2_direction == 1:
            block2_i = 1
            block2_direction = -1
        elif block2_direction == 1:
            block2_i -= 1
        else:
            block2_i += 1

        new_state = [state[0], state[1], block1_i, block1_direction, block2_i, block2_direction]

        return new_state

    def move_man(self, state, direction):

        new_state = list(state)
        new_state = self.hande_crates(new_state)

        if direction == "left":
            new_state[1] -= 1
        elif direction == "right":
            new_state[1] += 1
        elif direction == "up":
            new_state[0] -= 1
        else:
            new_state[0] += 1

        # Check if the player is in a legal position
        if new_state[0] < 0 or new_state[0] > self.dimensions[0]:
            return None
        if new_state[1] < 0 or new_state[1] > self.dimensions[1]:
            return None

        # Check if the player and the crate have crashed
        if new_state[0] == new_state[2] and new_state[1] == self.block1_j:
            return None
        if new_state[0] == new_state[4] and new_state[1] == self.block2_j:
            return None

        return tuple(new_state)

    def goal_test(self, state):
        house = tuple(state[0:2])
        return self.goal == house

    def successor(self, state):

        successor_states = dict()

        new_state = self.move_man(state, "right")
        if new_state:
            successor_states["Right"] = new_state

        new_state = self.move_man(state, "left")
        if new_state:
            successor_states["Left"] = new_state

        new_state = self.move_man(state, "up")
        if new_state:
            successor_states["Up"] = new_state

        new_state = self.move_man(state, "down")
        if new_state:
            successor_states["Down"] = new_state

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    man_position = tuple(map(int, input().split(" ")))
    house_position = tuple(map(int, input().split(" ")))
    lost_party_man_problem = LostPartyMan(man_position, house_position)
    search = breadth_first_graph_search(lost_party_man_problem)
    print(search)
    if search:
        print(search.solution())

'''
2 0
1 7
'''
