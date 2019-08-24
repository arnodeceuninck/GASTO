import random
import sys
f = open("234-insert-delete.txt", 'w')
arg = int (sys.argv[1])
randommode = int(sys.argv[2])
numbers = random.sample(range(arg), arg)
f.write("type=234T" + '\n')
if randommode is 0:
    for i in range(len(numbers)):
        f.write("insert " + str(numbers[i]) + '\n')
    f.write("print" + '\n')
    while len(numbers) is not 0:
        number = numbers[random.randrange(0, len(numbers))]
        f.write("delete " + str(number) + '\n')
        numbers.remove(number)

else:
    inserted = []
    while len(numbers) is not 0:
        if random.choice([0,1,2]) != 0:
            next = random.randrange(0, len(numbers))
            f.write("insert " + str(numbers[next]) + '\n')
            inserted.append(numbers.pop(next))
        elif inserted:
            next = random.choice(inserted)
            f.write("delete " + str(next) + '\n')
            inserted.remove(next)
    while inserted:
        next = random.choice(inserted)
        f.write("delete " + str(next) + '\n')
        inserted.remove(next)


f.write("print" + '\n')
f.close()

