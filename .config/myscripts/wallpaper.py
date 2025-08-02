import os
import random

debug = False
def dp(args):
    if debug: print(args)

home = os.path.expanduser('~')
wallpapers_dir = f"{home}/Pictures/wallpapers"
pictures = os.listdir(wallpapers_dir)

current_index = random.randint(0, len(pictures)-1)
dp(pictures[current_index])

os.system(f'swww img {wallpapers_dir}/{pictures[current_index]}')
