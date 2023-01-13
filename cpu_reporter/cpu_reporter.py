import psutil
from datetime import datetime, timedelta

class Reporter:
    def __init__(self, duration):
        self.duration = duration
        self.measurements = []

    def report(self):
        pass


class CPUReporter(Reporter):
    def report(self):
        finish = datetime.now() + timedelta(seconds=3)
        while datetime.now() < finish:
            percentage = psutil.cpu_percent(0.3)
            self.measurements.append((datetime.now(), percentage))
        return self.measurements
