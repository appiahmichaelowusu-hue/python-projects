def shout(func):
    result= func()
    def wrapper():
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello world"
print(greet())
