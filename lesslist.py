ab = [1,2,5,6,7,888,489,1,0,1,'fh',4,5]
l2=[]
# print(type(ab))
for x in ab:
    if isinstance(x,int):
         if  x<5:
             print(type(x))
             l2.append(x)

print("this is it",l2)

#print([x for x in ab if x<7])











