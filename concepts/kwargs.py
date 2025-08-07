#kwargs = key word  arguments
# Dictionary of keyword arguments

def greet(name,nationality):
    print('Name is',name)
    print('Nationality is', nationality)

greet(nationality='British',name='Newton' )

#kwargs solves the mismatch of arguments

##Kwargs Profile

def employee(**kwargs):
    print(kwargs)

employee(name='Newton', age=25, nationality='British', salary=100000)
employee(name='Newton', age=25, nationality='British', salary=100000, is_married=True)

# mixed args and kwargs

def mixed(*args, **kwargs):
    print(args)
    print(kwargs)

mixed(1,2,3,4, name='Newton', age=25)