import fpdf
import pypdf
import pandas as pd
import sys
from common import *


if len(sys.argv) > 1:
    CSV = sys.argv[1]
else:
    CSV = 'reg.csv'


TEMPLATE_PDF = os.path.join(CWD, 'templates/template_tag.pdf')
TAG_PDF = os.path.join(OUTPUT, 'tag_competitor.pdf')
NAME_CSV = os.path.join(CWD, CSV)
NAME_PDF = os.path.join(TMP, 'names_tag.pdf')

CENTER_X = 30
ID_Y = 300
NAME_Y = ID_Y + 120
FOREIGN_NAME_Y = NAME_Y + 90

EVENT_X = 135
EVENT_Y = 680
ID_SIZE = 100
FONT_SIZE = 60

SHOW_EVENT = True
ICON_SIZE = 40

ALL_FONTS = os.listdir(os.path.join(CWD, 'fonts'))


pdf = fpdf.FPDF(format=(709,1001), unit='pt')


for font in ALL_FONTS:
    pdf.add_font(fname=os.path.join(CWD, 'fonts', font))


names = pd.read_csv(NAME_CSV)


ICONS = ['333', '222', '444', '555', '666', '777', 
         '333bf', '333fm', '333oh', 'clock', 
         'minx', 'pyram', 'skewb', 'sq1', 
         '444bf', '555bf', '333mbf']


def reduce_font_size(long_name):
    if len(long_name) <= 18:
        return 0
    else:
        return len(long_name) - 5


for i, row in names.iterrows():
    id = row['ID']
    name = row['Name']
    region = row['Region']


    font = get_font(region)
    english_name, foreign_name = get_name(name)
    s = reduce_font_size(english_name)


    pdf.add_page()

    pdf.set_font(family=font, size=ID_SIZE)
    pdf.set_xy(CENTER_X, ID_Y)
    pdf.cell(0, text=str(id), align='C')


    if foreign_name:
        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')

        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, FOREIGN_NAME_Y)
        pdf.cell(0, text=foreign_name, align='C')
    else:
        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, NAME_Y+20)
        pdf.cell(0, text=english_name, align='C')


    if SHOW_EVENT:
        icon_x = EVENT_X
        for icon in ICONS[:9]:
            color = 'black' if row[icon] == 1 else 'white'
            pdf.image('icons_{}/{}.svg'.format(color,icon), x=icon_x, y=EVENT_Y, w=ICON_SIZE)
            icon_x += ICON_SIZE + 10
        
        icon_x = EVENT_X + (ICON_SIZE + 10) / 2
        for icon in ICONS[9:]:
            color = 'black' if row[icon] == 1 else 'white'
            pdf.image('icons_{}/{}.svg'.format(color,icon), x=icon_x, y=EVENT_Y+ICON_SIZE+20, w=ICON_SIZE)
            icon_x += ICON_SIZE + 10
    
    # back
    pdf.add_page()

    pdf.set_font(family=font, size=ID_SIZE)
    pdf.set_xy(CENTER_X, ID_Y)
    pdf.cell(0, text=str(id), align='C')


    if foreign_name:
        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')

        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, FOREIGN_NAME_Y)
        pdf.cell(0, text=foreign_name, align='C')
    else:
        pdf.set_font(family=font, size=FONT_SIZE-s)
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
    i = 1 - i

tag_pdf.write(open(TAG_PDF, 'wb'))