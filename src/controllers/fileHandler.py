from os import walk
import json

class FileHandler:
    def __init__(self, rowers):
        self.rowers = rowers
        self.dataRoot = "data/input/"
        _, _, self.inputFiles = next(walk(self.dataRoot))

    def readFile(self):
        dec = json.JSONDecoder()
        pos = 0

        for file in self.inputFiles:
            
            with open(self.dataRoot + file) as f:
                lines = f.readlines()
                
                for line in lines:
                    while not pos == len(str(line))-1:
                        rowerData, json_len = dec.raw_decode(str(line)[pos:])
                        pos += json_len

                        if rowerData["info"]["ip"] == "0.0.0.0":
                            pass

                        rower_index = rowerData["info"]["rower_index"]
                        rower = self.rowers[rower_index]
                        rower.addData(rowerData)
                    pos = 0
                