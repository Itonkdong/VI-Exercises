class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def __str__(self):
        return f"Currently on {self.x}, {self.y}"


agent1 = Agent(0,0)
agent1.move_down()
agent1.move_down()
agent1.move_left()
agent1.move_right()
agent1.move_up()
print(agent1)
