# This is a sample Python script.
import copy
from copy import deepcopy


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_next(array):
    summed_array = [array[i + 1] - array[i] for i in range(0, len(array) - 1)]
    if all(element == summed_array[0] for element in summed_array):
        return array[-1] + summed_array[0]
    else:
        return array[-1] + get_next(summed_array)


def sum(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input/input.txt", "r") as f:
        lines = f.read().split("\n")
    numberoflines = [[int(num) for num in line.split(" ")] for line in lines]
    print(numberoflines)
    sumedArray = [get_next(x) for x in numberoflines]

    print(sum(sumedArray))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# class read_stuff():
#     def __init__(self):
