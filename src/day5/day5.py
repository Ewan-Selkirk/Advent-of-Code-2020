flight_data = []


def setup():
    f = open("./input.txt", "r")

    for line in f:
        flight_data.append(line.rstrip())


def calculate_seat_id(row, col):
    return row * 8 + col


def day5_p1():
    highest_seat_id = 0

    for b_pass in flight_data:
        seat = ""
        for char in b_pass:
            if char == "F":
                seat = seat + "0"
            elif char == "B":
                seat = seat + "1"
            elif char == "L":
                seat = seat + "0"
            elif char == "R":
                seat = seat + "1"

        row = int(seat[0:7], 2)
        col = int(seat[7:10], 2)

        if highest_seat_id < calculate_seat_id(row, col):
            highest_seat_id = calculate_seat_id(row, col)

    print("The highest seat ID is", highest_seat_id)


def day5_p2():
    seat_ids = []

    for b_pass in flight_data:
        seat = ""
        for char in b_pass:
            if char == "F":
                seat = seat + "0"
            elif char == "B":
                seat = seat + "1"
            elif char == "L":
                seat = seat + "0"
            elif char == "R":
                seat = seat + "1"

        row = int(seat[0:7], 2)
        col = int(seat[7:10], 2)

        seat_ids.append(calculate_seat_id(row, col))

    seat_ids.sort()

    for s_id in seat_ids:
        if not int(s_id) + 1 in seat_ids:
            print("The missing seat ID is", int(s_id) + 1)
            break


if __name__ == '__main__':
    setup()
    day5_p1()
    day5_p2()
