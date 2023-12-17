if __name__ == '__main__':
    with open("input/input.txt", "r") as f:
        lines = f.read().split("\n")
    numberoflines = [[int(num) for num in line.split(" ")] for line in lines]
    print(numberoflines)
