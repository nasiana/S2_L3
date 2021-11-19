'''
EXERCISE 1
Create a @timer decorator. It will measure how long the decorated function takes to execute and print the
duration to the console.
'''

# Starter pack

import time


## Finished 'worker_function_numbers' in 0.00008740 secs

def timer(func):
    # KEY: *args, **kwargs to be passed as arguments to the inner function otherwise this will not work
    def inner(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time() - t1
        print("Finished {} in {} secs".format(func.__name__, t2))
        # KEY: the func(*args, **kwargs) must be returned otherwise the code will not behave as expected, the program
        # will not remember the function to be able to return a value to the user
        # KEY: func(*args, **kwargs) must be returned as this actually executes the function rather than than simply
        # func which will simply return a function
        return func(*args, **kwargs)

    return inner

# Your code here

@timer
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i / 2 + 5) for i in range(1000)])
    return total_sum

@timer
def worker_function_strings(word):
    print("going for a nap.. 😴")
    time.sleep(3)
    new_word = ''
    for char in word:
        new_word = new_word + ''.join('ZZZ-' + char + '-ZZZ-')
    return new_word.rstrip('-')


print(worker_function_numbers(1))
print(worker_function_numbers(80))

print(worker_function_strings('supercalifragilisticexpialidocious'))

'''
Exercise 2 - Remember, why dontcha?
We didn't have enough time to do this in the session so Hassan ran through it
'''

import time

class MemoizeDecorator:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("I did not run a function, just fetched a result for you! :)")
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


@MemoizeDecorator
def worker_function_numbers(num):
    time.sleep(1)
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


## run worker function many times with different arguments

for i in range(5):
    print(worker_function_numbers(i))

print(worker_function_numbers.cache)
#
## run again to see check a value was cached
print(worker_function_numbers(3))