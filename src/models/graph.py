import config
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, rowers, labels, measurement, graphOutputDir, fileFormats):
        plt.figure(measurement)

        for rowerIndex in rowers:
            rower = rowers[rowerIndex]

            rowerGraphData = rower.getGraphData()
            graphData = rowerGraphData[measurement]

            readings = graphData.getReadings()
            datetimes = graphData.getDatetimes()
        
            plt.plot(datetimes, readings, label = rower.getSeat())

        
        
        plt.ylabel(measurement + labels["force"] + labels['unit'])
        plt.xlabel('Measurement Date Time (hh:mm:ss)')
        plt.legend()
        # plt.show()
        for fileFormat in fileFormats:
            fileName = graphOutputDir + measurement + '.' + fileFormat
            plt.savefig(fileName, dpi=300, format=fileFormat)

        