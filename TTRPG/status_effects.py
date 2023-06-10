status_effects = [
    {'name': 'inspiration', 'description': '''When making any check, you can spend your inspiration to make it either
    lucky or have advantage, or negate unlucky or disadvantage.''',
    'cover': '''You can have up to 3 levels of cover against a ranged attacker. Each level reduces hit score by -1. 
    level one requires some objects to be between you and the attacker, that cover at least half of you. 
    Level 2 requires covering you at least 80% of you. Level 3 requires almost full cover. When you are fully covered, 
    then you cannot be attacked from range.''',},
    {'name': 'disoriented', 'description': '''(WILL) Has multiple levels, at level 1 disoriented creature gets -1 to all 
        checks and your AC. At level 2, they get -1 AP per turn, At level 3 or higher you can only take the refocus 
        action'''},
    {'name': 'afraid', 'description': '''
        (WILL) Has multiple levels, at level 1/2 one gets -2/-6 penalty to all their attacks. At level 3, 
        one is unable to attack or cast offensive spells. At level 4 one loses control completely and spends at least 2
         move actions per round to run away from the conflict in terror.'''},
    {'name': 'crazed', 'description': '''
        (WILL) Has multiple levels, at level 1 when it is your turn make a DC 15 WILL check, on failure you make a 
        basic attack against the closest creature. At level 2 you start your turn by making a basic attack against the 
        closest creature, at level 3 when it is your turn make a DC 15 WILL check, on failure you make the highest 
        stamina costing ability against the closest creature, and on success you do a basic attack instead. At level 4
        you do make the highest stamina costing ability against the closest creature. 
        If the closest creature is 1 AP move distance away you will move to them without spending any additional AP,
        otherwise if you would need to attack the closest creature, you do not do the attack action, 
        but instead waste 1 AP steaming with anger.'''},
    {'name': 'vulnerable', 'description': '''You have -1 to your AC per level in vulnerable. Vulnerable levels are lost
    at the beginning of your round.'''},
    {'name': 'unbalanced', 'description': '''
        (REF) You can have up to 4 levels of unbalanced, you need to spend 1 AP to remove all levels of unbalanced.
        if you get to 4 levels of unbalanced, you fall over, getting prone status but losing all levels of unbalanced,
        if you are wearing heavy armor or are a large creature and would get a level of unbalanced, you have a 50 % 
        chance to not get it.'''},
    {'name': 'entangled', 'description': '''Your position cannot change until you are entangled. When taking the move
        action, for every 2 m. of movement you can spend 2 stamina to reduce entangled by 1 level.'''},
    {'name': 'prone', 'description': '''Your attacks are unlucky, attacks against you are lucky. You must make a move 
        action to lose this condition'''},
    {'name': 'poisoned', 'description': '''
        (FORT) You have some specific poison on you. Each poison can stack, but only the highest stacked poison takes 
        effect. Every round one poison stack is removed from each poison after applying poison effect. And one can make 
        a FORT check for free to see if they lose one specific poison's stack. On a critical success they lose up to 3 
        stacks from chosen poison.'''},
    {'name': 'freezing', 'description': '''(FORT) Every level of freezing reduces stamina recovery by 1. Every 4 levels of freezing reduces one's 
        AP by 1. There is no default way to lower freezing levels. Freezing and burning levels cancel each other.'''},
    {'name': 'burning', 'description': '''(REF)For each level of burning, one takes 1d6 damage at the start of their round. 
        One can fall prone and spend the entire round (losing all concentration etc.) to lose all the stacks of
        burning. Freezing and burning levels cancel each other.'''},
    {'name': 'blinded', 'description': '''Characters who are blinded, cannot see. Attacks made outside their blind
    sight range have advantage. Character can only attack in melee unless the target is within the blind/sight range.
    Either way if the target is not within the blind/sight range, that attack has disadvantage. Same targeting 
    restrictions apply to spells.'''},
]

saves = {
    'WILL': ['afraid, crazed, disoriented'],
    'FORT': ['poison', 'freezing',],
    'REF': ['aoe_spells', 'unbalanced', 'burning'],
}