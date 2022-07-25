import math

colors_list = ['R', 'B', 'G']

def triangle(row):
    if len(row) == 1:
        return row
    simple_triangle = small_trianle(row)
    new_len = len(row) - simple_triangle + 1
    if new_len == 1:
        return color(row[0], row[len(row)-1])
    else:
        sub_colors = []
        for i in range(new_len):
            sub_colors.append(color(row[i], row[i+simple_triangle-1]))
        return triangle("".join(sub_colors))

def  small_trianle(arr):
    n = int(math.log(len(arr) - 1, 3))
    return 3**n + 1
 
def color(color1, color2):
    if color1 == color2:
        return color1
    else:
        sub_arr =  list(set(colors_list).difference(set([color1, color2])))
        return sub_arr[0]
