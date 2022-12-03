ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

shape_points = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


find_winner = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}


find_loser = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}


class Hand:
    def __init__(self, shape):
        self.shape = shape
        self.point = shape_points[shape]

    def __lt__(self, other):
        if self.shape == ROCK:
            if other.shape == SCISSORS:
                return False
            if other.shape == PAPER:
                return True
        if self.shape == SCISSORS:
            if other.shape == ROCK:
                return True
            if other.shape == PAPER:
                return False
        if self.shape == PAPER:
            if other.shape == ROCK:
                return False
            if other.shape == SCISSORS:
                return True
        return False

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.shape == other.shape


opponent_shapes = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

your_shapes = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
# score: shape score + outcome
# outcome score = 0 if lose, 3 for draw, 6 for win

input_lines = open('input.txt').read().splitlines()
total_score = 0


def calculate_score(you, opponent):
    if you < opponent:
        return you.point + 0
    if you == opponent:
        return you.point + 3
    if you > opponent:
        return you.point + 6


def find_your_hand(opponent, result):
    if result == "X":
        return Hand(find_loser[opponent.shape])
    if result == "Y":
        return opponent
    if result == "Z":
        return Hand(find_winner[opponent.shape])


for line in input_lines:
    hands = line.split(" ")
    opponent = Hand(opponent_shapes[hands[0]])
    result = hands[1]
    you = find_your_hand(opponent, result)
    total_score += calculate_score(you, opponent)

print(total_score)
