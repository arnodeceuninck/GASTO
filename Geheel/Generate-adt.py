import random
s = "type=rbt\n"
for i in range(128):
    s += "insert " + str(random.randint(0, 10000)) + "\n"
s += "print\n"
f = open("adt.auto", 'w')
f.write(s)