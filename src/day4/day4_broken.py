import re

passport_data = []
fields_to_search = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_reqs = {
    "byr": ["1920", "2002"],
    "iyr": ["2010", "2020"],
    "eyr": ["2020", "2030"],
    "hgt": {"cm": ["150", "193"], "in": ["59", "76"]},
    "hcl": "#[0-9a-f]{6}",
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": "[0-9]{9}"
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
        for index, field in enumerate(passport.split(" ")):

            s_field = field.split(":")

            try:
                if passport.find(s_field[0]) != -1:
                    if s_field[0] == "byr" or s_field[0] == "iyr" or s_field[0] == "eyr":
                        if not field_reqs[s_field[0]][0] <= int(s_field[1]) <= field_reqs[s_field[0]][1]:
                            count -= 1
                            break
                    elif s_field[0] == "hgt":
                        if s_field[1].find("cm") != -1:
                            if not field_reqs[s_field[0]]["cm"][0] <= int(s_field[1][0:-2]) <= \
                                   field_reqs[s_field[0]]["cm"][1]:
                                count -= 1
                                break
                        else:
                            if not field_reqs[s_field[0]]["in"][0] <= int(s_field[1][0:-2]) <= \
                                   field_reqs[s_field[0]]["in"][1]:
                                count -= 1
                                break
                    elif s_field[0] == "hcl":
                        if not re.search(field_reqs[s_field[0]], s_field[1]):
                            count -= 1
                            break
                    elif s_field[0] == "ecl":
                        for colour in field_reqs["ecl"]:
                            if passport.find(colour) != -1:
                                break
                        count -= 1
                    elif s_field[0] == "pid":
                        if not re.search(field_reqs[s_field[0]], s_field[1]):
                            count -= 1
                            break
                    else:
                        pass
                count -= 1
            except ValueError:
                pass

    print(count, "passports are valid")


if __name__ == '__main__':
    setup()
    day4_p1()
    day4_p2()
