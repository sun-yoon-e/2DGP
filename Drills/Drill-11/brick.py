from pico2d import *
import game_framework
import game_world


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 200
        self.dir = 1
        self.speed = 300

    def update(self):
        self.x += self.dir * self.speed * game_framework.frame_time

        if self.x <= 0 + 90:
            self.dir = 1
        elif self.x >= 1600 - 90:
            self.dir = -1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

