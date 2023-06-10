info = [
    '''
    Normally ghosts exist in the spectral realm parallel to the material world, and they cannot interact with the
    material realm, or be heard or seen normally.
    
    However necromancers and liches can lend their magic to provide ghosts Power points, which enables them to manifest
    in the material world.
    
    When that happens they can attack but also be attacked.
    
    Manifested ghosts have resistance to physical and cold damage, immune to poison, unbalanced, prone and freezing.
    
    To exist in the material plane, attack, use abilities they need to spend power points. When ghosts take damage,
    they lose power points. By reducing their power points to 0, they can be avoided for the time being. They need to have 
    at least 50 % of max PP to shift to material plane.
    
    Ghosts can only be killed if you find the object holding them in this world, which is 
    usually somewhere nearby and destroy that object.
    
    Depending on the ghost they can have 1 or no ways to get Power points. Ghosts only gain power points this way if
    they are in the spectral realm. Only 1 ghost can get power points from each instance. And usually the most powerful
    ghost gets it. In the case of ties the one who is closer: 
    
    * Feed upon fear (gain 5 Power points each time someone near by gets a level of afraid, but lose 3 power points,
    when they lose a level of afraid)
    
    * Feed upon pain (gain a power point for each HP lost)
    
    * Such the warmth from the living (gain 5 power points each time someone near gets a level of freezing), these 
    ghosts double damage from fire.
    
    * Feed upon magic (gain 2 power points for each difficulty + 1 spell cast).
    
    A lich or necromancer who is able to control the ghosts can spend their mana to boost the ghost by trading
    1 casting point for 5 PP.
    ''',
]

archetypes = [

    {
        'name': 'Wraiths',
        'description': '''
            AC 13 (10 + 3 natural armor)
            Crazed unitelligent ghosts. Because of their madness they ave advantage on will saves. 
        '''
     },
    {
        'name': 'Specters',
        'description': '''
            AC 13 (10 + 3 natural armor)
            Ghosts who have preserved their memory and intelligence and they have a self of control, they can be both
            friendly or hostile.
        '''
     },
]



general_feats = [

]

feats = [
    {
        'cost': 2,
        'name': 'Double attack',
        'action': {
            'speed': '1A',
            'range': 'melee',
            'target': 'single',
            'base_cost': '4PP',
            'effect': '''Attack with your weapon twice''',
        }
    },
    {
        'cost': 4,
        'name': 'Cold phasing',
        'effect': '''
When taking move actions, ghost can spend 10 PP to move through other creatures withtout triggering attacks of 
opportunities. When moving through a living creature that living creature takes 1d6 cold damage and must check for 
freezing once.
        ''',
    },
    {
        'cost': 2,
        'name': 'Haunting speed',
        'effect': '''
        Use 2 PP to move additional 6 m. during a move action.
        ''',
    },
    {
        'cost': 3,
        'name': 'Poof',
        'action': {
            'speed': '1A',
            'range': '10 m',
            'target': 'empty spot',
            'base_cost': '2PP',
            'effect': '''Teleport to an empty spot. All enemies around you make an afraid check. You get to do a 
            backstab attack after the poof if you teleported behind an enemy''',
        }
    },
    {'cost': 6,
     'name': 'Backstab',
     'effect': '''''',
     'action': {
         'speed': '1A',
         'range': 'melee',
         'target': 'single',
         'base_cost': '5PP',
         'effect': '''You can do this attack only when the opponent is unaware of your presence or is facing their 
        back to you. Reduce critical threshold by 5. On a critical strike you deal additional 5 damage for 
        every 3 proficiency bonus with your weapon and for every 20 total damage you do they must check for 
        disoriented. You can do this only once per round per enemy.''',
         'restrictions': 'any melee weapon',
     }
     },

]


advancement_options = [
             'Adopt a ghost feat',
             'Increase proficiency in all your attacks by 2',
             'Increase proficiency in all the freezing checks you force upon your enemies by 2',
             'Increase proficiency in all the will checks you force upon your enemies by 2',
             'Add 10 MAX Power points (PPs)',
             'Increase your AC by 1. This bonus cannot be higher than the total bonus from all other sources.',
             'Increase your WILL or REFLEX saving proficiency by 3',
         ]
