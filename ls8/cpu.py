"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8 
        self.pc = 0
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
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
                #set value of register to an integer
                self.reg[operand_a] = operand_b
                self.pc += 3
            
            elif IR == self.PRN:
                #Print numeric value stored in the given register.
                value = self.reg[operand_a]
                print(value)
                self.pc += 2

            elif IR == self.HLT:
                running = False
                
        
        
