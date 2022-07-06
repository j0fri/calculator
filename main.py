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
                print(f"Returned to line: {index}, Instructions: {instructions[index-1]}")
                break

            instruction_list = instructions[index-1].split(" ")

            seen_lines.add(index)

            if instruction_list[1].isdigit():
                index = int(instruction_list[1])
            elif instruction_list[1] == "calc":
                index = int(math.floor(calculate(*tuple(instruction_list[2:5]))))
            else:
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
