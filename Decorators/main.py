def myDecorator(function):
    def wrapper():
        print('I am decorating function!')
        function()
    return wrapper()

@myDecorator
def hello_world(person):
    print(f'Hello {person}!')

print(hello_world('Mike'))