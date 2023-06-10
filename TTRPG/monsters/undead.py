info = [
    '''Unintelligent undead are immune to WILL effects. All undead are immune to poison, freezing and 
    are resistant to cold damage. The
    unique defensive mechanic of the undead is Damage reduction. Undead can either be intelligent (vampires, liches) or
    unintelligent (skeletons, zombies, wraiths). Unintelligent undead are often controlled by a necromancer or lich.
    Undead cannot be healed through normal means like nature magic and they do not have hit dice. Undead cannot recover
    stamina or spell limit nor can they have luck. That means they need to recover using dark magic, stealing life
    force from the living or other limited means to sustain their abilities, and recover resources. That is the price of 
    this eternal life. 
    ''',
]

archetypes = [

    {
        'name': 'skeletons',
        'description': '''
            normal human stats. They can only be summoned by a necromancer, and to recover Stamina, their summoner
            needs to trade 1 casting point for 5 STA or 1 casting point for 5 HP. Can see in the dark.
        '''
     },
    {'name': 'zombie',
     'description': '''
        Normal human stats. They recover STA and life by eating living flesh or blood. Can see in the dark.
     '''
     },
    {'name': 'Vampire',
     'description': '''
        They have some super human abilities, but these require mana, they can recover mana by
        drinking blood of the living. Depending on the level of the vampire they require higher quality living to
        recover their mana. They are vulnerable to fire, and cannot walk in the light. Has legendary senses.
     '''
     },
    {'name': 'Lich',
     'description': '''
        The focus on mana, and spell casting. They have enormous amounts of mana (max), however they
        need a rare magic dust to recover this mana. Can see in the dark.
     '''
     },
    {'name': 'Ghost',
     'description': '''
Additionally immune to cold and physical damage. All their physical damage is converted to cold damage. Wields spectral weapons.
     '''
     },
]



general_feats = [
    {
        'cost': 2,
        'name': 'Double attack',
        'action': {
            'speed': '1A',
            'range': 'melee',
            'target': 'single',
            'base_cost': '2S',
            'next_attack_cost_increase': '1S',
            'effect': '''Attack with your weapon twice''',
        }
    },
]

ghost_feats = [
    {
        'cost': 4,
        'name': 'Cold phasing',
        'effect': '''
When taking move actions, ghost can move through other creatures withtout triggering attacks of opportunities. When
moving through a living creature they take 2d6 cold damage and must check for freezing once.
        ''',
    },
]

feats = []

advancement_options = [
             'Adopt a beast feat',
             'Increase proficiency in all your attacks by 2.',
             'Add 10 MAX HP',
             '''Add 4 to maximum stamina (each encounter is started having max stamina, you cannot recover stamina above 
             maximum stamina)''',
             'Increase your AC by 1. This bonus cannot be higher than the total bonus from all other sources.',
             'Increase your REFLEX or FORTITUDE saving proficiency by 3',
         ]
