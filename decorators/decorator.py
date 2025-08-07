# Decorators are a powerful feature in Python that allow you to modify the behavior of functions or methods. They are often used for logging, access control, memoization, and more.
#has to take a function as an argument and return a new function that enhances or modifies the original function's behavior.
def my_deco(func):
     def wrapper():
        print('Before function run')
        func()
        print('Function completed running')
     return wrapper

@my_deco
def hello():
    print('Hello world')

@my_deco
def bye():
    print('Bye world')


hello()
bye()
