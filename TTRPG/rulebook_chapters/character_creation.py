import math
from math import floor, ceil
from reportlab.platypus import Flowable, Paragraph, Table, TableStyle, Spacer, KeepTogether
from pdf_utils.styles import basic_paragraph_style, minor_title
from reportlab.lib import colors
from pdf_utils.elements import InteractiveCheckBox


def py2round(x):
    if x >= 0.0:
        return math.floor(x + 0.5)
    else:
        return math.ceil(x - 0.5)

def get_character_creation_chapter():
    profciency_cap_matrix = [5, 8, 10, 11, 12]
    proficiency_cap_table = [['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY', 'LEGENDARY+']]
    for i in range(1, 21):
        proficiency_cap_table.append([i] + [floor(x+1 + (i)*profciency_cap_matrix[x]/(20)) for x in range(0, 5)])

    difficulty_cap_table = [['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY']]
    for i in range(1, 21):
        difficulty_cap_table.append([i] + [py2round(i * x / 4) for x in range(1, 5)])

    proficiency_table = [['EFFECTIVE_LEVEL', 'PROFICIENCY_BONUS']]
    level_up = [1, 2, 3, 3, 4, 4, 100]
    ndx = 0
    cnt = 0
    proficiency=0
    for i in range(1, 21):
        cnt += 1
        if cnt >= level_up[ndx]:
            ndx += 1
            proficiency += 1
            cnt = 0
        proficiency_table.append([i] + [proficiency])

    ret =  [
        {'type': 'title', 'content': 'Character creation'},
        {'type': 'paragraph',
         'content': """
Instead of classes there are 3 Paths - Mage, Martial and Skilled. You define how good your character is in any of these  
paths. There are 4 levels in each PATH:


1 - acquinted

2 - adept

3 - talented

4 - legendary

Heroes get a total of 6 path points, which they can spread out among these 3 paths defining their innate ability. 
This determines how fast they advance in these paths while leveling up and what is their maximum potential in these 
paths. In a way the way they spread it out defines their class, so there are 19 classes in the sense of how many ways 
you can distribute those 6 path points, but each distribution of course has also very many ways to build your character.

For example you could be a Nature wizard who is either Talented or Legendary, and depending on that you could be
more or less diversified in other areas.

All players start with 6 d6 dice in their dice pool, for both combat and out of combat, 2 toughness (determines how much 
damage you can take before you die), proficiency in light armor and access to some general actions (all detailed in
general actions chapter), and 2 creative character traits. In addition they can start with +2 proficiency with one
trait, weapon or school of magic, and +1 proficiency with 2 other trait, weapon or school of magic. Both of the
character traits must start with at least +1 proficiency though.

In addition they get a foundation power for each path they have path points in, but the power of the feat depends on their 
level in that path. This further defines their character progression possibilities. Foundations are really powerful.

Finally each hero gets a play card for each path they have points in. Take the appropriate play card. So if you are
talented mage, adept martial and acquinted in skilled, then take the playcards with these names.

At level 1 and in all future levels players get to mark minor and major advancement options in these playcards (the
number is stated at the bottom of the playcard). Each option can be taken as many times as the number of check boxes
next to it. The number of check boxes increases at levels 5 and 9.

Also at level 1 decide how do scarred dice work. When you take damage, you lose dice, all magical healing does give you
back the damaged dice, but each healing scars one of the dice. There are however options (see scarred dice in glossary)
for how it will actually affect you.

Finally at level 1 and only at level 1 each character gets extra resources for each of the path they assigned points to.
For each point in mage path, player gets 3 maximum mana. For each point in Martial path, player gets 1 maximum stamina. 
For each point in skilled path, player gets 1 maximum luck tokens.

Advancement rules

The maximum proficiency is in general +4, but using some foundations it can be raised to up to +5.
In advancement options it is often stated "(max X prof)", that indicates the proficiency that can be attained with this
option. Note that this max only takes into consideration the proficiency gained from advancement options and not 
foundations.

Proficiency allows you to shift the dice results by 1 in order to get the dice result requires to perform the action
related with this proficiency. You can perform number of shifts equal to your profiency each round / scene.

"""},
        {'type': 'title', 'content': 'Playcards'},


    ]
    for path in cards.values():
        for indx in range(1, 5):
            ret.append({'type': 'flowables', 'content': get_playcard_flowable(path[indx])})

    return ret



