import unittest

from dataEnrichers.DefaultDataEnricher import DefaultDataEnricher


class MyTestCase(unittest.TestCase):

    def test_something(self):
        DefaultDataEnricher.combine_data([], {})


if __name__ == '__main__':
    unittest.main()
