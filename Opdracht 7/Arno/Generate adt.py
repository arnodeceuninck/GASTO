s = "type=rbt\n"
for i in range(50):
    s += "insert " + str(i) + "\n"
for i in range(49):
    s += "remove " + str(i) + "\n"
s += "print\n"
f = open("adt.auto", 'w')
f.write(s)