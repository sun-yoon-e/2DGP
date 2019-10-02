from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    x = 400
    while x < 750:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.001)

    y = 90
    while y < 550:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.001)

    while x > 30:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.001)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.001)

    x = 30
    while x < 400 :
       clear_canvas_now()
       grass.draw_now(400, 30)
       character.draw_now(x, 90)
       x = x + 2
       delay(0.001)

    r = 0
    while r < 360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        r = r + 10
        x = x + 30 * math.cos(r / 360 * 2 * math.pi)
        y = y + 30 * math.sin(r / 360 * 2 * math.pi)
        delay(0.05)

close_canvas()
