class Scorer:
    def __init__(self):
        self._throws = 21 * [0]
        self._current_throw = 0
        self._ball = 0

    def add_throw(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1

    def score_for_frame(self, frame):
        self._ball = 0
        score = 0
        for _ in range(frame):
            if self.strike():
                score += 10 + self.next_two_balls_for_strike()
                self._ball += 1
            elif self.spare():
                score += 10 + self.next_ball_for_spare()
                self._ball += 2
            else:
                score += self.two_balls_in_frame()
                self._ball += 2
        return score

    def strike(self):
        return self._throws[self._ball] == 10

    def spare(self):
        return self._throws[self._ball] + self._throws[self._ball + 1] == 10

    def next_two_balls_for_strike(self):
        return self._throws[self._ball + 1] + self._throws[self._ball + 2]

    def next_ball_for_spare(self):
        return self._throws[self._ball + 2]

    def two_balls_in_frame(self):
        return self._throws[self._ball] + self._throws[self._ball + 1]
