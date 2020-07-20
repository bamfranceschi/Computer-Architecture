PRINT_ANNA = 0b01  # 1
HALT = 0b10  # 2
PRINT_NUM = 0b11  # command 3
SAVE = 0b100
PRINT_REG = 0b101
ADD = 0b110

#registers[2] = registers[2] + registers[3]


memory = [PRINT_ANNA, PRINT_ANNA, PRINT_ANNA,
          PRINT_NUM, 42, SAVE, 2, 99, SAVE, 3, 1, ADD, 2, 3, PRINT_REG, 2, HALT]  # represents RAM

# write a program to pull each command ot of memory and execute

# we can loop over it!

# save number 99 into register2 or R2
# register aka memory
# R0-R7
registers = [0] * 8

program_counter = 0
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
        #reg = memory[pc + 1]
        #num_to_save = memory[pc + 2]
        #registers[reg] = num_to_save
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

    program_counter += 1
