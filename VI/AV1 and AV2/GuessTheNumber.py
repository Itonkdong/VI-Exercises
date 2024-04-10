def change_boundaries(to, interval):
    if to == "lower":
        interval[1] = (interval[0] + interval[1]) / 2
    elif to == "higher":
        interval[0] = (interval[0] + interval[1]) / 2


def get_middle_number(interval):
    return round((interval[0] + interval[1]) / 2)


current_interval = [0, 1_000_000_000]
print("Zamislete broj")

while True:
    guess = get_middle_number(current_interval)
    print(f"Dali vashiot broj e {guess}?")
    answer = input()
    if answer == "Pogolem":
        change_boundaries("higher", current_interval)
    elif answer == "Pomal":
        change_boundaries("lower", current_interval)
    else:
        print("EZ")
        break


