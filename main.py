# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def calculate(operation, arg1, arg2):
    arg1 = int(arg1)
    arg2 = int(arg2)

    match operation:
        case "x":
            result = arg1 * arg2
        case "+":
            result = arg1 + arg2
        case "-":
            result = arg1 - arg2
        case "/":
            result = arg1 / arg2
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with open("step_2.txt", 'r') as file:
        total = 0
        for instruction in file:
            instruction.rstrip()
            operation, arg1_str, arg2_str = tuple(instruction.split(" ")[1:])
            result = calculate(operation, int(arg1_str), int(arg2_str))
            #print(result)
            total += result

    print("Step 2 total: " + str(total))

    with open("step_3.txt", 'r') as file:
        instructions = [instruction.rstrip() for instruction in file.readlines()]
        index = 1
        seen_lines = set()
        while index < len(instructions):
            if index in seen_lines:
                print(f"Step 3 - Returned to line: {index}, Instructions: {instructions[index-1]}")
                break

            instruction_list = instructions[index-1].split(" ")

            seen_lines.add(index)

            if instruction_list[1].isdigit():
                index = int(instruction_list[1])
            elif instruction_list[1] == "calc":
                index = int(math.floor(calculate(*tuple(instruction_list[2:5]))))
            else:
                print("Invalid line")


    with open("step_4.txt", 'r') as file:
        instructions = [instruction.rstrip() for instruction in file.readlines()]
        index = 1
        seen_lines = [False] * len(instructions)

        while len(instructions) >= index > 0:

            if seen_lines[index - 1]:
                print(f"Step 4 - Returned to line: {index}, Instructions: {instructions[index-1]}")
                break

            instruction_list = instructions[index-1].split(" ")

            seen_lines[index - 1] = True
            match instruction_list[0]:
                case "goto":
                    if instruction_list[1].isdigit():
                        index = int(instruction_list[1])
                    elif instruction_list[1] == "calc":
                        index = int(math.floor(calculate(*tuple(instruction_list[2:5]))))
                case "remove":
                    line_num = int(instruction_list[1])
                    if 0 < line_num <= len(instructions):
                        instructions.pop(line_num - 1)
                        seen_lines.pop(line_num - 1)
                        if line_num > index:
                            index += 1
                    else:
                        index += 1
                case "replace":
                    to_replace = int(instruction_list[1])
                    replace_with = int(instruction_list[2])
                    if not ( 0 < to_replace <= len(instructions) or 0 < replace_with <= len(instructions)):
                        instructions[to_replace - 1] = instructions[replace_with - 1]
                    index += 1

                case _:
                    print("Invalid line")

    while True:
        print("Input operation:")
        operation = input()
        print("Input first integer operand:")
        arg1 = int(input())
        print("Input first integer operand:")
        arg2 = int(input())

        result = calculate(operation, arg1, arg2)
        print(f"{result}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
