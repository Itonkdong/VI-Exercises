import math

starting_position = (0, 0)
current_position = list(starting_position)


def move_robot(move):
    distance = int(move[1])
    where = move[0]
    if where == "UP":
        current_position[1] += distance
    elif where == "DOWN":
        current_position[1] -= distance
    elif where == "LEFT":
        current_position[0] -= distance
    elif where == "RIGHT":
        current_position[0] += distance


for i in range(4):
    move = tuple(input().split(" "))
    move_robot(move)

print(current_position)


euclidian_distance = ((starting_position[0] - current_position[0]) ** 2 + (
        starting_position[1] - current_position[1]) ** 2) ** (1 / 2)

manhattan_distance = math.fabs(starting_position[0] - current_position[0]) + math.fabs(
    starting_position[1] - current_position[1])

print("Euclidian Distance from start is")
print(euclidian_distance)
print("Manhattan Distance from start is")
print(manhattan_distance)

