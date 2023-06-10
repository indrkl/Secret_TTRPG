TTRPG ideas
Character creation

Classless system.
You pick between 3 Paths - magic, martial and skill. You define how good your character is in any of these paths. There are 4 levels in each PATH:

1 - acquinted
2 - skilled
3 - talented
4 - legendary

Heroes get a total of 6 points, which they can spread out among these 3 paths defining their innate ability. 
This in the future means how much stuff they gain in these paths while leveling up. Or how fast they progress in these paths so to speak. 
In a way the way they spread it out defines their class, so there are 19 classes in the sense of how many ways you can distribute those
6 points, but each distribution of course has also very many ways to build that class.

In addition they get a innate feat for each category they have points in, but the power of the feat depends on their level in that category. This further defines their character progression possibilities. Innate feats are really powerful.

You get another innate feat at lvl 5, and no more afterwards.

Everyone starts with 5 points of stamina and 1 stamina recovery. You need to spend 1 stamina to make a basic attack with a weapon. 
Everyone also starts with 3 * (2 * magic + 2 * skill + 3 * martial) hitpoints. Each level after level 1 you gain another (2 * magic + 2 * skill + 3 * martial) hitpoints

Finally for levels 1 and 10 you also get to spend 2 * path level of points to advance in that path.
In other levels you also get to spend 1 * path level of points to advance in that path.


MAGE advancement options

1. Increase proficiency by 2 in one school of magic.
2. Adopt a magic related feat, you need to be able to spend that many level up points to get that in one go.
3. increase your daily cast limit by 3
4. increase your encounter cast limit by 1
5. Increase your lore skill proficiency by 2
6. Learn a spell. You must meet its difficulty and school of magic requirements
7. Increase your WILL saving proficiency by 3


Martial advancement options:

1. Adopt a martial related feat, ...
2. Add 6 MAX HP
3. Add 2 to maximum stamina (each encounter is started having max stamina, you cannot recover stamina above maximum stamina)
4. Spend 2 points to gain 1 stamina recovery per round.
5. Increase your survival skill proficiency by 2
6. Increase proficiency in one group of weapons by 2.
7. Increase your AC by 1. This bonus cannot be higher than the total bonus from all other sources.
8. Increase your REFLEX or FORTITUDE saving proficiency by 3

Skilled advancement options:

1. Adopt a skills related feat, ...
2. Spend 2 points to increase your daily number of luck tokens
3. Increase any skill proficiency by 2
4. Increase any saving throw proficiency by 3. 

Determining MAX proficiency bonuses for skill checks, attack hit checks, spell DC, saving throws based on your character and appropriate path level:
PATH_LEVEL + CHARACTER_LEVEL * (3/5/6/7/8 depending on your PATH level) / 10 rounded down
[
    ['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY', 'LEGENDARY+'],
    [1, 1, 2, 3, 4, 5],
    [2, 1, 3, 4, 5, 6],
    [3, 1, 3, 4, 6, 7],
    [4, 2, 4, 5, 6, 8],
...
    [10, 4, 7, 9, 11, 13],
...
    [20, 7, 12, 15, 18, 21]
],
PATH used for determining max proficiency bonus:
Spell schools: mage
Weapon attacks: Martial
Skill checks: Skilled
WILL: Mage (or Skilled)
REFLEX: Martial (or Skilled)
Fortitude: Martial (or Skilled)
SKILLED PATH has access to all saving throws, but their max proficiency bonus from SKILLED PATH is divided by 2 rounded up.
However if your max proficiency would be higher from another PATH, then use that instead.

The max difficulty of your spells scales however differently, though also the effective max difficulty also being tied to proficiency in that school of magic.
CHARACTER_LEVEL * PATH_LEVEL / 4 rounded up

[
    ['CHARACTER_LEVEL', 'ACQUAINTED', 'SKILLED', 'TALENTED', 'LEGENDARY'],
    [1, 1, 1, 1, 1],
    [2, 1, 1, 2, 2],
    [3, 1, 2, 3, 3],
    [4, 1, 2, 3, 4],
    [5, 2, 3, 4, 5],
...
    [8, 2, 4, 6, 8],
    [10, 3, 5, 8, 10],
...
    [20, 5, 10, 15, 20],
]

Skill checks

For various situations during exploring and adventuring GM can have players roll their skill checks or saving throws
to determine what happens.

However if players want to pursue some specific goal or achieve something, either to learn about something, get an
item, improve relations with a lord etc. they can start a group focus. Group focus consists of a goal, a progress tracked by GM,
and fail conditions tracked by GM.

Party can have only 1 group focus active at a time, but Skilled path characters get access to a Planner feat, that let's
them start another one

Group focus progresses together with the main story line or whatever the players choose to do, and consists of skill checks
after certain well signalled conditions have been met.


Crtitical successes move the progress forward twice, while critical failures have some chance for negative consquences (GM discretion).

The first check can be done when the goal is set.

Using group focuses it is clear to the GMs what the players hope to get, and what they care about most, 
and at the same time lowers the amount of "let's try to squeeze lemonade out of anything".

Use Pathfinder 2 E critical success / failure system and 3 actions per round system

Armor rules:

Everyone are proficient with light armor.
Without proficiency in medium armor, You need to spend 1 STA for each AP you spend on attacks and movement
Heavy armors have: You need to spend 2 STA for each AP you spend on attacks and movement, 
when you are not proficient you also get -2AC and -1 AP.