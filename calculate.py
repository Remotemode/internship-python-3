import numpy as np

class Clocks:
    def __init__(self, numBalls):
        self.line_1  = []
        self.line_5  = []
        self.line_60 = []
        self.balls = np.arange(numBalls).tolist()
        self.fullCycles = 0
