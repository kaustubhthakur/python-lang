#lambda arguments = expression
add = lambda x : x+10
print(add(10))

mult = lambda x,y:x*y 
print(mult(2,7))

ans = [(1,2),(10,5),(3,4)]
point = sorted(ans,key=lambda x :x[1])
print(point)