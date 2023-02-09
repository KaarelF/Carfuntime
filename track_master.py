
class Track:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.track = ['|', '_', '_', '_', '_', '_', '_', '_', '_']
        self.track_info = None

    def create_track(self):
        track_segment = '_'
        for i in range(self.length - 1):
            self.track.append(track_segment)
        self.track.append('|')
        return self.track

    def get_track_info(self):
        return f'{self.name}: ' \
               f'\nTrack length is {len(self.track)} ' \
               f'\nand it looks like: {self.track}'
