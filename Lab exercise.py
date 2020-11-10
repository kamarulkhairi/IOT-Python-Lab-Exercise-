class Square:
    side = 1.0

    def setSide(self):
        if self < 0:
            self.side = 0
        else:
            self.side = self