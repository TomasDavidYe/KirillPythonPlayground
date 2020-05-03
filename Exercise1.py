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
        'salary': -10000,
        'weekly-sex': 100
    },
    {
        'name': 'Ruzek',
        'salary': -200000,
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

    def avg(self, column_name):
        result = self.sum(column_name)
        result = result / len(self.data)
        return result

    def max(self, column_name):
        result = self.data[0][column_name]
        for item in self.data:
            if item[column_name] > result:
                result = item[column_name]
        return result

    def min(self, column_name):
        result = self.data[0][column_name]
        for item in self.data:
            if item[column_name] < result:
                result = item[column_name]
        return result

    def person_min(self, column_name):
        result = self.data[0]
        for item in self.data:
            if item[column_name] < result[column_name]:
                result = item
        return result['name']

    def person_max(self, column_name):
        result = self.data[0]
        for item in self.data:
            if item[column_name] > result[column_name]:
                result = item
        return result['name']

    def find_higher_than(self, column_name, value):
        result = []
        for item in self.data:
            if item[column_name] > value:
                result.append(item)
        return result



#Here we test the code
print('Running the test')


statistics_helper = StatisticsHelper(test_set)
statistics_helper.print_data()
column_name = 'salary'
value = 10000
print('Sum by {} = {}'.format(column_name, statistics_helper.sum(column_name)))
print('Avg by {} = {}'.format(column_name, statistics_helper.avg(column_name)))
print('Max by {} = {}'.format(column_name, statistics_helper.max(column_name)))
print('Min by {} = {}'.format(column_name, statistics_helper.min(column_name)))
print('Person with Min by {} = {}'.format(column_name, statistics_helper.person_min(column_name)))
print('Person with Max by {} = {}'.format(column_name, statistics_helper.person_max(column_name)))
print('Person with {} higher than {} = {}'.format(column_name, value, statistics_helper.find_higher_than(column_name,value)))



#TODO
# Implement avg, min, max,

#TODO 2
# Implement a function which, given a column name, returns a name of the person with the min / max value

#TODO 3
# Given column name and a value return a subset of the test collection such that each item in the subcollection has its value
# higher than the given value

