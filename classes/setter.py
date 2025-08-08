# set is to update 
from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f'{txt} \n')

class Human():

    def __init__(self,gender,name,):
        print('initializer was called')
        # print(gender)
        # print(name)
        self._gender = gender
        self._name = name
        if self._gender == 'male':
            self._ribs =24
        else:
            self.ribs = 22

    @property
    def name(self):
        now = datetime.now()
        print('current date and time',now)
        write_file(f_name='log.txt', txt =f'at{now} got name from adam')
        return self._name

    @name.setter
    def name(self, new_name):
        now = datetime.now()
        print('current date and time',now)
        write_file(f_name='log.txt', txt =f'at{now} set name to {new_name} from {self._name}')
        self._name = new_name



adam=Human(name = 'Adam', gender = 'male')

adam.name= 'eric'

