#!/usr/bin/python
#
# Run from trunk directory like this:
# trunk$ python tools/generate.py

import fontforge
import os
from fontTools.ttLib import TTFont

def getHeights(font):
    return int(font['x'].boundingBox()[3]), int(font['H'].boundingBox()[3])

files = [
'Crimson-Italic.sfd',
'Crimson-Roman.sfd',
'Crimson-SemiboldItalic.sfd',
'Crimson-Semibold.sfd',
'Crimson-BoldItalic.sfd',
'Crimson-Bold.sfd'
]

for font in files:
    f = fontforge.open('sources/' + font)

    path = 'builds/' + f.fontname
    tmp_path = path + '.tmp'

    f.generate(tmp_path + '.otf')

    ff = TTFont(tmp_path + '.otf')
    ff['OS/2'].sxHeight, ff['OS/2'].sCapHeight = getHeights(f)
    ff.save(path + '.otf')
    ff.close()
    os.remove(tmp_path + '.otf')

    f.em = 2048
    f.round()
    f.selection.all()
    f.autoHint()
    f.autoInstr()
    f.generate(tmp_path + '.ttf')

    ff = TTFont(tmp_path + '.ttf')
    ff['OS/2'].sxHeight, ff['OS/2'].sCapHeight = getHeights(f)
    ff.save(path + '.ttf')
    ff.close()
    os.remove(tmp_path + '.ttf')
