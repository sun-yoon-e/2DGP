import game_framework
from pico2d import *

import game_world

# Bird Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10pixel 30cm
RUN_SPEED_KMPH = 30.0 #km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#TIME_PER_ACTION = 0.5
#ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
#FRAMES_PER_ACTION = 5


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 150
        self.image = load_image('bird_animation.png')
        self.dir = -1
        self.velocity = RUN_SPEED_PPS
        self.frame_x = 0
        self.frame_y = 0

    def update(self):
        self.frame_x = (self.frame_x + 1) % 5
        self.frame_y = (self.frame_y + 1) % 3
        if self.frame_x == 5 and self.frame_y == 3:
            self.frame_x = 0
            self.frame_y = 0

        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1500:
            self.velocity = -RUN_SPEED_PPS
            self.dir = 1
        elif self.x <= 100:
            self.velocity = RUN_SPEED_PPS
            self.dir = -1
        delay(0.05)

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame_x) * 183, int(self.frame_y) * 168, 183, 168, 0.0, 'h', self.x, self.y, 184, 169)
        elif self.dir == -1:
            self.image.clip_draw(int(self.frame_x) * 183, int(self.frame_y) * 168, 183, 168, self.x, self.y)
