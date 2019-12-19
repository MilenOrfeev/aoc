from aoc_utils import load_digits
import task8_1


def draw(layers):
    layer_size = len(layers[0])
    for pic_index in range(layer_size):
        if pic_index % 25 == 0:
            print()

        layer_index = 0
        while layers[layer_index][pic_index] == 2:
            layer_index += 1
        colour = layers[layer_index][pic_index]
        if colour == 1:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print()


def solve():
    w, h = 25, 6
    digits = load_digits("input8.txt")
    layers = task8_1.split(digits, w * h)
    draw(layers)
