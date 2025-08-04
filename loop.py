# for ,while , do_while loops
to_loop= True
i = 5

while to_loop:
    if i > 10:
        to_loop = False
    print('i is', i)
    i = i + 1

for i in range(20, 10, -3):
    print('For loop is', i)
