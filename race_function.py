from car_sub import blue, red, green, \
    yellow, black, white, orange, purple
from csv import writer


car_list = [
    blue,
    red,
    green,
    yellow,
    black,
    white,
    orange,
    purple
]


def rally_car_pick(a):
    ral = None
    if a == 1:
        ral = blue
    elif a == 2:
        ral = red
    elif a == 3:
        ral = green
    elif a == 4:
        ral = yellow
    elif a == 5:
        ral = black
    elif a == 6:
        ral = white
    elif a == 7:
        ral = orange
    elif a == 8:
        ral = purple

    return ral


# Makes the first choice on the input that you can't get an error
def choice_check(text, x, y):
    while True:
        try:
            a = int(input(text))

        except ValueError:
            print('Lets try this again, not a number')
        else:
            if x <= a <= y:
                break
            else:
                print('Lets try this again, not in range')
    return a


def race_result(x, y):

    if x.distance >= len(x.track_length) \
            and y.distance >= len(y.track_length):
        outcome = 'Tie'
    elif x.distance >= len(x.track_length):
        outcome = x.name
    else:
        outcome = y.name
    return outcome


# Updates the race records
def adding_records(a, b, c, d, e):
    race_list = [a, b, c, d, e]

    with open('race_records.csv', 'a', newline='') as race_records_file:
        writer_race_records = writer(race_records_file)
        writer_race_records.writerow(race_list)
        race_records_file.close()


# Starts the game with data from previous races,
# only good for small files
def save_info(a):
    with open('saved_data.txt', 'r') as f:
        b = f.readlines()[a]
    return b


# Saves data from previous races, only good for small files
def replace_info(a, b):
    with open('saved_data.txt', 'r') as f:
        c = f.readlines()
        c[a] = str(b) + '\n'
    with open('saved_data.txt', 'w') as f:
        for line in c:
            f.write(line)


# Updates the bet records
def adding_bets(a, b, c):
    bets_list = [a, b, c]

    with open('bets.csv', 'a', newline='') as bets_file:
        writer_race_records = writer(bets_file)
        writer_race_records.writerow(bets_list)
        bets_file.close()


def rally_result():
    a = blue.distance >= len(red.track_length)
    b = red.distance >= len(red.track_length)
    c = green.distance >= len(green.track_length)
    d = yellow.distance >= len(yellow.track_length)
    e = black.distance >= len(black.track_length)
    f = white.distance >= len(white.track_length)
    g = orange.distance >= len(orange.track_length)
    h = purple.distance >= len(purple.track_length)

    if sum([a, b, c, d, e, f, g, h]) >= 2:
        outcome = 'Tie'
    elif a:
        outcome = blue.name
    elif b:
        outcome = red.name
    elif c:
        outcome = green.name
    elif d:
        outcome = yellow.name
    elif e:
        outcome = black.name
    elif f:
        outcome = white.name
    elif g:
        outcome = orange.name
    else:
        outcome = purple.name
    return outcome
