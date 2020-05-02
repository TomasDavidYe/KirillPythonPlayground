import pandas as pd

# Create a class for calculating aggregation statistic for a list of items and test it


test_set = [
    {
        'name': 'Kirill',
        'salary': 100000,
        'weekly-sex': 10
    },
    {
        'name': 'Tommy',
        'salary': 200000,
        'weekly-sex': 0
    },
    {
        'name': 'Solo',
        'salary': 0,
        'weekly-sex': 100
    },
    {
        'name': 'Ruzek',
        'salary': 0,
        'weekly-sex': 0
    },
    {
        'name': 'Johny',
        'salary': 50000,
        'weekly-sex': 12
    }

]


class StatisticsHelper:
    def __init__(self, data):
        self.data = data

    def sum(self, column_name):
        result = 0
        for item in self.data:
            result += item[column_name]
        return result

    def print_data(self):
        for item in self.data:
            print(item)


#Here we test the code
print('Running the test')


statistics_helper = StatisticsHelper(test_set)
statistics_helper.print_data()
column_name = 'salary'
print('Sum by {} = {}'.format(column_name, statistics_helper.sum(column_name)))


#TODO
# Implement avg, min, max,

