import random


class Car:
    def __init__(self, name, init, acc, speed, boost):
        self.name = name
        self.init = init
        self.acc = acc
        self.speed = speed
        self.boost = boost
        self.track_length = None
        self.distance = 0

    def __repr__(self):
        return f'{self.name}: ' \
               f'Acceleration: {self.acc[-1]} ' \
               f'Speed: {self.speed[-1]} ' \
               f'Boost: {self.boost[-1]}'

    # TODO: If in all these methods you return the track_length,
    #  the consider naming the methods like get_beginning_race_track_length()
    def beginning_race(self, z):
        self.track_length = z
        self.track_length.insert(0, self.init)
        return self.track_length

    def acceleration_race(self):
        a1 = random.randint(self.acc[0], self.acc[-1])
        if a1-1 == 0:
            self.track_length.pop(a1)
            self.track_length.insert(0, '|')
            self.distance += 1
        else:
            for i in range(a1-1):
                self.track_length.insert(0, '_')
                self.track_length.pop(-2)
                self.distance += 1
            self.track_length.pop(a1)
            self.track_length.insert(0, '|')
            # TODO: So if in all cases self.distance += 1
            #  should we replicate it, or left at the end of the loop
            self.distance += 1

        return self.track_length

    def speed_race(self):
        # TODO: Do not leave spaces after method def
        # TODO: Avoid using one letter variables
        s = random.randint(self.speed[0], self.speed[-1])
        for i in range(s):
            self.track_length.insert(1, '_')
            self.track_length.pop(-2)
            self.distance += 1

        return self.track_length

    def boost_race(self):
        # TODO: Do not leave spaces after method def
        # TODO: Avoid using one letter variables

        # TODO: So basically s = b ?
        s = random.randint(self.speed[0], self.speed[-1])
        b = random.randint(self.boost[0], self.boost[-1])

        # TODO: Spaces before and after + operator
        for i in range(b+s):
            if b+s == 0:
                break
            # TODO: Spaces before and after - operator
            elif self.distance == len(self.track_length)-2:
                self.track_length.pop(-1)
                self.track_length.insert(1, '_')
                self.distance += 1
            # TODO: Spaces before and after - operator
            elif self.distance < len(self.track_length)-2:
                self.track_length.pop(-2)
                self.track_length.insert(1, '_')
                self.distance += 1
            else:
                # TODO: So if in all cases self.distance += 1
                #  should we replicate it, or left at the end of the loop
                self.distance += 1
                self.track_length.pop(1)
                self.track_length.insert(-1, '|')
                break
        return self.track_length
