#!/usr/bin/python
#
# Run from trunk directory like this:
# trunk$ python tools/generate.py

import fontforge

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
    f.generate('builds/' + f.fontname + '.otf')
    f.em = 2048
    f.round()
    f.selection.all()
    f.autoHint()
    f.autoInstr()
    f.generate('builds/' + f.fontname + '.ttf')
