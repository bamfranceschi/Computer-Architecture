"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010  # two params
PRN = 0b01000111  # one param
ADD = 0b10100000  # two params
AND = 0b10101000  # two params
CALL = 0b01010000  # one param
CMP = 0b10100111  # two params
DEC = 0b01100110  # one param
DIV = 0b10100011  # two params
INC = 0b01100101  # one param
INT = 0b01010010  # one param
IRET = 0b00010011
JEQ = 0b01010101  # one param
JGE = 0b01011010  # one param
JGT = 0b01010111  # one param
JLE = 0b01011001  # one param
JLT = 0b01011000  # one param
JMP = 0b01010100  # one param
JNE = 0b01010110  # one param
LD = 0b10000011  # two params
MOD = 0b10100100  # two params
MUL = 0b10100010  # two params
NOP = 0b00000000
NOT = 0b01101001  # one param
OR = 0b10101010  # two params
POP = 0b01000110  # one param
PRA = 0b01001000  # one param
PUSH = 0b01000101  # one param
RET = 0b00010001
SHL = 0b10101100  # two params
SHR = 0b10101101  # two params
ST = 0b10000100  # two params
SUB = 0b10100001  # two params
XOR = 0b10101011  # two params


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_ldi
        self.branchtable[PRN] = self.handle_prn
        self.branchtable[MUL] = self.handle_mul

    def handle_ldi(self, a, b):
        self.reg[a] = b
        self.pc += 2

    def handle_prn(self, a):
        print(self.reg[a])
        self.pc += 1

    def handle_mul(self, a, b):
        self.alu("MUL", a, b)
        self.pc += 2

    def load(self, file_name):
        """Load a program into memory."""
        try:
            address = 0
            with open(file_name) as file:
                for line in file:
                    split_line = line.split('#')
                    command = split_line[0].strip()

                    if command == '':
                        continue
        # For now, we've just hardcoded a program:
                    instruction = int(command, 2)
                    # where is self.ram defined?
                    self.ram[address] = instruction
                    address += 1
        except FileNotFoundError:
            print("oops, that file doesn't exist")
            sys.exit()

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]  # where is self.reg defined?
        # elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        running = True

        while running:

            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if (IR >> 6) == 2:
                self.branchtable[IR](operand_a, operand_b)

            if (IR >> 6) == 1:
                self.branchtable[IR](operand_a)

            if IR == HLT:
                running = False

            self.pc += 1

    def ram_read(self, address):
        # should accept the address to read and return the value stored there.
        return self.ram[address]

    def ram_write(self, value, address):
        # should accept a value to write, and the address to write it to.

        self.ram[address] = value

        return value
