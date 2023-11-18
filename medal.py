import fpdf
import pypdf
from common import *


TEMPLATE_PDF = os.path.join(CWD, 'templates/template_medal.pdf')
MEDAL_PDF = os.path.join(OUTPUT, 'medal.pdf')
AWARD_PDF = os.path.join(TMP, 'awards.pdf')

CENTER_X = 30
EVENT_Y = 400
RANK_Y = EVENT_Y + 70
CAT_Y = RANK_Y + 80
FONT_SIZE = 65
CAT_SIZE = 55

FONT = 'Alegreya-Bold'


pdf = fpdf.FPDF(format=(810,810), unit='pt')
pdf.add_font(fname=os.path.join(CWD, 'fonts/{}.otf'.format(FONT)))


for rank in RANKS:
    for cat in CATS:
        for event in EVENTS:
            pdf.add_page()
            pdf.set_font(family=FONT, size=FONT_SIZE)

            pdf.set_xy(CENTER_X, EVENT_Y)
            pdf.cell(0, text=rank, align='C')

            pdf.set_xy(CENTER_X, RANK_Y)
            pdf.cell(0, text=event, align='C')

            pdf.set_font(family=FONT, size=CAT_SIZE)
            pdf.set_xy(CENTER_X, CAT_Y)
            pdf.cell(0, text=cat, align='C')


pdf.output(AWARD_PDF)


award_pdf = pypdf.PdfReader(open(AWARD_PDF, 'rb'))
cert_pdf = pypdf.PdfWriter()


for award_page in award_pdf.pages:

    template_pdf = pypdf.PdfReader(open(TEMPLATE_PDF, 'rb'))
    template_page = template_pdf.pages[0]
    template_page.merge_page(award_page, expand=True)
    cert_pdf.add_page(template_page)


cert_pdf.write(open(MEDAL_PDF, 'wb'))