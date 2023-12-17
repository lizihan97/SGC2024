import fpdf
import pypdf
import pandas as pd
import sys
import os


if len(sys.argv) > 1:
    CSV = sys.argv[1]
else:
    CSV = 'reg.csv'

CWD = os.getcwd()
TMP = os.path.join(CWD, 'tmp')
OUTPUT = os.path.join(CWD, 'output')


if not os.path.exists(TMP):
    os.mkdir(TMP)

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)


TEMPLATE_PDF = os.path.join(CWD, 'templates/template_tag.pdf')
TAG_PDF = os.path.join(OUTPUT, 'tag_competitor.pdf')
NAME_CSV = os.path.join(CWD, CSV)
NAME_PDF = os.path.join(TMP, 'names_tag.pdf')

CENTER_X = 30 # center of the page
ID_Y = 110 # y of competitor id
NAME_Y = ID_Y + 50 # y of competitor name
FOREIGN_NAME_Y = NAME_Y + 35 # y of competitor's non-english name

EVENT_X = 38 # x of the first event icon
EVENT_Y = 250 # y of the first event icon
ID_SIZE = 40 # font size of competitor id
FONT_SIZE = 25 # default font size of competitor name

SHOW_EVENT = True
DOUBLE_SIDE = True
ICON_SIZE = 15 # width of event icons
SPACE = 7 # horizontal space between event icons
VERTICAL_SPACE = 7 # line space between event icons
TEMPLATE_SIZE = (266,379) # size of the tag template pdf

ALL_FONTS = os.listdir(os.path.join(CWD, 'fonts'))


pdf = fpdf.FPDF(format=TEMPLATE_SIZE, unit='pt')


for font in ALL_FONTS:
    pdf.add_font(fname=os.path.join(CWD, 'fonts', font))


names = pd.read_csv(NAME_CSV)


ICONS = ['333', '222', '444', '555', '666', '777', 
         '333bf', '333fm', '333oh', 'clock', 
         'minx', 'pyram', 'skewb', 'sq1', 
         '444bf', '555bf', '333mbf']


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


def adjust_font_size(long_name, default_size):
    if len(long_name) <= 18:
        return default_size
    elif 25 <= len(long_name) < 30:
        return default_size - 10
    elif len(long_name) >= 30:
        return default_size - 15
    else:
        return default_size + 15 - len(long_name)


for i, row in names.iterrows():
    id = row['ID']
    name = row['Name']
    region = row['Region']


    font = get_font(region)
    english_name, foreign_name = get_name(name)
    adjusted_font_size = adjust_font_size(english_name, FONT_SIZE)


    pdf.add_page()

    pdf.set_font(family=font, size=ID_SIZE)
    pdf.set_xy(CENTER_X, ID_Y)
    pdf.cell(0, text=str(id), align='C')


    if foreign_name:
        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')

        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, FOREIGN_NAME_Y)
        pdf.cell(0, text=foreign_name, align='C')
    else:
        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, NAME_Y+20)
        pdf.cell(0, text=english_name, align='C')


    if SHOW_EVENT:
        icon_x = EVENT_X
        for icon in ICONS[:9]:
            color = 'black' if row[icon] == 1 else 'white'
            pdf.image('icons_{}/{}.svg'.format(color,icon), x=icon_x, y=EVENT_Y, w=ICON_SIZE)
            icon_x += ICON_SIZE + SPACE
        
        icon_x = EVENT_X + (ICON_SIZE + SPACE) / 2
        for icon in ICONS[9:]:
            color = 'black' if row[icon] == 1 else 'white'
            pdf.image('icons_{}/{}.svg'.format(color,icon), x=icon_x, y=EVENT_Y+ICON_SIZE+VERTICAL_SPACE, w=ICON_SIZE)
            icon_x += ICON_SIZE + SPACE
    
    # back
    pdf.add_page()

    pdf.set_font(family=font, size=ID_SIZE)
    pdf.set_xy(CENTER_X, ID_Y)
    pdf.cell(0, text=str(id), align='C')


    if foreign_name:
        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')

        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, FOREIGN_NAME_Y)
        pdf.cell(0, text=foreign_name, align='C')
    else:
        pdf.set_font(family=font, size=adjusted_font_size)
        pdf.set_xy(CENTER_X, NAME_Y+20)
        pdf.cell(0, text=english_name, align='C')


pdf.output(NAME_PDF)


name_pdf = pypdf.PdfReader(open(NAME_PDF, 'rb'))
tag_pdf = pypdf.PdfWriter()

i = 0

for name_page in name_pdf.pages:
    template_pdf = pypdf.PdfReader(open(TEMPLATE_PDF, 'rb'))
    template_page = template_pdf.pages[i]
    template_page.merge_page(name_page)
    tag_pdf.add_page(template_page)
    if DOUBLE_SIDE:
        i = 1 - i

tag_pdf.write(open(TAG_PDF, 'wb'))