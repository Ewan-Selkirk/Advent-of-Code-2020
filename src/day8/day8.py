instructions = []


def setup():
    f = open("./input.txt", "r")

    for line in f:
        instructions.append(line.rstrip().split())


def day8_p1():
    accumulator = 0
    count = 0
    visited = []

    while True:
        if count in visited:
            print("Loop detected!\nAccumulator =", accumulator)
            break
        else:
            visited.append(count)

        if instructions[count][0] == "acc":
            accumulator += int(instructions[count][1])
            count += 1
            continue
        elif instructions[count][0] == "jmp":
            count += int(instructions[count][1])
            continue
        else:
            count += 1


def day8_p2():
    pass


if __name__ == '__main__':
    setup()
    day8_p1()
    day8_p2()
