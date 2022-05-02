# 1. Pass function to argument
def my_func(func):
    return func

def my_argument_func():
    return 'Hello My func!'

result = my_func(my_argument_func)
print(result())


# 2. map
numbers = [0, 9, 99]

def plus_one(number):
    return number + 1

print(list(map(plus_one, numbers)))
