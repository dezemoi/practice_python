import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a= random.sample(range(2,25),9)
b = random.sample(range(1,30),15)
print("this is a",a)
print("this is b",b)
abc=[]
ab=[]


ab=[x for x in a if x in b]
for x in ab:
    if ab.count(x)>1:
        g=ab.index(x)
        print(g)
        v=int(g)
        # ab.pop([v])

print(ab)    

bzz=[]
for x in a:
    if x in b:
        bzz.append(x)
        if bzz.count(x)>1:
            bzz.pop(x)
print("This is bzz",bzz)
