# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


#TODO Implement in this skeleton


class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name



class RecentlyUsedList:
    def __init__(self, n):
        self.entities = []
        self.length = n

    #TODO Implement
    def record(self, entity: Entity):
        if len(self.entities) < self.length:
            self.entities.append(entity)
        else:
            self.entities.pop(0)
            self.entities.append(entity)
        pass

    #TODO Implement
    def get_last(self, i):
        if i > len(self.entities):
            print('You are fucking knedlik, i should be lower than n')
        else:
            print('Id = {}, Name = {}'.format(self.entities[-i].id, self.entities[-i].name))
        pass



list = RecentlyUsedList(2)
a = Entity(1, 'A')
b = Entity(2, 'B')
c = Entity(3, 'C')

print(a)

#EXAMPLE
# list.record(a)
# list.record(b)
# list.record(c)
# list.record(b)
# list.record(a)

# x = list.get_last(1) # -> x should be a
# y = list.get_last(2) # -> y should be b
# z = list.get_last(3) # -> should throw an error
