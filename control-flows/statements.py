"""
x = input("please enter your age\n")

if x < 18:
    print("you are simply not allowed")
elif x==18:
    print("we can think about you")
else :
    print("you can enter")



cats = ["white","black","oranges","others"]
 
for i in cats:
    print(i,len(i))



for i in range(10):
    print(i)



for i in range(2,10):
    for j in range(2,i):
        if i%j==0:
            print(i,'=',j)
            break;
        elif i%2==0:
            print(i)
            continue
        else :
            print(i)

    """
