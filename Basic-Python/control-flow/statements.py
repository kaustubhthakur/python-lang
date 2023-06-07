"""
x = int(input("please enter the number"))
if x<0:
    print('x is negative')
elif x==0:
    print('x is zero')
else :
    print('x is =non zero')


words = ['cat','window','drugs']

for i in words:
    print(i)

for i in range(len(words)):
    print(words[i])
    


#functions

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()

fib(10)
"""

#lambda function

def ans(n):
    return lambda x:x+n

s = ans(2)
print(s)