import matplotlib.pyplot as plt

class GraphHandler:

    def __init__(self, rowers):
        self.rowers = rowers
        self.graphMeasurement = ['rx']

    def plot(self):
        for rowerIndex in self.rowers:
            rower = self.rowers[rowerIndex]
            rowerGraphData = rower.getGraphData()
            
            graphData = rowerGraphData['rx']

            readings = graphData.getReadings()
            datetimes = graphData.getDatetimes()

            plt.plot(datetimes, readings)
            plt.show()

            break