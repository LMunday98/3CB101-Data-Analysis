from controllers.fileHandler import FileHandler
from controllers.graphHandler import GraphHandler
from models.rower import Rower

rowers = {}

for index in range(4):
    rowers[index] = Rower(index)
    
fileHandler = FileHandler(rowers)
fileHandler.readFile()

graphHandler = GraphHandler(rowers)
graphHandler.plot()