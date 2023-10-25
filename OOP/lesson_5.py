class RGB:
    red = 0
    green = 0
    blue = 0


def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
        return rgb.red, rgb.green, rgb.blue


red = RGB()
green = RGB()
blue = RGB()
red.red = 255
green.green = 255
blue.blue = 255

print(rgb2tuple(42))
print(rgb2tuple(red))  # (255, 0, 0)
print(rgb2tuple(green))  # (0, 255, 0)
print(rgb2tuple(blue))
