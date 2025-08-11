# static is a property that should not change

from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f'{txt} \n')

class Human():

    species = 'H.sapiens'
    genus = 'Homo'
    count = 0

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
        
        # Human.count = Human.count +1
        self.__class__.count = self.__class__.count +1

    @property
    def get_name(self):
        now = datetime.now()
        print('current date and time',now)
        write_file(f_name='log.txt', txt =f'at{now} got name from adam')
        return self.name

    @classmethod
    def get_general_info(cls):
        print('Species',cls.species)
        print('Species',cls.genus)
        print('Species', cls.count)


adam=Human(name = 'Adam', gender = 'male')
eve = Human(name = 'Eve', gender= 'female')

# print('adam species', adam.species)
# print('eve species', eve.species)
# print('Total Humans', Human.count)
Human.get_general_info()
eve.get_general_info()