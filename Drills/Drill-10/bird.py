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

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 150
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS

        self.frame = 0
        self.frame_x = 0
        self.frame_y = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = self.frame % 5
        if self.frame % 14 == 0:
            self.frame_y = 2
        elif self.frame % 14 == 5:
            self.frame_y = 1
        elif self.frame % 14 == 10:
            self.frame_y = 0

        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1500:
            self.velocity = -RUN_SPEED_PPS
            self.dir = -1
        elif self.x <= 100:
            self.velocity = RUN_SPEED_PPS
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 183, 168, 0.0, 'h', self.x, self.y, 183, 169)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 183, 168, self.x, self.y, 183, 169)
