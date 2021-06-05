class Avg:

    def __init__(self, rowers):
        self.rowers = rowers

    def calcAvgs(self):
        for rowerIndex in self.rowers:
            rower = self.rowers[rowerIndex]
            rower.calcAvgData()