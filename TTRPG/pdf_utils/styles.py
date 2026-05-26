from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

basic_paragraph_style = ParagraphStyle(
    name='Custom Style',
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    spaceBefore=5,
    spaceAfter=3,
    alignment=TA_LEFT,
    bulletFontName='Helvetica',
    bulletFontSize=10,
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
    fontSize=13,
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
    fontSize=12,
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
    fontSize=9,
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
    fontSize=11,
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
    fontSize=10,
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
    fontSize=8,
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

def add_dice_images(some_str, size=15):
    map = {
        'R1': f'<img src="images/one.png" width={size} height={size} />',
        'R2': f'<img src="images/two.png" width={size} height={size} />',
        'R3': f'<img src="images/three.png" width={size} height={size} />',
        'R4': f'<img src="images/four.png" width={size} height={size} />',
        'R5': f'<img src="images/five.png" width={size} height={size} />',
        'R6': f'<img src="images/six.png" width={size} height={size} />',
    }

    for key in map:
        some_str = some_str.replace(key, map[key])
    return some_str