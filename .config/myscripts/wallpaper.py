import os
import random


debug = False
def dp(args):
    if debug: print(args)

home = os.path.expanduser('~')

local_storage = (f'{home}/.config/myscripts/localStorage')
dp(os.listdir(local_storage))
if 'wallpaperIndex' not in os.listdir(local_storage):
    dp('WP Index not found!, creating index')
    with open(f'{local_storage}/wallpaperIndex', 'w') as fp:
        fp.write("0")
else:
    dp('WP index found! reading')
    with open(f'{local_storage}/wallpaperIndex') as fp:
        current_index = int(fp.read())
        dp(f'old WP index is {current_index}')
# Wallpaper randomzier
wallpapers_dir = f"{home}/Pictures/wallpapers"
pictures = os.listdir(wallpapers_dir)

n = len(pictures)
dp(f'number of pictures: {n}')
indices = list(range(n))
indices.remove(current_index)
dp(indices)

new_indices_index = random.randint(0, len(indices)-1)
new_index = indices[new_indices_index]
dp(f"new number is {new_index}")

os.system(f'swww img {wallpapers_dir}/{pictures[new_index]}')
with open(f'{local_storage}/wallpaperIndex', 'w') as fp:
        fp.write(str(new_index))
