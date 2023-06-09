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
HP (Health points), 5 Stamina, 1 stamina recovery and ability to do a basic attack, which costs 1 Stamina for first
attack in the round, 2 for second and 3 for third and so on. 

In addition they get a innate feat for each category they have points in, but the power of the feat depends on their 
level in that category. This further defines their character progression possibilities. 
Innate feats are really powerful.

Heroes gain 1 progression feat in each category which they have points in at levels 4, 7, 10, 13 and 16 and before
they make their advancement decisions in that level.

Everyone starts with 5 points of stamina and 1 stamina recovery. You need to spend 1 stamina to make your first basic 
attack with a weapon in a round. 

Everyone starts with 2 * (2 * magic + 2 * skill + 4 * martial) hitpoints. Each level after level 1 you gain another 
(2 * magic + 2 * skill + 4 * martial) hitpoints

Finally for levels 1, 5, 11 and 18 you also get to spend 2 * path level of points to advance in that path.
In other levels you get to spend 1 * path level of points to advance in that path.

Advancement rules

You need to spend all of your advancement points as you level up and they can not be saved for future level ups. That 
means you do not get access to feats that cost more than the level up you get for that path. Note that in some levels 
you get double the amount of points so you can get access to much more powerful feats that you do not get access to 
in most levels.

MAGE advancement options:
"""},
        {'type': 'list',
         'content': [
             'Adopt a magic related feat',
             'Gain 2 levels in one school of magic',
             'increase your maximum mana by 4 and base daily mana recovery by 1',
             'Gain 2 levels in lore skill',
             'Learn a spell. Gain one level in the school of magic of that spell',
             'Gain 3 levels in Will saving throws',
         ]},
        {'type': 'paragraph', 'content': 'Martial advancement options:'},
        {'type': 'list',
         'content': [
             'Adopt a martial related feat',
             'Gain 2 levels in one group of weapons.',
             'Add 7 MAX HP',
             '''Add 3 to maximum stamina (each encounter is started having max stamina, you cannot recover stamina above 
             maximum stamina)''',
             'Spend 2 advancement points to gain 1 stamina recovery (you recover stamina every round).',
             'Gain 2 levels in physique or survival skill',
             # '''Increase your AC prificiency by 1. This bonus's effective value cannot be higher than the total bonus
             # from all other sources.''',
             'Gain 3 levels in either reflex or fortitude saving throws',
             'Gain 3 levels in initiative',
         ]},
        {'type': 'paragraph', 'content': 'Skilled advancement options:'},
        {'type': 'list',
         'content': [
             'Adopt a skills related feat',
             'Increase your daily number of luck tokens by 1',
             'Gain 2 levels in any skill',
             'Gain 3 levels in will, reflex or fortitude saving throws',
         ]},
        {'type': 'paragraph', 'content': '''
You can gain as many levels as you want, but the effective level of any skill, school of magic, weapon or saving throw
is capped by your character level and your PATH choices. 

The levels in any of those given things determines 2 things.

1. Your proficiency bonus. You're proficiency bonus becomes +1 at level 1, +2 at level 3, +3 at level 6, +4 at level 9,
+5 at level 13, +6 at level 18.

2. Higher levels allows you to perform more difficult and complex actions. For magic, allows you to cast more powerful
spells, for weapons, allows you to add extras to your attacks, for saving throws, allows you to be more effective with
removing negative modifiers etc.

The maximum level is determined by PATH_LEVEL * CHARACTER_LEVEL / 4:

Or simply refer to the following table:
'''},
        {'type': 'table',
         'content': difficulty_cap_table},
        {'type': 'paragraph', 'content': '''
PATH used for determining max level:

Spell schools: mage

Weapon attacks: Martial

Skill checks: Skilled

Lore skill: Mage or Skilled

Physique skill: Martial or Skilled

WILL: Mage (or Skilled)

REFLEX: Martial (or Skilled)

Fortitude: Martial (or Skilled)

SKILLED PATH has access to all saving throws, but their max level is divided by 2 rounded 
up. However if your max level would be higher from another PATH, then use that instead.

The proficiency bonus based on the level
    '''},
        {'type': 'table',
         'content': proficiency_table},
    ]