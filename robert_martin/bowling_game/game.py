class Game:
    def __init__(self):
        self._current_frame = 1
        self._current_throw = 0
        self._first_throw = True
        self._throws = 21 * [0]
        self._score = 0

    def adjust_current_frame(self, pins):
        if self._first_throw:
            if pins == 10:  # strike
                self._current_frame += 1
            else:
                self._first_throw = False
        else:
            self._first_throw = True
            self._current_frame += 1
        self._current_frame = min(11, self._current_frame)

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins
        self.adjust_current_frame(pins)

    def get_current_frame(self):
        return self._current_frame

    def score_for_frame(self, frame):
        score, ball = 0, 0
        for _ in range(frame):
            first_throw = self._throws[ball]
            ball += 1
            if first_throw == 10:
                score += 10 + self._throws[ball] + self._throws[ball + 1]
            else:
                second_throw = self._throws[ball]
                ball += 1
                frame_score = first_throw + second_throw
                # spare needs next frames first throw
                if frame_score == 10:
                    score += frame_score + self._throws[ball]
                else:
                    score += frame_score
        return score

    def get_score(self):
        return self.score_for_frame(self.get_current_frame() - 1)
