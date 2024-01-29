from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

basic_paragraph_style = ParagraphStyle(
    name='Custom Style',
    fontName='Helvetica',
    fontSize=11,
    leading=13,
    spaceBefore=8,
    spaceAfter=6,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=14,
    bulletIndent=0,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

spell_block_style = ParagraphStyle(
    name='Spell block style',
    backColor='yellow'
)

basic_para_title_style = ParagraphStyle(
    name='Heading1',
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=24,
    spaceBefore=24,
    spaceAfter=12,
    alignment=TA_CENTER,
    bulletFontName='Helvetica',
    bulletFontSize=14,
    bulletIndent=0,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

basic_para_sub_title_style = ParagraphStyle(
    name='Heading2',
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=24,
    spaceBefore=24,
    spaceAfter=12,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=14,
    bulletIndent=0,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

basic_list_style = ParagraphStyle(
    name='Custom Style',
    fontName='Helvetica',
    fontSize=10,
    leading=18,
    spaceBefore=0,
    spaceAfter=0,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=12,
    bulletIndent=12,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)


minor_title = ParagraphStyle(
    name='Minor title Style',
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=24,
    spaceBefore=24,
    spaceAfter=12,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=14,
    bulletIndent=0,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

minor_subtitle = ParagraphStyle(
    name='Minor title Style',
    fontName='Helvetica',
    leftIndent=20,
    fontSize=12,
    leading=16,
    spaceBefore=12,
    spaceAfter=5,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=14,
    bulletIndent=8,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

option_style = ParagraphStyle(
    name='Custom Style',
    fontName='Helvetica',
    fontSize=10,
    leading=12,
    leftIndent=0,
    spaceBefore=0,
    spaceAfter=0,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=12,
    bulletIndent=24,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    allowOrphans=0,
    textTransform=None,  # 'uppercase' | 'lowercase' | None
    endDots=None,
    splitLongWords=1,
)

def add_dice_images(some_str):
    map = {
        'R1': '<img src="images/one.png" width=15 height=15 />',
        'R2': '<img src="images/two.png" width=15 height=15 />',
        'R3': '<img src="images/three.png" width=15 height=15 />',
        'R4': '<img src="images/four.png" width=15 height=15 />',
        'R5': '<img src="images/five.png" width=15 height=15 />',
        'R6': '<img src="images/six.png" width=15 height=15 />',
    }

    for key in map:
        some_str = some_str.replace(key, map[key])
    return some_str