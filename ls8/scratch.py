import sys
"""
Change memory from being hardcoded to being read from outside files
1. get file path from command line
2. ignore blank lines, comments, whitespace
3. splitting input file line by line
4. Turn the program from the file into instructions (str -> int)
"""

memory = [0] * 256 #this will get loaded with numbers (instructions) from an outside file

with open(sys.argv[1]) as f:
    for line in f:
        t = line.split('#')
        n = t[0].strip()

        if n == '':
            continue
        n = int(n)
        print(repr(n))

sys.exit()

registers = [0] * 8 #R0 - R7


#"Variables" in hardware.  Known as registers
#They are a fixed number of registers
#They have fixed names
# R0, R1, R2, ... R7, R8

pc = 0 #Program counter - address of the currently executing instruction

running = True

while running:
    ir = memory[pc] #Instruction register - copy of currently executing instruction

    if ir == 1:
        print('Beej')
        pc += 1

    elif ir == 2:
        break

    elif ir == 3: 
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        registers[reg_num] = value
        print(registers)
        pc += 3


    else:
        print(f"Unknown instruction {ir}")
