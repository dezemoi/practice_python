l1 = [1, 1,1, 2, 3,5, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 1,2, 3, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lll=[]
llll=[]

'''for x in l1:
    for y in l2:
        if x==y: 
            lll.append(x)'''

#The way I created
'''for x in l1:
    if x in l2:
        lll.append(x)
        if lll.count(x)>1:
            lll.remove(x)'''
ab=[]
ab=[x for x in l1 if x in l2]
print(ab)

#The right way

for x in l1:
    if x in l2:
        if x not in lll :
            lll.append(x)
print(lll)
             

'''for x in lll:
    for y in lll:
        if x!=y:
            llll.append(x)

'''