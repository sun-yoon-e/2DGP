from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 - event.y
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
hand = load_image('hand_arrow')
character = load_image('animation_sheet')
kpu_ground = load_image('KPU_GROUND')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()