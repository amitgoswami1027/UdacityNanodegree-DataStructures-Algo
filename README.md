# Udacity NanoDegree DataStructures & Algorithms
## Python Basics
### Python Generators
A generator in Python is similar to a function except instead of returning a value and exiting a process, a generator will pause the process, saving its state for next time. The biggest difference between a function and generator from a code perspective is one word: return is changed to yield.

A generator becomes very useful when dealing with very large collections of data that you don’t want to store in memory all at once. It’s also very useful for dealing with extremely large or even infinite series.

Below is an example of how to use a generator to print even numbers. Printing all even numbers at once would take an infinite amount of time, but the generator allows the process to pause, and go back to creating even numbers when needed.

To create the next successive even number simply call next() on the generator object, and it will yield the next iteration. After yield is called, everything in the state of the generator function freezes, and the value is returned. When the generator is called again with next(), it picks back up right where it stopped at yield from before.
```
## Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

## Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

## Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

## Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))
```
