map = []


def setup():
    f = open("input.txt", "r")

    for line in f:
        map.append(line.strip("\n"))


def check_tree(x, y):
    if map[y][x] == "#":
        return True
    else:
        return False


def day3(right, down):
    count = 0
    x = 0
    y = 0

    while y < len(map):
        if check_tree(x, y):
            count += 1
        x = (x + right) % (len(map[0]))
        y += down

    print(count)
    return count


if __name__ == '__main__':
    setup()
    day3(3, 1)
    print(day3(1, 3) * day3(3, 1) * day3(5, 1) * day3(7, 1) * day3(1, 2))
