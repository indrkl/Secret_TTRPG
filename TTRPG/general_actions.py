actions = [
    {
        'name': 'Move',
        'profieciency': 'Physique',
        'description': '''
Move X squares where X is the dice result that you use to move. This action can only be taken twice per turn.
        ''',
        'difficulty': 'RX',
    },
    {
        'name': 'Defend',
        'profieciency': 'Physique',
        'description': '''
Recover your defense up to maximum defense
        ''',
        'difficulty': 'R2.R2',
    },
    {
        'name': 'Refocus',
        'profieciency': 'Will',
        'description': '''
Remove a level of disoriented or afraid from you.
        ''',
        'difficulty': 'R4.R5',
        'scaling': [
            {'D': 'R4.R5', 'description': '''Remove all levels of that type from you'''},
        ],
    },
    {
        'name': 'Recover',
        'profieciency': 'Fortitude',
        'description': '''
            Remove a level of poison or freezing from you
        ''',
        'difficulty': 'R2.R2',
        'scaling': [
            {'D': 'R2.R2', 'description': '''Remove all levels of that type from you'''},
        ],
    },
    {
        'name': 'Study opponent',
        'profieciency': 'Lore',
        'description': '''
Study one of the opponents and learn their HP / ATK / MV if they are mobs, or Toughness, Defense and one ability if it
is enemy hero.
        ''',
        'difficulty': 'R4',
        'scaling': [
            {'D': 'R4.R4.R4', 'description': '''Find a vulnerability for the particular opponent, describe what this is,
            that opponent has 1 vulnerability that is not discarded at the beginning of their turn'''},
        ],
    },
    {
        'name': 'Taunt',
        'profieciency': 'Diplomacy',
        'description': '''
Taunt one opponent, they are more likely to attack you, but if they don't, they have disadvantage
        ''',
        'difficulty': 'R2',
        'scaling': [
            {'D': 'R2', 'description': '''
            Target also loses 1 morale
            '''},
        ],
    },
    {
        'name': 'Mark enemy',
        'profieciency': 'Leadership',
        'description': '''
Mark an enemy, attacks and spells against him have advantage. 
        ''',
        'difficulty': 'R3.R3.R3',
        'scaling': [
            {'D': 'R2', 'description': '''
            Target also loses 1 morale
            '''},
        ],
    },
    {
        'name': 'Wrestle',
        'cost': '1 stamina',
        'profieciency': 'Physique',
        'difficulty': 'R2.R2',
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

8. You lose 1 stamina at the beginning of round, if you have at least 3 levels of upper hand against you.

9. If someone has upper hand against you, you can only wrestle those who have upper hand against you.

10. Character which has upper hand against another character is considered to be in the same space (same square in battle
map)

11. Ranged attacks made onto a character in the space where the wrestling is taking place has a 1/6 chance of hitting
the other person.
        ''',
        'scaling': [
            {'D': 'R2.R2', 'description': '''Gain one additional level of upper hand'''},
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
        [f"Action cost: {action.get('cost', '-')}", f"Duration: {action.get('duration', '-')}", f"Concentration: {action.get('concentration', 'NO')}", f"Proficiency: {action.get('profieciency', '-')}"]
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
