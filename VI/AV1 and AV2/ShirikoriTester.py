class Shiritori:
    __LOSE_MESSAGE = "Game over"
    __RESTART_MESSAGE = "Game restarted"

    def __init__(self):
        self.words = []
        self.__game_over = False

    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words

        if word in self.words:
            self.__game_over = True
            return self.__class__.__LOSE_MESSAGE

        last_word = self.words[-1]
        if last_word[-1] != word[0]:
            self.__game_over = True
            return self.__class__.__LOSE_MESSAGE

        self.words.append(word)
        return self.words

    def restart(self):
        self.words = []
        self.__game_over = False
        return self.__class__.__RESTART_MESSAGE


#TEST CASES
my_shiritori = Shiritori()

print(my_shiritori.play("apple"))
print(my_shiritori.play("ear"))
print(my_shiritori.play("rhino"))
print(my_shiritori.play("corn"))

print(my_shiritori.words)
print(my_shiritori.restart())
print(my_shiritori.words)

print(my_shiritori.play("hostess"))
print(my_shiritori.play("stash"))
print(my_shiritori.play("hostess"))
