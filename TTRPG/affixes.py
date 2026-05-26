import copy
import random

weapon_affixes = [
    {
        'unique': True,
    'name': 'venomous',
     'effect': 'Can apply poison on the weapon.',
     'bonus_variants': [
         {'effect': 'When coating the weapon, it gets additional {roll} stacks of poison',
          'lvls': [1, 5, 9, 13, 17],
          'roll': [1, 2, 3, 4, 5],
          },
         {'effect': 'each attack applies {roll} additional stacks of poisons per attack',
          'lvls': [5, 15],
          'roll': [1, 2],
          'min_lvl': 5,
          },
         {'effect': 'this weapon deals {roll} extra damage for each stack of poison on the enemy',
          'lvls': [10, 20],
          'roll': [1, 2],
          'min_lvl': 10,
          },
        ]
     },
    {
        'unique': True,
    'name': 'Ethereal',
     'effect': '''Converts all physical damage to psychic damage. This bypasses target's defenses when dealing damage,
     but a R4 using will proficiency can negate 2 damage.''',
     'bonus_variants': [
         {'effect': '{roll} additional psychic damage',
          'lvls': [6, 9, 12, 15, 18],
          'roll': [1, 2, 3, 4, 5],
          },
         {'effect': 'Apply {roll} levels of afraid on a successful attack',
          'lvls': [7, 14],
          'roll': [1, 2],
          'min_lvl': 7,
          },
         {'effect': 'Apply {roll} levels of disoriented on a successful attack',
          'lvls': [6, 12, 18],
          'roll': [1, 2, 3],
          'min_lvl': 6,
          },
        ],
        'min_lvl': 6
     },
    {'unique': True,'name': 'fiery',
     'effect': 'converts all physical damage to fire damage, this weapon can only do fire damage.',
     'bonus_variants': [
         {'effect': '{roll} additional fire damage',
          'lvls': [1, 5, 9, 13, 17],
          'roll': [1, 2, 3, 4, 5],
          },
         {'effect': 'Apply {roll} levels of burning on a successful attack',
          'lvls': [6, 12, 18],
          'roll': [1, 2, 3],
          'min_lvl': 6,
          },
     ]
     },
    {'unique': True,
      'name': 'freezing',
     'effect': 'converts all physical damage to cold damage, this weapon can only do cold damage.',
    'bonus_variants': [
        {'effect': '{roll} additional cold damage',
         'lvls': [1, 5, 9, 13, 17],
         'roll': [1, 2, 3, 4, 5],
         },
        {'effect': 'Apply {roll} levels of freezing on a successful attack',
         'lvls': [8, 14, 20],
         'roll': [1, 2, 3],
         'min_lvl': 8,
         },
    ]
     },
    {'name': 'heart seeker',
     'effect': '''Attacks involving 5 or more power strikes get {roll} additional power dice to use''',
     'lvls': [1, 6, 11, 16],
     'roll': [1, 2, 3, 4],
     },
    {'name': 'clarity',
     'effect': '''Attacks with weapon cannot be unlucky or have disadvantage''',
     'lvls': [1],
     'roll': [1],
     },
    {'name': 'strife',
     'effect': '''Hits with this weapon drain {roll} stamina from target''',
     'lvls': [2, 6, 10, 14, 18],
     'roll': [1, 2, 3, 4, 5],
     'min_lvl': 2,
     },
    {'name': 'siphoning',
     'effect': '''Hits with this weapon steal {roll} stamina from target''',
     'lvls': [7, 13, 19],
     'roll': [1, 2, 3],
     'min_lvl': 7,
     },
    {'name': 'resolve',
     'effect': '''When you successfully hit with this weapon, remove {roll} lvl of a negative status effect from yourself''',
     'lvls': [3, 10, 17],
     'roll': [1, 2, 3],
     'min_lvl': 3,
     },
    {'name': 'anti-magic',
     'effect': '''When you successfully hit with this weapon, target loses {roll} mana''',
     'lvls': [1, 4, 7, 10, 13, 16, 19],
     'roll': [1, 2, 3, 4, 5, 6, 7],
     'min_lvl': 1,
     },
]

