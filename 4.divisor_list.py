adad = int(input(" give me an adad:"))
divisors = [ x for x in range(1,adad+1) if adad%x==0]
print(divisors)


bbb=list(range(3,14))
print(bbb)


#  other longer way
'''divisors=[]
adad = int(input(" give me an adad:"))
for x in range(1,adad+1):
    if adad%x == 0:
        divisors.append(x)

print(divisors)        '''
