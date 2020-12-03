psw_req = []
psw_char = []
psw = []
count = 0


def checkPassword(p_min, p_max, char, password, debug):
    if int(p_min) <= password.count(char) <= int(p_max):
        if debug:
            print(password, "is a valid password!")
        return True
    else:
        if debug:
            print(password, "is not a valid password!")
        return False


def checkPassword_p2(p_min, p_max, char, password, debug):
    psw_list = list(password)

    if psw_list[p_min - 1] == char or psw_list[p_max - 1] == char:
        if not (psw_list[p_min - 1] == char and psw_list[p_max - 1] == char):
            if debug:
                print(password, "is a valid password!")
            return True
    else:
        if debug:
            print(password, "is not a valid password!")
        return False


def setup():
    f = open("./input.txt", "r")

    for line in f:
        split_line = line.split(" ")

        psw_req.append(split_line[0])
        psw_char.append(split_line[1].strip(":"))
        psw.append(split_line[2].strip("\n"))


def day2_p1():
    global count

    for x in range(0, 1000):
        min_req = int(psw_req[x].split("-")[0])
        max_req = int(psw_req[x].split("-")[1])

        if checkPassword(min_req, max_req, psw_char[x], psw[x], debug=False):
            count += 1

    print(count)
    count = 0


def day2_p2():
    global count

    for x in range(0, 1000):
        min_req = int(psw_req[x].split("-")[0])
        max_req = int(psw_req[x].split("-")[1])

        if checkPassword_p2(min_req, max_req, psw_char[x], psw[x], debug=False):
            count += 1

    print(count)
    count = 0


if __name__ == '__main__':
    setup()
    day2_p1()
    day2_p2()
