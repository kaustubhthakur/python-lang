#counter,namedtuple,ordereddict,defaultdict,deque
from collections import namedtuple
from collections import Counter
from collections import OrderedDict
from collections import deque
"""
#counter

a = "aaaaaabaccbabcggggg"
my_counter = Counter(a);
print(my_counter.keys())
print(my_counter.values())

#namedtuple

point = namedtuple('point','x,y')
pt = point(1,3)
print(pt.x,pt.y)

#ordereddict

ordered_dict = OrderedDict()
ordered_dict['a']=1
ordered_dict['b'] = 2;
ordered_dict['c'] =3;
print(ordered_dict)


#deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.appendleft(4)
d.pop()
print(d)

"""