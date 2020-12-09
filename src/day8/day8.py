instructions = []


def setup():
    f = open("./input.txt", "r")

    for line in f:
        instructions.append(line.rstrip().split())


def day8_p1(debug=True):
    accumulator = 0
    count = 0
    visited = []

    while True:
        if count in visited:
            if debug:
                print("Loop detected!")
            break
        else:
            visited.append(count)

        if instructions[count][0] == "acc":
            accumulator += int(instructions[count][1])
            count += 1
        elif instructions[count][0] == "jmp":
            count += int(instructions[count][1])
        else:
            count += 1

        if count == len(instructions):
            return True, accumulator

    return False, accumulator


def day8_p2():
    for i in range(len(instructions)):
        if instructions[i][0] == "nop":
            instructions[i][0] = "jmp"

            run = day8_p1(debug=False)
            if run[0]:
                return run[1]
            else:
                instructions[i][0] = "nop"

        elif instructions[i][0] == "jmp":
            instructions[i][0] = "nop"

            run = day8_p1(debug=False)
            if run[0]:
                return run[1]
            else:
                instructions[i][0] = "jmp"


if __name__ == '__main__':
    setup()
    print(day8_p1(debug=False)[1])
    print(day8_p2())
