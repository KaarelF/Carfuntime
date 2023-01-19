# TODO: Better no name the "main" file as main.py

# TODO: I do not remember if I wrote that previously,
#  but long import list should be included in brackets and aligned vertically. Fix the rest
from car_sub import (
    blue,
    red,
    green,
    yellow,
    black,
    white,
    orange,
    purple,
)
from track_sub import short_track, medium_track, long_track
from time import sleep
# TODO: Fix the import list as above
from race_function import choice_check, \
    adding_records, save_info, replace_info, \
    adding_bets, rally_car_pick, rally_result, race_result
import csv
import random
import time

game_over = 'yes'

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
track_list = [
    short_track,
    medium_track,
    long_track
]

field_names_race = {
    'ID',
    'RACE',
    'TRACK',
    'WINNER',
    'TIME'
}

print(' _______  __   __  ______    _______  _______  __   __ ')
print('|       ||  | |  ||    _ |  |   _   ||       ||  | |  |')
print('|       ||  |_|  ||   | ||  |  |_|  ||  _____||  |_|  |')
print('|       ||       ||   |_||_ |       || |_____ |       |')
print('|      _||       ||    __  ||       ||_____  ||       |')
print('|     |_ |   _   ||   |  | ||   _   | _____| ||   _   |')
print('|_______||__| |__||___|  |_||__| |__||_______||__| |__|')
print('               BET YOUR SAVINGS AWAY')
while game_over.lower() == 'yes':

    your_pick = None
    amount_bet = 0
    # Using numbers because it's a small list
    id_race = int(save_info(3))
    id_bet = int(save_info(5))
    balance = int(save_info(1))

    print(' \n ')
    print('                1. New Drag Race 1v1')
    print('                     2. History')
    print('                   3. Previous bets')
    print('                    4. Car stats')
    print('         5. Enter THE CODE for something special')
    print('                      6. Quit')
    print(' \n ')

    menu_pick = choice_check('Choose your action 1 - 6: ', 1, 6)
    if menu_pick == 1:
        first_car = random.choice(car_list)
        second_car = random.choice(car_list)
        while first_car == second_car:
            second_car = random.choice(car_list)

        # TODO: A better way how to style multi-line print()
        print(
            f' \nNext we have the {first_car.name} '
            f'going against the {second_car.name} !!!\n '
        )
        print(f'Looks pretty close: \n{first_car}, \n{second_car}')

        race_track = random.choice(track_list)
        print(f' \nAnd they are gonna have a epic '
              f'showdown on a {race_track.name}!!!\n ')
        race_track_namer = race_track
        race_track1 = race_track.create_track()
        race_track2 = race_track1.copy()

        place_bet = input('Do you want to bet on this race? yes/no: ')
        while place_bet.lower() != 'no' and place_bet.lower() != 'yes':
            print('I am sorry, I did not understand that')
            place_bet = input('Do you want to bet on this race? yes/no: ')

        if place_bet.lower() == 'yes':
            sleep(0.5)
            print(f'Your balance is {balance} gold\n ')
            if balance == 0:
                sleep(0.5)
                print('Looks like you are out of funds, '
                      'BUT we will lend you 100 gold\n ')
                replace_info(1, 100)
                balance = int(save_info(1))

            sleep(0.5)
            # TODO: A better way how to style multi-line print()
            # TODO: No need to make a first line f-string
            #  as no data goes inside that part
            car_bet_pick = choice_check(
                'Do you want to bet on: '
                f'\n1. {first_car.name} '
                f'\n2. {second_car.name} \nPick: ', 1, 2
            )
            if car_bet_pick == 1:
                your_pick = first_car.name
            else:
                your_pick = second_car.name
            # TODO: A better way how to style multi-line print()
            # TODO: No need to make a first line f-string
            #  as no data goes inside that part
            amount_bet = choice_check(
                'How much you want to bet?'
                f' Max bet is {balance}: ', 1, balance
            )

            id_bet += 1
            replace_info(5, id_bet)
        else:
            print('Your Loss :)')

        sleep(0.5)
        print('READY')
        sleep(0.5)
        print('SET')
        sleep(0.5)
        print('GO')
        sleep(0.5)

        start_time = time.time()

        race_time1 = first_car.beginning_race(race_track1)
        race_time2 = second_car.beginning_race(race_track2)
        print(*race_time1, sep='')
        print(*race_time2, sep='')
        sleep(0.5)

        race_time1 = first_car.acceleration_race()
        race_time2 = second_car.acceleration_race()
        print(*race_time1, sep='')
        print(*race_time2, sep='')
        sleep(0.5)

        # TODO: It is okay to leave it so long and split at and
        while first_car.distance < len(first_car.track_length) - 8 \
                and second_car.distance < len(second_car.track_length) - 8:
            race_time1 = first_car.speed_race()
            race_time2 = second_car.speed_race()
            print(*race_time1, sep='')
            print(*race_time2, sep='')
            sleep(0.5)

        while not first_car.distance >= len(first_car.track_length) \
                and not second_car.distance >= len(second_car.track_length):
            race_time1 = first_car.boost_race()
            race_time2 = second_car.boost_race()
            print(*race_time1, sep='')
            print(*race_time2, sep='')
            sleep(0.5)

        end_time = time.time()
        # time.time() gives the time as a float,
        # want to show only minutes and seconds
        stopper = end_time - start_time
        stopper = time.strftime('%M:%S', time.gmtime(stopper))
        winner_is = race_result(first_car, second_car)

        if winner_is == 'Tie':
            print(f'And we have a {winner_is} with the time {stopper}')
        else:
            print(f'And the Winner is {winner_is} with the time {stopper}')

        if your_pick == winner_is:
            # TODO: Fix these lines as I fixed them above
            print(f'Congratulations you WON, '
                  f'\nHere is your reward of {amount_bet * 2} gold')
            replace_info(1, balance + amount_bet)
            result = 'WIN'
            adding_bets(id_bet, amount_bet, result)
        elif place_bet.lower() == 'yes' and your_pick != winner_is:
            print(f'You LOST, Did not see that coming, did you ?')
            replace_info(1, balance - amount_bet)
            result = 'LOSS'
            adding_bets(id_bet, amount_bet, result)

        id_race += 1
        replace_info(3, id_race)

        # TODO: A better argument stylingt
        adding_records(
            id_race,
            '1vs1',
            race_track_namer.name,
            winner_is,
            stopper,
        )

    elif menu_pick == 2:
        with open('race_records.csv', 'r') as race_records_file:
            csv_reader = csv.reader(race_records_file)
            for line in csv_reader:
                print(*line, sep=',  ')

    elif menu_pick == 3:
        with open('bets.csv', 'r') as bets_file:
            csv_reader = csv.reader(bets_file)
            for line in csv_reader:
                print(*line, sep=',  ')

    elif menu_pick == 4:
        sleep(0.5)
        print('Here is the list of our Racers:')
        print(*car_list, sep='\n')

    elif menu_pick == 5:
        code_hack = input('Please enter the code: ')
        # TODO: Nice! :D
        if code_hack.lower() == 'up up down down left lef right right b a':
            # TODO: Rally game and regular 1v1 could be separated
            #  into files or functions resulting in a cleaner code

            # TODO: Fix this print according to the notes above
            print(f' \nNext we will have ALL the cars racing'
                  f' \nAnd they are gonna have a epic '
                  f'showdown on a {long_track.name}!!!\n ')
            sleep(0.5)
            print('Here is the list of our Racers:')
            print(*car_list, sep='\n')

            rally_track = long_track
            rally_track1 = rally_track.create_track()
            rally_track2 = rally_track1.copy()
            rally_track3 = rally_track1.copy()
            rally_track4 = rally_track1.copy()
            rally_track5 = rally_track1.copy()
            rally_track6 = rally_track1.copy()
            rally_track7 = rally_track1.copy()
            rally_track8 = rally_track1.copy()

            place_bet = input('Do you want to bet on this race? yes/no: ')
            while place_bet.lower() != 'no' and place_bet.lower() != 'yes':
                print('I am sorry, I did not understand that')
                place_bet = input('Do you want to bet on this race? yes/no: ')

            if place_bet.lower() == 'yes':
                sleep(0.5)
                print(f'Your balance is {balance} gold\n ')
                if balance == 0:
                    sleep(0.5)
                    # TODO: Fix this print according to the notes above
                    print('Looks like you are out of funds, '
                          'BUT we will lend you 100 gold\n ')
                    replace_info(1, 100)
                    balance = int(save_info(1))

                sleep(0.5)
                # TODO: Fix this print according to the notes above
                car_bet_pick = choice_check(f'What car you want to bet on: '
                                            f'\n1. {blue.name} '
                                            f'\n2. {red.name}'
                                            f'\n3. {green.name}'
                                            f'\n4. {yellow.name}'
                                            f'\n5. {black.name}'
                                            f'\n6. {white.name}'
                                            f'\n7. {orange.name}'
                                            f'\n8. {purple.name} \nPick: ', 1, 8)

                car_bet_pick = rally_car_pick(car_bet_pick)

                # TODO: Fix this print according to the notes above
                amount_bet = choice_check(f'How much you want to bet?'
                                          f' Max bet is {balance}: ', 1, balance)

                id_bet += 1
                replace_info(5, id_bet)
            else:
                print('Your Loss :)')

            sleep(0.5)
            print('READY')
            sleep(0.5)
            print('SET')
            sleep(0.5)
            print('GO')
            sleep(0.5)

            start_time = time.time()

            rally_time1 = blue.beginning_race(rally_track1)
            rally_time2 = red.beginning_race(rally_track2)
            rally_time3 = green.beginning_race(rally_track3)
            rally_time4 = yellow.beginning_race(rally_track4)
            rally_time5 = black.beginning_race(rally_track5)
            rally_time6 = white.beginning_race(rally_track6)
            rally_time7 = orange.beginning_race(rally_track7)
            rally_time8 = purple.beginning_race(rally_track8)

            print(*rally_time1, sep='')
            print(*rally_time2, sep='')
            print(*rally_time3, sep='')
            print(*rally_time4, sep='')
            print(*rally_time5, sep='')
            print(*rally_time6, sep='')
            print(*rally_time7, sep='')
            print(*rally_time8, sep='')
            sleep(0.5)

            rally_time1 = blue.acceleration_race()
            rally_time2 = red.acceleration_race()
            rally_time3 = green.acceleration_race()
            rally_time4 = yellow.acceleration_race()
            rally_time5 = black.acceleration_race()
            rally_time6 = white.acceleration_race()
            rally_time7 = orange.acceleration_race()
            rally_time8 = purple.acceleration_race()

            print(*rally_time1, sep='')
            print(*rally_time2, sep='')
            print(*rally_time3, sep='')
            print(*rally_time4, sep='')
            print(*rally_time5, sep='')
            print(*rally_time6, sep='')
            print(*rally_time7, sep='')
            print(*rally_time8, sep='')
            sleep(0.5)

            while blue.distance < len(blue.track_length) - 8 \
                    and red.distance < len(red.track_length) - 8 \
                    and green.distance < len(green.track_length) - 8 \
                    and yellow.distance < len(yellow.track_length) - 8 \
                    and black.distance < len(black.track_length) - 8 \
                    and white.distance < len(white.track_length) - 8 \
                    and orange.distance < len(orange.track_length) - 8 \
                    and purple.distance < len(purple.track_length) - 8:
                rally_time1 = blue.speed_race()
                rally_time2 = red.speed_race()
                rally_time3 = green.speed_race()
                rally_time4 = yellow.speed_race()
                rally_time5 = black.speed_race()
                rally_time6 = white.speed_race()
                rally_time7 = orange.speed_race()
                rally_time8 = purple.speed_race()

                print(*rally_time1, sep='')
                print(*rally_time2, sep='')
                print(*rally_time3, sep='')
                print(*rally_time4, sep='')
                print(*rally_time5, sep='')
                print(*rally_time6, sep='')
                print(*rally_time7, sep='')
                print(*rally_time8, sep='')
                sleep(0.5)

            while not blue.distance >= len(blue.track_length) \
                    and not red.distance >= len(red.track_length) \
                    and not green.distance >= len(green.track_length) \
                    and not yellow.distance >= len(yellow.track_length) \
                    and not black.distance >= len(black.track_length) \
                    and not white.distance >= len(orange.track_length) \
                    and not green.distance >= len(orange.track_length) \
                    and not purple.distance >= len(purple.track_length):
                rally_time1 = blue.boost_race()
                rally_time2 = red.boost_race()
                rally_time3 = green.boost_race()
                rally_time4 = yellow.boost_race()
                rally_time5 = black.boost_race()
                rally_time6 = white.boost_race()
                rally_time7 = orange.boost_race()
                rally_time8 = purple.boost_race()

                print(*rally_time1, sep='')
                print(*rally_time2, sep='')
                print(*rally_time3, sep='')
                print(*rally_time4, sep='')
                print(*rally_time5, sep='')
                print(*rally_time6, sep='')
                print(*rally_time7, sep='')
                print(*rally_time8, sep='')
                sleep(0.5)

            end_time = time.time()
            stopper = end_time - start_time
            stopper = time.strftime('%M:%S', time.gmtime(stopper))

            winner_is = rally_result()
            if winner_is == 'Tie':
                print(f'And we have a {winner_is} with the time {stopper}')
            else:
                print(f'And the Winner is {winner_is} with the time {stopper}')

            if your_pick == winner_is:
                # TODO: Fix this print according to the notes above
                print(f'Congratulations you WON, '
                      f'\nHere is your reward of {amount_bet * 2} gold')
                replace_info(1, balance + amount_bet)
                result = 'WIN'
                adding_bets(id_bet, amount_bet, result)
            elif place_bet.lower() == 'yes' and your_pick != winner_is:
                print(f'You LOST, Did not see that coming, did you ?')
                replace_info(1, balance - amount_bet)
                result = 'LOSS'
                adding_bets(id_bet, amount_bet, result)

            id_race += 1
            replace_info(3, id_race)

            # TODO: Fix this print according to the notes above
            adding_records(id_race, 'Rally', long_track.name,
                           winner_is, stopper)

        else:
            print('This is not the right CODE')

    elif menu_pick == 6:
        sleep(0.5)
        print(' \n \nUNTIL NEXT TIME!!!\n \n ')
        exit()

    game_over = input('Do you want to go again? yes/no: ')
    while game_over.lower() != 'no' and game_over.lower() != 'yes':
        print('I am sorry, I did not understand that')
        game_over = input('Do you want to go again? yes/no: ')
    if game_over.lower() == 'no':
        sleep(0.5)
        print(' \n \nUNTIL NEXT TIME!!!\n \n ')
        exit()
