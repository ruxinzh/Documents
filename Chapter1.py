# python cookbook 
# Chapter 1: Data Structures and Algorithms

# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.
p = (4,5)
x,y = p
x #4
y #5

data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date = data
name #ACME
date #(2012,12,21)

name,shares,price,(year,mon,day) = data
name #ACME
year #2012
mon #12
day #21

# discard certain value
_,shares,price,_ = data
shares #50
price #91.1

# *Python “star expressions” can be used to “too many values to unpack”
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

#recursive algorithm 
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [1, 10, 7, 4, 5, 9]
print(sum(items))

# keeping a limited history is a perfect use for a collections.deque

# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# 1.6 Mapping Keys to Multiple Values in a Dictionary
# A dictionary is a mapping where each key is mapped to a single value
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}