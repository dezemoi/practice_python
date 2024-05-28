
adad=int(input("Give me a adad:"))
import random
ans= random.randint(1,9)
i=0

while adad!="exit":

    if adad==ans:
        print("ajab hadsi!")
        i+=1
        break
    elif adad>ans:
        print("bozorge!")
        i+=1
        adad=int(input("Give me a adad:"))
    elif adad<ans:
        print("kuchike!")
        i+=1
        adad=int(input("Give me a adad:"))


print("You tried", i ,"times")

