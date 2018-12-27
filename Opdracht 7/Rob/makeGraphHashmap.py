
def addNode(i, count):
    if count == 0:
        return i
    else:
        return " | " + i

def auto():
    leeg = ""
    count = 0
    f = open("Hahsmap.dot", "w+")
    f.write("graph hashmap{\n")
    f.write("node[shape=record];\n")
    for i in getallen:
        leeg += addNode(str(i), count)
        count += 1
    print(leeg)
    f.write('Hashmap [label = "{%s}"]\n' %leeg)
    f.write("}")

auto()