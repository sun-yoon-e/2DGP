import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
        self.plus_x = 0
        self.brick = main_state.brick
        self.collide = False
        self.init = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.collide == False:
            self.y -= self.fall_speed * game_framework.frame_time
        if self.collide and self.init:
            self.x = self.brick.x + self.plus_x
            self.y = self.brick.y + 40

    def stop(self):
        self.fall_speed = 0


class BigBall(Ball):
    MIN_FALL_SPEED = 50   # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.brick = main_state.brick
        self.collide = False
        self.init = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20