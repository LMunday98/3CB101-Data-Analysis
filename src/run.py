from controllers.fileHandler import FileHandler
from models.rower import Rower

rowers = {}

for index in range(4):
    rowers[index] = Rower(index)
    
fileHandler = FileHandler(rowers)
fileHandler.readFile()