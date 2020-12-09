data = []
key = 0


def is_valid(num, values):
    for v in values:
        if num - v in values:
            return True


def setup():
    f = open("./input.txt", "r")

    for line in f:
        data.append(int(line.rstrip()))


def day9_p1():
    global key

    # Change to 5 for sample data
    counter = 25

    for x in range(counter, len(data)):
        if not is_valid(data[x], data[x - counter:x]):
            key = data[x]
            print(key)
            break


def day9_p2():
    num = [0]
    accumulator = 0

    for d in data:
        accumulator += d
        num.append(accumulator)

    for i in range(len(num)):
        j = i + 2

        while 0 <= j < len(num) and num[j] - num[i] <= key:
            if num[j] - num[i] == key:
                print(max(data[i:j]) + min(data[i:j]))
                break

            j += 1


if __name__ == '__main__':
    setup()
    day9_p1()
    day9_p2()
