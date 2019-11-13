from pico2d import *
import game_framework
import game_world


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 200

    def update(self):
        

    def draw(self):
        self.image.draw(500, 200)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

