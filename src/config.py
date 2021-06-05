from datetime import datetime

startTime = datetime(2021, 6, 4, 8, 44)
finishTime = datetime(2021, 6, 4, 9, 51)

dataDir = "data/"
inputDir = dataDir + "input/"
outputDir = dataDir + "output/"

flip = {
    0 : True,
    1 : True,
    2 : True,
    3 : False
}

graphedMeasurements = ['sax', 'say', 'saz', 'rx', 'ry']