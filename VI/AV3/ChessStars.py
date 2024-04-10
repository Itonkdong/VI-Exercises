from VI.searching_framework import Problem, breadth_first_graph_search


class ChessStars(Problem):
    horse_moves = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1))
    bishop_moves = ((-1, 1), (1, 1), (-1, -1), (1, -1))
    board_size = (8, 8)

    def __init__(self, horse, bishop, star1, star2, star3):
        goal = {star1: 1, star2: 1, star3: 1}
        self.stars_positions = star1, star2, star3
        initial = (horse, bishop, (1, 1, 1))
        super().__init__(initial, goal)

    @staticmethod
    def is_sate_valid(state):

        horse, bishop = state[0], state[1]
        if horse[0] < 0 or horse[1] < 0:
            return False

        if horse[0] >= ChessStars.board_size[0] or horse[1] >= ChessStars.board_size[1]:
            return False

        if bishop[0] < 0 or bishop[1] < 0:
            return False

        if bishop[0] >= ChessStars.board_size[0] or bishop[1] >= ChessStars.board_size[1]:
            return False

        if bishop == horse:
            return False

        return True

    def move_figure(self, move, state, figure):
        new_state = list(state)

        if figure == "horse":
            new_state[0] = (new_state[0][0] + move[0], new_state[0][1] + move[1])
            moved_figure_position = new_state[0]
        else:
            new_state[1] = (new_state[1][0] + move[0], new_state[1][1] + move[1])
            moved_figure_position = new_state[1]

        if moved_figure_position in self.stars_positions:
            stars_booleans = list(new_state[2])
            stars_booleans[self.stars_positions.index(moved_figure_position)] = 0
            new_state[2] = tuple(stars_booleans)
        return tuple(new_state)

    def successor(self, state):
        successor_states = dict()

        # Horse Moves
        for horse_move in ChessStars.horse_moves:
            new_state = self.move_figure(horse_move, state, "horse")
            if ChessStars.is_sate_valid(new_state):
                successor_states["K" + str(ChessStars.horse_moves.index(horse_move) + 1)] = new_state

        # Bishop Moves
        for bishop_move in ChessStars.bishop_moves:
            new_state = self.move_figure(bishop_move, state, "bishop")
            if ChessStars.is_sate_valid(new_state):
                successor_states["B" + str(ChessStars.bishop_moves.index(bishop_move) + 1)] = new_state

        return successor_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return sum(state[2]) == 0


if __name__ == "__main__":
    star1 = tuple(map(int, input().split(" ")))
    star2 = tuple(map(int, input().split(" ")))
    star3 = tuple(map(int, input().split(" ")))
    horse = tuple(map(int, input().split(" ")))
    bishop = tuple(map(int, input().split(" ")))

    chess_stars_problem = ChessStars(horse, bishop, star1, star2, star3)
    search = breadth_first_graph_search(chess_stars_problem)
    print(search)
    if search:
        print(search.solution())

'''
1 1
4 3
6 6
2 5
5 1
'''
