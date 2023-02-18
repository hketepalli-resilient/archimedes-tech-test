from dataEnrichers.DefaultDataEnricher import DefaultDataEnricher
from dataReaders.CallDataReader import CallDataReader
from dataReaders.OperatorDataReader import OperatorDataReader
from dataWriters.CsvDataWriter import CsvDataWriter


def main():
    calls = CallDataReader.read_data('data/calls.json')
    operators = OperatorDataReader.read_data('data/operators.json')

    calls_summaries = DefaultDataEnricher.combine_data(calls, operators)

    CsvDataWriter.write(calls_summaries)


if __name__ == "__main__":
    main()
