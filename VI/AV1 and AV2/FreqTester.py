
line_input = input()
freq = dict()

for word in line_input.split(" "):
    if word in freq:
        freq[word] = freq[word] + 1
        continue
    freq[word] = 1

sorted_list = sorted(freq, key=lambda str1: str1)
for key in sorted_list:
    print(f"{key}:{freq[key]}")
