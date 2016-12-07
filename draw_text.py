import os
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont


# DEV
BOTDIR = os.getcwd() + '/'

sprite_map_rows = [ ('W', 0, 22, 22),
                    ('@', 22, 44, 20),
                    ('AMVXYZmw%', 44, 66, 14),
                    ('CDGHKNOPQRU#_', 66, 88, 12),
                    ('BEFLSTabcdeghnopquvyk234567890?$^&+=', 88, 110, 10),
                    ('Jsxz/"<>\\', 110, 132, 8),
                    ('1*{}', 132, 154, 6),
                    ('frt()-;[], ', 154, 176, 4),
                    ("ijlI.!':|", 176, 198, 2)
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

def build_sprite_dict(sprite_map, sprite_img):
    """
    Build a dictionary of the actual sprites

    Takes:

        sprite_map: a dictionary of charcters/crop positions
        sprite_img: a PIL image object of the sprite sheet to process

    """

    sprite_dict = {}

    for char, pos in sprite_map.items():
        img = sprite_img.copy()
        img = img.crop(box=pos)
        sprite_dict[char] = img

    return sprite_dict

def composite_msgs(msgs, bg_img, x, y, sprite_dict, char_height=22, kerning=2, line_spacing=5, msg_margin_bottom=20, wrap_width=200, bullet=None):
    """
    Composites a list of of messages to a background image, returning a new copy of
    the composite.

    Takes:

        Required
        - msgs: A list of messages to composite
        - bg_img: The background image to composite text onto
        - x, y: Upper left corner starting coordinates
        - sprite_dict: A dictioanry of sprite PIL image objects (the hacked together win 3.1 font)
    
        Optional
        - char_height: height of characters in font
        - kerning: Amount of space between characters
        - line_spacing: Space between lines in multiple line message
        - msg_margin_bottom: Space between messages
        - wrap_width: maximum width of message 
        - Bullet: Autuomatically add bullet text to beginning of each message

    """

    new_bg_img = bg_img.copy()
    x_pos, x_indent, y_pos = x, x, y
    for msg in msgs:
        
        # Composite bullet before message
        if bullet:
            indent_length = 0
            for char in bullet:
                new_bg_img.paste(sprite_dict[char], (x_pos, y_pos))
                x_pos = x_pos + sprite_dict[char].width + kerning
                indent_length += sprite_dict[char].width + kerning

            x_indent = x + indent_length

        # Split message into lines
        msg = wrap(msg, wrap_width)

        for line in msg:
            for char in line:
                new_bg_img.paste(sprite_dict[char], (x_pos, y_pos))
                x_pos = x_pos + sprite_dict[char].width + kerning

            # New Line, reset X and increment Y
            x_pos = x_indent
            y_pos = y_pos + char_height + line_spacing

        # Reset x-pos and x-indent after each message
        x_pos, x_indent = x, x
        y_pos = y_pos + msg_margin_bottom

    return new_bg_img


def init_chars():
    """
    Build sprite dict and store in memory on program run
    """
    sprite_img = Image.open("%sspritesheet.png" % BOTDIR).convert('RGBA')

    sprite_map = {}
    for row in sprite_map_rows:
        result = build_sprite_map(row[0], row[1], row[2], row[3])
        sprite_map = dict( sprite_map.items() + result.items() )

    sprite_dict = build_sprite_dict(sprite_map, sprite_img)
    return sprite_dict

# Run at startup
chars = init_chars()

# Running in shell for now
# from draw_text import *
# background = Image.open("%stemplates/accessible.png" % BOTDIR).convert('RGBA')
# msgs = ["Large fonts, high-contrast color schemes, large mouse pointers, and pointer trails make your screen easier to read.", "FilterKeys, StickyKeys and MouseKeys make your keyboard and mouse pointer easier to control.", "Ease your sense of existential dread with our Fun Color Themes"]
# result = composite_msgs(msgs, background, 500, 380, chars, wrap_width=57, bullet="-    ")
# result.show()






