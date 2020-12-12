data = []


def setup():
    f = open("./input.txt", "r")

    for line in f:
        data.append(int(line.rstrip()))

    data.sort()


def day10_p1():
    ones = 1
    threes = 0

    data.append(data[len(data) - 1] + 3)

    for index, e in enumerate(data):
        if index < len(data) - 1:
            if data[index + 1] - e == 1:
                ones += 1
            elif data[index + 1] - e == 3:
                threes += 1
            else:
                print("Totally fucking fucked it mate, big time")

    print(ones * threes)


def day10_p2():
    pass


if __name__ == '__main__':
    setup()
    day10_p1()
