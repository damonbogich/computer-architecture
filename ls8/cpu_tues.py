"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8 
        self.pc = 0
        self.stack_pointer = self.reg[7]
        self.reg[7] = self.ram[0xf4]
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.MUL = 0b10100010
        self.PUSH = 0b01000101
        self.POP = 0b01000110

    def load(self, file_name):
        """Load a program into memory."""

        with open(file_name) as f:
            address = 0

            for line in f:
                line = line.split('#')
                try:
                    v = line[0].strip()
                except ValueError:
                    continue
                if len(v) > 0:
                    self.ram[address] = int(v,2)
                    address += 1


            print('memmory', self.ram[:15])


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            #multiply the two registers together and store the answer in rega
            self.reg[reg_a] *= self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    def push(self, register):
        #decrement stack pointer
        self.stack_pointer -= 1
        #Copy the value in the given register to the address pointed to by SP.
        #value
        value = self.reg[register]
        #copy value to the where stack pointer is pointing
        self.ram[self.stack_pointer] = value

        self.pc += 2
    def pop(self, register):
        ##Pop the value at the top of the stack into the given register.

        # Copy the value from the address pointed to by SP to the given register.
        # Increment SP.
        value = self.ram[self.stack_pointer]
        
        self.reg[register] = value

        self.stack_pointer += 1

        self.pc += 2

    def ldi(self, register, integer):
        self.reg[register] = integer
        self.pc += 3

    def prn(self, register):
        print(self.reg[register])
        self.pc += 2
    



    


    #Memory Address Register (MAR) - contains the address that is being read or written to
    #Memory Data Register (MDR) - contains the data that was read or the data to write
    def ram_read(self, MAR):
        #should accept the address to read and return the value stored there.
        MDR = self.ram[MAR]
        return MDR
    
    def ram_write(self, MDR, MAR):
        # should accept a value to write, and the address to write it to.
        self.ram[MAR] = MDR
    
    def run(self):
        """
        1. It needs to read the memory address that's stored in register PC, and store that result in IR, the Instruction Register. This can just be a local variable in run().
        
        2. Some instructions requires up to the next two bytes of data after the PC in memory to perform operations on. Sometimes the byte value is a register number, other times it's a constant value (in the case of LDI). Using ram_read(), read the bytes at PC+1 and PC+2 from RAM into variables operand_a and operand_b in case the instruction needs them.
        """

        running = True
        while running:
            IR = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == self.LDI:
                self.ldi(operand_a, operand_b)
            
            elif IR == self.PRN:
                self.prn(operand_a)
                
            elif IR == self.MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3

            elif IR == self.PUSH:
                self.push(operand_a)

            elif IR == self.POP:
                self.pop(operand_a)
                
            elif IR == self.HLT:
                running = False