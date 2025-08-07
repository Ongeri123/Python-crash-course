# initializer is a special method in python classes that is called when an object of that class is created. It is used to initialize the attributes of the object with some default values or with the values passed as arguments during object creation.

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
            

    def  another_one(self):
        print('another one was called')


adam = Human(name= 'Adam', gender= 'male')
# adam.__init__()

# adam.another_one()
adam = Human(name= 'Adam', gender= 'male')
print ('name:', adam.name)
print ('gender:', adam.gender)
print ('ribs:', adam.ribs)

eve = Human(name= 'eve', gender= 'female')
print ('name:', eve.name)
print ('gender:', eve.gender)
print ('ribs:', eve.ribs)

