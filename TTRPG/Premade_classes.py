premade_classes = [
    {
    'name': 'Paladin',
    'MARTIAL': 4,
    'MAGE': 2,
    'Innate_feat_martial': 'Bulwark',
    'Innate_feat_mage': 'Divine protector',
    'Levels': [
        {
            'notes': ['''
            Choose a primary weapon, either sword, mace or axe, that you are going to use together with a shield.
            Sword is recomended due to it's reliability of R5, which conflicts least with harmony's R3.
            '''],
            'Mage advancements': [
                'proficiency (first): harmony',
                'spell: guardian',
                '1 mana'
            ],
            'Martial advancements': [
                'feat: Heavy armor proficiency'
                , 'proficiency (first): primary weapon',
            ],
        },
        {
            'Mage advancements': [
                '1 mana'
                'proficiency (first): will',
                'proficiency (second): will',
            ],
            'Martial advancements': [
                'feat: Blessed warrior',
                'proficiency (first): physique',
                'proficiency (second): primary weapon',
            ],
        },
        {
            'Mage advancements': [
                'proficiency (second): harmony',
                'spell: bless',
            ],
            'Martial advancements': [
                'proficiency (first): shield',
                'proficiency (second): physique',
                '1 stamina',
            ],
        },
        {
            'Mage advancements': [
                '2 mana',
            ],
            'Martial advancements': [
                'Progression feat: Defensive',
                'proficiency (third): primary weapon',
                '1 stamina',
            ],
        },
        {
            'Mage advancements': [
                'proficiency (first): toughness',
                'proficiency (second): toughness',
                '1 mana'
            ],
            'Martial advancements': [
                'feat: Master of defenses',
                '1 stamina',
            ],
        },
        {
            'Mage advancements': [
                '2 mana'
            ],
            'Martial advancements': [
                'proficiency (second): shield',
                '2 stamina',
            ],
        },
        {
            'Mage advancements': [
                '2 mana'
            ],
            'Martial advancements': [
                'Progression feat: Mastery',
                'proficiency (extra): sword',
                'feat: Defensive stance',
                '2 stamina',
            ],
        },
        {
            'Mage advancements': [
                '2 mana'
            ],
            'Martial advancements': [
                'proficiency (third): physique',
                'proficiency (first): fortitude',
            ],
        },
    ],
    'equipment': ['sword', 'shield', 'Heavy chain mail'],
},
    {
        'name': 'Mercenary (2 weapon variant)',
        'MARTIAL': 3,
        'SKILLED': 3,
        'Innate_feat_martial': 'Tough',
        'Innate_feat_skilled': 'Well connected',
        'Levels': [
            {
                'notes': ['''
Mercenary is a balanced to be able to perform well both combat and out of combat activities. In this
example we chose to use two weapon fighting with sabre and dagger, because their power dice add up
to 6 but are furthest appart of each other making use of widest range of dice rolls. As 6, 4 and 2
are already useful without proficiency. And the rest are just 1 away from being used as a power dice
for either sabre or dagger.''',
'''
As for the use of skilled path, it is completely separate and does not need to synergise with the combat part at all.
So when making changes to it you can simply choose to only change the choices made regarding skills and skill related
feats. The reason why in this variant skilled path doesn't complement combat at all, is that the two weapon fighting 
already provides a wide dice coverage so adding more options doesn't make it more efficient, only more flexible.
                '''],
                'Skilled advancements': [
                    'proficiency (first): treasure hunting',
                    'proficiency (second): treasure hunting',
                ],
                'Martial advancements': [
                    'feat: Medium armor proficiency'
                    'proficiency (first): sabre',
                ],
            },
            {
                'Skilled advancements': [
                    '1 luck'
                    'feat: Fortunate',
                ],
                'Martial advancements': [
                    'feat: Two weapon fighter',
                    'proficiency (first): dagger',

                ],
            },
            {
                'Skilled advancements': [
                    'proficiency (third): treasure hunting',
                ],
                'Martial advancements': [
                    'proficiency (first): physique',
                    'proficiency (second): sabre',
                ],
            },
            {
                'Skilled advancements': [
                    '2 luck',
                    'proficiency (first): survival',

                ],
                'Martial advancements': [
                    'Progression feat: Deadly',
                    'proficiency (second): dagger',
                    '1 stamina',
                ],
            },
            {
                'Skilled advancements': [
                    'feat: Lucky finder',
                    '1 luck',
                    'proficiency (second): survival',
                ],
                'Martial advancements': [
                    'feat: Two weapon master',
                    'proficiency (first): reflex',
                ],
            },
            {
                'Skilled advancements': [
                    'proficiency (third): survival',
                ],
                'Martial advancements': [
                    'proficiency (first): fortitude',
                    'proficiency (second): physique',
                ],
            },
            {
                'Skilled advancements': [
                    'Progression feat: Resourceful',
                    'proficiency (first): diplomacy',
                    '2 luck',
                ],
                'Martial advancements': [
                    '1 stamina',
                    'proficiency (second): reflex',
                ],
            },
        ],
    'equipment': ['sabre', 'dagger', 'padded leather armor'],

    },
    {
        'name': 'Genius',
        'MARTIAL': 2,
        'SKILLED': 4,
        'Innate_feat_martial': 'Harmonious body',
        'Innate_feat_skilled': 'Prodigy',
        'Levels': [
            {
                'notes': ['''
This example class is meant to demonstrate how to approach a super campaign oriented character. He has minimal offensive
capabilities in combat, and is more focused on surviving, using heavy armor and physique skill to recover defenses and
not take damage to health.

However in campaign is where this character shines. It goes all in to the skilled path and doubles down by taking the
Prodigy innate feat, which allows him to spend 16 points on the skilled path at second level. This allows him to take
the Master mind and Excellent instructor feat to buff the whole party's ability to do stuff out of combat. This is meant
for a true role player playstyle, someone who engages with the story and what is happening around the world, who comes
up with plans to influence what is going on, and with this character build are well equipped to do so.

Some things to consider, you could switch out Martial with Magic and go for some of the schools of magic instead.
Another idea is to instead of Master mind and leadership to instead take Master feat right away at level 2, and choose
some other skill instead of leadership to instruct the party on. 
                '''],
                'Skilled advancements': [
                    'proficiency (first): leadership',
                    'proficiency (first): lore',
                    'proficiency (second): leadership',
                ],
                'Martial advancements': [
                    'proficiency (first): physique',
                    'proficiency (first): reflex',
                    'proficiency (first): fortitude',
                ],
            },
            {
                'Skilled advancements': [
                    'feat: Excellent instructor',
                    'feat: Master plan',
                    'proficiency (third): leadership',
                    'proficiency (second): lore',
                    'proficiency (first): diplomacy',
                ],
                'Martial advancements': [
                    'feat: Heavy armor proficiency',
                    'proficiency (first): sword',

                ],
            },
            {
                'Skilled advancements': [
                    'proficiency (third): lore',
                    '1 luck',
                ],
                'Martial advancements': [
                    'proficiency (second): physique',
                ],
            },
            {
                'Skilled advancements': [
                    'Progression feat: Resourceful',
                    'proficiency (fourth): leadership',

                ],
                'Martial advancements': [
                    'proficiency (second): reflex',
                    'proficiency (second): fortitude',
                ],
            },
            {
                'Skilled advancements': [
                    'feat: Master',
                    '1 luck',
                ],
                'Martial advancements': [
                    'proficiency (third): physique',
                    '1 stamina',
                ],
            },
            {
                'Skilled advancements': [
                    'proficiency (third): lore',
                    'proficiency (first): survival',
                ],
                'Martial advancements': [
                    'proficiency (second): sword',
                ],
            },
            {
                'Skilled advancements': [
                    'Progression feat: Mastery(leadership)',
                    'proficiency (extra): leadership',
                    'proficiency (second): diplomacy',
                    'proficiency (second): survival',
                ],
                'Martial advancements': [
                    '2 stamina',
                ],
            },
        ],
    'equipment': ['sword', 'Heavy chain mail'],

    },
    {
        'name': 'Pyromancer',
        'MAGE': 4,
        'SKILLED': 2,
        'Innate_feat_mage': 'Metamagician',
        'Innate_feat_skilled': 'Lucky',
        'Levels': [
            { # 1
                'notes': ['''

                '''],
                'Mage advancements': [
                    'proficiency (first): elemental',
                    'proficiency (second): elemental',
                    'spell: Fireball',
                    'spell: Chain lightning',
                    '1 mana',
                ],
                'Skilled advancements': [
                    'proficiency (first): survival',
                    'proficiency (first): diplomacy',
                ],
            },
            { # 2
                'Mage advancements': [
                    'feat: Pyromancy',
                    'proficiency (third): elemental',
                    'spell: Frostbite',
                ],
                'Skilled advancements': [
                    'feat: Deep apology',
                    'proficiency (second): survival',

                ],
            },
            { # 3
                'Mage advancements': [
                    '3 mana',
                    'feat: Distant magic'
                ],
                'Skilled advancements': [
                    'proficiency (second): diplomacy',
                ],
            },
            { # 4
                'Mage advancements': [
                    'Progression feat: Deep pools',
                    'proficiency (fourth): elemental',
                    'spell: Elemental weapon',
                ],
                'Skilled advancements': [
                    '2 luck',
                ],
            },
            { # 5
                'Mage advancements': [
                    'feat: Twin magic',
                    '5 mana'
                ],
                'Skilled advancements': [
                    'proficiency (third): survival',
                    'proficiency (first): physique',
                ],
            },
            { # 6
                'Mage advancements': [
                    '1 mana',
                    'proficiency (first): will',
                    'proficiency (second): will',
                ],
                'Skilled advancements': [
                    'proficiency (second): physique',
                ],
            },
            { # 7
                'Mage advancements': [
                    '4 mana',
                    'Progression feat: Battle mage',
                ],
                'Skilled advancements': [
                    '2 luck',
                ],
            },

        ],
    'equipment': ['staff'],

    },
]

