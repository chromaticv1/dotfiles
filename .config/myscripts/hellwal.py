import subprocess
import json
import colorsys

def get_sorted_colors(img_path):  
    hw_o = subprocess.check_output(f"hellwal -i {img_path} --skip-term-colors -j",
                            shell=True)
    colors =json.loads(hw_o)['colors'].values()

    colors = list([x for x in colors])
    sep_colors = []
    for color in colors:
        sep_colors.append (tuple(map(lambda x: int(x, base=16),(color[1:3], color[3:5],color[5:7]))))

    def convert_to(col: tuple, kind='hsl') -> tuple:
        r = col[0]/255.0
        g = col[1]/255.0
        b = col[2]/255.0
        converter = colorsys.hls_to_rgb if kind=='rgb' else colorsys.rgb_to_hls
        rv = tuple(map(lambda x: round(255*x),converter(r,g,b)))
    
        return rv

    hls_colors = []
    for color in sep_colors:
        hls_colors.append(convert_to(color))

    hls_colors.sort(key = lambda x: (x[2], x[1]), reverse=True)

    sorted_colors = []
    for hls_col in hls_colors:
        sorted_colors.append(convert_to(hls_col, 'rgb'))

    hex_cols = []
    for col in sorted_colors:
        hex_cols.append(
            ''.join(map(lambda x: str(hex(x))[2:] ,col))
        )
    return hex_cols
