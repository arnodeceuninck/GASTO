import sys
import T234

if len(sys.argv) != 2:
    print('Usage: adts.py <inputfile>')
else:
    print('Running ADT operations given in file ', sys.argv[1])
    # hier komt je code
    f = open(sys.argv[1], 'r')
    printcount = 0
    for line in f:
        i = 0
        j = 0
        if "type=234" in line:
            tree = T234.createSearchTree()

        elif "insert" in line:
            for i in range(len(line)):
                if line[i] == ' ':
                    start = i+1
                if line[i] == '\n':
                    stop = i
            input = []
            for j in range(start, stop):
                input.append(str(line[j]))
            input = ''.join(input)

            tree._234TInsert(T234.TreeItem("test", int(input)))

        elif "delete" in line:
            for i in range(len(line)):
                if line[i] == ' ':
                    start = i+1
                if line[i] == '\n':
                    stop = i-1
            tree._234TDelete(int(str(line[start] + line[stop])))

        elif "print" in line:
            printcount += 1
            tree.print(printcount)

# parameters meegeven in pycharm
# - klik in het menu op Run
# - klik op Edit configurations
# - geef de naam van het inputbestand in bij parameters (dus bv adt.txt zoals op BB)