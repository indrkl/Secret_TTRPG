actions = [
    {
        'name': 'Refocus',
        'speed': '1A',
        'profieciency': 'Will',
        'description': '''
You attempt use your will to remove crazed, disoriented or afraid status effect from yourself. 
The DC is equal to the largest DC check you were supposed to make when receiving any of these status effect.
When you succeed, remove 1 level of any of these status effects. On a critical success, double the amount of levels
you remove using this action.
        ''',
        'difficulty': 0,
        'scaling': [
            {'D': '2/3/4/5/6', 'L': 5, 'description': '''When successful remove an additional level'''},
        ],
    },
    {
        'name': 'Attack',
        'speed': '1A',
        'profieciency': 'Weapon',
        'cost': '1 STA',
        'description': '''
You attack an enemy, make a weapon check if it is equal to or larger than your opponents AC, you hit them.
All future attack actions until the beginning of your next turn cost 1 additional STA.
        ''',
        'difficulty': 0,
        'scaling': [
        ],
    },
    {
        'name': 'Wrestle',
        'speed': '1A',
        'profieciency': 'Physique',
        'cost': '2 STA',
        'description': '''
Wrestling is all about getting an upper hand, rooting the opponent in place and draining their stamina faster than you
lose stamina. There are a few rules for wrestling:

1. If someone has upper hand against you, then you must first get rid of it before you can get upper hand against them

2. If anyone has upper hand against you, you cannot move

3. If someone gets upper hand against you, you lose upper hand against everyone.

4. Normally 1 character can only have upper hand against 1 other character

5. Upper hand has multiple levels.

6. When someone has upper hand against you, you cannot use weapons, except for dagger and you can only use spells that
have a range of touch or target yourself.

7. When you have 3 levels of upper hand against you, you cannot even use the dagger, nor cast spells that touch.

8. You lose STA at the beginning of round equal to the number of Upper hands against you.

9. If someone has upper hand against you, you can only wrestle those who have upper hand against you.

10. Character which has upper hand against another character is considered to be in the same space (same square in battle
map)

11. Attacks that miss against characters, which are in the same space, have 50 % chance to hit someone else in that
space.

Check physique against 10 + target's physique proficiency bonus. If you succeed, then the enemy loses 1 levels of upper 
hand against you, if they didn't have any, you gain 1 upper hand against them.

If you wrestled someone who did not have upper hand against you or you didn't have upper hand against them, they do get
an attack of opportunity, unless you managed to wrestle them from behind.
        ''',
        'difficulty': 0,
        'scaling': [
        ],
    },
]

from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style
from reportlab.lib import colors
import re

def prep_action_flowable(action):
    elements = []
    elements.append(Paragraph(action['name'], style=minor_title))
    data = [
        [f"Difficulty: {action.get('difficulty')}", f"Target: {action.get('target', '-')}", f"Range: {action.get('range', '-')}", f"Area radius: {action.get('radius', '-')}"],
        [f"Action cost: {action.get('speed', '-')}", f"Duration: {action.get('duration', '-')}", f"Concentration: {action.get('concentration', 'NO')}", f"Proficiency: {action.get('profieciency', '-')}"]
    ]
    table = Table(data, colWidths=[120]*4)
    table.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)

    for para in action['description'].split('\n\n'):
        para = para.replace('\n', ' ')
        elements.append(Paragraph(para, style=basic_paragraph_style))

    data = []
    # style = ParagraphStyle(name='Table Cell', fontSize=12, textColor='black', textWrap=True)
    for scaling in action.get('scaling', []):
        description = re.sub('\s+', ' ', scaling['description'])
        data.append([f"Difficulty: {scaling['D']}", f"Use limit: {scaling.get('L', 'unlimited')}", Paragraph(description, basic_paragraph_style)])
    if data:
        table = Table(data, colWidths=[100, 100, 280])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    table_overall = Table([[x] for x in elements], colWidths=[490])
    table_overall.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
    ]))


    return [KeepTogether([table_overall]), Spacer(480, 15)]
    # return [table_overall, Spacer(480, 15)]


def get_general_actions_chapter():
    elements = [
        {'type': 'title', 'content': 'General actions'},

    ]

    for action in actions:
        elements.append({'type': 'flowables', 'content': prep_action_flowable(action)})

    return elements
