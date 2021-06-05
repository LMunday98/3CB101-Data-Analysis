import os
import config

class Dir:

    def __init__(self):
        self.mode = 0o777
        self.createDir(config.outputDir)


    def createDir(self, path):
        try: 
            os.makedirs(os.path.join(path), self.mode)
        except OSError as error:
            print(error)