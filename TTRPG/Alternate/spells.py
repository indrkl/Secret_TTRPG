spells = {
    'elemental': [
        {
            'name': 'fireball',
            'power': 'R6',
            'utility': 'R2',
            'cost': 'R6.R6',
            'effect': 'deal 2 damage in 1 square radius within 6 squares',
            'range': '6 squares',
            'options': [
                {'cost': 'R6.R6', 'effect': 'Deal additional 3 damage'},
                {'cost': 'R2',
                 'effect': '''One target enemy within range gets 1 level of burning (At the beginning of round they
                 take 1 damage per level of burning. Anyone can spend dice with a sum of at least 18 to remove all stacks of
                 burning or a single 6 dice to remove 1 stack of burning)'''},
            ]
        }
    ],
    'nature': [
        {
            'name': 'heal',
            'power': 'R1',
            'utility': 'R4',
            'cost': 'R1.R1',
            'effect': 'Target ally recovers 1 dice',
            'range': 'touch',
            'options': [
                {'cost': 'R1', 'effect': 'Target ally recovers 1 additional dice'},
                {'cost': 'R4',
                 'effect': '''Target ally removes 1 level of burning/freezing/poisoned'''},
            ]
        }
    ],
}