import random
import secrets

b = random.normalvariate(0,1);
mylist = list('ALE');
print(b);
print(mylist);
a = random.choices(mylist,k=2);
print(a);
z = secrets.randbits(3);
print(z);