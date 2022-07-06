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
