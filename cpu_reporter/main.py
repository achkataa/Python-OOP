from cpu_reporter import CPUReporter
from formatter import DiagramFormatter, PlainTextFormatter, formatter
from datetime import timedelta


def main():

    cpu_report = CPUReporter(duration=timedelta(3)).report()
    formatter(PlainTextFormatter(cpu_report))



if __name__ == '__main__':
    main()