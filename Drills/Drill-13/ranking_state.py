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

