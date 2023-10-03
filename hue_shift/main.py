import colorsys
import random


def return_color():
    # Generate random RGB values
    r, g, b = random.random(), random.random(), random.random()

    # Convert RGB values to HSV
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    # Convert HSV back to RGB with saturation and value set to maximum for a bright color
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)

    # Convert RGB values (0 to 1 range) to an ANSI escape code
    return f"\033[38;2;{int(r * 255)};{int(g * 255)};{int(b * 255)}m"


def reset():
    return "\033[0m"
