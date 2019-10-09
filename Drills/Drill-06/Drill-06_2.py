from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def character_draw(p1, p2, p3, p4):
    global KPU, character
    character_dir = 3
    frame = 0
    global t_x, t_y
    for i in range(0, 100, 2):
        if i > 95:
            t_x, t_y = x, y

        t = i / 100
        x = ((-t**3+2*t**2-t)*p1[0]+(3*t**3-5*t**2+2)*p2[0]+(-3*t**3+4*t**2+t)*p3[0]+(t**3-t**2)*p4[0])/ 2
        y = ((-t**3+2*t**2-t)*p1[1]+(3*t**3-5*t**2+2)*p2[1]+(-3*t**3+4*t**2+t)*p3[1]+(t**3-t**2)*p4[1])/ 2

        clear_canvas()
        #kpu_ground.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT, KPU_WIDTH / 2, KPU_HEIGHT / 2)
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100, 100 * 3, 100, 100, t_x, t_y)
        character.clip_draw(frame * 100, character_dir * 100, 100, 100, x, y)
        update_canvas()
        delay(0.02)

    update_canvas()

open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

t_x, t_y = -100, -100
count = 10
point = 3
points = [(random.randint(0, 1280-200), random.randint(0, 1024-200)) for i in range(count)]

while True:
    character_draw(points[point - 3], points[point - 2], points[point - 1], points[point])
    point = (point + 1) % count