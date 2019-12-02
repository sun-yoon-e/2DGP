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
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.w = 1800 # self.image.w
        self.h = 1100 # self.image.h
        self.x, self.y, self.fall_speed = random.randint(0, 1800-1), random.randint(0, 1100-1), 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_center_object(self, back):
        # fill here
        self.center_object = back
        pass

    def draw(self):
        # fill here
        tmp_x = clamp(400, main_state.boy.x, 1440)
        tmp_y = clamp(300, main_state.boy.y, 810)
        self.image.draw(self.x - tmp_x + 400, self.y - tmp_y + 300)
        pass

    def update(self):
        # fill here
        self.window_left = clamp(-self.w - self.canvas_width,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)
        pass
