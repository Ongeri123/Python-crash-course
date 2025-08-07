import time
import platform
def time_fn(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        diff= end_time - start_time
        txt = f"function:{func.__name__} time taken {diff} seconds"
        f_name='test.txt'
        write_file(f_name, txt)
        return result
    return wrapper

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f'{txt} \n')

# write_file(f_name='test.txt', txt='Hello World')


@time_fn
def counter():
    time.sleep(1)  # Simple test function
    return "Counter finished"

# Call the function to test the decorator
counter()

print(f'machine is',{platform.machine()})

