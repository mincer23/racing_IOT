#!/usr/bin/env python

# import time
# from colorsys import hsv_to_rgb
import pygame
from PIL import Image, ImageDraw, ImageFont
from ST7789 import ST7789


SPI_SPEED_MHZ = 80

width = 240
height = 240
image = Image.new("RGB", (240, 240), (255, 178, 102))
draw = ImageDraw.Draw(image)
center = (width // 2, height // 2)

pygame.init()
screen = pygame.display.set_mode((240,240))


st7789 = ST7789(
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,       # SPI port
    cs=1,         # SPI port Chip-select channel
    dc=9,         # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000
)

background = [0,0,153]
lines = [0,153,153]

# Define gear positions
gear_positions = {
    1: (center[0] - 30, center[1] - 30),
    2: (center[0] - 30, center[1] + 30),
    3: (center[0], center[1] - 30),
    4: (center[0], center[1] + 30),
    5: (center[0] + 30, center[1] - 30),
    'R': (center[0] + 30, center[1] + 30),
}

# Draw lines connecting the gear positions
draw.line((gear_positions[1], gear_positions[2]), fill="teal", width=5)
draw.line((gear_positions[3], gear_positions[4]), fill="teal", width=5)
draw.line((gear_positions[5], gear_positions['R']), fill="teal", width=5)

# center line
draw.line(((center[0] - 30 , center[1]), (center[0] + 30, center[1])), fill="teal", width=5)
# draw.line((gear_positions[4], gear_positions['R']), fill="teal", width=5)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", size=15)
except IOError:
    print("font error")
    font = ImageFont.load_default()

top_set = [1,3,5]
bot_set = [2,4,'R']

# Draw gear numbers
for gear, pos in gear_positions.items():
    if gear in top_set:
        draw.text((pos[0] - 3 , pos[1] - 18), str(gear), fill="teal", font=font)
    elif gear in bot_set:
        draw.text((pos[0] -3 , pos[1] + 6), str(gear), fill="teal", font=font)

image.show()
st7789.display(image)
