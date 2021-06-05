class GraphHandler:

    def __init__(self, rowers):
        self.rowers = rowers
        self.graphMeasurement = ['rx']

    def plot(self):
        for rowerIndex in self.rowers:
            rower = self.rowers[rowerIndex]
            graphData = rower.getGraphData()
            print(graphData['rx'])