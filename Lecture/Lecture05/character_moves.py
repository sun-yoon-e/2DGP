from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.
x = 0
while (x < 800):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x, 90)
    x = x+2
    update_canvas()
    delay(0.01)
    get_events() # 딜레이 겟 이벤트를 없애면 모래시계가 나오면서 ..??

close_canvas()

