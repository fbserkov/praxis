class Game:
    def __init__(self):
        self._current_throw = 0
        self._throws = 21 * [0]
        self._score = 0

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins

    def score_for_frame(self, frame):
        score, ball = 0, 0
        while frame > 0 and ball < self._current_throw:
            score += self._throws[ball] + self._throws[ball + 1]
            frame -= 1
            ball += 2
        return score

    def get_score(self):
        return self._score
