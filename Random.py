import random
def randString(length=500000000):
        letters='abcdefghijklmnopqrstuvwxyz'
        return ''.join((random.choice(letters) for i in range(length)))

print ("Processing...")
print (randString(),file=open("output.txt", "a"))
print ("FINSIHED")
input ("Press ENTER to exit")
