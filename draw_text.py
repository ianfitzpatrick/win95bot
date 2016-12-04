import os
from PIL import Image, ImageDraw, ImageFont
from gen_messages import get_lines

# DEV
BOTDIR = os.getcwd() + '/'

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
	
	for idx, char in enumerate('abcdeghnopquvyk'):
		sprite_map[char] = (idx * 10,  22, (idx * 10) + 10, 45)

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
		bg_img.paste(sprite_sheet[char], (x, y))
		x = x + char_width + kerning

# Running in shell for now

# Create canvas
background = Image.open("%stemplates/accessible.png" % BOTDIR).convert('RGBA')
sprite_img = Image.open("%stemplates/font/spritesheet.png" % BOTDIR).convert('RGBA')


background = Image.open("%stemplates/accessible.png" % BOTDIR).convert('RGBA')
print_sprites('abc', 500, 400, sprite_sheet, background)
background.show()









