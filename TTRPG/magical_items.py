
equipment = {
    'Burning two handed axe of the devils': {
        'action': {
            'cost': 'R6.R6',
            'damage': 4,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R6',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R6',
                    'effect': 'Deal 1 fire damage and apply a stack of burning onto the enemy',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Apply 1 afraid for every 3 stacks of burning on the enemy rounded up',
                },
                {
                    'cost': 'R1',
                    'effect': 'Apply 1 vulnerable for every 3 stacks of burning on the enemy rounded up',
                },
            ]
        }
    },
    'dagger of poison': {
        'action': {
            'cost': 'R4.R4',
            'damage': 2,
            'range': 'melee',
            'effect': '''Poison applied to this blade applies 1 extra stack (does not consume a stack from the coating)
            ''',
            'difficulty_options': [
                {
                    'cost': 'R1',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R4.R4',
                    'effect': 'Double damage',
                },
                {
                    'cost': 'R4',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Disrupt 2',
                },
            ]
        }
    },
    'Plate mail of scarabus': {
        'effect': '''
This is a heavy armor that provides 5 maximum defense and 1 damage reduction. In addition you gain a magical ability
to move through sand with half your move speed. 
        '''
    },
    'staff of freezing (can be replaced by any spell)': {
        'effect':
            '''
Instead you have 2 additional normal spell slots. In addition you have freezing spell as your signature spell, meaning
casting it has advantage.

Enables you to cast the freezing skill without elemental proficiency and knowing that spell. You may replace elemental
proficiency for casting it using this staff with your highest proficiency in any school minus one.'''
    },

}
