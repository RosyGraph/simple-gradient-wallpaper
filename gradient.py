#!/usr/bin/env python3
import sys
from random import choice, randint
from PIL import Image, ImageDraw, ImageColor


def random_hex():
    return "#" + "".join(choice("0123456789abcdef") for _ in range(6))


def generate_random_colors():
    return [random_hex() for _ in range(randint(2, 5))]


def png_gradient(path, colors, w=1920, h=1080):
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    gradient_height = int(h / (len(colors) - 1))
    for color_index in range(len(colors) - 1):
        r, g, b = ImageColor.getrgb(colors[color_index])
        dr, dg, db = ImageColor.getrgb(colors[color_index + 1])
        dr = (dr - r) / gradient_height
        dg = (dg - g) / gradient_height
        db = (db - b) / gradient_height
        stop = gradient_height * (color_index + 1)
        for i in range(gradient_height * color_index, stop):
            r, g, b = r + dr, g + dg, b + db
            draw.line((0, i, 1920, i), fill=(int(r), int(g), int(b)))
    img.save(path + ".png", "PNG")


if __name__ == "__main__":
    # set defaults if no filename found
    path = "randomgradient"
    colors = generate_random_colors()
    if len(sys.argv) > 1:
        args = sys.argv[1].split()
        path = args[0]
        if len(args) > 1:
            colors = args[1:]

    png_gradient(path, colors)
