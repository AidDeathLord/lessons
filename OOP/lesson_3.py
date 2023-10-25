def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)


print(Color.red)  # (255, 0, 0)

print(Color.green == rgb(0, 255, 0))  # True
