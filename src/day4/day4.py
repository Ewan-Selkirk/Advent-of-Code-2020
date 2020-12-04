passport_data = []
fields_to_search = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_reqs = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "hgt": {"cm": [150, 193], "in": [59, 76]},
    "hcl": [],
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
}


def shrink_array(a_input):
    shrunk = ""
    for e in a_input:
        shrunk = shrunk + e
        if e != a_input[len(a_input) - 1]:
            shrunk = shrunk + " "

    return shrunk


def setup():
    tmp = []

    with open("./input.txt", "r") as f:
        for line in f:
            if line == "\n":
                passport_data.append(shrink_array(tmp))
                tmp.clear()
            else:
                tmp.append(line.rstrip())

        # print(passport_data)


def day4_p1():
    count = len(passport_data)
    print(count, "passports to check")

    for passport in passport_data:
        for validation in fields_to_search:
            if passport.find(validation) == -1:
                count -= 1
                break

    print(count, "passports are valid")


def day4_p2():
    count = len(passport_data)
    print(count, "passports to check")

    for passport in passport_data:
        for validation in fields_to_search:
            if passport.find(validation) != -1:
                if field_reqs[validation][0] >= int(passport.split(":")[1].split(" ")[0]) <= field_reqs[validation][1]:
                    print(validation, "is valid")
                    break
                break
            count -= 1

    print(count)


if __name__ == '__main__':
    setup()
    day4_p1()
    # day4_p2()
