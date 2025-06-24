schools = {
    'Fog (cunning)': {
        'spells': [
            {
                'name': 'Soul pressure',
                'range': '10 sq.',
                'effect': '''Target gains 1 spiritual exhaustion''',
                'target': 'single',
                'difficulty': 'R1.R1',
                'scaling': [
                    {'D': 'R1', 'L': 2, 'description': '''Target gains an additional level of spiritual exhaustion
                    '''},
                    {'D': 'R1.R1', 'description': '''Target has to roll twice the amount of dice at the same time
                    for gaining these levels of spiritual exhaustion'''},
                ],
            },
            {
                'name': 'Manifest fears',
                'range': '10 sq.',
                'effect': '''Target takes 1 psychic damage for each spiritual exhaustion.''',
                'target': 'single',
                'difficulty': 'R1.R1.R1',
                'scaling': [
                    {'D': 'R1', 'L': 2, 'description': '''Target gains a level of afraid.
                    '''},
                    {'D': 'R1.R1', 'description': '''Also trigger the exhaustion'''},
                ],
            },
            {
                'name': 'Summon fear',
                'effect': '''Sacrifice another person and summon their greatest fears as a fog creature. That creature
                will not be hostile towards you, but will otherwise act out the fear. This is a ritual.
                
                The strength of the monster is a level 1 legendary creature.''',
                'target': '1 individual',
                'difficulty': 'R1 X 15',
                'scaling': [
                    {'D': 'R1 X 10', 'description': '''Increase the level of the monster by 1.'''},
                ],
            },
            {
                'name': 'Summon fog',
                'effect': '''Summon a fog to an area of around 100 acres. This is a ritual. To maintain it you need
                to spend 150 mana over the course of each strategic turns.''',
                'difficulty': 'R1 X 50',
                'scaling': [
                    {'D': 'R1 X 25', 'L': 3, 'description': '''Double the size of the area'''},
                    {'D': 'R1 X 50', 'L': 3, 'description': '''Increase the intensity of the fog by 1 level'''},
                ],
            },
        ]
    },
}