def get_next(array):
    summed_array = [array[i + 1] - array[i] for i in range(0, len(array) - 1)]
    if all(element == summed_array[0] for element in summed_array):
        return array[-1] + summed_array[0]
    else:
        return array[-1] + get_next(summed_array)


def get_previus(array):
    summed_array = [array[i + 1] - array[i] for i in range(0, len(array) - 1)]
    if all(element == summed_array[0] for element in summed_array):
        return array[0] - summed_array[0]
    else:
        return array[0] - get_previus(summed_array)


if __name__ == '__main__':
    with open("input/input.txt", "r") as f:
        lines = f.read().split("\n")
    numberoflines = [[int(num) for num in line.split(" ")] for line in lines]

    sumedArray = [get_next(x) for x in numberoflines]
    print(sum(sumedArray))

    sumedArrayPt2 = [get_previus(x) for x in numberoflines]
    print(sum(sumedArrayPt2))
