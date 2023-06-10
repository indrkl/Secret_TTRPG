"""

"""

thugs = [
    {
        'MARTIAL': 2,
        'Advances': [{
            'lvl': 1,
            'max_stamina': 1,
            'feats': ['rampage']
        },
        {'lvl': 2,
         'max_stamina': 2,
         },
        {'lvl': 3,
         'axe_mastery': 2,
         },
        ],
        'General strategy': ['''
This is a thug who just wants to burst down the enemy. So focus on max stamina, weapon mastery and uses rampage
as much as possible.
        ''']
    },
    {
        'MARTIAL': 2,
        'Advances': [{
            'lvl': 1,
            'weapon_mastery': 2,
            'stamina_recovery': 1
        },
        {'lvl': 2,
         'AC': 2,
         },
        {'lvl': 3,
         'stamina_recovery': 1,
         },
        ],
        'General strategy': ['''
Tries to makes as many attacks per turn as possible. Focuses on having as much as weapon mastery as possible.
        ''']
    },
    {
        'MARTIAL': 3,
        'Advances': [{
            'lvl': 1,
            'feats': ['medium armor proficiency'],
            'stamina_recovery': 1,
            'AC': 1,
        },
        {'lvl': 2,
         'AC': 2,
         'weapon_mastery': 1,
         },
        {'lvl': 3,
         'AC': 1,
         'stamina recovery': 1,
         },
        ],
        'General strategy': ['''
A tank, increasing AC, also HP later on. Uses a shield. Take some in weapon mastery. This can be like a boss of the 
group.
        ''']
    },
    {
        'MARTIAL': 3,
        'Advances': [{
            'lvl': 1,
            'stamina_recovery': 1,
            'AC': 1,
            'hp': 2,
            'weapon mastery': 1
        },
        {'lvl': 2,
         'hp': 2,
         'weapon_mastery': 1,
         },
        {'lvl': 3,
         'hp': 1,
         'stamina recovery': 1,
         },
        ],
        'General strategy': ['''
A tank, increasing AC, also HP later on. Uses a shield. Take some in weapon mastery. This can be like a boss of the 
group.
        ''']
    },
]

scenese = {
    'Chase scene': {
        'progress options': [
            'Heroes manage to keep track',
            'The chased distracts using guards, "help, this murderer is chasing me!"',
            'Hero gets near their base, but must avoid ambush',
            'The chased gets lost and is cornered in an ally, so a duel?'
        ],
        'things that can go wrong': [
            'Loses the chased',
            'Gets ambushed after over-extending',
            'Gets arrested by guards, so this will need to be worked out',

        ],
        ''
    }
}