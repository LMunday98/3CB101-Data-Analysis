class GraphData:

    def __init__(self, rower, measurement):
        self.rower = rower
        self.measurement = measurement

        self.data = {}
        self.datetimes = []
        self.readings = []
        
    
    def addData(self, reading, datetime):
        if datetime not in self.data:
            self.datetimes.append(datetime)
            self.data[datetime] = []
        self.data[datetime].append(reading)

    def calcAvg(self, flip):
        for datetime in self.datetimes:
            data = self.data[datetime]

            avg = sum(data) / len(data)
            if flip:
                avg = avg * -1
            self.readings.append(avg)

        print("\n\n")
        print("Rower index:", self.rower)
        print("Measurement:", self.measurement)
        print("Len readings:", len(self.readings))
        print("Len datetimes:", len(self.datetimes))

    def getReadings(self):
        return self.readings

    def getDatetimes(self):
        return self.datetimes