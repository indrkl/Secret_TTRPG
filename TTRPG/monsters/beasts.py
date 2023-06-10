info = [
    '''beasts have weak will, but high fortitude, so they gain a natural bonus of +1 to FORT saves, but -1 to will 
    saves. Their basic attacks have same stamina costs as humanoids and deal 1d6+X damage, where X is based on their
    archetype.
    ''',
]

archetypes = [
    {
        'name': 'small animal',
        'description': '''
            13 AC (1 natural armor, 2 size bonus), small amount of HP (2 per path level per level), damage dice is d6, 
                Has advanced senses. +1 REF saves +2 to survival checks, 25 move speed.
        '''
     },
    {'name': 'medium sized predators',
     'description': '''
        13 AC (3 natural armor), high amounts of HP (4 per path levl per level). Damage dice is d6+1. Has advanced senses. This is 
        Leopards, wolves, tigers etc. 12 m. move speed.
     '''
     },
    {'name': 'large sized predators',
     'description': '''
        12 AC (3 natural armor, 1 size penalty), very high amounts of HP (5 per path level per level). Damage dice is d6+2. Has 
        advanced senses. This is something like a bear. 14 m. move speed but after first move action per turn movement
        costs 1 STA.
     '''
     },
    {'name': 'Bird predator',
     'description': '''
        12 AC (2 natural armor), OK amounts of HP (3 per path level per level). Damage dice is d6. Has advanced senses. Has legendary 
        wings.
        Example: eagle
     '''
     },
    {'name': 'Tiny bird',
     'description': '''
        14 AC (no natural armor, 4 size bonus), few amounts of HP (1 per path level per level). No damage. Has advanced senses. 
        Has legendary wings. +2 REF saves, +2 to survival checks, 12 m. fly speed
        Example: mockingbird
     '''
     },
]


feats = [
    {
        'cost': 3,
        'name': 'Bite grappling',
        'effect': '''
        if you succeed in a bite attack, then in addition to the damage and other effects, target becomes grappled. 
        While grappled, target cannot take the move action if their size is same or smaller than yours. Otherwise, if
        they do a move action, they move you along with them. If you take damage, make a FORTITUDE check with a DC of 
        damage / 2. When you fail the check, the grappling ends. You must spend 2 STA to hold the grapple at the 
        beginning of your turn. While grappling you cannot do another bite attack.
        ''',
        'action': {
            'speed': '2A',
            'range': 'melee',
            'target': 'single',
            'base_cost': '3S',
            'next_attack_cost_increase': '1S',
            'effect': '''3d6+X damage piercing damage bite attack ''',
        }
    },
    {
        'cost': 2,
        'name': 'Claw attacks',
        'action': {
            'speed': '1A',
            'range': 'melee',
            'target': 'single',
            'base_cost': '2S',
            'next_attack_cost_increase': '1S',
            'effect': '''Attack with your claws twice, dealing 2d6+X damage with each attack''',
        }
    },
    {
        'cost': 4,
        'name': 'Legendary speed',
        'effect': 'During your move action you can spend 2 additional stamina to move additional 20 feet.'
    },
    {
        'cost': 2,
        'name': 'Fast beast',
        'effect': 'During your move action you can spend 1 additional stamina to move additional 15 feet.'
    },
    {
        'cost': 3,
        'name': 'Leaper',
        'effect': '''During your move action you can spend 2 stamina to leap over all obstacles for 15 feet. These 15 
        feet must still be part of your move distance.'''
    },
    {
        'cost': 5,
        'name': 'Venomous bite',
        'effect': '''When choosing this trait, choose an effect:
            at the beginning of round, deals 1d6 poison damage,
            acts as 1 lvl of afraid,
            acts as 1 lvl of disoriented,
            acts as 1 lvl of crazed,
            acts as 1 lvl of freezing.
            ''',
        'action': {
            'speed': '2A',
            'range': 'melee',
            'target': 'single',
            'base_cost': '3S',
            'next_attack_cost_increase': '1S',
            'effect': '''1d6+X piercing damage. A successful attack applies 2 stacks of poison with your chosen effect. 
            A critical attack applies 4 stacks instead. You can only do 3 venomous bites per encounter. This poison's
            DC is 8 + attack proficiency.''',
        }
    },
    {'cost': 3,
     'name': 'Rampage',
     'action': {
         'speed': '2A',
         'range': 'melee',
         'target': 'single',
         'base_cost': '6 stamina',
         'next_attack_cost_increase': '3 stamina',
         'effect': '''Attack all enemies around you twice. When scoring a critical hit, the target needs to succeed 
        8 + weapon proficiency DC WILL save or gain 1 level of afraid.
     Until the start of the next turn you gain 1 levels of vulnerable.''',
         'restrictions': '2 handed melee weapon',
         'exert': {'cost': '6 stamina', 'effect': 'attacks 1 additional times.'}
     }
     },
    {'cost': 3,
     'name': 'Leaping attack',
     'Attack option': {
         'proficiency_penalty': 5,
         'effect': '''You can do a melee attack to someone who is 10 feet away from you and there is a free space
         between you and the target. Leap to the free spot and make the attack. You do not trigger any attacks of
         opportunities this way, since this is not a move action.'''
        }
     },
    {'cost': 6,
     'name': 'Charge',
     'action': {
         'speed': '2A',
         'range': 'melee',
         'target': 'single',
         'base_cost': '5S',
         'next_attack_cost_increase': '2S',
         'effect': '''Charge at an enemy at least 15 feet away from you, but no further than your move distance
         doing 3d10 damage and forcing them to check for unbalanced 4 times. If you are large, then they need to check
         for unbalanced 2 additional times.
         ''',
     }
     },
    {'cost': 6,
     'name': 'Web',
     'action': {
         'speed': '2A',
         'range': '6 m.',
         'target': 'single',
         'base_cost': '2S',
         'effect': '''The target gains 4 levels of entangled.  
         ''',
     }
     },
    {'cost': 3,
     'name': 'Web range',
     'requires': 'Web feat',
     'effect': '''Range of the web action increases to 25 m.'''
     },
    {'cost': 6,
     'name': 'Powerful web',
     'requires': 'Web feat',
     'effect': '''Web action applies another 3 levels of entangled.'''
     },
    {'cost': 4,
     'name': 'Fearless',
     'effect': '''Immune to afraid condition and has advantage against all WILL saves.'''
     },
]

advancement_options = [
             'Adopt an undead feat',
             'Increase level in all your attacks by 2.',
             'Add 10 MAX HP',
             '''Add 4 to maximum stamina (each encounter is started having max stamina, you cannot recover stamina above 
             maximum stamina)''',
             'Increase your AC by 1. This bonus cannot be higher than the total bonus from all other sources.',
             'Increase your REFLEX or FORTITUDE saving proficiency by 3',
         ]
