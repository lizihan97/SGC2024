import fpdf
import pypdf
import sys
import common
import os


if len(sys.argv) > 1:
    CAT = sys.argv[1]
else:
    CAT = input('CAT [open or sin]: ').lower()


TEMPLATE_PDF = os.path.join(common.CWD, 'templates/template_{}.pdf'.format(CAT))
CERT_PDF = os.path.join(common.OUTPUT, 'cert_{}.pdf'.format(CAT))
AWARD_PDF = os.path.join(common.TMP, 'awards_{}.pdf'.format(CAT))

CENTER_X = 30
EVENT_Y = 270
RANK_Y = EVENT_Y + 40
FONT_SIZE = 35

FONT = 'Alegreya-Bold'


pdf = fpdf.FPDF(format='A4', unit='pt')
pdf.add_font(fname= os.path.join(common.CWD, 'fonts/{}.otf'.format(FONT)))
pdf.set_font(family=FONT, size=FONT_SIZE)


for event in common.EVENTS:
    for rank in common.RANKS:
        pdf.add_page()

        pdf.set_xy(CENTER_X, EVENT_Y)
        pdf.cell(0, text=rank, align='C')

        pdf.set_xy(CENTER_X, RANK_Y)
        pdf.cell(0, text=event, align='C')


pdf.output(AWARD_PDF)


award_pdf = pypdf.PdfReader(open(AWARD_PDF, 'rb'))
cert_pdf = pypdf.PdfWriter()


for award_page in award_pdf.pages:
    template_pdf = pypdf.PdfReader(open(TEMPLATE_PDF, 'rb'))
    template_page = template_pdf.pages[0]
    template_page.merge_page(award_page, expand=True)
    cert_pdf.add_page(template_page)


cert_pdf.write(open(CERT_PDF, 'wb'))