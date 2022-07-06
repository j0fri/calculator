# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculate(operation, arg1, arg2):
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
            print(result)
            total += result

    print("Total: " + str(total))


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
