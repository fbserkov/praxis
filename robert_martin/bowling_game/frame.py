class Frame:
    def __init__(self):
        self._score = 0

    def add(self, pins):
        self._score += pins

    def get_score(self):
        return self._score
