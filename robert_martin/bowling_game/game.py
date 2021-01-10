class Game:
    def __init__(self):
        self._score = 0

    def add(self, pins):
        self._score += pins

    def score_for_frame(self, frame):
        return 0

    def get_score(self):
        return self._score
