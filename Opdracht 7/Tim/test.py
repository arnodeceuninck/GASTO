import random
import sys
f = open("234-insert-delete.txt", 'w')
arg = int (sys.argv[1])
prints = list(sys.argv[2])
numbers = []
f.write("type=234T" + '\n')
for i in range(arg):
    number = random.randint(0,200)
    f.write("insert " + str(number) + '\n')
    numbers.append(number)
while len(numbers) is not 0:
    number = numbers[random.randrange(0, len(numbers))]
    if number in prints:
        f.write("print"+'\n')
    f.write("delete " + str(number) + '\n')
    numbers.remove(number)
f.close()

