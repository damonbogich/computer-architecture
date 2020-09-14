memory = [
    1, #print Beej  ##address 0
    3, #SAVE_REG R1,37
    1,
    37,
    2  #Halt
]

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