def get_playcard_flowable(playcard):
    gold = colors.Color(red=(252.0/255),green=(235.0/255),blue=(194.0/255)) # 252, 235, 194
    light_blue = colors.Color(red=(235.0/255),green=(247.0/255),blue=(247.0/255)) # 235, 247, 247

    elements = []
    data = [
        [Paragraph(playcard['name'], style=minor_title), '', '', ''],
        [Paragraph('Major advancement options', style=minor_title), 'lvl 1-4', 'lvl 5-8', 'lvl 9-12'],
    ]

    for big_perk in playcard['big_perks']:
        checkboxes = []
        checkboxes5_8 = []
        checkboxes9_12 = []

        for i in range(big_perk['available1-4']):
            checkboxes.append(InteractiveCheckBox('%s_%d'%(big_perk['description'], i), offset=i*16))
        for i in range(big_perk['available 5-8']):
            checkboxes5_8.append(InteractiveCheckBox('%s_%d'%(big_perk['description'], i), offset=i*16))
        for i in range(big_perk['available 9-12']):
            checkboxes9_12.append(InteractiveCheckBox('%s_%d'%(big_perk['description'], i), offset=i*16))
        data.append([Paragraph(big_perk['description'], style=basic_paragraph_style), checkboxes, checkboxes5_8, checkboxes9_12])

    table = Table(data, colWidths=[260, 55, 55, 55])
    table.setStyle(TableStyle([
        ('LINEBELOW', (0, 1), (-1, -1), 0.25, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, -1), gold),
    ]))
    elements.append(table)


    data = [[Paragraph('Minor advancement options', style=minor_title), '', '', '']]


    for big_perk in playcard['small_perks']:
        checkboxes = []
        checkboxes5_8 = []
        checkboxes9_12 = []

        for i in range(big_perk['available1-4']):
            checkboxes.append(InteractiveCheckBox('%s_%d_1to4'%(big_perk['description'], i), offset=i*16))
        for i in range(big_perk['available 5-8']):
            checkboxes5_8.append(InteractiveCheckBox('%s_%d_5to8'%(big_perk['description'], i), offset=i*16))
        for i in range(big_perk['available 9-12']):
            checkboxes9_12.append(InteractiveCheckBox('%s_%d_9to12'%(big_perk['description'], i), offset=i*16))
        data.append([Paragraph(big_perk['description'], style=basic_paragraph_style), checkboxes, checkboxes5_8, checkboxes9_12])

    data.append([Paragraph(playcard['progression'], style=basic_paragraph_style)])
    table = Table(data, colWidths=[260, 55, 55, 55])
    table.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -2), 0.25, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, -1), light_blue),
        ('SPAN', (0, -1), (-1, -1)),
    ]))

    elements.append(table)

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True


    table_overall = Table([[x] for x in elements], colWidths=[490])
    table_overall.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               # ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
    ]))


    return [KeepTogether([table_overall]), Spacer(480, 15)]



    return elements

