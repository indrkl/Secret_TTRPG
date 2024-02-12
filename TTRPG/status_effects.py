status_effects = [
    {'name': 'confusion', 'description': '''
When a character gets confusion, then they roll a dice and if they have any same value dice, they lose it until the next 
re-roll.
    '''},
    {'name': 'disruption', 'description': '''
When a character gets disruption, then they lose a dice until the next re-roll chosen by the character who applied the
disruption.
    '''},
    {'name': 'inspiration', 'description': '''
You can spend your inspiration to either become lucky for a round / scene or gain advantage or negate disadvantage
for a roll.''',},
    {'name': 'cover', 'description': '''
    You can have up to 3 levels of cover against a ranged attacker. Each level makes them require 1 additional power
    dice to hit you. First level is achieved with 50 % of your body being covered. Second level when at least 80% of
    your body is covered from sight of the ranger. Third level is reached when you have full cover. Then you cannot be
    attacked with ranged attack at all.''',},
    {'name': 'disoriented', 'description': '''Each level of disoriented gives you 1 confusion after you roll your dice
    pool (WILL)'''},
    {'name': 'afraid', 'description': '''
In order to make any offensive actions during your turn you need to meet a roll target of R5 for each level of afraid.
(WILL)
'''},
    # {'name': 'crazed', 'description': '''
    #     (WILL) Has multiple levels, at level 1 when it is your turn make a DC 15 WILL check, on failure you make a
    #     basic attack against the closest creature. At level 2 you start your turn by making a basic attack against the
    #     closest creature, at level 3 when it is your turn make a DC 15 WILL check, on failure you make the highest
    #     stamina costing ability against the closest creature, and on success you do a basic attack instead. At level 4
    #     you do make the highest stamina costing ability against the closest creature.
    #     If the closest creature is 1 AP move distance away you will move to them without spending any additional AP,
    #     otherwise if you would need to attack the closest creature, you do not do the attack action,
    #     but instead waste 1 AP steaming with anger.'''},
    {'name': 'vulnerable', 'description': '''You take 1 additional damage per level in vulnerable, this counteracts
    damage reduction. Vulnerable levels are lost at the beginning of your round.'''},
    {'name': 'unbalanced', 'description': '''
        (REF R4) You can have up to 4 levels of unbalanced, you can spend R3.R4 (reflex) to remove all levels of unbalanced.
        if you get to 4 levels of unbalanced, you fall over, getting prone status but losing all levels of unbalanced,
        if you are wearing heavy armor or are a large creature and would get a level of unbalanced, you have a 50 % 
        chance to not get it.'''},
    {'name': 'entangled', 'description': '''Your position cannot change until you are entangled. You need to meet a R5
    physique target to reduce the entangled by 1 level.'''},
    {'name': 'prone', 'description': '''You have disadvantage. You need to spend dice worth of 10 points total to lose
    prone status effect.'''},
    {'name': 'poisoned', 'description': '''
        (FORT) You have some specific poison on you. Each poison can stack, but only the highest stacked poison takes
        effect. Every round one poison stack is removed from each poison after applying poison effect.'''},
    {'name': 'freezing', 'description': '''(FORT) Every level of freezing disable one dice from your dice pool.'''},
    {'name': 'burning', 'description': '''(REF R3.R4) For each level of burning, one takes 1 damage at the start of 
        their round. One can fall prone and spend the entire round (losing all concentration etc.) to lose all the 
        stacks of burning. Freezing and burning levels cancel each other.'''},
    {'name': 'blinded', 'description': '''Characters who are blinded, cannot see. Movement costs twice as much unless
    you have blind-sight. Cannot target outside blind sight range. And attacks require 1 additional power dice to make
    '''},
]

saves = {
    'WILL': ['afraid, crazed, disoriented'],
    'FORT': ['poison', 'freezing',],
    'REF': ['aoe_spells', 'unbalanced', 'burning'],
}