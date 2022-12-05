from collections import Counter


with open("day2_rock_paper_scissors/input.txt") as f:
    lines = f.read().splitlines()

matches = [tuple(el.split(" ")) for el in lines]
print(matches)

MAPPING_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

MAPPING_SIGNALS = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "rock",
    "Y": "paper",
    "Z": "scissor",
}


def match(hand1, hand2):
    points = 0
    points += MAPPING_POINTS[hand2]
    if MAPPING_SIGNALS[hand1] == MAPPING_SIGNALS[hand2]:
        return points + 3
    elif MAPPING_SIGNALS[hand2] == "rock" and MAPPING_SIGNALS[hand1] == "scissor":
        return points + 6
    elif MAPPING_SIGNALS[hand2] == "paper" and MAPPING_SIGNALS[hand1] == "rock":
        return points + 6
    elif MAPPING_SIGNALS[hand2] == "scissor" and MAPPING_SIGNALS[hand1] == "paper":
        return points + 6
    return points


c = Counter(matches)
print(c)

# part 1
outcome = [match(e[0], e[1]) for e in matches]
print(sum(outcome))

# part 2
MAPPING_POINTS_2 = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}


def match2(opponent_hand, strategy):
    points = 0
    if strategy == "X":
        if MAPPING_SIGNALS[opponent_hand] == "rock":
            return MAPPING_POINTS_2["scissor"]
        elif MAPPING_SIGNALS[opponent_hand] == "paper":
            return MAPPING_POINTS_2["rock"]
        elif MAPPING_SIGNALS[opponent_hand] == "scissor":
            return MAPPING_POINTS_2["paper"]
    if strategy == "Y":
        return MAPPING_POINTS_2[MAPPING_SIGNALS[opponent_hand]] + 3
    if strategy == "Z":
        if MAPPING_SIGNALS[opponent_hand] == "rock":
            return MAPPING_POINTS_2["paper"] + 6
        elif MAPPING_SIGNALS[opponent_hand] == "paper":
            return MAPPING_POINTS_2["scissor"] + 6
        elif MAPPING_SIGNALS[opponent_hand] == "scissor":
            return MAPPING_POINTS_2["rock"] + 6


outcome = [match2(e[0], e[1]) for e in matches]
print(sum(outcome))