legendary_mage_card = {
    'name': 'Legendary Mage path',
    'big_perks': [
        {'description': 'gain major mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 20 maximum mana', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 spell school proficiency (max prof. 4)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 medium mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small mage feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 spell school proficiency and learn a spell from that school (max prof. 2)',
            'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 spell school proficiency (max prof. 3)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'learn 2 spells from any schools of magic', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'Grant an additional 2 mental slots that can be used for spells.', 'available1-4': 1, 'available 5-8': 0, 'available 9-12': 1},
        {'description': 'Grant an additional 1 mental slots that can be used for spells.', 'available1-4': 1, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 intelligent trait proficiency (max prof. 2)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 8 mana', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 6 mana', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Mark 4 minor options at levels 1 and 3, and 1 minor and 1 major option at levels 2 and 4''',
}

talented_mage_card = {
    'name': 'Talented Mage path',

    'big_perks': [
        {'description': 'gain major mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 20 maximum mana', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 spell school proficiency (max prof. 4)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
    ],
    'small_perks': [
        {'description': 'gain 1 medium mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small mage feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 spell school proficiency and learn a spell from that school (max prof. 2)',
         'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 spell school proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'learn 2 spells from any schools of magic', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'Grant an additional 2 mental slots that can be used for spells.', 'available1-4': 0,
         'available 5-8': 1, 'available 9-12': 0},
        {'description': 'Grant an additional 1 mental slots that can be used for spells.', 'available1-4': 2,
         'available 5-8': 1, 'available 9-12': 2},

        {'description': 'gain 1 intelligent trait proficiency (max prof. 2)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 8 mana', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 6 mana', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Gain 3 minor options at levels 1 and 3, and 1 major option at levels 2 and 4''',
}

adept_mage_card = {
    'name': 'Adept Mage path',

    'big_perks': [
        {'description': 'gain 1 medium mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 16 maximum mana', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 spell school proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 small mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 spell school proficiency and learn a spell from that school (max prof. 1)',
         'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 spell school proficiency (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'learn 2 spells from any schools of magic', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Grant an additional 1 mental slots that can be used for spells.', 'available1-4': 1,
         'available 5-8': 1, 'available 9-12': 2},
        {'description': 'gain 1 intelligent trait proficiency (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 8 mana', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 6 mana', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
    ],
    'progression': '''Gain 2 minor options at levels 1, 3 and 4, and 1 major option at levels 2''',
}

acquainted_mage_card = {
    'name': 'Acquainted Mage path',

    'big_perks': [
        {'description': 'gain 1 small mage feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 12 maximum mana', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 spell school proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 spell school proficiency and learn a spell from that school (max prof. 1)',
         'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 spell school proficiency (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'learn 2 spells from any schools of magic', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Grant an additional 1 mental slots that can be used for spells.', 'available1-4': 1,
         'available 5-8': 0, 'available 9-12': 1},
        {'description': 'gain 1 intelligent trait proficiency (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 6 mana', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
    ],
    'progression': '''Gain 1 minor option at levels 1, 2 and 4, and 1 major option at levels 3''',
}

legendary_martial_card = {
    'name': 'Legendary Martial path',
    'big_perks': [
        {'description': 'gain major martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 8 maximum stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 2 times in toughness or with any weapon or shield.
        (max prof. 4)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 medium martial feat', 'available1-4': 2, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small martial feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 toughness', 'available1-4': 3, 'available 5-8': 1, 'available 9-12': 0},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 weapon or shield proficiency with 2 different weapons (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 3)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 3 stamina', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 2 stamina', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 stamina', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Mark 4 minor options at levels 1 and 3, and 1 minor and 1 major option at levels 2 and 4''',
}

talented_martial_card = {
    'name': 'Talented Martial path',

    'big_perks': [
        {'description': 'gain major martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 8 maximum stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 2 times in toughness or with any weapon or shield. 
        (max prof. 4)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
    ],
    'small_perks': [
        {'description': 'gain 1 medium martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small martial feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 toughness', 'available1-4': 2, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 weapon proficiency with 2 different weapons (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 3 stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 stamina', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 stamina', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Gain 3 minor options at levels 1 and 3, and 1 major option at levels 2 and 4''',
}

adept_martial_card = {
    'name': 'Adept Martial path',

    'big_perks': [
        {'description': 'gain 1 medium martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 6 maximum stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 1 times in toughness or with any weapon or shield. 
        (max prof. 3)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
    ],
    'small_perks': [
        {'description': 'gain 1 small martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 toughness (max prof. 2)', 'available1-4': 1, 'available 5-8': 2, 'available 9-12': 1},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 2)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 2 stamina', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 stamina', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Gain 2 minor options at levels 1, 3 and 4, and 1 major option at levels 2''',
}

acquainted_martial_card = {
    'name': 'Acquainted Martial path',

    'big_perks': [
        {'description': 'gain 1 small martial feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 4 maximum stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 1 times in toughness or with any weapon or shield. 
        (max prof. 3)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
    ],
    'small_perks': [
        {'description': 'gain 1 toughness (max prof. 2)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 weapon or shield proficiency (max prof. 1)', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 2 stamina', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 stamina', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
    ],
    'progression': '''Gain 1 minor option at levels 1, 3 and 4, and 1 major option at levels 2''',
}

legendary_skilled_card = {
    'name': 'Legendary Skilled path',
    'big_perks': [
        {'description': 'gain major skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Gain a new creative skill, which starts with 2 proficiency', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 8 maximum luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''gain 2 any skill proficiencies (max prof. 4)''',
         'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 medium skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small skilled feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'Gain a new creative skill',
         'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 skill proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 skill proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 any skill proficiencies (max prof. 1)', 'available1-4': 2, 'available 5-8': 1, 'available 9-12': 0},
        {'description': 'gain 3 luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 luck', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 luck', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Mark 4 minor options at levels 1 and 3, and 1 minor and 1 major option at levels 2 and 4''',
}

talented_skilled_card = {
    'name': 'Talented Skilled path',

    'big_perks': [
        {'description': 'gain major skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Gain a new creative skill, which starts with 2 proficiency', 'available1-4': 1, 'available 5-8': 1,
         'available 9-12': 1},
        {'description': 'gain 8 maximum luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 2 times with any skill (max prof. 4)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 medium skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 small skilled feat', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'Gain a new creative skill',
         'available1-4': 1, 'available 5-8': 0, 'available 9-12': 1},
        {'description': 'gain 1 skill proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 1 skill proficiency (max prof. 3)', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 any skill proficiencies (max prof. 1)', 'available1-4': 1, 'available 5-8': 1,
         'available 9-12': 0},
        {'description': 'gain 3 luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 2 luck', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 luck', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Gain 3 minor options at levels 1 and 3, and 1 major option at levels 2 and 4''',
}

adept_skilled_card = {
    'name': 'Adept Skilled path',

    'big_perks': [
        {'description': 'gain 1 medium skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Gain a new creative skill, which starts with 1 proficiency', 'available1-4': 1, 'available 5-8': 1,
         'available 9-12': 1},
         {'description': 'gain 6 maximum luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 1 times with any skill (max prof. 3)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 small skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 skill proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 2 luck', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
        {'description': 'gain 1 luck', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
    ],
    'progression': '''Gain 2 minor options at levels 1, 3 and 4, and 1 major option at levels 2''',
}

acquainted_skilled_card = {
    'name': 'Acquainted Skilled path',

    'big_perks': [
        {'description': 'gain 1 small skilled feat', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'Gain a new creative skill, which starts with 0 proficiency', 'available1-4': 1, 'available 5-8': 1,
         'available 9-12': 1},
        {'description': 'gain 4 maximum luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': '''advance 1 times with any skill (max prof. 3)''', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},

    ],
    'small_perks': [
        {'description': 'gain 1 skill proficiency (max prof. 2)', 'available1-4': 3, 'available 5-8': 3, 'available 9-12': 3},
        {'description': 'gain 2 luck', 'available1-4': 1, 'available 5-8': 1, 'available 9-12': 1},
        {'description': 'gain 1 luck', 'available1-4': 2, 'available 5-8': 2, 'available 9-12': 2},
    ],
    'progression': '''Gain 1 minor option at levels 1, 3 and 4, and 1 major option at levels 2''',
}

cards = {
    'MAGE': {
        1: acquainted_mage_card,
        2: adept_mage_card,
        3: talented_mage_card,
        4: legendary_mage_card
    },
    'MARTIAL': {
        1: acquainted_martial_card,
        2: adept_martial_card,
        3: talented_martial_card,
        4: legendary_martial_card
    },
    'SKILLED': {
        1: acquainted_skilled_card,
        2: adept_skilled_card,
        3: talented_skilled_card,
        4: legendary_skilled_card
    },
}