#TODO 1
#Create a new class and put there a method for sorting lists of numbers in ascending order
# Example 1) [4, 1, 5, 2] -> [1, 2, 4, 5],
# Example 2) [3, 1, 1, 2] -> [1, 1, 2, 3]

test_data = [4, 1, 5, 2]
test_data2 = [3, 1, 1, 2]
test_data3 = [-3, 1, 111, 23, -12]
test_data4 = [-3, -3, -3, 2, 1, 1, 1]

class SortingHelper:
    def __init__(self, data):
        self.data = data.copy()

    def sort_data(self):
       result = self.data
       result.sort()
       return result

    def find_max(self):
        max_number = self.data[0]
        max_index = 0
        for i in range(0, len(self.data)):
            if self.data[i] > max_number:
                max_number = self.data[i]
                max_index = i
        return (max_number, max_index)

    def sort_data_defined(self):
        result = []
        for i in range(0,len(self.data)):
            max_tuple = self.find_max()
            result.append(max_tuple[0])
            self.data.pop(max_tuple[1])
        return result

    #             return


#Here we test the code
print('Running the test')

sorting_helper = SortingHelper(test_data)
sorting_helper2 = SortingHelper(test_data2)
sorting_helper3 = SortingHelper(test_data3)
sorting_helper4 = SortingHelper(test_data4)
print('Sorting {} desc= {}'.format(test_data, sorting_helper.sort_data_defined()))
print('Sorting {} desc= {}'.format(test_data2, sorting_helper2.sort_data_defined()))
print('Sorting {} desc= {}'.format(test_data3, sorting_helper3.sort_data_defined()))
print('Sorting {} desc= {}'.format(test_data4, sorting_helper4.sort_data_defined()))
# print(test_data)