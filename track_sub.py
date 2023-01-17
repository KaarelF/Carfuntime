from track_master import Track
import random

short_track = Track(
    name='Short Track',
    length=random.randint(10, 15)
)

medium_track = Track(
    name='Medium Track',
    length=random.randint(16, 25),
)

long_track = Track(
    name='Long Track',
    length=random.randint(26, 40)
)
