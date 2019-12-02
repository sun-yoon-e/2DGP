import random
from pico2d import *
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.w = 1800
        self.h = 1100
        self.x, self.y, self.fall_speed = random.randint(0, 1800-1), random.randint(0, 1100-1), 0

    def set_center_object(self, b):
        self.center_object = b

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        draw_x = clamp(400, main_state.boy.x, 1440)
        draw_y = clamp(300, main_state.boy.y, 810)
        self.image.draw(self.x - draw_x + 400, self.y - draw_y + 300)
        
    def update(self):
        self.window_left = clamp(-self.w - self.canvas_width,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)
        pass
