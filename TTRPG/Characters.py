xd6_characters = [
    {
        'name': 'assassin',
        'MAGE': 2,
        'MARTIAL': 4,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Shifter',
                'Innate_feat_marital': 'Advanced senses',
                'Mage advancements': [
                    '''first illusion proficiency, false threats spell'''
                ],
                'Martial advancements': [
                    'first and second knife proficiency, first toughness proficiency',
                ],
            },
            2: {
                'Mage advancements': [
                    '''2 mana, second illusion proficiency'''
                ],
                'Martial advancements': [
                    'Shadow feat, Two weapon fighter feat',
                ],
            },
            3: {
                'Mage advancements': [
                    '''first will proficiency, 1 mana'''
                ],
                'Martial advancements': [
                    'Backstabber feat',
                ],
            },
        },
        'equipment': ['axe', 'dagger', '2 MD leather armor'],

    },
    {
        'name': 'elementalist',
        'MAGE': 4,
        'SKILLED': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Raw caster',
                'Innate_feat_skilled': 'Natural armor',
                'Mage advancements': [
                    '''first elemental proficiency, second elemental proficiency, fireball spell'''
                ],
                'Skilled advancements': [
                    'first lore proficiency, 1 luck',
                ],
            },
            2: {
                'Mage advancements': [
                    '''Pyromancy feat, first dimension proficiency, pass object spell, 1 mana'''
                ],
                'Skilled advancements': [
                    'Second lore proficiency, 2 luck',
                ],
            },
            3: {
                'Mage advancements': [
                    '''third elemental proficiency, 1 mana'''
                ],
                'Skilled advancements': [
                    'first will proficiency, first fortitude proficiency',
                ],
            },
        },
        'equipment': ['staff', 'robes (no armor)', '2 healing potions'],

    },
    {
        'name': 'Mastermind',
        'MAGE': 4,
        'SKILLED': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Raw caster',
                'Innate_feat_skilled': 'Specialist (leader',
                'Mage advancements': [
                    '''first and second discord proficiency, 'Weapon of horrors' spell'''
                ],
                'Skilled advancements': [
                    'first leadership proficiency, 1 luck',
                ],
            },
            2: {
                'Mage advancements': [
                    '''Enchanter feat, first elemental proficiency, 1 mana, enchant weapon spell'''
                ],
                'Skilled advancements': [
                    'Mastermind',
                ],
            },
            3: {
                'Mage advancements': [
                    '''second elemental proficiency, chain lightning, 1 mana'''
                ],
                'Skilled advancements': [
                    'Second leadership proficiency',
                ],
            },
        },
        'equipment': ['staff', 'robes (no armor)', '2 healing potions'],

    },
    {
        'name': 'Paladin',
        'MARTIAL': 4,
        'MAGE': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Divine protector',
                'Innate_feat_martial': 'Warcaster',
                'Mage advancements': [
                    '''1 harmony proficiency, guardian spell'''
                ],
                'Martial advancements': [
                    'Heavy armor proficiency, first sword proficiency',
                ],
            },
            2: {
                'Mage advancements': [
                    '''first and second toughness proficiency, 1 mana'''
                ],
                'Martial advancements': [
                    'Holy warrior feat, first shield proficiency, second sword proficiency',
                ],
            },
            3: {
                'Mage advancements': [
                    '''2 mana'''
                ],
                'Martial advancements': [
                    'first physique proficiency, second shield proficiency, 1 stamina',
                ],
            },
        },
        'equipment': ['sword', 'shield', '2 MD leather armor'],
    },
    {
        'name': 'Holy savage',
        'MARTIAL': 4,
        'MAGE': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Divine protector',
                'Innate_feat_martial': 'Defiant',
                'Mage advancements': [
                    '''first toughness proficiency, first will proficiency'''
                ],
                'Martial advancements': [
                    'first and second two handed axe proficiency, 1 stamina',
                ],
            },
            2: {
                'Mage advancements': [
                    '''second toughness and will proficiency'''
                ],
                'Martial advancements': [
                    'Savage axe and power strike feats',
                ],
            },
            3: {
                'Mage advancements': [
                    '''first force proficiency and push/pull'''
                ],
                'Martial advancements': [
                    '3 stamina, first physique proficiency',
                ],
            },
        },
        'equipment': ['Two handed axe', '2 MD leather armor'],
    },
    {
        'name': 'Inspiring leader',
        'SKILLED': 4,
        'MARTIAL': 2,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Prodigy',
                'Innate_feat_martial': 'Advanced senses',
                'Skilled advancements': [
                    '''first and second leadership proficiency, first diplomacy proficiency'''
                ],
                'Martial advancements': [
                    'first bow proficiency and first fortitude proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Inspiring, Inspiring leader, first survival proficiency, 3 luck'''
                ],
                'Martial advancements': [
                    'second bow proficiency and first toughness and physique proficiency',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''third leadership proficiency, 1 luck'''
                ],
                'Martial advancements': [
                    'second toughness proficiency',
                ],
            },
        },
        'equipment': ['axe', 'shield', '3 MD, 1 DR padding and chain mail heavy armor combo'],
    },
    {
        'name': 'Trickster',
        'SKILLED': 3,
        'MAGE': 3,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Lucky',
                'Innate_feat_mage': 'Raw caster',
                'Skilled advancements': [
                    '''first and second survival proficiency'''
                ],
                'Mage advancements': [
                    'first illusion proficiency, 1 mana, false threats',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Agent of chaos, 1 luck'''
                ],
                'Mage advancements': [
                    'Trickster feat, maddening hex spell, second illusion proficiency',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''3 luck'''
                ],
                'Mage advancements': [
                    'first and second discord proficiency' ,
                ],
            },
        },
        'equipment': ['staff', '2 MD leather armor'],
    },
    {
        'name': 'Sentinel',
        'SKILLED': 2,
        'MARTIAL': 4,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Specialist (survival)',
                'Innate_feat_martial': 'Defiant',
                'Skilled advancements': [
                    '''first survival and diplomacy proficiency'''
                ],
                'Martial advancements': [
                    'first polearm proficiency and second polearm proficiency, 1 stamina',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Foresight, 1 luck, first physique proficiency'''
                ],
                'Martial advancements': [
                    'Sentinel and heavy armor feat',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''Second survival proficiency'''
                ],
                'Martial advancements': [
                    'third polearm proficiency, 1 stamina' ,
                ],
            },
        },
        'equipment': ['spear', '3 MD, 1 DR padding and chain mail heavy armor combo'],
    },
]

player_characters = [
    {
        'name': 'Jack of all trades',
        'SKILLED': 2,
        'MARTIAL': 2,
        'MAGE': 2,
        'defense': 4,
        'Innate_feat_skilled': 'Lucky',
        'Innate_feat_martial': 'Extraordinary senses',
        'Innate_feat_mage': 'Shifter',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): diplomacy''',
                    '''proficiency (first): lore''',
                    # '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    'proficiency (first): illusion',
                    'spell: Side step',
                ],
                'Martial advancements': [
                    'feat: Medium armor proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (first): crafting''',
                    '''proficiency (first): treasure hunting''',
                    '''feat: Foresight'''

                ],
                'Mage advancements': [
                    'feat: Commune with animals',
                    '''proficiency (first): will''',
                    '''1 mana'''
                ],
                'Martial advancements': [
                    'feat: Medium armor proficiency',
                    '''proficiency (first): sword''',
                    '1 stamina'
                ],
            },
            3: {
                'Skilled advancements': [
                    '''2 luck'''
                ],
                'Mage advancements': [
                    'proficiency (second): illusion',
                ],
                'Martial advancements': [
                    '''proficiency (second): sword''',
                ],
            },
        },
        'equipment': ['sword', 'padded leather armor',],
    },
    {
        'name': 'Quigly the demon hunter',
        'SKILLED': 2,
        'MARTIAL': 3,
        'MAGE': 1,
        'defense': 5,
        'Innate_feat_skilled': 'Specialist(lore)',
        'Innate_feat_martial': 'Anti mage',
        'Innate_feat_mage': 'Divine protector',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (second): lore''',
                    '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    '''proficiency (first): lore''',
                ],
                'Martial advancements': [
                    'feat: Heavy armor proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (third): lore''',
                    '''proficiency (first): survival''',
                ],
                'Mage advancements': [
                    '''proficiency (first): will''',
                    '''1 mana'''
                ],
                'Martial advancements': [
                    'feat: Blessed warrior',
                    '''proficiency (first): sword''',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''proficiency (second): survival''',
                ],
                'Mage advancements': [
                    'proficiency (first): toughness',
                ],
                'Martial advancements': [
                    '''proficiency (second): sword''',
                    '''1 stamina'''
                ],

            },
            4: {
                'Skilled advancements': [
                    '''proficiency (first): physique''',
                    '''proficiency (first): diplomacy''',
                ],
                'Mage advancements': [
                    '1 mana',
                ],
                'Martial advancements': [
                    '''proficiency (first): shield''',
                    '''proficiency (second): shield''',
                ],

            },
        },
        'equipment': ['sword', 'Heavy chain mail', 'shield'],
    },
    {
        'name': 'Esmeralda the warden of silver bats',
        'SKILLED': 2,
        'MAGE': 4,
        'Innate_feat_skilled': 'Specialist(lore)',
        'Innate_feat_mage': 'Divine protector',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): will''', '''proficiency (first): lore''',
                    '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    'proficiency (first): elemental', 'proficiency (second): elemental', 'spell: fireball',
                    'spell: Elemental weapon', '1 mana'
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (second): lore''', '2 luck'
                ],
                'Mage advancements': [
                    'proficiency (first): nature', 'proficiency (second): nature', 'feat: iron concentration',
                    'spell: heal', 'spell: grant luck'
                ],
            },
            3: {
                'Skilled advancements': [
                    '''2 luck'''
                ],
                'Mage advancements': [
                    'proficiency (third): nature', 'spell: tremor', '1 mana',
                ],
            },
            4: {
                'Skilled advancements': [
                    '''1 luck''', 'proficiency (first): physique'
                ],
                'Mage advancements': [
                    'Progression feat: Spice specialist',
                    'feat: Commune with animals',
                    '2 mana',
                ],
            },
        },
        'equipment': ['staff'],
    },
    {
        'name': 'Fred the Forgetful mage',
        'SKILLED': 2,
        'MAGE': 4,
        'Innate_feat_skilled': 'Specialist(survival)',
        'Innate_feat_mage': 'Raw caster',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): survival''', '''proficiency (first): lore''',
                    '''proficiency (extra): survival'''
                ],
                'Mage advancements': [
                    'proficiency (first): force', 'proficiency (second): force', 'spell: push/pull', 'spell: Telekinesis',
                    'proficiency (first): dimension', 'spell: pass object'
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (second): survival''', '2 luck'
                ],
                'Mage advancements': [
                    'proficiency (second): dimension', 'proficiency (third): force',
                    '3 mana', 'spell: Explosive force', 'spell: Blink jump',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''2 luck''',
                ],
                'Mage advancements': [
                    '4 mana',
                ],
            },
            4: {
                'Skilled advancements': [
                    '''Progression feat: Resourceful''',
                    'feat: Deep apology',
                ],
                'Mage advancements': [
                    'feat: Twin magic',
                ],
            },
        },
        'equipment': ['a single lucky broken beer mug'],
    },
    {
        'name': 'Ralf the Troll diplomat',
        'SKILLED': 4,
        'MARTIAL': 2,
        'defense': 5,
        'Innate_feat_skilled': 'Natural armor(heavy armor)',
        'Innate_feat_martial': 'Extraordinary senses',
        'Levels': {
            1: {
                'Skilled advancements': [
                    '''proficiency (first): diplomacy''', 'proficiency (second): diplomacy', '1 luck'
                ],
                'Martial advancements': [
                    'proficiency (first): toughness', 'proficiency (first): physique',
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Offer them to surrender', 'proficiency (third): diplomacy'
                ],
                'Martial advancements': [
                    'proficiency (second): toughness', 'proficiency (second): physique',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (first): lore', 'proficiency (first): leadership', 'proficiency (second): leadership'
                ],
                'Martial advancements': [
                    '2 stamina',
                ],
            },
            4: {
                'Skilled advancements': [
                    'feat: Master plan', 'Progression feat: Powerful'
                ],
                'Martial advancements': [
                    '1 stamina', 'proficiency (first): unarmed',
                ],
            }
        },
        'equipment': [],
        'normal_actions': ['Wrestle'],
    },
    {
        'name': 'Tom the religious gangsta poet',
        'SKILLED': 2,
        'MARTIAL': 4,
        'defense': 3,
        'Innate_feat_skilled': 'Prodigy',
        'Innate_feat_martial': 'Extraordinary senses',
        'Levels': {
            1: {
                'Skilled advancements': [
                    'proficiency (first): concealment', 'proficiency (first): survival'
                ],
                'Martial advancements': [
                    'proficiency (first): dagger', 'proficiency (second): dagger', 'proficiency (first): toughness'
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Agent of chaos', 'proficiency (second): survival', 'proficiency (first): diplomacy'
                ],
                'Martial advancements': [
                    'feat: Shadow', 'feat: Two weapon fighter',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (second): concealment'
                ],
                'Martial advancements': [
                    'feat: Backstabber',
                ],
            },
            4: {
                'Skilled advancements': [
                    'Progression feat: Resourceful', '2 luck'
                ],
                'Martial advancements': [
                    'proficiency (first): mace', 'proficiency (second): mace', '1 stamina'

                ],
            }
        },
        'equipment': ['1 handed mace', 'dagger', 'simple leather armor'],

    },
    {
        'name': 'Deadeye the Gang leader',
        'SKILLED': 3,
        'MARTIAL': 3,
        'defense': 2,
        'Innate_feat_skilled': 'Prodigy',
        'Innate_feat_martial': 'Natural killer',
        'Levels': {
            1: {
                'Skilled advancements': [
                    'proficiency (first): leadership', 'proficiency (second): leadership'
                ],
                'Martial advancements': [
                    'proficiency (first): bow', 'proficiency (second): bow',
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Natural leader', 'proficiency (first): survival', 'proficiency (third): leadership'
                    , '2 luck', 'proficiency (first): will',
                ],
                'Martial advancements': [
                    'feat: Shadow', 'proficiency (first): toughness', 'proficiency (first): sword',
                    'proficiency (first): fortitude',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (second): survival', '1 luck'
                ],
                'Martial advancements': [
                    'proficiency (third): bow',
                ],
            },
        },
        'equipment': ['shortbow', 'sword', 'simple leather armor'],

    },
    {
        'name': 'Jaxxen, the assassing',
        'MARTIAL': 4,
        'SKILLED': 2,
        'defense': 2,
        'Levels': {
            1: {
                'Skilled advancements': [
                    'proficiency (first): physique', 'proficiency (first): leadership'
                ],
                'Martial advancements': [
                    'proficiency (first): dagger', 'proficiency (second): dagger', 'proficiency (first): toughness'
                ],
            },
            2: {
                'Skilled advancements': [
                    'proficiency (second): physique', 'proficiency (second): leadership'
                ],
                'Martial advancements': [
                    'feat: Two weapon fighter', 'feat: Opportunist'
                ],
            },
            3: {
                'Skilled advancements': [
                    'feat: Poison specialist'
                ],
                'Martial advancements': [
                ],
            },
            4: {
                'Skilled advancements': [
                    'proficiency (first): will', 'proficiency (first): fortitude'
                ],
                'Martial advancements': [
                    'proficiency (third): dagger'
                ],
            },
            5: {
                'Skilled advancements': [
                    'proficiency (third): physique', 'proficiency (first): reflex'
                ],
                'Martial advancements': [
                    'feat: Dodging', 'proficiency (second): toughness', '1 stamina'
                ],
            },
        },
        'equipment': ['dagger', 'simple leather armor'],

    },
    {
        'name': 'Ember - Kole ja naiivne nõid',
        'SKILLED': 2,
        'MAGE': 4,
        'Innate_feat_skilled': 'Good fortune',
        'Innate_feat_mage': 'Divine protector',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''2 luck''',
                ],
                'Mage advancements': [
                    'feat: Commune with animals',
                    'proficiency (first): illusion', 'spell: Create illusionary images',
                    'proficiency (first): harmony', 'spell: Bless'
                ],
            },
            2: {
                'Skilled advancements': [
                    '4 luck'
                ],
                'Mage advancements': [
                    'feat: Holy bonds',
                    'proficiency (first): divination',
                    '1 mana', 'spell: Glimpse into future', 'proficiency (first): toughness'
                ],
            },
        },
        'equipment': ['staff'],
    },
    {
        'name': 'Wolfgang "Olly" Olivier - Monster Connoisseur',
        'SKILLED': 4,
        'MARTIAL': 2,
        'Innate_feat_skilled': 'Prodigy',
        'Innate_feat_martial': 'Natural armor',
        'defense': 4,
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): crafting''','''proficiency (first): leadership''',
                    '''proficiency (first): harvesting''','''proficiency (first): survival''',
                ],
                'Martial advancements': [
                    'proficiency (first): sword',
                    'proficiency (first): fortitude'
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (first): lore''',
                    '''proficiency (second): lore''',
                    '''proficiency (second): crafting''',
                    '''proficiency (third): crafting''',
                    '''proficiency (second): leadership''',
                    '''proficiency (second): harvesting''',
                    'feat: Master plan'
                ],
                'Martial advancements': [
                    'proficiency (first): shield',
                    'proficiency (first): reflex',
                    '1 stamina',
                    'proficiency (first): toughness'
                ],
            },
        },
        'equipment': ['sword', 'shield', 'butchering knife', 'extensive cooking equipment', 'Butchering clothes'],
    },
    {
        'name': 'Big axe dude',
        'SKILLED': 2,
        'MARTIAL': 4,
        'Innate_feat_skilled': 'Natural armor',
        'Innate_feat_martial': 'Defiant',
        'defense': 3,
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): diplomacy''','''proficiency (first): physique''',
                ],
                'Martial advancements': [
                    'proficiency (first): axe',
                    'proficiency (second): axe',
                    '1 stamina',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''feat: Intimidating presence''',
                    '''proficiency (first): survival''',
                    '''proficiency (first): fortitude''',
                ],
                'Martial advancements': [
                    'proficiency (third): axe',
                    '2 stamina',
                    'proficiency (first): toughness',
                    'proficiency (second): toughness'
                ],
            },
        },
        'equipment': ['two handed axe', 'axe', 'clothes'],
    },
    {
        'name': 'Ispen',
        'SKILLED': 2,
        'MARTIAL': 4,
        'Innate_feat_skilled': 'Extraordinary senses',
        'Innate_feat_martial': 'Tough',
        'defense': 4,
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''1 luck''','''proficiency (first): physique''',
                ],
                'Martial advancements': [
                    'feat: Heavy armor proficiency',
                    'proficiency (first): toughness',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''4 luck''',
                ],
                'Martial advancements': [
                    'proficiency (first): mace',
                    '4 stamina',
                    'proficiency (first): shield',
                    'proficiency (second): mace'
                ],
            },
        },
        'equipment': ['Heavy chain mail', 'shield', '1 handed mace', ],
    },
    {
        'name': 'Zenui',
        'MAGE': 2,
        'MARTIAL': 4,
        # 'Innate_feat_skilled': 'Natural armor',
        'Innate_feat_martial': 'Tough',
        'defense': 2,
        'Levels': {
            1: {

                'Mage advancements': [
                    '''proficiency (first): force''',
                    '''proficiency (first): will''',
                    'spell: telekinesis',
                ],
                'Martial advancements': [
                    'proficiency (first): unarmed',
                    'proficiency (second): unarmed',
                    'proficiency (first): toughness',
                ],
            },
            2: {
                'Mage advancements': [
                    '''proficiency (second): force''', '''2 mana''',
                    'spell: Force field',
                ],
                'Martial advancements': [
                    '''feat: Dodging''',
                    '''proficiency (third): unarmed''',
                    '''proficiency (second): toughness''',
                ],
            },
        },
        'equipment': ['dagger', 'simple leather armor'],
    },
    {
        'name': 'Gruthna, the elemental touched',
        'MAGE': 3,
        'MARTIAL': 1,
        'SKILLED': 2,
        'Innate_feat_mage': 'Duality(Illusion and Elemental)',
        'Innate_feat_martial': 'Wings',
        'Innate_feat_skilled': 'Specialist(lore)',
        'defense': 2,
        'Levels': {
            1: {

                'Mage advancements': [
                    '''proficiency (first): duality''',
                    '''proficiency (second): duality''',
                    'spell: False threats',
                    'spell: Fireball',
                ],
                'Martial advancements': [
                    'proficiency (first): physique',
                ],
                'Skilled advancements': [
                    'proficiency (extra): lore',
                    'proficiency (first): lore',
                    'proficiency (first): reflex',
                ],
            },
            2: {
                'Mage advancements': [
                    '''proficiency (third): duality''',
                    'spell: Create illusionary images',
                    '1 mana',
                    'feat: Large magic'
                ],
                'Martial advancements': [
                    'proficiency (first): fortitude',
                    'proficiency (first): toughness',
                ],
                'Skilled advancements': [
                    'proficiency (second): lore',
                    'proficiency (first): reflex',
                ],
            },
        },
        'equipment': ['staff', 'simple leather armor'],
    },
]



import re
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style
from reportlab.lib import colors


spell_schools = ['']

def split_data_into_columns(data, column_number):
    rows = []
    indx = 0
    row = []
    for i in range(len(data)):
        row.append(data[i])
        indx += 1
        if indx == column_number:
            rows.append(row)
            row = []
            indx = 0
    if indx > 0:
        while indx < column_number:
            row.append('')
            indx+=1
        rows.append(row)
    return rows

def get_feat_and_flowable(name, name_addon=''):
    from Innate_feats import feats as all_innate_feats
    from Normal_feats import feats as all_normal_feats
    from progression_feats import feats as all_progression_feats
    from Innate_feats import prep_feat_flowable as prep_innate_feat_flowable
    from Normal_feats import prep_feat_flowable as prep_normal_feat_flowable
    from progression_feats import prep_feat_flowable as prep_progression_feat_floable

    for path in all_innate_feats:
        for feat in all_innate_feats[path]:
            if feat['name'].lower() == name.lower():
                return feat, prep_innate_feat_flowable(feat,name_addon=name_addon)
    for path in all_normal_feats:
        for feat in all_normal_feats[path]:
            if feat['name'].lower() == name.lower():
                return feat, prep_normal_feat_flowable(feat)
    for path in all_progression_feats:
        for feat in all_progression_feats[path]:
            if feat['name'].lower() == name.lower():
                return feat, prep_progression_feat_floable(feat)
    print(name)

def find_general_action(name, all_general_actions):
    for action in all_general_actions:
        if action['name'] == name:
            return action

def get_spell_flowable(name):
    from Spells import schools
    from Spells import prep_spell_flowable as prep_spell_flowable


    for school in schools:
        for spell in schools[school]['spells']:
            if spell['name'].lower() == name.lower():
                return prep_spell_flowable(spell)

def get_equipment_flowable(name):
    from equipment import equipment as all_equipment
    from equipment import prep_equipment_flowable


    if name in all_equipment:
        return prep_equipment_flowable(all_equipment[name], name)
    else:
        return [Paragraph(name, style=minor_subtitle)]

mana_multiplier = 2
luck_multiplier = 1
def generate_character_flowable(character):

    from Skills import skills
    skill_names = [x['name'] for x in skills]

    from Spells import schools

    spell_school_names = [key.lower() for key in schools]

    from equipment import weapon_classes

    innate_feats = [{'name': character[key], 'path': key[12:]} for key in ['Innate_feat_skilled', 'Innate_feat_mage', 'Innate_feat_martial'] if key in character]
    feats = []
    prog_feats = []
    proficiencies = {}
    spells = []
    stats = {'mana': 0, 'stamina': 0, 'luck': 0, 'toughness': 2, 'will': 0, 'fortitude': 0, 'reflex': 0}

    for indx in character['Levels']:
        level = character['Levels'][indx]
        for key in level:
            for advancement in level[key]:
                proficiency = re.search('proficiency \((first|second|third|fourth|extra)\): ([a-z ]*)', advancement)
                if proficiency:
                    proficiency = proficiency[2]
                    proficiencies[proficiency] = proficiencies.get(proficiency, 0) + 1
                    continue

                spell = re.search('spell: ([A-Za-z\' \/]*)', advancement)
                if spell:
                    spells.append(spell[1])
                    continue
                prog_feat = re.search('Progression feat: ([A-Za-z ]*)', advancement)
                if prog_feat:
                    print ("PROG FEAT")
                    prog_feats.append(prog_feat[1])
                    continue
                feat = re.search('feat: ([A-Za-z ]*)', advancement)
                if feat:
                    feats.append(feat[1])
                    continue
                stat = re.search('([0-9]*) (mana|stamina|luck)', advancement)
                if stat:
                    stats[stat[2]] += int(stat[1])
                    continue

                raise Exception(advancement + ' is unhandled')

    stats['toughness'] += proficiencies.get('toughness', 0)
    stats['will'] += proficiencies.get('will', 0)
    stats['fortitude'] += proficiencies.get('fortitude', 0)
    stats['reflex'] += proficiencies.get('reflex', 0)

    stats['mana'] = stats['mana'] * mana_multiplier
    stats['luck'] = stats['luck'] * luck_multiplier

    elements = []
    elements.append(Paragraph(character['name'], style=minor_title))
    data = [
        [f"Martial: {character.get('MARTIAL', 0)}", f"Mage: {character.get('MAGE', '0')}", f"Skilled: {character.get('SKILLED', '0')}"],
        [f"Stamina: {stats.get('stamina')}", f"Mana: {stats.get('mana')}", f"Luck: {stats.get('luck')}"],
        [f"Toughness: {stats.get('toughness')}", f"Defense: {character.get('defense', 0)}", f""],
        [f"Will: {stats.get('will')}", f"Fortitude: {stats.get('fortitude', 0)}", f"Reflex: {stats.get('reflex')}"],
    ]

    skill_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in skill_names]

    data.extend(split_data_into_columns(skill_proficiencies, 3))

    spell_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in spell_school_names]

    data.extend(split_data_into_columns(spell_proficiencies, 3))

    weapon_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in weapon_classes]

    data.extend(split_data_into_columns(weapon_proficiencies, 3))

    table = Table(data, colWidths=[160]*3)
    table.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)




    elements.append(Paragraph('Feats', style=minor_subtitle))

    path_mapping = {1: 'Acquinted', 2: 'Adept', 3: 'Talented', 4: 'Legendary'}

    for feat in innate_feats:
        feat_name = re.search('(^[A-Za-z ]*)', feat.get('name'))[1]
        path_power = character.get(feat['path'].upper())
        name_addon = ' (%s)'%(path_mapping[path_power])
        _, feat_flowable = get_feat_and_flowable(feat_name, name_addon=name_addon)

        elements.extend(feat_flowable)

    for feat in feats:
        _, feat_flowable = get_feat_and_flowable(feat)
        elements.extend(feat_flowable)

    for feat in prog_feats:
        _, feat_flowable = get_feat_and_flowable(feat)
        elements.extend(feat_flowable)

    elements.append(Paragraph('Spells', style=minor_subtitle))

    for spell in spells:
        spell_obj = get_spell_flowable(spell)
        elements.extend(spell_obj)

    if character.get('normal_actions'):
        from general_actions import actions as general_actions
        from general_actions import prep_action_flowable
        elements.append(Paragraph('General actions', style=minor_subtitle))

        for action in character.get('normal_actions'):
            action_obj = find_general_action(action, general_actions)
            elements.extend(prep_action_flowable(action_obj))


    elements.append(Paragraph('Equipment', style=minor_subtitle))

    for equipment in character.get('equipment', []):
        elements.extend(get_equipment_flowable(equipment))

    return elements

def get_player_character_chapter():
    elements = [
        # {'type': 'title', 'content': 'Player characters'},
    ]
    first = True
    for character in player_characters:
        if not first:
            elements.append({'type': 'flowables', 'content': [PageBreak()]})
        else:
            first = False
        elements.append({'type': 'flowables', 'content': generate_character_flowable(character)})


    return elements

def get_player_character_chapters():

    for character in player_characters:
        elements = [{'type': 'flowables', 'content': generate_character_flowable(character)}]
        yield (elements, character['name'])
