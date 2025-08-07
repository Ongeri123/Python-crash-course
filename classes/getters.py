#getters and setters are used to access and modify private attributes of a class
# they are used to encapsulate the data and provide a controlled interface for accessing and modifying it

from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f'{txt} \n')

class Human():

    def __init__(self,gender,name,):
        print('initializer was called')
        # print(gender)
        # print(name)
        self.gender = gender
        self.name = name
        if self.gender == 'male':
            self.ribs =24
        else:
            self.ribs = 22
    @property
    def get_name(self):
        now = datetime.now()
        print('current date and time',now)
        write_file(f_name='log.txt', txt =f'at{now} got name from adam')
        return self.name


adam=Human(name = 'Adam', gender = 'male')

print(adam.get_name)
print()
