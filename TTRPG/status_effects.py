status_effects = [
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
    {'name': 'disoriented', 'description': '''
When a character gets a level of disoriented they roll a die and discard a die in their pool with a matching number.
During each re-roll of the dice pool, this process is repeated for each level of disoriented. Disoriented can be removed
using the Refocus general action.

For example if Jack has 3 levels of disoriented and 5 dice remaining in their dice pool then he first rolls his 5 dice
from the pool and suppose he gets R2,R3,R3,R5,R6. After that he rolls 3 disoriented dice and suppose he gets R2,R5,R5.
Then he discards R2 and R5 from the pool and therefore cannot use those dice in the turn. Notice that since he rolled
2 R5 for disoriented, but only had 1 R5 in the pool, then the final disoriented die result had no effect. If Jack had
rolled 2 x R5 into the pool, he would have lost both of them.
    '''},
    {'name': 'afraid', 'description': '''
While having any levels of afraid, all offensive actions require an additional power dice for every 3 levels of
afraid (rounded down). Afraid can be removed using the refocus action.

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
    damage reduction. Vulnerable levels are discarded at the beginning of your turn.'''},
    {'name': 'unbalanced', 'description': '''
        You can have up to 4 levels of unbalanced, you can use recover action to remove all levels of unbalanced.
        if you get to 4 levels of unbalanced, you fall over, getting prone status but losing all levels of unbalanced,
        if you are wearing heavy armor or are a large creature and would get a level of unbalanced, you have a 50 % 
        chance to not get it.'''},
    {'name': 'entangled', 'description': '''Your position cannot change until you are entangled. You may spend a R5 
    (physique) to reduce the entangled by 1 level.'''},
    {'name': 'prone', 'description': '''You have disadvantage. You need to spend dice worth of 10 points total to lose
    prone status effect.'''},
    {'name': 'poisoned', 'description': '''
        You have some specific poison on you. Each poison can stack, but only the highest stacked poison takes
        effect. Poison can be removed using the recover general action.'''},
    {'name': 'freezing', 'description': '''Every level of freezing disable one dice from your dice pool.'''},
    {'name': 'burning', 'description': '''For each level of burning, one takes 1 damage at the start of 
        their round. One can fall prone and spend the entire round (losing all concentration etc.) to lose all the 
        stacks of burning. Freezing and burning levels cancel each other.'''},
    {'name': 'blinded', 'description': '''Characters who are blinded, cannot see. Movement costs twice as much unless
    you have blind-sight. Cannot target outside blind sight range. And you have double disadvantage when making melee 
    attacks, and enemies have advantage when attacking you. Enemies who already have advantage upgrade it to double 
    advantage.
    '''},
]

saves = {
    'WILL': ['afraid, crazed, disoriented'],
    'FORT': ['poison', 'freezing',],
    'REF': ['aoe_spells', 'unbalanced', 'burning'],
}