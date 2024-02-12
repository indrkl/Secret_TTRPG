skills = [
    {'name': 'diplomacy',
     'description': '''Used to either improve relations, or get someone to do something for you who is otherwise not 
        inclined to do so, without using force. It is also used to learn what the other party values highly, 
        in order to achieve a good deal for both parties.
        
        When creating your character you can have familiarity with a group of people, granting you a advantage to diplomacy
        when interacting with them. But that must come at the cost of having unfamiliriaty towards other group(s) 
        (meaning having disadvantage when interacting with that group).       
        Discuss with your GM to make sure all the groups are relevant to your campaign. 
        
        Example of groups: Mages, nobility, peasants, craftsmen, traders, criminals, soldiers, spies.
        
        The maximum bonus from a familiarity can be +1, but that means that much of a penalty in some other relevant
        unfamiliriaty to the campaign.
        '''
     , 'group focuses': [
        'improve relations', 'negotiate a deal to receive a specific item/request/information/boon',
        ]
    },
    {'name': 'leadership',
     'description': '''Group coordination, inspiration, executing of complex plans
     
     The same familiriarity bonuses and penalties from the diplomacy apply to this skill.
     '''
     , 'group focuses': ['Lead a war campaign', 'Start a revolution', 'Run for political position',
                         'Increase the renown of the group']
    },
    {
        'name': 'survival',
        'description': '''Surviving in a tough environment. Tracking, hunting when in the wild. Pick pocketing, escaping
    from the law when in the streets, having 6th senses about when someone is going to assassinate someone when
    living in a court of intrigue etc. Spotting threats in general. This is used for hiding and pretty much everything
    that is required for your survival in any tough environment.

    When creating your character you can have favored environments, but they must come at a cost of having
    unfavored environments. Discuss with GM to make sure both ot those environments are relevant to the campaign.

    Examples of environments are: Streets of metropolis, royal court, sea, mountains, forest.

    While in favored environment you have advantage for survival challanges, in unfavored environment you have 
    disadvantage.
    ''',
        'group focuses': ['have a great hunt', 'track someone in the wild', 'Travel a long distance by foot']
    },
    {
        'name': 'concealment',
        'description': '''Deceive, hide your intentions, withhold information, avoid detection. Whenever you want to
        contest withholding knowledge from someone that is not in their interest, you are dealing with concealment.
        
        This is the skill for assassins, spies, agents etc.
        
        Basically, if you as a player want to plot, lie, sneak etc. you need this skill.
    ''',
        'group focuses': ['have a great hunt', 'track someone in the wild', 'Travel a long distance by foot']
    },
    {'name': 'lore',
     'description': '''Knowing about the history, religion, magic, lore of the game world. This is used to find more 
        about the game and an excuse for the GM to tell you about what is going on. You can use this skill for medical
        skill checks
        
    Both the familiarity and environment bonuses may apply to some lore challanges.
    ''',
     'group focuses': ['learn about anything', 'knowledge about disease, or a way to alleviate medical problems'],
    },
    {
        'name': 'crafting',
        'description': '''This skill involves crafting yourself, knowing crafters, knowing good crafters,
            and anyways knowing what to do in order to craft great items for the party. Crafting for a specific item
            is easier than finding it, but harder than finding any item of similar power level.''',
        'group focuses': ['craft a specific item']
    },
    {
        'name': 'harvesting',
        'description': '''This is harvesting for specific materials, knowing where to get them, also knowing where
            to buy them. It also involves knowing how to extract magical, but also none magical materials from slain 
            beasts.''',
        'group focuses': ['gather resources for profit'],
        'notes': ['''note that gathering resources for specific item can be 
            done as part of the craft a specific item quest'''],
    },
    {
        'name': 'physique',
        'description': '''This is used for making all sort of checks requiring bodily accuracy, like when performing
        acrobatic feats, climbing, having balance while crossing a narrow path, being able to endure long journey,
        wrestling, martial arts, dancing.
        ''',
        'group focuses': [],
    },
]


activities = [
    'climbing', #physique
    'dancing', #physique
    'jumping', #physique
    'wrestling', #physique
    'unarmed fighting', #physique
    'enduring physical hardship', #physique
    'accuracy challange', #physique
    'chase someone', #physique
    'ride horse', #physique
    'persuasion', #diplomacy
    'improving relations', #diplomacy
    'negotiations', #diplomacy
    'haggling', #diplomacy
    'selling', #diplomacy
    'hiring', #diplomacy
    'inspire', #leadership
    'ignite hope', #leadership
    'incite a revolution', #leadership
    'lead troops', #leadership
    'ambush', #leadership
    'hunt', #survival
    'track', #survival
    'forage', #survival
    'hide campsite', #survival
    'camouflage', #survival
    'flee', #survival
    'detect ambush', #survival
    'detect traps', #survival
    'pickpocket for survival', #survival
    'sneak', #survival
    'lock-pick', #survival
    'lie', #concealment
    'withhold information', #concealment
    'deceive', #concealment
    'misdirect', #concealment
    'study', #lore
    'extract information in a conversation', #lore / diplomacy*
    'extract information through torture', #lore / diplomacy*
    'converse', #lore
    'medical related', #lore / survival
    'craft an item', #crafting
    'evaluate worth of an item', #crafting
    'know the best crafters', #crafting
    'gather resources', #harvesting
    'extract resources from slain beasts', #harvesting
]