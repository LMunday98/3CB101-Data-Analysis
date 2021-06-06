from datetime import datetime

stroke = 0
stroke2 = 1
bow2 = 2
bow = 3

startTime = datetime(2021, 6, 4, 8, 44)
finishTime = datetime(2021, 6, 4, 9, 51)

dataDir = "data/"
inputDir = dataDir + "input/"
outputDir = dataDir + "output/"

flip = {
    stroke : True,
    stroke2 : True,
    bow2 : True,
    bow : False
}


graphedRowers = [stroke, stroke2, bow2, bow]
# graphedMeasurements = ['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'sgx', 'sgy', 'sgz', 'sax', 'say', 'saz', 'rx', 'ry']
graphedMeasurements = ['say']
graphFormats = ['png', 'svg']
graphSize = {
    'x' : 128,
    'y' : 40
}