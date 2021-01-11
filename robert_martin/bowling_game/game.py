from scorer import Scorer


class Game:
    def __init__(self):
        self._current_frame = 0
        self._first_throw_in_frame = True
        self._scorer = Scorer()

    def score(self):
        return self.score_for_frame(self._current_frame)

    def score_for_frame(self, frame):
        return self._scorer.score_for_frame(frame)

    def add(self, pins):
        self._scorer.add_throw(pins)
        self.adjust_current_frame(pins)

    def adjust_current_frame(self, pins):
        if self.last_ball_in_frame(pins):
            self.advance_frame()
        else:
            self._first_throw_in_frame = False

    def last_ball_in_frame(self, pins):
        return self.strike(pins) or not self._first_throw_in_frame

    def strike(self, pins):
        return self._first_throw_in_frame and pins == 10

    def advance_frame(self):
        self._current_frame = min(10, self._current_frame + 1)
