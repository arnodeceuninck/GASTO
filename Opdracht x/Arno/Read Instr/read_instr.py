file_location = "instr.txt"

instructions = {"init":"Functie om te initialieseren", "vak":"vak_functie()"}

instr_file = open(file_location, "r")

for instruction_line in instr_file:
    if instruction_line[0] == "#":
        print("Skipping comment line...")
        continue
    else:
        print("Instruction found, analyzing...")
        instr_segments = instruction_line.split()
        print(instructions[instr_segments[0]]) # Run de bijhorende functie van de dictionary
