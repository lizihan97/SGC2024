import fpdf
import pypdf
import pandas as pd
import sys
import common
import os


if len(sys.argv) > 1:
    CSV = sys.argv[1]
else:
    CSV = 'reg.csv'


TEMPLATE_PDF = os.path.join(common.CWD, 'templates/template_cop.pdf')
COP_PDF = os.path.join(common.OUTPUT, 'cert_cop.pdf')
NAME_CSV = os.path.join(common.CWD, CSV)
NAME_PDF = os.path.join(common.TMP, 'names_cop.pdf')

CENTER_X = 30
NAME_Y = 350
FONT_SIZE = 40
ENGLISH_NAME_Y = NAME_Y - 30
FOREIGN_NAME_Y = NAME_Y + 20
SMALL_FONT_SIZE = 35

ALL_FONTS = os.listdir(os.path.join(common.CWD, 'fonts'))
ENGLISH_FONT = 'Amaranth-Bold'


pdf = fpdf.FPDF(format='A4', unit='pt')


for font in ALL_FONTS:
    pdf.add_font(fname=os.path.join(common.CWD, 'fonts', font))


names = pd.read_csv(NAME_CSV)


def reduce_font_size(long_name):
    if len(long_name) > 30:
        return 15
    elif len(long_name) > 20:
        return 5
    else:
        return 0


for i, row in names.iterrows():
    id = row['ID']
    name = row['Name']
    region = row['Region']
    pdf.add_page()


    font = common.get_font(region)
    english_name, foreign_name = common.get_name(name)
    s = reduce_font_size(english_name)


    if foreign_name:
        pdf.set_font(family=ENGLISH_FONT, size=SMALL_FONT_SIZE-s)
        pdf.set_xy(CENTER_X, ENGLISH_NAME_Y)
        pdf.cell(0, text=english_name, align='C')

        pdf.set_font(family=font, size=SMALL_FONT_SIZE-s)
        pdf.set_xy(CENTER_X, FOREIGN_NAME_Y)
        pdf.cell(0, text=foreign_name, align='C')
    elif region == 'Vietnam':
        pdf.set_font(family=font, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')
    else:
        pdf.set_font(family=ENGLISH_FONT, size=FONT_SIZE-s)
        pdf.set_xy(CENTER_X, NAME_Y)
        pdf.cell(0, text=english_name, align='C')


pdf.output(NAME_PDF)


name_pdf = pypdf.PdfReader(open(NAME_PDF, 'rb'))
cop_pdf = pypdf.PdfWriter()


for name_page in name_pdf.pages:
    template_pdf = pypdf.PdfReader(open(TEMPLATE_PDF, 'rb'))
    template_page = template_pdf.pages[0]
    template_page.merge_page(name_page)
    cop_pdf.add_page(template_page)


cop_pdf.write(open(COP_PDF, 'wb'))