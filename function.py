def greet_user():
    print("hi my name is pratik")
    print("welcome aord")

print("start")
greet_user()
print("finish\n\n")

#with parameters

def user(name):
    print("hi i am " +name)

abc = input()
user(abc)

print("enter no of parameters")

i = int(input())

for item in range(i):
    print(item+1)
    name = input()
    user(name)

#square function

def sq(num):
    return num * num
print(sq(3))