import re
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style, basic_para_title_style
from reportlab.lib import colors


from Characters import get_feat_and_flowable, find_general_action, find_spell_object, mana_multiplier, luck_multiplier

def generate_class_flowable(premade_class):
    from Innate_feats import prep_feat_flowable as prep_innate_feat_flowable
    from Innate_feats import feats as all_innate_feats
    from Normal_feats import feats as all_normal_feats
    from progression_feats import feats as all_progression_feats
    from Normal_feats import prep_feat_flowable as prep_normal_feat_flowable
    from progression_feats import prep_feat_flowable as prep_progression_feat_floable

    from Spells import schools
    from Spells import prep_spell_flowable as prep_spell_flowable


    from equipment import weapon_classes, prep_equipment_flowable
    from equipment import equipment as all_equipment

    innate_feats = [{'name': premade_class[key], 'path': key[12:]} for key in ['Innate_feat_skilled', 'Innate_feat_mage', 'Innate_feat_martial'] if key in premade_class]
    feats = []
    progression_feats = []
    spells = []


    elements = []
    # elements.append(Paragraph(premade_class['name'], style=basic_para_title_style))
    data = [
        [f"Martial: {premade_class.get('MARTIAL', 0)}", f"Mage: {premade_class.get('MAGE', '0')}", f"Skilled: {premade_class.get('SKILLED', '0')}"],
    ]

    table = Table(data, colWidths=[160]*3)
    table.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)

    elements.append(Paragraph('Innate Feats', style=minor_title))

    path_mapping = {1: 'Acquinted', 2: 'Adept', 3: 'Talented', 4: 'Legendary'}

    for feat in innate_feats:
        feat_name = re.search('(^[A-Za-z ]*)', feat.get('name'))[1]
        path_power = premade_class.get(feat['path'].upper())
        name_addon = ' (%s)'%(path_mapping[path_power])

        _, feat_flowable = get_feat_and_flowable(feat_name, name_addon=name_addon)

        elements.extend(feat_flowable)

    for indx in range(len(premade_class['Levels'])):
        elements.append(Paragraph('Level %d' % (indx+1), style=minor_title))

        level = premade_class['Levels'][indx]
        for key in level:
            if key == 'notes':
                for note in level['notes']:
                    elements.append(Paragraph(note, style=basic_paragraph_style))
                continue
            for advancement in level[key]:
                # print(advancement)
                proficiency = re.search('proficiency \((first|second|third|fourth|extra)\): ([a-z ]*)', advancement)
                if proficiency:
                    proficiency_name = proficiency[2]
                    indx = proficiency[1]
                    elements.append(Paragraph('%s level of proficiency in %s'%(indx, proficiency_name), style=basic_paragraph_style))

                    continue

                spell = re.search('spell: ([A-Za-z \/]*)', advancement)
                if spell:
                    elements.append(Paragraph('New spell: %s'%(spell[1]), style=basic_paragraph_style))
                    spells.append(spell[1])
                    continue
                prog_feat = re.search('Progression feat: ([A-Za-z ]*)', advancement)
                if prog_feat:
                    print ("PROG FEAT")
                    elements.append(Paragraph('New progression feat: %s'%(prog_feat[1]), style=basic_paragraph_style))

                    progression_feats.append(prog_feat[1])
                    continue
                feat = re.search('feat: ([A-Za-z ]*)', advancement)
                if feat:
                    elements.append(Paragraph('New feat: %s'%(feat[1]), style=basic_paragraph_style))

                    feats.append(feat[1])
                    continue

                stat = re.search('([0-9]*) (mana|stamina|luck)', advancement)
                if stat:
                    stat_amount = int(stat[1])
                    if stat[2] == 'mana':
                        stat_amount *= mana_multiplier
                    if stat[2] == 'luck':
                        stat_amount *= luck_multiplier
                    elements.append(Paragraph('%d %s' % (stat_amount, stat[2]), style=basic_paragraph_style))
                    continue

                raise Exception(advancement + ' is unhandled')

    elements.append(Paragraph('Feats', style=minor_title))


    for feat in feats:
        _, feat_flowable = get_feat_and_flowable(feat)
        elements.extend(feat_flowable)


    for feat in progression_feats:
        _, feat_flowable = get_feat_and_flowable(feat)
        elements.extend(feat_flowable)

    elements.append(Paragraph('Spells', style=minor_title))

    for spell in spells:
        spell_obj = find_spell_object(spell, schools)
        elements.extend(prep_spell_flowable(spell_obj))
    if premade_class.get('normal_actions'):
        from general_actions import actions as general_actions
        from general_actions import prep_action_flowable
        elements.append(Paragraph('General actions', style=minor_title))

        for action in premade_class.get('normal_actions'):
            action_obj = find_general_action(action, general_actions)
            elements.extend(prep_action_flowable(action_obj))

    elements.append(Paragraph('Equipment', style=minor_title))

    for equipment in premade_class.get('equipment', []):
        if equipment in all_equipment:
            elements.extend(prep_equipment_flowable(all_equipment[equipment], equipment))
        else:
            elements.append(Paragraph(equipment, style=minor_subtitle))


    return elements


def get_premade_class_chapter():
    elements = [
        {'type': 'title', 'content': 'Premade classes'},
        {'type': 'paragraph',
         'content': """
Here we provide some premade classes. Treat these as templates or get inspiration for your own characters. When you
start the game, you can of course use them one on one, but whenever you feel like making changes to them, then know that
they have been made using the same rules as the normal character creation so adding and removing stuff can be done
without worries.
            """},

    ]

    for premade_class in premade_classes:
        elements.append({'type': 'subtitle', 'content': premade_class['name']})
        elements.append({'type': 'flowables', 'content': generate_class_flowable(premade_class)})

    return elements