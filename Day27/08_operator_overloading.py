class Score:
    def __init__(self, points):
        self.points = points

    def __add__(self, other):
        return Score(self.points + other.points)


score1 = Score(40)
score2 = Score(50)

total = score1 + score2

print("Total score:", total.points)