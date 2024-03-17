from reportlab.platypus import Flowable, Paragraph, Table, TableStyle
from pdf_utils.styles import basic_paragraph_style, minor_title, add_dice_images
from reportlab.lib import colors
from pdf_utils.elements import InteractiveCheckBox, IniteractiveTextBox
from generate_docs import MyDocTemplate, prep_elements_from_chapter
from reportlab.lib.pagesizes import letter

from rulebook_chapters.character_creation import get_playcard_flowable, cards


def generate_character_sheet(mage, martial, skilled, spells=[], feats=[], equipment=[], name=""):
    from Characters import get_spell_flowable, get_feat_and_flowable, get_equipment_flowable
    elements = []
    # Whole page is separated into chunks of 20 px. Total 420 px wide, meaning 21 columns.
    # Name, background 3 | 4 | 3 | 11
    # Description 3 | 18
    # Mage, Martial, Skilled 3 | 4 | 3 | 4 | 3 | 4
    # Damage, 6 dice, break, column, mana, stamina, luck. 3 | 6 x 1 | 2 | 3 | 2 | 2 | 2
    # Will, Fort, Reflex 3 | 1, 3 | 1, 3 | 1
    # Status effects 7 x 3


    name_text_box = IniteractiveTextBox(text='name', width=78)
    background_text_box = IniteractiveTextBox(text='name', width=232)
    description_text_box = IniteractiveTextBox(text='name', width=386)
    path_type_box = IniteractiveTextBox(text='name', width=78)
    box_3 = IniteractiveTextBox(text='name', width=56)
    box_2 = IniteractiveTextBox(text='name', width=34)
    box_1 = IniteractiveTextBox(text='name', width=12)
    box_5 = IniteractiveTextBox(text='name', width=100)
    box_6 = IniteractiveTextBox(text='name', width=122)
    box_9 = IniteractiveTextBox(text='name', width=188)
    box_21 = IniteractiveTextBox(text='name', width=22*21-10)

    checkbox = InteractiveCheckBox(text='tick')
    data = [
        [Paragraph('Name', style=basic_paragraph_style), '', '', name_text_box, '', '', ''
            , Paragraph('Background', style=basic_paragraph_style), '', '', background_text_box, '', '', '', '', '', '', '', '', '', ''],
        [Paragraph('Description', style=basic_paragraph_style), '', '', description_text_box],
        [
            Paragraph('Martial', style=basic_paragraph_style), '', '', path_type_box, '', '', '',
            Paragraph('Mage', style=basic_paragraph_style), '', '', path_type_box, '', '', '',
            Paragraph('Skilled', style=basic_paragraph_style), '', '', path_type_box, '', '', '',

         ],
        # [
        #     '', '', '', Paragraph(add_dice_images('R1'), style=basic_paragraph_style), Paragraph(add_dice_images('R2'), style=basic_paragraph_style),
        #     Paragraph(add_dice_images('R3'), style=basic_paragraph_style), Paragraph(add_dice_images('R4'), style=basic_paragraph_style),
        #     Paragraph(add_dice_images('R5'), style=basic_paragraph_style), Paragraph(add_dice_images('R6'), style=basic_paragraph_style),
        #     '', '', '', '', '', Paragraph('Stamina', style=basic_paragraph_style), '',
        #     Paragraph('Mana', style=basic_paragraph_style), '', Paragraph('Luck', style=basic_paragraph_style), '',
        # ],
        [
            '',  '', '', Paragraph(add_dice_images('R1', size=10), style=basic_paragraph_style),
            Paragraph(add_dice_images('R2', size=10), style=basic_paragraph_style),
            Paragraph(add_dice_images('R3', size=10), style=basic_paragraph_style),
            Paragraph(add_dice_images('R4', size=10), style=basic_paragraph_style),
            Paragraph(add_dice_images('R5', size=10), style=basic_paragraph_style),
            Paragraph(add_dice_images('R6', size=10), style=basic_paragraph_style),
            '', '', '', '', '', Paragraph('Stamina', style=basic_paragraph_style), '', '',
            Paragraph('Mana', style=basic_paragraph_style), '', Paragraph('Luck', style=basic_paragraph_style), '',
        ],
        ['Damage'] + [''] * 2 + [box_1] * 6 + [''] + ['Maximum'] + [''] * 3 + [box_3, '', '', box_2, '', box_2, ''],
        ['Scarred'] + [''] * 2 + [checkbox] * 6 + [''] + ['Current'] + [''] * 3 + [box_3, '', '', box_2, '', box_2, ''],
        ['Proficiencies'] + [''] * 5 + ['Inventory'] + [''] * 5 + ['Spells'] + [''] * 8
    ]

    style = [
        # ('LINEBELOW', (0, 1), (-1, -1), 0.25, colors.black),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('SPAN', (0, 0), (2, 0)),
        ('SPAN', (3, 0), (6, 0)),
        ('SPAN', (7, 0), (9, 0)),
        ('SPAN', (10, 0), (-1, 0)),
        ('SPAN', (0, 1), (2, 1)),
        ('SPAN', (3, 1), (-1, 1)),
        ('SPAN', (0, 2), (2, 2)),
        ('SPAN', (3, 2), (6, 2)),
        ('SPAN', (7, 2), (9, 2)),
        ('SPAN', (10, 2), (13, 2)),
        ('SPAN', (14, 2), (16, 2)),
        ('SPAN', (17, 2), (-1, 2)),
        ('SPAN', (0, 6), (5, 6)),
        ('SPAN', (6, 6), (11, 6)),
        ('SPAN', (12, 6), (-1, 6)),
    ]
    for x in range(3, 6):
        style.extend([
        ('SPAN', (0, x), (2, x)),
        ('SPAN', (10, x), (13, x)),
        ('SPAN', (14, x), (16, x)),
        ('SPAN', (17, x), (18, x)),
        ('SPAN', (19, x), (20, x)),
        ])

    i = 0
    premade_list = ['Will', 'Fortitude', 'Reflex', 'Lore', 'Diplomacy', 'Physique', 'Survival', 'Leadership', 'concealment', 'crafting', 'harvesting']

    for x in range(7, 25):
        data.append([Paragraph(premade_list[i], style = basic_paragraph_style) if len(premade_list) > i else box_5] + [''] * 4 + [box_1, box_6] + [''] * 5 + [box_9] + [''] * 8)
        i += 1
        style.extend([
            ('SPAN', (0, x), (4, x)),
            ('SPAN', (5, x), (5, x)),
            ('SPAN', (6, x), (11, x)),
            ('SPAN', (12, x), (-1, x)),
        ])
    style.append(('SPAN', (0, 25), (-1, 25)))
    data.append(['Feats'] + ['']*20)
    for x in range(26, 36):
        data.append([box_21] + [''] * 20)
        style.extend([
            ('SPAN', (0, x), (-1, x)),
        ])

    table = Table(data, colWidths=[22]*21)
    table.setStyle(TableStyle(style))
    elements.append(table)

    if mage:
        elements.extend(get_playcard_flowable(cards['MAGE'][mage]))
    if martial:
        elements.extend(get_playcard_flowable(cards['MARTIAL'][martial]))
    if skilled:
        elements.extend(get_playcard_flowable(cards['SKILLED'][skilled]))

    for spell in spells:
        elements.extend(get_spell_flowable(spell))
    for feat in feats:
        _,feat_flowable = get_feat_and_flowable(feat)
        elements.extend(feat_flowable)
    for equip in equipment:
        elements.extend(get_equipment_flowable(equip))

    pdf_content = prep_elements_from_chapter([{'type': 'flowables', 'content': elements}], add_title_page_break=False)

    if name:
        pdf_file = MyDocTemplate(f"{name}_character_sheet.pdf", pagesize=letter)
    else:
        pdf_file = MyDocTemplate("character_sheet.pdf", pagesize=letter)
    pdf_file.multiBuild(pdf_content)



if __name__ == '__main__':
    generate_character_sheet(3, 1, 2, spells=['Fireball', 'Chain lightning', 'False threats', 'Invisibility'],
                             name='Gurthna', feats=[], equipment=[])
    generate_character_sheet(0, 3, 3, spells=[],
                             name='Andrew Cannon', feats=['Shadow', 'Medium armor proficiency', 'Two weapon fighter', 'Tinkerer', 'Agent of chaos'], equipment=['dagger', 'sword'])
