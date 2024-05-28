a=int(input("give me a number:"))
l=[]
j=0

for i in range(1,a+1):
    if a%i==0:
        j=j+1
        l.append(i)

if j>2:
    print("avval nist!", l, j,"ta maghsum elayh dare")
else:
    print(a, "adade avvale")    




def get_integer():
    return int(input("Give me a number: "))

age = get_integer()
school_year = get_integer()
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))


def div():
    return int(input("give me num:"))

a=div()
