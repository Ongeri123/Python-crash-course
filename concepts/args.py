#Args = arguments

def greet(*args):
    for value in args:
        print('Name is ', value)

greet('Kev', 'John', 'Alice')
greet(123, True, None,[1,2,3])



def add(*args):
    ans = 0
    for value in args:
        print(f'{ans}= {ans} + {value}')
        ans = ans + value

    print('Answer is', ans)
    return ans

add(2,3)