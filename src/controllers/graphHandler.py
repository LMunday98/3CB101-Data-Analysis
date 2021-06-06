import config
# import matplotlib.pyplot as plt

from models.graph import Graph
from util.timer import Timer
from util.dir import Dir
from datetime import datetime

class GraphHandler:

    def __init__(self, rowers):
        self.rowers = rowers
        self.graphMeasurements = config.graphedMeasurements
        self.saveTime = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        self.outputDir = config.outputDir + str(self.saveTime) + '/'

    def plot(self):
        Dir().createDir(self.outputDir)

        for fileFormat in config.graphFormats:
            Dir().createDir(self.outputDir + fileFormat + '/')

        for measurement in self.graphMeasurements:
            measurementTimer = Timer("Plotting " + measurement)
            labels = self.getLabel(measurement)
            Graph(self.rowers, labels, measurement, self.outputDir)
            measurementTimer.end()

    def getLabel(self, measurement):
        rotations = ['gx', 'gy', 'gz', 'sgx', 'sgy', 'sgz', 'rx', 'ry']

        if measurement in rotations:
            return {
                'force' : ' Rotation',
                'unit' : ' (°)'
            }
        else:
            return {
                'force' : ' Acceleration',
                'unit' : ' (m/s^2)'
            }