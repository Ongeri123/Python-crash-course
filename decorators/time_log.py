# time log is a concept that represents a record of time spent on tasks or activities.
# It can be used to track work hours, project progress, or personal time management.
# In Python, you can implement a time log using decorators to measure the execution time of 
import time
def time_fn(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        diff= end_time - start_time
        print('Time taken to run',diff)
    return wrapper

@time_fn
def my_fn():
    for i in range(1, 20):
        print(i)
    
my_fn() 
