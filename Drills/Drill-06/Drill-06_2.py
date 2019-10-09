from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def character_draw(p1, p2, p3, p4):
    global character, kpu_ground
    character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
    character_d = 3
    frame = 0
    global t_x, t_y
    for i in range(0, 100, 2):
        if i > 95:
            t_x, t_y = x, y

        if t_x - character_x < 0:
            character_d = 1
        elif t_x - character_x > 0:
            character_d = 0

        t = i / 100
        x = ((-t**3+2*t**2-t)*p1[0]+(3*t**3-5*t**2+2)*p2[0]+(-3*t**3+4*t**2+t)*p3[0]+(t**3-t**2)*p4[0])/ 2
        y = ((-t**3+2*t**2-t)*p1[1]+(3*t**3-5*t**2+2)*p2[1]+(-3*t**3+4*t**2+t)*p3[1]+(t**3-t**2)*p4[1])/ 2

        move_x = (t_x - character_x) / 20
        move_y = (t_y - character_y) / 20
        character_x += move_x
        character_y += move_y

        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100, 100 * 0, 100, 100, t_x, t_y)
        character.clip_draw(frame * 100, character_d * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

t_x, t_y = -100, -100
count = 10
point = 3
points = [(random.randint(0, KPU_WIDTH-100), random.randint(0, KPU_HEIGHT-100)) for i in range(count)]

while True:
    character_draw(points[point - 3], points[point - 2], points[point - 1], points[point])
    point = (point + 1) % count
