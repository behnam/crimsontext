#!/usr/bin/python
#
# Run from trunk directory like this:
# trunk$ python tools/generate.py

import fontforge
import os
from fontTools.ttLib import TTFont

name = 'Crimson'
styles = ['Roman', 'Semibold', 'Bold', 'Italic', 'SemiboldItalic', 'BoldItalic']
source = 'sources'
build = 'builds'

def getHeights(font):
    # ymax + ymin, using the later as an overshoot
    xHeight = font['x'].boundingBox()[3] + font['x'].boundingBox()[1]
    cHeight = font['H'].boundingBox()[3] + font['H'].boundingBox()[1]

    return int(xHeight), int(cHeight)

def generate(font, extension):
    if extension == 'ttf':
        font.em = 2048
        font.round()
        font.selection.all()
        font.autoHint()
        font.autoInstr()

    path = '%s/%s.%s' %(build, font.fontname, extension)
    tmp_path = '%s.tmp.%s' %(font.fontname, extension)

    font.generate(tmp_path)

    tmp_font = TTFont(tmp_path)
    tmp_font['OS/2'].sxHeight, tmp_font['OS/2'].sCapHeight = getHeights(font)
    tmp_font.save(path)
    tmp_font.close()
    os.remove(tmp_path)

for style in styles:
    f = fontforge.open('%s/%s-%s.sfd' %(source, name, style))

    generate(f, 'otf')
    generate(f, 'ttf')
