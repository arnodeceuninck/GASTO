s = "type=rbt\n"
for i in range(128):
    s += "insert " + str(i) + "\n"
s += "print\n"
f = open("adt.auto", 'w')
f.write(s)