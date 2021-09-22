from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def getContext( data ):
    dic = {
        'model': '',
        'volume': '',
        'type': '',
        'power': '',
        'transmission': '',
        'ntransmission': '',
        'drive': '',
        'body': '',
        'country': ''

    }
    i = 0
    with open( data, 'r', encoding='utf8' )  as  f:
        s = f.read()
        lst = s.split('\n')

    for v in dic.keys():
        dic[ v ] = lst[i]
        i += 1


    return dic

#****************************************************************************************************
def from_template(  data, template, signature  ):
    template = DocxTemplate(template)

    context = getContext( data )

    img_size = Cm(10)
    acc = InlineImage(  template, signature, img_size)

    context['foto'] = acc

    template.render( context )

    template.save( 'auto_report.docx')

#******************************************************************************************************
def generate_report( ):
    data = 'dataauto.txt'
    template = 'autotempl.docx'
    signature = 'foto.jpg'
    from_template(  data, template, signature )