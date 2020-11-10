class Square:
    side = 1.0

    def __init__(self, side):
        self.side = side

    def setSide(self, insert):
        if insert < 0:
            self.side = 0
        else:
            self.side = insert
