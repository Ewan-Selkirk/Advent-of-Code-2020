import re

passport_data = []
fields_to_search = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_reqs = {
    "byr": "(byr:(19[2-9][0-9]|200[0-2]))",
    "iyr": "(iyr:(201[0-9]|2020))",
    "eyr": "(eyr:(202[0-9]|2030)",
    "hgt": "((hgt:1[5-9][0-9]cm)|(hgt:(59|6[0-9]|7[0-6])in))",
    "hcl": "(hcl:#[0-9a-f]{6})",
    "ecl": "(ecl:(amb|blu|brn|gry|grn|hzl|oth))",
    "pid": "(pid:([0-9]{9})))"
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

    print(count, "passports are valid\n")


def day4_p2():
    count = len(passport_data)
    print(count, "passports to check")

    for passport in passport_data:
        if len(re.findall(str(field_reqs["byr"] + "|" + field_reqs["iyr"] + "|" + field_reqs["eyr"] + "|" +
                              field_reqs["hgt"] + "|" + field_reqs["hcl"] + "|" + field_reqs["ecl"] + "|" +
                              field_reqs["pid"]), passport)) < 7:
            count -= 1

    print(count, "passports are valid")


if __name__ == '__main__':
    setup()
    day4_p1()
    day4_p2()
