import json
import config
from os import walk
from datetime import datetime

class FileHandler:
    def __init__(self, rowers):
        self.rowers = rowers
        self.dataRoot = config.inputDir
        _, _, self.inputFiles = next(walk(self.dataRoot))

        self.start = config.startTime
        self.finish = config.finishTime

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
                            break

                        datetimeString = rowerData["info"]["datetime"]
                        datetimeObj = datetime.strptime(datetimeString, '%d/%m/%y %H:%M:%S')

                        if (self.start < datetimeObj) and (datetimeObj < self.finish):
                            # print(datetimeObj)
                            rower_index = rowerData["info"]["rower_index"]
                            rower = self.rowers[rower_index]
                            rower.addData(rowerData)
                    pos = 0
                