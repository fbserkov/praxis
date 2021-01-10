class Game:
    def __init__(self):
        self._current_frame = 0
        self._current_throw = 0
        self._first_throw = True
        self._throws = 21 * [0]
        self._score = 0

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins
        if self._first_throw:
            self._first_throw = False
            self._current_frame += 1
        else:
            self._first_throw = True

    def get_current_frame(self):
        return self._current_frame

    def score_for_frame(self, frame):
        score, ball = 0, 0
        for _ in range(frame):
            frame_score = self._throws[ball] + self._throws[ball + 1]
            # spare needs next frames first throw
            if frame_score == 10:
                score += frame_score + self._throws[ball + 2]
            else:
                score += frame_score
            ball += 2
        return score

    def get_score(self):
        return self._score
