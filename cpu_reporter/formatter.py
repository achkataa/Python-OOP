import matplotlib.pyplot as plt

def formatter(type):
    type.format()


class Formatter:
    def __init__(self, report):
        self.report = report

    def format(self):
        pass


class PlainTextFormatter(Formatter):
    def format(self):
        print('\n'.join(([time.strftime("%H:%M:%S") + ' ' + str(measurement) for time, measurement in self.report])))


class DiagramFormatter(Formatter):
    def format(self):
        time = [time.strftime("%H:%M:%S.%f") for time, _ in self.report]
        measurements = [measurement for _, measurement in self.report]

        plt.plot(time, measurements, color='red', marker='o')
        plt.title('CPU Load', fontsize=14)
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Load', fontsize=14)
        plt.grid(True)
        plt.show()



