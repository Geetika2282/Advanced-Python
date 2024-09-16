import time


def deco(func):
    def wrapper(*args, **kwargs):
        print("Before: ", time.time())
        func(*args, **kwargs)
        print("After: ", time.time())
    return wrapper

@deco
def hi():
    time.sleep(2)
    print("Hi")

hi()




def debug(fnc):
    def wrapper(*args, **kwargs):
        argsVal = ', '.join(str(arg) for arg in args)
        kwargsVal = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        return fnc(*args, **kwargs)
    return wrapper()


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

print(greet("Geet", "Heyy"))


def cache(func):
    cacheVal = {}
    def wrapper(*args):
        if args in cacheVal:
            return cacheVal
        res = func(*args)
        cacheVal[args] = res
        return res
    return wrapper

def longRunningFunc(a, b):
    time.sleep(4)
    return a+b

print(longRunningFunc(4, 5))
print(longRunningFunc(4, 5))