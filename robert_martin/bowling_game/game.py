class Game:
    def __init__(self):
        self._ball = 0

        self._score = 0
        self._throws = 21 * [0]
        self._current_throw = 0
        self._current_frame = 1
        self._first_throw_in_frame = True

    def adjust_current_frame(self, pins):
        if self._first_throw_in_frame:
            if pins == 10:  # strike
                self._current_frame += 1
            else:
                self._first_throw_in_frame = False
        else:
            self._first_throw_in_frame = True
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
        self._ball = 0
        score = 0
        for _ in range(frame):
            first_throw = self._throws[self._ball]
            self._ball += 1
            if first_throw == 10:
                score += (
                    10 +
                    self._throws[self._ball] +
                    self._throws[self._ball + 1]
                )
            else:
                second_throw = self._throws[self._ball]
                self._ball += 1
                frame_score = first_throw + second_throw
                # spare needs next frames first throw
                if frame_score == 10:
                    score += frame_score + self._throws[self._ball]
                else:
                    score += frame_score
        return score

    def get_score(self):
        return self.score_for_frame(self.get_current_frame() - 1)
