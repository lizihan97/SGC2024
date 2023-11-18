import os

EVENTS = ['2x2x2 Cube', '3x3x3 Cube', '4x4x4 Cube', 
          '5x5x5 Cube', '6x6x6 Cube', '7x7x7 Cube',
          '3x3x3 Blindfolded', '3x3x3 Fewest Moves', '3x3x3 One-Handed',
          'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1',
          '4x4x4 Blindfolded', '5x5x5 Blindfolded', '3x3x3 Multi-Blind'
          ]

RANKS = ['Champion', '1st Runner-Up', '2nd Runner-Up']

CATS = ['(Open Category)', '(Singaporean Category)']


CWD = os.getcwd()
TMP = os.path.join(CWD, 'tmp')
OUTPUT = os.path.join(CWD, 'output')


if not os.path.exists(TMP):
    os.mkdir(TMP)

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)


def get_font(region):
    if 'Hong Kong' in region \
        or 'Taipei' in region \
        or 'Taiwan' in region \
        or 'Macau' in region:
        font = 'NotoSansTC-Bold'
    elif 'Korea' in region:
        font = 'NotoSansKR-Bold'
    elif 'Japan' in region:
        font = 'NotoSansJP-Bold'
    elif 'Thailand' in region:
        font = 'NotoSansThai-Bold'
    else:
        font = 'NotoSansSC-Bold'
    return font


def get_name(name):
    foreign_start = name.find('(')

    if foreign_start != -1:
        english_name = name[:foreign_start].strip()
        foreign_name = name[foreign_start:]
    else:
        english_name = name
        foreign_name = None
    
    return english_name, foreign_name