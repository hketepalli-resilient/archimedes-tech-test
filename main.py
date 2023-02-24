from data_enrichers.DefaultDataEnricher import DefaultDataEnricher
from data_readers.CallDataReader import CallDataReader
from data_readers.OperatorDataReader import OperatorDataReader
from data_writers.CsvDataWriter import CsvDataWriter


def main():
    calls = CallDataReader.read_data('data/calls.json')
    operators = OperatorDataReader.read_data('data/operators.json')

    calls_summaries = DefaultDataEnricher.combine_data(calls, operators)

    CsvDataWriter.write(calls_summaries)


if __name__ == "__main__":
    main()
