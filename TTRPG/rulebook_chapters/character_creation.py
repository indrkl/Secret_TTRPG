import math
from math import floor, ceil

def py2round(x):
    if x >= 0.0:
        return math.floor(x + 0.5)
    else:
        return math.ceil(x - 0.5)

def get_character_creation_chapter():
    profciency_cap_matrix = [5, 8, 10, 11, 12]
    proficiency_cap_table = [['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY', 'LEGENDARY+']]
    for i in range(1, 21):
        proficiency_cap_table.append([i] + [floor(x+1 + (i)*profciency_cap_matrix[x]/(20)) for x in range(0, 5)])

    difficulty_cap_table = [['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY']]
    for i in range(1, 21):
        difficulty_cap_table.append([i] + [py2round(i * x / 4) for x in range(1, 5)])

    proficiency_table = [['EFFECTIVE_LEVEL', 'PROFICIENCY_BONUS']]
    level_up = [1, 2, 3, 3, 4, 4, 100]
    ndx = 0
    cnt = 0
    proficiency=0
    for i in range(1, 21):
        cnt += 1
        if cnt >= level_up[ndx]:
            ndx += 1
            proficiency += 1
            cnt = 0
        proficiency_table.append([i] + [proficiency])

    return [
        {'type': 'title', 'content': 'Character creation'},
        {'type': 'paragraph',
         'content': """
Instead of classes there are 3 Paths - Mage, Martial and Skilled. You define how good your character is in any of these  
paths. There are 4 levels in each PATH:


1 - acquinted

2 - adept

3 - talented

4 - legendary

Heroes get a total of 6 points, which they can spread out among these 3 paths defining their innate ability. 
This determines how fast they advance in these paths while leveling up and what is their maximum potential in these 
paths. In a way the way they spread it out defines their class, so there are 19 classes in the sense of how many ways 
you can distribute those 6 points, but each distribution of course has also very many ways to build your character.

For example you could be a Nature wizard who is either Talented or Legendary, and depending on that you could be
more or less diversified in other areas.

Absolutely all abilities, actions, spells, maximum mana, armor proficiencies etc. will have to be unlocked using
these very precious advancement points that players get each level up. Only things that all players get by default are
2 toughness (determines how much damage you can take before you die), proficiency in light armor and access to some 
general actions (move, punch, wrestle). They also start with a dice pool of 6 d6 and action limit of 5.

In addition they get a innate feat for each category they have points in, but the power of the feat depends on their 
level in that category. This further defines their character progression possibilities. 
Innate feats are really powerful.

Heroes gain 1 progression feat at levels 4, 7, 10, 13 and 16

Finally for levels 2, 5, 11 and 18 you also get to spend 2 * path level of points to advance in that path.
In other levels you get to spend 1 * path level of points to advance in that path.

Advancement rules

You need to spend all of your advancement points as you level up and they can not be saved for future level ups. That 
means you do not get access to feats that cost more than the level up you get for that path. Note that in some levels 
you get double the amount of points so you can get access to much more powerful feats that you do not get access to 
in most levels.

The maximum proficiency in anything is determined by the related path. It is +1 for acquinted, +2 for adept, +3 for
talented and +4 for legendary. Each consecutive  upgrade costs 1 more than previous upgrade start with the cost of 1.

Proficiency allows you to shift the dice results by 1 in order to get the dice result requires to perform the action
related with this proficiency. You can perform number of shifts equal to your profiency each round / scene.

MAGE advancement options:
"""},
        {'type': 'list',
         'content': [
             'Adopt a magic related feat',
             'Advance proficiency in one school of magic',
             'increase your maximum mana by 4 and base daily mana recovery by 1',
             'Advance proficiency in lore skill',
             'Learn a spell',
             'Advance proficiency in will',
         ]},
        {'type': 'paragraph', 'content': 'Martial advancement options:'},
        {'type': 'list',
         'content': [
             'Adopt a martial related feat',
             'Advance proficiency with one type of weapon',
             'Increase your toughness. Cost increases by 1 each time you choose this option. Maximum toughness is 6',
             'Increase your maximum stamina by 1',
             # '''Add 3 to maximum stamina (each encounter is started having max stamina, you cannot recover stamina above
             # maximum stamina)''',
             # 'Spend 2 advancement points to gain 1 stamina recovery (you recover stamina every round).',
             'Advance proficiency in physique or survival skill',
             # '''Increase your AC prificiency by 1. This bonus's effective value cannot be higher than the total bonus
             # from all other sources.''',
             'Advance proficiency in either reflex or fortitude saves',
             # 'Gain 3 levels in initiative',
         ]},
        {'type': 'paragraph', 'content': 'Skilled advancement options:'},
        {'type': 'list',
         'content': [
             'Adopt a skills related feat',
             'Increase your maximum number of luck tokens by 1',
             'Advance proficiency in any skill',
             '''Advance proficiency in will, reflex or fortitude. The maximum proficiency from skilled path for these 
             is 2''',
         ]},
    ]