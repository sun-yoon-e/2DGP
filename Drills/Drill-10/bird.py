import game_framework
from pico2d import *

import game_world

# Bird Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10pixel 30cm
RUN_SPEED_KMPH = 20.0 #km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 150
        self.image = load_image('bird_animation.png')
        self.dir = -1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1500:
            self.velocity = -RUN_SPEED_PPS
            self.dir = 1
        elif self.x <= 100:
            self.velocity = RUN_SPEED_PPS
            self.dir = -1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 184, int(self.frame) * 169, 184, 169, 0.0, 'h', self.x, self.y, 184, 169)
        elif self.dir == -1:
            self.image.clip_draw(int(self.frame) * 184, int(self.frame) * 169, 184, 169, self.x, self.y)
