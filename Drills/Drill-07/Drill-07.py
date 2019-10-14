from pico2d import *
import random

# Game object class here
class Boy:
    def __init__(self):
        #self.x, self.y = 0, 90
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Small:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
        self.move = random.randint(5, 10)

    def update(self):
        self.y -= self.move
        if self.y <= 65:
            self.y = 65

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Big:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
        self.move = random.randint(5, 10)

    def update(self):
        self.y -= self.move
        if self.y <= 65:
            self.y = 65

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

small = random.randint(5, 10)
big = 20 - small
small_ball = [Small() for i in range(small)]
big_ball = [Big() for i in range(big)]
#boy = Boy()
team = [Boy() for i in range(11)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    #boy.update()
    for boy in team:
        boy.update()
    for ball in small_ball:
        ball.update()
    for ball in big_ball:
        ball.update()

    clear_canvas()
    grass.draw()
    #boy.draw()
    for boy in team:
        boy.draw()
    for ball in small_ball:
        ball.draw()
    for ball in big_ball:
        ball.draw()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()