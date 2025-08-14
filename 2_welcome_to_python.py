#print("Hi welcome to python beginner's course")
#print('*' * 2)

a=10
b=20
c=10
if (id(a) != id(b)):
    print("a and b are the same object in memory")

if (id(a) == id(b)):
    print("a and b are different objects in memory")