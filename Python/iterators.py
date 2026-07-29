# Iteration: The process of going through a sequence of elements, typically one by one, to perform some operation on each element.

#  Iterators: Iterator is an object that allows programmers to traverse through sequance of data without having to store the entire sequence in memory. It provides a way to access elements of a collection one at a time, without exposing the underlying representation of the collection.

#  Iterables: An iterable is an object that can return an iterator. In Python, an object is considered iterable if it implements the __iter__() method, which returns an iterator object. Common examples of iterables include lists, tuples, strings, and dictionaries.

import sys

l = [ x for x in range(100000) ]  # This is a list comprehension that creates a list of numbers from 0 to 9

print(sys.getsizeof(l))  # This will return the size of the list in bytes, which is 800112 bytes for a list of 100000 integers

X = range(100000)  # This is a range object that generates numbers from 0 to 99999

print(sys.getsizeof(X))  # This will return the size of the range object in bytes, which is 48 bytes for a range of 100000 integers

L = [1,2,3]

print(type(L))  # This is Iterable, which is a list object

print(type(iter(L)))  # This is an Iterator, which is a list_iterator object

#  Every iterator is also an iterable, but not every iterable is an iterator. An iterator is an object that implements the __next__() method, which returns the next item in the sequence. When there are no more items to return, it raises a StopIteration exception.

#  Every Iterable have Iter function
#  Every Iterator have Iter and __next__ function 

# How For Loop works in Python:

Num = [1,2,3]

# for i in Num:
#     print(i)  # This will print each element in the list Num one by one

# internally, the for loop uses the iter() function to get an iterator from the iterable (Num in this case) and then repeatedly calls the __next__() method on the iterator to get each element until a StopIteration exception is raised.

# step 1:
iterator = iter(Num)  # This creates an iterator object from the iterable Num

# Step 2:
print(next(iterator))  # This will print the first element in the iterator, which is 1
print(next(iterator))  # This will print the second element in the iterator, which is 2
print(next(iterator))  # This will print the third element in the iterator, which is 3
# print(next(iterator))  # This will raise a StopIteration exception, as there are no more elements in the iterator

#  Creating a own for loop

def my_for_loop(iterable):
    iterator = iter(iterable)  # Get an iterator from the iterable
    while True:
        try:
            item = next(iterator)  # Get the next item from the iterator
            print(item)  # Perform some operation on the item (in this case, print it)
        except StopIteration:
            break  # Exit the loop when there are no more items


my_for_loop([1, 2, 3])  # This will print each element in the list one by one

#  Own range function

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        else:
            current_value = self.iterable.start
            self.iterable.start += 1
            return current_value

for i in MyRange(1, 5):
    print(i)  # This will print numbers from 1 to 4, one by one