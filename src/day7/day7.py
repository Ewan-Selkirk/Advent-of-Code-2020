import re

rules = []


def setup():
    f = open("./input.txt", "r")
    reg = r"(\d(.+?)(bag[s]?))"

    for line in f:
        tmp = []

        tmp.append(line.split(" bags contain ")[0])
        tmp.append([result[0] for result in re.findall(reg, line)])

        rules.append(tmp)


def day7_p1():
    last_count = 0
    gold = []

    for bag, rule in rules:
        for r in rule:
            if re.search("(shiny gold)", r):
                gold.append(bag)
    count = len(set(gold))

    # Brute forcing it because I am dumb :'(
    while last_count != count:
        last_count = count
        for bag, rule in rules:
            for r in rule:
                for g in gold:
                    if re.search(g, r):
                        if bag not in gold:
                            gold.append(bag)
        count = len(set(gold))

    print(count)


def day7_p2():
    pass


if __name__ == '__main__':
    setup()
    day7_p1()
    day7_p2()
