feats = {
    'Mage': [
        {
            'name': 'Master of one',
            'description': '''Choose one school of magic, you're max level in that school is increased by 1
            for acquainted and adept in mage path, and by 2 for talented and legendary. Note that the highest possible
            proficiency bonus is still +6, regardless of the level you achieve through this.''',
        },
        {
            'name': 'Variety mage',
            'description': '''Each advancement in a school of magic provides 1 additional level in 2 other
                schools of magic. When you take this feat multiple times, then it still provides at most 1 level
                per school for the secondary choices, you can simply choose more schools to receive this benefit.''',
        },
        {
            'name': 'Deep pools',
            'description': '''Each advancement in maximum mana provides you 3 additional maximum mana''',
        },
        {
            'name': 'Spice specialist',
            'description': '''
                You recover twice as much mana from adding magical spices to your food if you take this trait once, 
                or thrice as much if you take it the second time. This trait can only be taken twice.
            '''
        },
        {
            'name': 'Arcane understanding',
            'description': '''Whenever you choose to advance in a school of magic or maximum mana, you can learn 1 
            additional spell''',
        },
        {
            'name': 'Battle mage',
            'description': '''All spells cost 1 mana less to cast for acquainted and adept in mage path, and 2 mana less 
            to cast for talented and legendary, but no less than 0. This feat can only
            be taken at most half the times rounded up. (So at most once by level 4 and 7, at most twice by level 10 and
            13, and at most three times at levels 16 and 19)''',
        },
    ],
    'Martial': [
        {
            'name': 'Weapon mastery',
            'description': '''
            Choose a weapon, your proficiency bonus with this weapon increases by 1. This feat can only be taken once
            and only by talented and legendary in martial.
            '''
        },
        {
            'name': 'Versatile combatant',
            'description': '''All advancements in weapon levels provides 2 additional level in another 
            weapon. When you take this feat multiple times, then it still provides at most 2 levels
            per weapon class for the secondary choices, you can simply choose more weapon classes to receive this 
            benefit.
             ''',
        },
        {
            'name': 'Vigorous',
            'description': '''+1 HP per martial path level for every character level. All advancements in HP provide +5
            HP and +1 fortitude''',
        },
        {
            'name': 'Enduring',
            'description': '''All advancements in max stamina provide 2 additional max stamina and every second 
            advancement in stamina recovery provides 1 additional stamina recovery.''',
        },
        {
            'name': 'Defensive',
            'description': '''This feat can only be taken once and only by Talented and legendary martials. Gain +1 AC,
             and increase your FORT AND REF proficiency bonuses by 1.''',
        },
    ],
    'Skilled': [
        {
            'name': 'Versatility',
            'description': '''All advancements in some skill provides 1 level in 2 other skills as well.''',
        },
        {
            'name': 'Mastery',
            'description': ''' Choose a skill, your proficiency bonus with this skill increases by 1. This feat can only 
            be taken once and only by talented and legendary in skilled.''',
        },
        {
            'name': 'Lucky',
            'description': '''Every other advancement in luck provides 1 additional luck token.
            ''',
        },
        {
            'name': 'Resourceful',
            'description': '''All advancements in Will, Reflex or Fortitude using skilled path provide +3 proficiency
            in one of the other saving throws as well. +1 to max level for Will, reflex and fortitude. This feat
            can only be taken once.
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
Heroes gain 1 progression feat in each category which they have points in at levels 4, 7, 10, 13, 16 and 19 and before
they make their advancement decisions in that level.
        """},
    ]

    for path_name, path_feats in feats.items():
        elements.append({'type': 'subtitle', 'content': path_name})


        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
