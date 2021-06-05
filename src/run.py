from controllers.fileHandler import FileHandler
from controllers.graphHandler import GraphHandler
from models.rower import Rower
from util.avg import Avg
from util.timer import Timer

rowers = {}

for index in range(4):
    rowers[index] = Rower(index)

rowers[0].setFlip(False)
rowers[1].setFlip(False)
rowers[2].setFlip(False)
rowers[3].setFlip(False)

fileTimer = Timer("File parsing")
fileHandler = FileHandler(rowers)
fileHandler.readFile()
fileTimer.end()

avgTimer = Timer("Calculating avgs")
avg = Avg(rowers)
avg.calcAvgs()
avgTimer.end()

graphTimer = Timer("Graphing")
graphHandler = GraphHandler(rowers)
graphHandler.plot()
graphTimer.end()