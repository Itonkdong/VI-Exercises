from VI.searching_framework import Problem, astar_search, manhattan_distance
from VI.AV3.LostPartyMan import LostPartyMan


class LostPartyManInformal(LostPartyMan):

    def h(self, node):
        state = node.state
        man = state[0], state[1]
        house = self.goal
        total_distance = manhattan_distance(man, house)
        return total_distance


if __name__ == '__main__':
    man_position = tuple(map(int, input().split(" ")))
    house_position = tuple(map(int, input().split(" ")))
    lost_party_man_problem = LostPartyManInformal(man_position, house_position)
    search = astar_search(lost_party_man_problem)
    print(search)
    if search:
        print(search.solution())

'''
3 0
1 7
'''
