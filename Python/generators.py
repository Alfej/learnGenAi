#  Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example of a generator function that yields numbers from 0 to n-1 is shown below:
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return MyRangeIterator(self)

# class MyRangeIterator:

#     def __init__(self, iterable):
#         self.iterable = iterable

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.iterable.start >= self.iterable.end:
#             raise StopIteration
#         else:
#             current_value = self.iterable.start
#             self.iterable.start += 1
#             return current_value

# for i in MyRange(1, 5):
#     print(i)

def gen_demo():
    for i in range(3):
        yield i  # This will yield numbers from 0 to 2, one by one

x = gen_demo()
print(next(x))  # This will print the first value yielded by the generator
print(next(x))  # This will print the second value yielded by the generator
print(next(x))  # This will print the third value yielded by the generator
# print(next(x))  # This will raise a StopIteration exception, as there are no more values to yield

#  Difference between normal function and generator function
#  A normal function returns a single value and then terminates, while a generator function can yield multiple values over time, pausing and resuming execution between each yield.

#  custom range function using generator
def my_range(start, end):
    current = start
    while current < end:
        yield current  # Yield the current value
        current += 1  # Increment the current value

for i in my_range(1, 5):
    print(i)  # This will print numbers from 1 to 4, one by one


# Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets. For example, the following generator expression yields the squares of numbers from 0 to 4:
squares = (x**2 for x in range(5))  # This creates a generator that yields squares of numbers from 0 to 4
for square in squares:
    print(square)  # This will print the squares of numbers from 0 to 4, one by one


