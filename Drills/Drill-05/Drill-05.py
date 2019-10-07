from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global end_x, end_y
    global character_x, character_y
    global character_dir

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            character_dir = 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            end_x, end_y = event.x - 25, KPU_HEIGHT - 1 - event.y + 25
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_d = 3
end_x = character_x
end_y = character_y
frame = 0
hide_cursor()

while running:
    move_x = (end_x - character_x) / 20
    move_y = (end_y - character_y) / 20
    character_x += move_x
    character_y += move_y

    if end_x - character_x < 0:
        character_d = 0
    elif end_x - character_x > 0:
        character_d = 1
    elif end_x - character_x == 0:
        character_d = 3

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    character.clip_draw(frame * 100, 100 * character_d, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()