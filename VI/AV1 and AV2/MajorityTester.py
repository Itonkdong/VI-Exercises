def majority_vote(votes):
    if not votes:
        return None

    freq = {}
    total_votes = len(votes)
    for vote in votes:
        if vote in freq:
            freq[vote] += 1
            continue
        freq[vote] = 1

    most_freq = max(freq.items(), key=lambda item: item[1])
    if most_freq[1] / total_votes < 0.5:
        return None
    return most_freq[0]


result1 = majority_vote(["A", "A", "B"])
result2 = majority_vote(["A", "A", "A", "B", "C", "A"])
result3 = majority_vote(["A", "B", "B", "A", "C", "C"])
result4 = majority_vote([])
print(result1)
print(result2)
print(result3)
print(result4)



