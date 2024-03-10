feats = {
    'General': [
        {
            'name': 'Mastery',
            'description': '''
            Upgrade a proficiency once. This can be chosen once per proficiency, it doesn't increase the cost of
            further improvement in that proficiency and is not taken into account when considering the normal maximum
            proficiency for that skill.
            ''',
        },
    ],
    'Mage': [
        {
            'name': 'Variety mage',
            'description': '''Grant an additional 2 mental slots that can be used for spells.''',
        },
        {
            'name': 'Deep pools',
            'description': '''Each advancement in maximum mana provides you 1 additional maximum mana''',
        },
        {
            'name': 'Spice specialist',
            'description': '''
                You recover mana using spices twice as effectively. Meaning the first 20 mana cost 1.5 gp to recover,
                the next 40 cost 2.5 gp to recover and the rest cost 5 gp to recover. This feat can only be taken once.
            '''
        },
        {
            'name': 'Arcane understanding',
            'description': '''Whenever you choose to advance in a school of magic or maximum mana, you can learn 1 
            additional spell from any school. This works retroactively.''',
        },
        {
            'name': 'Battle mage',
            'description': '''The mana cost for offensive spells scales better. It now costs 2 mana for 2 additional
            power dice, 4 mana for 3 additional power dice and 7 mana for 4 additional power dice''',
        },
    ],
    'Martial': [
        {
            'name': 'Enduring',
            'description': '''Every second advancement in stamina provide + 1 maximum stamina''',
        },
        {
            'name': 'Powerful',
            'description': '''You have one additional dice during combat''',
        },
        {
            'name': 'Defensive',
            'description': '''+2 maximum defenses, this can only be taken once''',
        },
        {
            'name': 'Deadly',
            'description': '''Each of your attacks applies 1 vulnerable. This can only be taken once''',
        },
    ],
    'Skilled': [
        {
            'name': 'Lucky',
            'description': '''Every second advancement in luck provides 1 additional luck token.
            ''',
        },
        {
            'name': 'Resourceful',
            'description': '''You have one additional dice during scenes
            ''',
        },
    ]
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style


def prep_feat_flowable(feat):
    elements = []
    elements.append(Paragraph(feat['name'], style=minor_title))
    if feat.get('requires'):
        elements.append(Paragraph(f"Requires: {feat['requires']}", style=minor_subtitle))

    elements.append(Paragraph(feat['description'], style=basic_paragraph_style))

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements


def get_progression_feat_chapter():
    elements = [
        {'type': 'title', 'content': 'Progression feats'},
        {'type': 'paragraph',
         'content': """
Heroes gain 1 progression feat at levels 4, 7, 10, 13, 16 and 19. All progression feats work retroactively.
        """},
    ]

    for path_name, path_feats in feats.items():
        elements.append({'type': 'subtitle', 'content': path_name})


        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
