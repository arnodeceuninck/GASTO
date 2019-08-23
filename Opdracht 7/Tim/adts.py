import sys
import NewT234
import subprocess

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
            tree = NewT234.T234()

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

            tree.insert(int(input))

            #tree.T234Insert(T234.TreeItem("test", int(input)))

        elif "delete" in line:
            for i in range(len(line)):
                if line[i] == ' ':
                    start = i+1
                if line[i] == '\n':
                    stop = i
            input = []
            for j in range(start, stop):
                input.append(str(line[j]))
            input = ''.join(input)
            #tree.T234Delete(int(str(input)))
            tree.delete(int(str(input)))

        elif "print" in line:
            printcount += 1
            name = "234T-" + str(printcount) + ".dot"
            tree.print(name)

    subprocess.call([r'D:\School\Git\GASTO\GASTO\Opdracht 7\Tim\dotToPng.bat'])

# parameters meegeven in pycharm
# - klik in het menu op Run
# - klik op Edit configurations
# - geef de naam van het inputbestand in bij parameters (dus bv adt.txt zoals op BB)