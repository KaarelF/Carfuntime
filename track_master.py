
class Track:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.track_length = ['|', '_', '_', '_', '_', '_', '_', '_', '_']

    def create_track(self):
        x = '_'
        for i in range(self.length - 1):  # range(a-1) cause the last line on a track is |
            self.track_length.append(x)
        self.track_length.append('|')
        return self.track_length

    def track_info(self):   # This is not in use, but it's good for info when I need corrections
        return f'{self.name}: ' \
               f'\nTrack length is {len(self.track_length)} ' \
               f'\nand it looks like: {self.track_length}'
