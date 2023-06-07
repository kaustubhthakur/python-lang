# function decorators

def start(func):

    def wrapper(*args,**kwargs):
        print('start') 
        result = func(*args,**kwargs)
        print('end')
        return result;
    return wrapper

@start
def ans(x):
    return x+10;

result = ans(100)
print(result)

#class decorators