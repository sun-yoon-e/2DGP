import json
import pickle
import os

from pico2d import *
import game_world
import game_framework
import world_build_state

font = None
time = None

ranking = []


def enter():
    global font, ranking
    if font is None:
        font = load_font('ENCR10B.TTF', 20)

    with open('ranking.txt', 'r') as f:
        ranking = json.load(f)

    ranking.append(time)
    ranking.sort()
    ranking.reverse()

    while ranking.__len__() > 10:
        ranking.remove(ranking[-1])

    with open('ranking.txt', 'w') as f:
        json.dump(ranking, f)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    for game_object in game_framework.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(int(40 * 100 / 3) // 2 - 80,  int(30 * 100 / 3) // 2 + 250, "[Total Ranking]")

    for i in range(0, ranking.__len()):
        font.draw(int(40 * 100 / 3) // 2 - 80,  int(30 * 100 / 3) // 2 + 80 * i,
                  "#" + str(i + 1) + "." + '%.2f' % ranking[i])

    update_canvas()
