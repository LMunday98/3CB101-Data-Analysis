class GraphData:

    def __init__(self, rower, measurement):
        self.rower = rower
        self.measurement = measurement

        self.measurementReadings = []
        self.measurementDatetimes = []
    
    def addData(self, reading, datetime):
        self.measurementReadings.append(reading)
        self.measurementDatetimes.append(datetime)

    def getReadings(self):
        return self.measurementReadings

    def getDatetimes(self):
        return self.measurementReadings