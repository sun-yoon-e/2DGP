from pico2d import *

font = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    pass

def update():
    pass

def draw():
    font.draw(640, 512, 'game_over', (255, 255, 0))