def get_nr_mods():
    i = random.random()*100
    if i > 99:
        return 3
    elif i > 90:
        return 2
    else:
        return 1

def select_random_mod(mods, allow_uniques, lvl, existing_mods=[]):
    choices = []
    for x in mods:
        if (allow_uniques or not x.get('unique', False)) and x.get('min_lvl', 1) <= lvl and x.get('name', '') not in existing_mods:
            choices.append(x)
    return random.choice(choices)

def solidify_effect(mod, lvl):
    if mod.get('roll', []):
        lvls = mod.get('lvls', [])
        indx = random.choice([i for i in range(len(lvls)) if lvls[i] <= lvl])
        roll = mod['roll'][indx]
        if type(roll) is tuple:
            roll = random.choice([r for r in range(roll[0], roll[1]+1, 1)])
        mod['effect'] = mod['effect'].format(roll=roll)

    if 'bonus_variants' in mod:
        bonus_mod = copy.deepcopy(select_random_mod(mod['bonus_variants'], True, lvl))
        solidify_effect(bonus_mod, lvl)
        mod['effect'] += '\n%s'%(bonus_mod['effect'])


def roll_random_weapon(lvl):
    no_mods = get_nr_mods()
    mods = []

    unique = False
    for i in range(no_mods):
        new_mod = copy.deepcopy(select_random_mod(weapon_affixes, not unique, lvl, [m['name'] for m in mods]))
        if new_mod.get('unique', False):
            unique = True
        solidify_effect(new_mod, lvl)

        mods.append(new_mod)

    return mods


def print_mods(mods):
    for mod in mods:
        print (mod['effect'])


print_mods(roll_random_weapon(5))
    


armor_affixes = [
    {
        'name': 'Nourishing',
        'effect': '''Provides {roll} stamina recovery''',
        'lvls': [5, 15],
        'roll': [1, 2],
    },
    {
        'name': 'Resistance',
        'effect': '''
        You have {roll} damage reduction against {damage_type} damage. 
        ''',
        'lvls': [3, 10, 17],
        'roll': [1, 2, 3],
        'options': [
            {'damage_type': ['physical', 'fire', 'cold', 'lightning', 'psychic', 'poison']}
        ]
    },
    {
        'name': 'Valor',
        'effect': '''Negative status effects have no effect unless they are at least level {roll}. After that level they
        however have their full effect.''',
        'lvls': [1, 5, 9, 13, 16, 19],
        'roll': [2, 3, 4, 5, 6, 7],
    },
    {
        'name': 'Cleansing',
        'effect': '''At the beginning of your turn, reduce {roll} levels of negative status effects on you divided
        as you choose.''',
        'lvls': [1, 6, 11, 16],
        'roll': [1, 2, 3, 4],
    },
]

boots_affixes = [
    {
        'name': 'Hasted',
        'effect': '''During combat, each turn roll {roll} additional dice, which can only be used for movement but do 
        not spend action-limit''',
        'lvls': [3, 13],
        'roll': [1, 2],
    },
]

jewelry_affixes = [
    {'name': 'condition immunity',
     'effect': 'Immune to {one condition} condition',
     },
    {'name': 'skill safety',
     'effect': 'Critical failures for {one skill} checks are treated as normal failures instead',
     },
    {
        'name': 'Hasted',
        'effect': '''Activate the effect once per day / encounter: Recover all encounter mana''',
        'lvls': '''7, 17'''
    },
    {
        'name': 'Hexproof',
        'effect': '''You have advantage against will checks for removing hexes and status effects gained through hexes.
        ''',
        'lvls': '''5'''
    },
]

pricing_of_items = """
Each affix has a level requirement, but also each magical item can have 1 to 3 affixes. Items with 2 affixes double
their price, and items with 3 affixes double their price on top of that. But the base price is based on the level of
affixes in the item and is additive per property
"""

affix_lvl_cost = {
    1: 200,
    2: 250,
    3: 300,
    4: 350,
    5: 400,
    6: 500,
    7: 650,
    8: 800,
    9: 1000,
    10: 1200,
    11: 1400,
    12: 1600,
    13: 1800,
    14: 2000,
    15: 2500,
    16: 3000,
    17: 3500,
    18: 4000,
    19: 5000,
    20: 7500
}