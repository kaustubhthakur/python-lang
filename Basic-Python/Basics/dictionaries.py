#it is collection dataype which is unordered mutable ,key-value pairs

mydict = {"name":"ALEX","age":19,"city":"Pen City"}
print(mydict)
mydict2 = dict(name="kastubh",age=19,city="Mumbai City")
print(mydict2)
mydict["email"]="alex123@gmail.com"
for i in mydict:
    print(i,"=",mydict[i])


my_dict_cp = mydict
my_dict_cp["gender"]="male"
print(my_dict_cp)



mydict.update(my_dict_cp) #update the dictionary
print("original",mydict)