from VI.searching_framework import astar_search
from VI.AV3.Atoms import Atoms


class AtomsInformal(Atoms):
    def h(self, node):
        state = node.state
        h1 = state[0]
        o = state[1]
        h2 = state[2]
        value = 0

        if h1[0] == o[0] - 1:
            if h1[1] != o[1]:
                value += 1
        elif h1[0] < o[0] - 1:
            if h1[1] != o[1]:
                value += 2
            else:
                value += 1
        elif h1[0] == o[0]:
            value += 2
        elif h1[0] > o[0]:
            if h1[1] == o[1]:
                value += 3
            else:
                value += 2

        #######################

        if h2[0] == o[0] + 1:
            if h1[1] != o[1]:
                value += 1
        elif h2[0] > o[0] + 1:
            if h1[1] != o[1]:
                value += 2
            else:
                value += 1
        elif h2[0] == o[0]:
            value += 2
        elif h2[0] < o[0]:
            if h2[1] == o[1]:
                value += 3
            else:
                value += 2

        if h1[0] - 1 == o[0] == h2[0] + 1:
            if h1[1] == h2[1]:
                if h1[1] < o[1] or h1[1] > o[1]:
                    value = 1
        return value


if __name__ == '__main__':
    problem = AtomsInformal((2, 1), (7, 2), (2, 6))
    search = astar_search(problem)
    if search:
        print(search.solution())
