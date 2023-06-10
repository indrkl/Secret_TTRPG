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
     'effect': '''Converts all physical damage to psychic damage. Target's AC is 10 + their WILL proficiency + 
     AC proficiency (AC proficiency is now capped by Will proficiency)''',
     'bonus_variants': [
         {'effect': '{roll} d6 additional psychic damage',
          'lvls': [6, 9, 12, 15, 18],
          'roll': [1, 2, 3, 4, 5],
          },
         {'effect': 'force {roll} checks of afraid on a successful attack',
          'lvls': [6, 12, 18],
          'roll': [1, 2, 3],
          'min_lvl': 6,
          },
         {'effect': 'force {roll} checks of disoriented on a successful attack',
          'lvls': [6, 12, 18],
          'roll': [1, 2, 3],
          'min_lvl': 6,
          },
         {'effect': 'force {roll} checks of crazed on a successful attack',
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
         {'effect': '{roll} d6 additional fire damage',
          'lvls': [1, 5, 9, 13, 17],
          'roll': [1, 2, 3, 4, 5],
          },
         {'effect': 'force {roll} checks of burning on a successful attack',
          'lvls': [6, 12, 18],
          'roll': [1, 2, 3],
          'min_lvl': 6,
          },
         {'effect': 'force {roll} checks of burning on a critical attack',
          'lvls': [6, 12, 18],
          'roll': [(1, 2), (3, 4), (5, 6)],
          'min_lvl': 6,
          },
     ]
     },
    {'unique': True,
      'name': 'freezing',
     'effect': 'converts all physical damage to cold damage, this weapon can only do cold damage.',
    'bonus_variants': [
        {'effect': '{roll} d6 additional cold damage',
         'lvls': [1, 5, 9, 13, 17],
         'roll': [1, 2, 3, 4, 5],
         },
        {'effect': 'force {roll} checks of freezing on a successful attack',
         'lvls': [8, 14, 20],
         'roll': [1, 2, 3],
         'min_lvl': 8,
         },
        {'effect': 'force {roll} checks of freezing on a critical attack',
         'lvls': [8, 14, 20],
         'roll': [(1, 2), (3, 4), (5, 6)],
         'min_lvl': 8,
         },
    ]
     },
    {'name': 'heart seeker',
     'effect': '''Critical threshold is reduced by {roll}''',
     'lvls': [1, 5, 9, 13, 17],
     'roll': [1, 2, 3, 4, 5],
     },
    {'name': 'clarity',
     'effect': '''Attacks with weapon cannot be unlucky''',
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
     'lvls': [1, 6, 11, 16],
     'roll': [1, 2, 3, 4],
     'min_lvl': 1,
     },
]

def get_no_mods():
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
    # print(str(choices))
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
    no_mods = get_no_mods()
    print(no_mods)
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
    print(str(mods))
    for mod in mods:
        print (mod['effect'])


print_mods(roll_random_weapon(5))
    


armor_affixes = [
    {
        'name': 'Nourishing',
        'effect': '''Provides {roll} stamina recovery''',
        'lvls': [1, 5, 9, 13, 17],
        'roll': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Resistance',
        'effect': '''When attuning to this item, choose {roll} options from among physical, fire, cold, lightning,
        poison and psychic. You have resistance to chosen damage type(s). When re-attuning, these choices may be changed
        ''',
        'lvls': [3, 10, 17],
        'roll': [1, 2, 3],
    },
    {
        'name': 'Valor',
        'effect': '''Negative status effects have no effect unless they are at least level {roll}. After that level they
        however have their full effect.''',
        'lvls': [1, 5, 9, 13, 16, 19],
        'roll': [3, (4, 5), (6, 7), (8,9), (10,11), (12,14)],
    },
    {
        'name': 'Cleansing',
        'effect': '''At the beginning of your turn, reduce {roll} levels of negative status effects on you divided
        as you choose.''',
        'lvls': [1, 6, 11, 16],
        'roll': [(1, 2), (3, 4), (5, 6), (7, 8)],
    },
]

boots_affixes = [
    {
        'name': 'Hasted',
        'effect': '''Activate the effect once per day: For next 5 rounds you have 1-2 bonus AP (only 1 AP bonus can be 
        active)''',
        'lvls': '''8-18'''
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