import numpy as np

class Clocks:
    def __init__(self, numBalls):
        self.line_1  = []
        self.line_5  = []
        self.line_60 = []
        self.balls = np.arange(numBalls).tolist()
        self.fullCycles = 0

    def tick(self):
        self.line_1.append(self.balls.pop(0))
        if len(self.line_1) == 5:
            self.line_5.append(self.line_1.pop(-1))
            for i in range(4):
                self.balls.append(self.line_1.pop(-1))
            if len(self.line_5) == 12:
                self.line_60.append(self.line_5.pop(-1))
                for i in range(11):
                    self.balls.append(self.line_5.pop(-1));
                if len(self.line_60) == 12:
                    lastBall = self.line_60.pop(-1)
                    for i in range(11):
                        self.balls.append(self.line_60.pop(-1))
                    self.balls.append(lastBall)
                    self.fullCycles += 1
                    return True
        return False
