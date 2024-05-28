str = input("give me a string:") #dina

rv=str[::-1]
if rv==str:
    print("it's palindrome")
else:
    print("not palindrome")    

'''print(type(str))
print(str[0,3])
n=len(str)
rev=[]
b=n
print(n)
for e in str:
    print(e)
    print(b)
    rev.insert(b,e)
    b=b-1
    print("this is b-1:",b)
    print("this is rev[b]",rev[b])
print(rev)
'''