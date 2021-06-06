import config
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, rowers, labels, measurement, graphOutputDir):
        plt.figure(measurement)

        figure = plt.gcf()
        figure.set_size_inches(config.graphSize['x'], config.graphSize['y'])

        for rowerIndex in config.graphedRowers:
            rower = rowers[rowerIndex]

            rowerGraphData = rower.getGraphData()
            graphData = rowerGraphData[measurement]

            readings = graphData.getReadings()
            datetimes = graphData.getDatetimes()
        
            plt.plot(datetimes, readings, label = rower.getSeat())

        plt.ylabel(measurement + labels["force"] + labels['unit'])
        plt.xlabel('Measurement Time (hh:mm:ss)')
        plt.legend()
        plt.show()
        # for fileFormat in config.graphFormats:
        #     fileName = graphOutputDir + fileFormat + '/' + measurement + '.' + fileFormat
        #     plt.savefig(fileName, dpi=300, format=fileFormat)

        