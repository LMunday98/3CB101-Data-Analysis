from os import walk

class FileHandler:
    def __init__(self):
        self.dataRoot = "data/input/"
        _, _, self.inputFiles = next(walk(self.dataRoot))

    def readFile(self):
        for file in self.inputFiles:
            with open(self.dataRoot + file) as f:
                content = f.readlines()
                print(content)