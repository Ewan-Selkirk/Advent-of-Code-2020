groups = []


def setup():
    tmp = []
    f = open("./input.txt", "r")

    for line in f:
        if line == "\n":
            groups.append(list(tmp))
            tmp.clear()
        else:
            tmp.append(line.rstrip())
    groups.append(tmp)


def day6_p1():
    q_sum = 0

    for g in groups:
        questions = ""
        for value in g:
            questions = questions + value

        q_sum += len(set(questions))

    print("Total sum of questions answered 'yes':", q_sum)


def day6_p2():
    q_sum = 0

    for g in groups:
        group = g[0]
        for value in g:
            group = set(group) & set(value)

        q_sum += len(group)

    print("Total sum of questions everyone answered 'yes':", q_sum)


if __name__ == '__main__':
    setup()
    day6_p1()
    day6_p2()
