import os
from PIL import Image, ImageDraw, ImageFont

# DEV
BOTDIR = os.getcwd() + '/'

sprite_map_rows = [ ('W', 0, 22, 22),
                    ('@', 22, 44, 20),
                    ('AMVXYZmw%', 44, 66, 14),
                    ('CDGHKNOPQRU#', 66, 88, 12),
                    ('BEFLTSabcdeghknopquvy234567890?$^&+', 88, 110, 10),
                    ('J/"', 110, 132, 8),
                    ('sxz1*', 132, 154, 6),
                    ('frt()-;[]', 154, 176, 4),
                    ("ijlI.!':", 176, 198, 2)
                    ] 


def build_sprite_map(chars, top, bottom, width):
    """
    Automatically build a sprite map dictionary.

    Takes:
    
        chars: String of characters like 'abcde'
        top: X of top row of sprites
        bottom: X of bottom of row of sprites
        width: the width of each sprite
    """

    sprite_map = {}
    
    for idx, char in enumerate(chars):
        sprite_map[char] = (idx * width,  top, (idx * width) + width, bottom)

    return sprite_map

def build_sprite_sheet(sprite_map, sprite_img):
    """
    Build a dictionary of the actual sprites

    Takes:

        sprite_map: a dictionary of charcters/crop positions
        sprite_img: a PIL image object of the sprite sheet to process

    """

    sprite_sheet = {}

    for char, pos in sprite_map.items():
        img = sprite_img.copy()
        img = img.crop(box=pos)
        sprite_sheet[char] = img

    return sprite_sheet

def print_sprites(text, x, y, sprite_sheet, bg_img, char_width=10, kerning=2):

    for char in text:

        # Print character unless it's a space
        if char != ' ':
            bg_img.paste(sprite_sheet[char], (x, y))

        x = x + char_width + kerning


def init_chars():
    sprite_img = Image.open("%sspritesheet.png" % BOTDIR).convert('RGBA')

    sprite_map = {}
    for row in sprite_map_rows:
        result = build_sprite_map(row[0], row[1], row[2], row[3])
        sprite_map = dict( sprite_map.items() + result.items() )

    sprite_sheet = build_sprite_sheet(sprite_map, sprite_img)
    return sprite_sheet

# Run at startup
chars = init_chars()

# Running in shell for now
# print_sprites('W', 500, 400, sprite_sheet, background)
# background.show()











