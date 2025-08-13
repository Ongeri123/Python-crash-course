class User:
    
    def __init__(self, name, phone, email,user):
        self.name = name
        self.phone = phone
        self.email = email
        self.user= user
    
    def say_my_name(self):
        print(f"Hi, my name is {self.name} my number is {self.phone}")
                                   
    
    def details(self):
        print('-------------------------------------')
        print(f'Name:', self.name)
        print(f'Phone:', self.phone)
        print(f'Email:', self.email)
        print(f'User:', self.user)
        print('-------------------------------------')

class employee(User):
 def __init__(self, name,phone,email, user ,salary):
    super().__init__(name, phone, email,user)
    self.salary = salary 

class customer(User):
 def __init__(self, name, phone, email, user,discount=0):
    super().__init__(name, phone, email,user)
    self.discount = discount






emp1 = employee(name = 'John', phone = '123456', email = 'groot@marvel.com',user= 'Chef', salary = 1000)
emp1.say_my_name()
emp1.details()


c1= customer(name='Jane', phone='123456', email='jane@marvel.com',user='Customer', discount=10)
c1.details()


