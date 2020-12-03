num_list = []


def day1_p1():
    f = open("./input.txt", "r")

    for line in f:
        num_list.append(line.strip("\r\n"))

    for num1 in num_list:
        for num2 in num_list:
            if num1 != num2:
                if (int(num1) + int(num2)) == 2020:
                    print(num1, "and", num2, "equals 2020!")
                    print("Total sum:", int(num1) * int(num2))
                    return


def day1_p2():
    for num1 in num_list:
        for num2 in num_list:
            for num3 in num_list:
                if num1 != num2 and num1 != num3:
                    if num2 != num3:
                        if (int(num1) + int(num2) + int(num3)) == 2020:
                            print(num1, ",", num2, "and", num3, "equals 2020!")
                            print("Total sum:", int(num1) * int(num2) * int(num3))
                            return


if __name__ == '__main__':
    day1_p1()
    day1_p2()
