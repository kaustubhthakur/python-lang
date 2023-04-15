#Lists:ordered ,mutable,allows duplicate;
mylist = ["banana","apple","cherry",True,1,2,3,4,4,4,"apple"];


mylist.append("lemon");
mylist.insert(11,"bluberry");
mylist.reverse()

# mylist.sort()

print(mylist[1]);
for i in mylist:
    print(i)

print(len(mylist))

if 0 in mylist:
    print("YES");
else :
    print("NO")

