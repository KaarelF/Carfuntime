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

    def get_beginning_race_track_length(self, z):
        self.track_length = z
        self.track_length.insert(0, self.init)
        return self.track_length

    def get_acceleration_race_track_length(self):
        acceleration = random.randint(self.acc[0], self.acc[-1])
        if acceleration - 1 == 0:
            self.track_length.pop(acceleration)
            self.track_length.insert(0, '|')
        else:
            for i in range(acceleration - 1):
                self.track_length.insert(0, '_')
                self.track_length.pop(-2)
                self.distance += 1
            self.track_length.pop(acceleration)
            self.track_length.insert(0, '|')
        self.distance += 1
        return self.track_length

    def get_speed_race_track_length(self):
        speed = random.randint(self.speed[0], self.speed[-1])
        for i in range(speed):
            self.track_length.insert(1, '_')
            self.track_length.pop(-2)
            self.distance += 1
        return self.track_length

    def get_boost_race_track_length(self):
        speed = random.randint(self.speed[0], self.speed[-1])
        boost = random.randint(self.boost[0], self.boost[-1])
        for i in range(speed + boost):
            if speed + boost == 0:
                break
            elif self.distance == len(self.track_length) - 2:
                self.track_length.pop(-1)
                self.track_length.insert(1, '_')
                self.distance += 1
            elif self.distance < len(self.track_length) - 2:
                self.track_length.pop(-2)
                self.track_length.insert(1, '_')
                self.distance += 1
            else:
                self.track_length.pop(1)
                self.track_length.insert(-1, '|')
                self.distance += 1
                break
        return self.track_length
