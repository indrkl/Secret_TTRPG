glossary = [
    {
        'name': 'Various checks',
        'description': """
During gameplay players and NPC/s will need to do various checks, to determine weather they succeed in using their
skills, making attacks, saving throws or using magic. The checks are done using 3d6 (3 six sided dice). This means the
average results are much more common than the extreme results.
        """
    },
    {
        'name': 'DC',
        'description': '''
Dice check. This is used to refer to the difficulty of the dice check. The base DC in the game is 10. that means to
succeed the player needs to throw 10 or more using 3d6. The difficulty modifiers for the checks are as follows: 

+1 - has some potential difficulties

+2 - Difficult

+3 - Hard

+4 - Extremely hard

+5 - Impossible for most mortals

+6 and +7 - Succeeding in this task is a legendary feat.
        '''
    },

    {
        'name': 'Proficiency',
        'description': '''
Players can have proficiency in a skill, weapon class, school of magic or a saving throw. That means they have invested
path points to gain levels in that proficiency. There exists level of proficiency (based on how much player has invested
path points), max level of proficiency (which is based on character and path level, refer to character creation) and
effective level, which the least of the 2 previous. 
        '''
    },
    {
        'name': 'Proficiency bonus',
        'description': '''
When making any check, add your related proficiency bonus to the 3d6 roll. Proficiency bonus is determined based on your
effective level in that proficiency (refer to the tables in character creation)
        '''
    },
    {'name': 'Lucky and unlucky',
     'description':'''
Some effects can make a dice roll lucky or unlucky. It can theoretically be any dice roll, even damage rolls.
A lucky dice roll means that you throw 4d6 and choose the best 3 results to determine the outcome. An unlucky
dice roll means that you throw 4d6 and choose the worse 3 results to determine the outcome. When you would be granted
lucky and unlucky at the same time, roll as normal, no matter how many sources of luck or unluckyness there are.
     '''
     },
    {'name': 'Advantage and disadvantage',
     'description':'''
Some effects can apply advantage or disadvantage to a skill check, attack roll, saving throw etc. On advantage you
gain +1 to the result, on a disadvantage you gain -1 to the roll. If multiple sources would grant you advantage, then 
they do not stack and you still get +1, same with disadvanatage. If you would get both advantage and disadvantage then
you gain +0 to the roll no matter how many sources there are to either of those effects.
     '''
     },
    {'name': 'Critical success and failures',
     'description': '''
When making a d20 check, it is always against some target value called DC (dice check). When you meet it or roll higher
along with your bonuses then it is a success, if below, it is a failure. However if your result is higher than 
DC + critical threshold of 3, then it is a critical success. Effects that reduce the critical threshold cannot reduce
it to below +1.
 
When the roll is lower than DC - 3  then it is critical failure. Out of combat, the exact bonus or 
penalty for these extremes is decided by GM. In combat, even though there is no critical failure penalty (except for a
few abilities), when scoring a critical success, all your damage dice are automatically their maximum value. Meaning on
average a critical hit is twice as much damage as a regular hit. In addition all flat bonuses to the damage are doubled,
unless the flat bonus is specifically given due to the attack being a critical hit.
     '''
     },
    {'name': 'Epic moments',
     'description':'''
GM can decide, and players can request for something to be an epic moment, meaning this roll matters. In this case the
normal rules of no matter how many sources of lucky, unlucky, advantage or disadvantage you have, they cancel out, does
not apply. If one has more sources of lucky than unlucky then they get the lucky bonus and vica versa. Same goes for
advantage and disadvanatage. However they still do not stack. Advantage and disadvantage will still only provide either
+1 or -1
     '''
     },
    {'name': 'Aid',
     'description': '''
Usually when a skill check is made, then party must choose who does it, like in the case of diplomacy, or tracking etc.
However others can choose to take a helping role. By rolling for the same skill, they need to roll against original 
DC-2. If they succeed they grant advantage to the player doing the skill check. However if they fail critically they 
grant disadvantage. 

Lore skill can be used for aiding in all skill checks, however when aiding a none-lore skill check, it is done against 
the original DC.
     '''
     },
    {
        'name': 'Campaign mode and combat mode',
        'description': '''
At all times the game is either in campaign mode or combat mode. In campaign mode the order of things is much more loose
and really a constant negotiation and feel good between the GM and players.

In combat however, the order of action is determined by initiative order and the rules of what actions are allowed, what
is their effect and where everyone are are strictly determined by the rules of this game.
        '''
    },
    {'name': 'Action points',
     'description': """
Action points (AP) are used to do actions during combat encounters. During each player's turn in a round, they have by 
default 3 AP, which they can use to attack, cast spells, move or use some other abilities. The base AP can be increased 
by only 1 Martial innate feat. 
Each character can gain bonus AP only from a single buff. If multiple buffs would grant AP, then only the best of them 
is used. Many debuffs can lower the amount of AP.
     """
     },
    {'name': 'stamina',
     'description': """
Stamina is used to make attacks, dodging, and when wearing heavy armor, then for doing any actions. All characters have 
by default 5 MAX Stamina, and they recover 1 Stamina per round. All characters start each encounter with full stamina.
Martial path can improve their maximum stamina, and also their stamina recovery per round. Basic weapon attack costs
1 STA, and increases the stamina cost of each additional attack by 1, that lasts until the beginning of your next round. 
That means that reaction attacks also suffer from the additional STA cost from the previous attacks made since the
beginning of your last round. Special attacks gained from the martial feat pool have their own stamina costs and they 
also vary in how much the increase the cost of each additional attack.
     """,
     },
    {'name': 'Forced movement / falling damage',
     'description': '''
When characters are moved forcefully through some effect, but during their movement they meet an obstacle, they take
1d6 damage for every remaining 2m. of movement they were supposed to do.

When a character is moved onto another character, the second character needs to make a REF save of 10 + 1 for every 2m
left of forced movement. On fail they both take damage equal to 1d6 damage for every remaining 2m. of movement. On
success he dodges and the guy moved forcefully passes through.

When falling from heights, characters take 1d6 damage for every 2 m. after the first 2 m. When also falling from height
greater than 2 m. they need to make a REF save of 10 + 1 for every 2 m. On fail they fall prone.

When a character falls onto another character, the character on the ground needs to make a REF save of 
10 + 1 for every 2 m. On fail they also take the fall damage and fall prone. The falling character is put onto a random
empty tile next to felled upon character.
'''
     },
    {
    'name': 'Hit points / Health',
     'description': """
Hit points determine how much damage you can take before becoming incapacitated, or even worse die. When you fall to 0 or
below hitpoints, you fall prone and become incapacitated, meaning you are unable to act
. 
When you have negative HP, you cannot do any actions and every round you must roll one of your hit dice and 1 additional 
hit die for every 30 HP you are missing from 0 and recover that much HP until you have at least 1 HP. If you don't have 
the necessary amount of hit dies to roll, you die. 
     """,
    },
    {
    'name': 'Hit dice',
     'description': """
All players have hit dice, that they need to use whenever they are healing themselves or get healed by other sources.
When they have no more hit dice and need to roll a hit dice, they die. All players have a maximum 6 hit dice at level 1,
and gain 2 additional maximum hit dice every level. The dice depends on the number of points in martial path. 

Legendary martials have d6 +3 as hit dice, Talented martials have d6 +2, Adebt martials have d6 +1 and Acquinted and players 
without any points in martial have d6 as their hit dice. (the +X means that they roll d6 and add X to the result).

When finishing the daily rest, unless player has no food rations, they recover at least 5 hit dice. When finishing it
in a comfortable establishment, they recover at least 10 hit dice. By eating special more expensive food, they can
recover more hit dice.
     """,
    },
    {
    'name': 'incapacitated',
     'description': """
When a creature drops to 0 or less hit points, they become incapacitated. They drop on the ground and can no longer
act. That means they are prone. When their hit points get back to above 0 through rolling hit dice every 
turn or through healing they remove incapacitated status condition and gain up to 10 levels of disoriented.
     """,
    },
    {
    'name': 'Death',
     'description': """
When a creature has 0 or less hit points and they are forced to through a hit dice, but they have none left, they die.
Death is permanent. So if this happens to a player, they simply discard that character and need to make a new one.
     """,
    },
    {'name': 'Action difficulty',
     'description': """
Both spells, attacks and other various actions can have difficulty requirement, and additional options that increase
the difficulty of the action in addition to making those actions stronger. The maximum difficulty of an action a player
can perform is determined by the effective level in the underlying proficiency.

For spells higher difficulty also increases the mana cost by 1 per difficulty. For attacks there is no additional cost
for increasing difficulty unless specified otherwise.
     """},
    {'name': 'Mana',
     'description': """
When advancing in the mage path, characters can increase their maximum mana. 
When casting spells one must spend mana. If one is out of mana, they can no longer cast spells that require them.
Mana is required during daily rest. Characters who have taken points in maximum mana also have some amount of daily mana
recovery. This base is always recovered. However magic users can consume quite pricy magical spices to recover increased
amounts of mana.

For the first 1 - 10 mana, the cost of spices is 3 gp per mana.

For the next 11 - 25 mana, the cost of spices is 5 gp per mana.

For all mana after that, the cost of spices is 10 gp per mana.

Suppose a spell caster with 100 maximum mana, 25 base mana recovery, has spent 60 mana. During the daily rest, he would
recover 25 mana as a baseline, but then would need to spend magical spices worth of 30 (first 10) + 75 (next 15) + 
100 (final 10) gp = total of 205 gp worth of spices to recover their mana fully. They could also choose to
only spend for example 30 gp worth of food and recover only 35 total mana ending up having 75 mana.
     """,
     },
    {'name': 'checking for "status effect"',
     'description': """
Many spells, abilities or difficulty adjustment options can have a statement: "check for {status effect}". That means
whoever needs to check for it, needs to throw a 3d6, add either reflex, will or fortitude proficiency bonus 
(depending on the status effect) to it and compare it to 10 + attacker's/caster's proficiency bonus. When it was caused by a 
weapon attack, the weapon proficiency bonus is being used. When by a spell, then the spell school's proficiency bonus is 
being used. When the one who checks for the status effect fails the check, they gain the status effect. 
     """,
     },
    {'name': 'Concentration',
     'description': """
Some spells can last more than 1 round of combat, but in order to do so they require concentration to be maintained.
When a spell has concentration 2, then that means caster would need to spend 2 AP next round to maintain that 
concentration. In addition to the AP cost, concentration spells also require mana to be spent each round,
unless the spell has duration, in which case mana is needed to be spent at the end of duration.
The base cost for the concentration cost is spell's difficulty at casting divided by 2 rounded down. 
Whenever you take damage you must make a WILL check with a DC of 8 + damage / 7 rounded up. If you fail, you lose 
concentration of one spell of your choice. If you critically fail, you lose concentration of all spells.
     """
     },
    {'name': 'Spell duration',
     'description': """
When duration is not specified then the spell effect is immediate or for concentration spells, until you manage to hold
concentration. When duration is specified the spell lasts for the duration. If this is concentration spell, it can last
longer, but every time it's duration would end you will need to spend the mana cost as described previously
when talking about concentration. When your concentration breaks, the spell ends regardless of it's duration. Duration
spells without concentration cannot be ended by breaking concentration, but the spell caster may end their effect
pre-maturely voluntarily.
     """
     },
    {'name': 'Magical potions',
     'description': """
Throughout the game-world players may find potions with magical effects and mages with the potion maker feat can make
them themselves. Potions however have limitations. You can safely only use 1 potion per encounter. Each additional
potion forces you to make a Fortitude check, second potion having DC of 8, third one 10, and each consecutive 
increasing DC by another 2. If you fail the save through, you don't receive the effect and instead puke it out, losing
your 1 AP and the potion. And yes, to consume a potion requires 1 AP.
     """
     },
    {'name': 'Stealth',
     'description': '''
There is no stealth skill in the game, instead survival skill is used and depending on your familarity with the
environment you get a bonus. Still there are some things that refer to it, in the forms of penalties etc.
     '''
     },
    {'name': 'Different armors',
     'description': '''
There are 3 different armor categories in the game. Light armor, which provide between 1 and 2 AC, Medium armor, which
provide between 2 and 3 AC and heavy armor providing between 3 and 4 AC (Higher AC versions in each category being 
exceedingly more expensive). In addition heavy armor provides resistance to to all damage except for psychic damage.

Neither armors nor weapons receive any AC or accuracy bonus from magical effects, instead
magical effects focus on other things.

Everyone are proficient with light armor and wearing them has no penalty.

Without proficiency in medium armor, You need to spend 1 STA for each AP you spend on attacks and movement while wearing
medium armor. While having proficiency medium armors have no penalty.

Heavy armors have: You need to spend 2 STA for each AP you spend on attacks and movement, or 1 STA for each AP you spend
on anything else (like casting spells).
when you are not proficient you also get -1AC and -1 AP. However the upside of heavy armor is that you have resistance
to all damage except for psychic and lightning.
         '''
    },
    {'name': 'Shields',
     'description': '''
Similarly as in Pathfinder, in order to get the bonus AC from shields, which are between 1 and 2, you need to spend 1 AP
for the raise shield action. If you are proficient with shields, then raising shield is a free action.
         '''
    },
    {'name': 'Resistance',
     'description': '''
You can have resistance to various damage types, the incoming damage to these damage types is halved, rounded down.
         '''
    },
    {'name': 'Attunement',
     'description': '''
In order for characters to make use of magical items they need to attune to them. There are also some other effects
that require attunement. By default all players can attune to up to 3 items, but some feats in the mage path allow
for increased attunement.
         '''
    },
    {'name': 'Story beat / scene',
     'description': '''
The story is divided into scenes or beats. Each scene has a setup and description by the GM and they can serve as
normal story progression scenes, where players do stuff, or tactical scenes, where players are presented a problem,
or problems, or they can spot even more potential problems, and they need to describe a strategy or tactics how they
try to solve those problems. Then they decide who does which roles, who aids who, and then they roll the necessary
skill checks and the combination of presented problems, hidden problems, their tactics and strategy, and the skill
checks presents an outcome moving the story forward.
    '''
    },
    {'name': 'Is there such a thing in the game-world',
     'description': '''
During each of the encounters and story beats, each player may ask the GM if there is some thing in the game-
world, which the GM didn't describe beforehand but which might sound plausible. When making the request, it
is recommended to also ask for the functionality that they imagine they would want to get out of it. This
allows the GM to provide something that is more plausible but with similar functionality. 
The GM sets the base DC (0, very likeyly, 5, plausible, 10, unlikely, 15, very unlikely, 20, nearly impossible) 
and rolls a d20 to add to the base DC to make the final DC. Then choose a check they need to make, and if 
successful then you describe a way this can exist, and how they can achieve what they want using this knowledge.        
     '''
     },
    {'name': 'Group focuses',
     'description': '''
At all times the group can have 1 group focus active, which let's them progress towards a goal that the players have
completely set themselves. This is in addition to the main quest that GM is presenting. Usually a story beat progresses
either the main quest or one of the group focuses. Group focuses are often tied to some skill, meaning that these skills
are often most important in achieving these goals, but of course not solely used.
'''
     },

]
