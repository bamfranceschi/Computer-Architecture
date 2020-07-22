import sys
PRINT_ANNA = 0b01  # 1
HALT = 0b10  # 2
PRINT_NUM = 0b11  # command 3
SAVE = 0b100
PRINT_REG = 0b101
ADD = 0b110
PUSH = 0b111
POP = 0b1000


# registers[2] = registers[2] + registers[3]


# memory = [PRINT_ANNA, PRINT_ANNA, PRINT_ANNA,
#           PRINT_NUM, 42, SAVE, 2, 99, SAVE, 3, 1, ADD, 2, 3, PRINT_REG, 2, HALT]  # represents RAM

memory = [0] * 256  # load up program into this memory


def load_memory(file_name):

    try:
        address = 0
        with open(file_name) as file:
            for line in file:
                split_line = line.split('#')
                command = split_line[0].strip()

                if command == '':
                    continue

                # load them up as int(command, 2) into our program (makes into a number identifying original command is in binary format)
                instruction = int(command, 2)
                memory[address] = instruction
                address += 1
     except FileNotFoundError:
        print("oops, that ifle doesn't exist")
        sys.exit()

if len(sys.argv) < 2:
    print("you need to give a second file name")
    sys.exit()



file_name = sys.argv[1]
load_memory(file_name)

# write a program to pull each command ot of memory and execute

# we can loop over it!

# save number 99 into register2 or R2
# register aka memory
# R0-R7
registers = [0] * 8

program_counter = 0
registers[7] = 0xF4
running = True

while running:
    command = memory[program_counter]

    if command == PRINT_ANNA:
        print("Anna!")
    if command == PRINT_NUM:
        print(memory[program_counter + 1])
        program_counter += 1
    if command == SAVE:
        registers[memory[program_counter + 1]] = memory[program_counter + 2]
        program_counter += 2
        # reg = memory[pc + 1]
        # num_to_save = memory[pc + 2]
        # registers[reg] = num_to_save
    if command == PRINT_REG:
        print(registers[memory[program_counter + 1]])
        program_counter += 1

    if command == ADD:
        first_reg = memory[program_counter + 1]
        second_reg = memory[program_counter + 2]

        registers[first_reg] = registers[first_reg] + registers[second_reg]
        program_counter += 2

    if command == HALT:
        running = False
    
    if command == PUSH:
        # decrement stack pointer
        registers[7] -=1

        # get a value from the given register
        value = registers[memory[program_counter + 1]] 
        
        # put at the stack pointer address

        sp = registers[7]
        memory[sp] = value

        program_counter += 1
    
    if command == POP:
        # get the stack pointer (where do we look?)
        sp = registers[7]

        # get register number to put value in
        reg = memory[program_counter + 1]
        value = memory[sp] 

        # use stack pointer to get the value
        registers[reg] = value
        # put the value into the given register
        registers[7] +=1

        program_counter +=1

    program_counter += 1
