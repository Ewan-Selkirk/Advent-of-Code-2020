import math

data = []
directions = ["E", "S", "W", "N"]


def setup():
    f = open("./input.txt", "r")

    for line in f:
        data.append((line[0], int(line[1:].rstrip())))


def move_ship(direct, val, coords):
    x, y = coords

    if direct == "N":
        y += val
    elif direct == "S":
        y -= val
    elif direct == "E":
        x += val
    elif direct == "W":
        x -= val

    return x, y


def rotate_ship(direct, val, facing):
    i_facing = directions.index(facing)

    if direct == "R":
        return directions[(i_facing + int(val / 90)) % 4]
    elif direct == "L":
        for x in range(int(val/90)):
            i_facing -= 1
            if i_facing < 0:
                i_facing = 3

        return directions[i_facing]


def day12_p1():
    location = {"X": 0, "Y": 0}
    facing = directions[0]

    for instruction, val in data:
        if instruction in ["L", "R"]:
            facing = rotate_ship(instruction, val, facing)
        else:
            if instruction == "F":
                new_coords = move_ship(facing, val, (location["X"], location["Y"]))
            else:
                new_coords = move_ship(instruction, val, (location["X"], location["Y"]))

            location["X"] = new_coords[0]
            location["Y"] = new_coords[1]

    print(location)
    print(abs(location["X"]) + abs(location["Y"]))


def day12_p2():
    pass


if __name__ == '__main__':
    setup()
    day12_p1()
    day12_p2()
