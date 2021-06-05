import config
from models.graphData import GraphData

class Rower:
    def __init__(self, rower_index):
        self.rower_index = rower_index
        self.seat = self.getSeatName(rower_index)
        self.flip = False
        self.measurements = config.graphedMeasurements
        self.graphData = {}

        self.setup()

    def setup(self):
        for measurement in self.measurements:
            self.graphData[measurement] = GraphData(self.rower_index, measurement)

    def addData(self, data):
        for measurement in self.measurements:
            measurementReading = data["data"][measurement]
            measurementDatetime = data["info"]["datetime"]

            self.graphData[measurement].addData(measurementReading, measurementDatetime)

    def getData(self):
        return self.graphData

    def getSeatName(self, rower_index):
        seats = {
            0 : "Stroke",
            1 : "Stroke 2",
            2 : "Bow 2",
            3 : "Bow"
        }

        return seats[rower_index]

    def getIndex(self):
        return self.rower_index

    def getSeat(self):
        return self.seat

    def getGraphData(self):
        return self.graphData

    def calcAvgData(self):
        for measurementIndex in self.measurements:
            self.graphData[measurementIndex].calcAvg(self.flip)

    def setFlip(self, flip):
        self.flip = flip