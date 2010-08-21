#!/usr/bin/python

import fontforge

files = [
'CrimsonText-Roman.sfd',
'crimson_text_italic.sfd',
'crimson_text_semibold.sfd',
'crimson_text_semibold_italic.sfd',
'crimson_text_bold.sfd',
'crimson_text_bold_italic.sfd'
]

for font in files:
    f = fontforge.open(font)
    f.generate('builds/' + f.fontname + '.otf')
