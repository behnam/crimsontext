#!/usr/bin/python
#
# When SFDs are in ./sources/ and a ./builds/ directory exists, run this with
# $ python tools/generate.py

import fontforge

files = [
'CrimsonText-Italic.sfd',
'CrimsonText-Roman.sfd',
'CrimsonText-SemiboldItalic.sfd',
'CrimsonText-Semibold.sfd',
'CrimsonText-BoldItalic.sfd',
'CrimsonText-Bold.sfd'
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
