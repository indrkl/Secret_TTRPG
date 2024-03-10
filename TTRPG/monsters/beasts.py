info = [
    '''
    ''',
]

archetypes = [
    {
        'name': 'small animal',
        'description': '''
            Free dodge per turn. -1 Toughness, max toughness is 3. Raw damage is halved. +1 reflex. Has bite attack only
        '''
     },
    {'name': 'medium sized predators',
     'description': '''
        3 Defense. Has 2 claws and bite attack
     '''
     },
    {
        'name': 'medium sized spider',
        'description': '''
        2 defense, is a web weaver, Can bite.  
        '''
    },
    {'name': 'large sized predators',
     'description': '''
        3 Defense, 1 damage reduction, -1 reflex. 50 % more raw damage, -1 progression points per level. 
        Has 2 claws and bite attack
     '''
     },
    {'name': 'Bird predator',
     'description': '''
        3 Defense, ability to fly, -1 progression points per level.  Has 2 claws and bite attack
     '''
     },
    {'name': 'Tiny bird',
     'description': '''
        Free dodge per turn, -1 toughness, max toughness is 3. Raw damage is halved, +1 reflex, - 1 progression points
        per level. Has bite attack only
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
    },
    {
        'cost': 4,
        'name': 'Legendary speed',
        'effect': '''During your move action you can spend 1 stamina to move additional squares equal to the number on 
        the dice used to move.'''
    },
    {
        'cost': 2,
        'name': 'Fast beast',
        'effect': 'Your move action allows you to move 2 additional squares'
    },
    {
        'cost': 3,
        'name': 'Leaper',
        'effect': '''During your move action you can spend 1 stamina to leap over all obstacles for 3 sqares. These 3
        squares must still be part of your move action'''
    },
    {
        'cost': 5,
        'name': 'Venomous bite',
        'effect': '''When choosing this trait, choose an effect:
            at the beginning of round, deals 1 poison damage,
            acts as 1 lvl of afraid,
            acts as 1 lvl of disoriented,
            acts as 1 lvl of freezing.
            
            Adds a new option for bite: For 1 power dice to apply 1 level of poison.
            ''',
    },
    {'cost': 3,
     'name': 'Rampage',
     'effect': '''
     You get a new option to spend 3 stamina to make the copy of an attack you did to one target, to attack another
     target who is adjacent to you.
     '''
     },
    {'cost': 3,
     'name': 'Leaping attack',
     'effect': '''You are can do a melee attack to someone who is 2 squares away from you and there is a free space
     between you and the target. Leap to the free spot and make the attack. You do not trigger any attacks of
     opportunities this way, since this is not a move action.'''
     },
    # {'cost': 6,
    #  'name': 'Charge',
    #  'action': {
    #      'speed': '2A',
    #      'range': 'melee',
    #      'target': 'single',
    #      'base_cost': '5S',
    #      'next_attack_cost_increase': '2S',
    #      'effect': '''Charge at an enemy at least 15 feet away from you, but no further than your move distance
    #      doing 3d10 damage and forcing them to check for unbalanced 4 times. If you are large, then they need to check
    #      for unbalanced 2 additional times.
    #      ''',
    #  }
    #  },
    {'cost': 5,
     'requires': 'Web weaver',
     'effect': 'Using the web requires web proficiency',
     'name': 'Web',
     'action': {
         'cost': 'R6.R6.R6',
         'range': '3 sq.',
         'target': 'single',
         'effect': '''The target gains 4 levels of entangled.  
         ''',
     'difficulty_options': [
             {
                 'cost': 'R6.R6',
                 'effect': 'The target gains 3 additional levels of entangled',
             },
             {
                 'cost': 'R3.R3.R3',
                 'effect': 'Apply 2 lvls disoriented',
             },
         ]
     }
     },
    {'cost': 3,
     'name': 'Web range',
     'requires': 'Web feat',
     'effect': '''Range of the web action increases to 5 sq.'''
     },
    {'cost': 3,
     'name': 'Fearless',
     'effect': '''Immune to afraid condition'''
     },
    {'cost': 3,
     'name': 'Thick skin',
     'effect': '''Get 1 additional defense'''
     },
    {'cost': 5,
     'name': 'Rage',
     'effect': '''
    Gain rage action.
 ''',
     'action': {
         'cost': 'R6',
         'proficiency': 'fortitude',
         'target': 'self',
         'limit': 'once per encounter',
         'duration': '5 rounds',
         'effect': '''You go into rage where you stay for 5 rounds or until you go unconscious.
        While raging you are immune to confusion and disruption.

        You lose all your defense and cannot recover any defense. However you still roll all the dice that were
        set aside because of damage and scarred dice can be used for targets 4, 5 and 6 as well.
        ''',
     }
     },
    {'cost': 3,
     'name': 'Dodging',
     'effect': '''Whenever you would receive damage you can react with a R5 physique dice to negate that damage.
     This cost goes up by 1 X R5 every time you use this ability during encounter. You can take the recover
     action to reset it to 1 dice again.

     Dodging requires no or light armor''',
     'action': {
         'cost': 'R5.R5.R5',
         'proficiency': 'physique',
         'additional_costs': '1 stamina',
         'target': 'self',
         'effect': '''reset the dodging reaction dice cost to 1 dice''',
     },
     },
]

advancement_options = [
             'For feat cost: Adopt a beast related feat',
             'For 1/2/3/4 points: Advance proficiency in claw, bite, physique, concealment, fortitude or reflex',
             'For 1/2/3/4 points: Increase your toughness. Cost increases by 1 each time you choose this option. Maximum toughness is 6',
             '''For 1 point: Increase your maximum stamina by 1''',
             'For 1/2 points: Advance proficiency in will',
         ]
