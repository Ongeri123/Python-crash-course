# print('30')
# m = 50
# k = 10

# c =m-k
# print(c)

def FizzBuzz(num):
    result = []
    num = int(num)
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print(*FizzBuzz(50))