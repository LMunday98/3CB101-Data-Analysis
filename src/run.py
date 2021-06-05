from controllers.fileHandler import FileHandler
from controllers.graphHandler import GraphHandler
from models.rower import Rower
from util.timer import Timer

rowers = {}

for index in range(4):
    rowers[index] = Rower(index)

fileTimer = Timer("File parsing")
fileHandler = FileHandler(rowers)
fileHandler.readFile()
fileTimer.end()

graphHandler = GraphHandler(rowers)
graphHandler.plot()