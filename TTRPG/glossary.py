glossary = [
    {
        'name': 'Dice pool',
        'description': """
All characters have a dice pool. For example by default heroes start with a dice pool of 6 dice. Level ups, feats, spell
effects etc. can increase the size of the dice pool. However when a character takes damage they must set aside dice from
the dice pool, until they have no more of them in the dice pool at which point they are left incapacitated
        """
    },
    {
        'name': 'Action limit',
        'description': """
While you can never spend more dice than in your dice pool. You also cannot spend more dice on actions per round 
than your action limit. By default heroes start with an action limit of 5. Action limit does not apply outside combat 
        """
    },
    {
        'name': 'Roll target',
        'description': """
All actions have some certain roll target. For example R6.R6.R6 means that you need 3 dices with the 6 result in order
to perform this action. Also various outcomes in social encounters or campaign in general have roll targets, which have
to be met in order to get the desirable results. 
        """
    },
    {
        'name': 'Proficiency',
        'description': '''
Players can have proficiency in a skill, weapon class, school of magic or a saving throw. Proficiency allows them to
nudge dice results in order to easily meet the roll target so that the desired rolls are met much more consistently.
        '''
    },
    {
        'name': 'Proficiency bonus',
        'description': '''
Proficiency bonus ranges from 1 to 4. That means how many times you can nudge dice by 1 in a given round  / scene to
meet a roll target that is related to the skill, weapon or school of magic of the proficiency at hand.

For example with a proficiency of 2 you can nudge the roll of 2 dice by 1, or a roll of a single dice by 2. You can only
nudge the rolls of a dice used on the roll target that you actually use on the roll target.
        '''
    },
    {'name': 'Lucky',
     'description':'''
A player can be lucky during a round or scene. In that case they can switch one of their d6 to any desired result
without spending any proficiency nudging.
     '''
     },
    {'name': 'Advantage and disadvantage',
     'description':'''
A character who has advantage against an enemy requires 1 less power dice for any attack against them. A character with
disadvantage requires 1 more power dice to do an attack.
     '''
     },
#     {'name': 'Critical success and failures',
#      'description': '''
# When making a d20 check, it is always against some target value called DC (dice check). When you meet it or roll higher
# along with your bonuses then it is a success, if below, it is a failure. However if your result is higher than
# DC + critical threshold of 3, then it is a critical success. Effects that reduce the critical threshold cannot reduce
# it to below +1.
#
# When the roll is lower than DC - 3  then it is critical failure. Out of combat, the exact bonus or
# penalty for these extremes is decided by GM. In combat, even though there is no critical failure penalty (except for a
# few abilities), when scoring a critical success, all your damage dice are automatically their maximum value. Meaning on
# average a critical hit is twice as much damage as a regular hit. In addition all flat bonuses to the damage are doubled,
# unless the flat bonus is specifically given due to the attack being a critical hit.
#      '''
#      },
    {
        'name': 'Campaign mode and combat mode',
        'description': '''
At all times the game is either in campaign mode or combat mode. In campaign mode the order of things is much more loose
and really a constant negotiation and feel good between the GM and players.

In combat however, the order of action is determined by initiative order and the rules of what actions are allowed, what
is their effect and where everyone are are strictly determined by the rules of this game.
        '''
    },
    {
        'name': 'taking damage and various defenses',
        'description': '''
If you X damage then it is mitigated followingly:

1. First substract damage reduction from the damage

2. Then character's remaining defense mitigates it as much as possible. All mitigated damage lowers character's defense,
but not maximum defense.

3. The rest of the damage hits the character's "life pool", see next topic

Defense can be recovered by taking the compose defense action, with which one recovers up to their maximum number of
defense.
        '''
    },
    {
        'name': 'taking damage to life',
        'description': '''
In combat or certain situations out of combat characters may take damage. When that happens they set aside dice from
their dice pool following these rules:

1. Each dice mitigates damage equal to character's toughness.

2. When you have a dice that is set aside that can still mitigate some damage, it mitigates that damage before a new
dice is set aside.

3. When you have no dice set aside which can mitigate damage but there is still incoming damage to be mitigated, then
you must take another dice from dice pool and set it aside and use it to mitigate the remaining damage

4. Note that the maximum toughness is 6, so that you can always use the set aside D6 to mark the remaining damage it can
still mitigate.

5. Note that you cannot set aside bonus dice from the dice pool, but only the dice granted to you inherently.

6. You cannot set aside scarred dice as long as you have normal dice.
        '''
    },
    {
    'name': 'Healing and scarred dice',
     'description': """
Each time you receive healing and recover some of the set aside dice, one of those dice become scarred (try to have
them in different color, like red for example).

Scarred dice can only be used as 1, 2 or 3 in any roll target. You can still nudge them lower if they roll 4, 5 or 6.

At the beginning of each day after a proper rest, by spending various resources like herbs, good food etc. one can
change scarred dice back to normal dice.
To change a single dice back it costs 3 gp worth of resources, to change 2 dice back it costs 15 gp and to change 3 dice
back it costs 50 gp worth of resources.
     """,
    },
    {
    'name': 'Exhausting dice',
     'description': """
Some effects force players to exhaust dice. They are set aside from the dice pool. By default players recover 1
exhausted dice per round.
     """,
    },
    {
    'name': 'incapacitated',
     'description': """
When you have no more dice in your dice pool, you are incapacitated, cannot move nor do any actions, even if you have
bonus actions.
     """,
    },
    {
    'name': 'moral',
     'description': """
All enemies and NPC allies have moral. That means their willingness to fight. GM can obviously determine the moral for
enemies. But here are the general guidelines for how moral is lost:

1. Each dice lost from the dice pool loses 1 moral
2. Each ally lost reduces moral by 1
3. Losing a stronger ally reduces moral by additional 2
4. Dropping to 2 dice in your dice pool reduces moral by additional 3
5. Dropping to 1 dice in your dice pool reduces moral to 0 unless enemy is raging or smth equivelant.
6. Getting outnumbered reduces moral by 2
7. Defeating an enemy increases moral by 2
     """,
    },
#     {
#     'name': 'Death',
#      'description': """
# When a creature has 0 or less hit points and they are forced to through a hit dice, but they have none left, they die.
# Death is permanent. So if this happens to a player, they simply discard that character and need to make a new one.
#      """,
#     },
    {'name': 'Mana',
     'description': """
When advancing in the mage path, characters can increase their maximum mana. When casting spells or concentrating one 
must spend 1 mana per dice used in the spell. 

If one is out of mana, they can no longer cast spells that require them.
Mana is recovered during daily rest. Characters who have taken points in maximum mana also have some amount of daily 
mana recovery. This base is always recovered. However magic users can consume quite pricy magical spices to recover 
increased amounts of mana.

For the first 1 - 10 mana, the cost of spices is 3 gp per mana.

For the next 11 - 25 mana, the cost of spices is 5 gp per mana.

For all mana after that, the cost of spices is 10 gp per mana.

Suppose a spell caster with 100 maximum mana, 25 base mana recovery, has spent 60 mana. During the daily rest, he would
recover 25 mana as a baseline, but then would need to spend magical spices worth of 30 (first 10) + 75 (next 15) + 
100 (final 10) gp = total of 205 gp worth of spices to recover their mana fully. They could also choose to
only spend for example 30 gp worth of food and recover only 35 total mana ending up having 75 mana.
     """,
     },
#     {'name': 'Forced movement / falling damage',
#      'description': '''
# When characters are moved forcefully through some effect, but during their movement they meet an obstacle, they take
# 1 damage for every remaining sq. of movement they were supposed to do.
#
# When a character is moved onto another character, the second character needs to make a REF save of 10 + 1 for every 2m
# left of forced movement. On fail they both take damage equal to 1d6 damage for every remaining 2m. of movement. On
# success he dodges and the guy moved forcefully passes through.
#
# When falling from heights, characters take 1d6 damage for every 2 m. after the first 2 m. When also falling from height
# greater than 2 m. they need to make a REF save of 10 + 1 for every 2 m. On fail they fall prone.
#
# When a character falls onto another character, the character on the ground needs to make a REF save of
# 10 + 1 for every 2 m. On fail they also take the fall damage and fall prone. The falling character is put onto a random
# empty tile next to felled upon character.
# '''
#      },
    {'name': 'status effect',
     'description': """
Since whenever someone meets their roll target, then they always succeed, if anyone's actions grant other characters
status effetcs they cannot be avoided unless there is a reflex save option. Other status effects have usually other ways
to remove them usually using fortitude or will.

When making reflex saves, you roll 2d6 and when you can make the save using those dice and your proficiency you succeed,
otherwise you fail. Note that the number of times you can nudge during reflex saves resets only at the beginning of your
round. So if you need to make more than 1 reflex save in between your turns they all share the total number of nudges
you can do based on your proficiency.

For fortitude you need to spend your dice from the dice pool, but they don't lower you action limit.

For will saves, the spent dice also count towards you action limit.
     """,
     },
    {'name': 'Concentration',
     'description': """
Some spells can last more than 1 round of combat, but in order to do so they require concentration to be maintained.
The concentration cost is displayed next to the spell info. It is also a roll target. At the beginning of your round
in order not to lose the effect of the spell one must spend dice on the roll targets. Note that if you need to use
your proficiency to meet these targets, then you have that many less nudges for all spells this round of the same school
of magic.
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
them themselves. Potions however have limitations. The roll target for the first potion is RX, meaning any 1 dice will
do. The roll target for the second potions is RX for drinking the potion and R3 fortitude check to stomach that potion.
After that an additional R3 is added to the fortitude check each time. To make these fortitude checks does not consume
action limit, like all fortitude checks.
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
There are 3 different armor categories in the game. Light armor, Medium armor and heavy armor.

Armor provides maximum defense. Light armor provides 2-3 maximum defense. Medium armor provides 3-5 maximum defense.
Heavy armor also provides 3-5 maximum defense, but it also provides 1-2 damage reduction. The range depends on the
quality of the armor and better quality armor becomes available as players progress in the campaign.

However each armor has certain additional upsides / downsides.

Having no armor and no shield: You have 1 additional action limit and have access to dodge.

Having light armor: You have access to dodge.

Having medium armor: No upside or downside with proficiency. You have 1 less action limit without medium armor 
proficiency.

Having heavy armor: You have 1 less action limit, or 2 less action limit without heavy armor proficiency.
         '''
    },
    {'name': 'Shields',
     'description': '''
Shields can be used to provide additional defensive actions. In addition they also provide 1-2 maximum defense. 
         '''
    },
#     {'name': 'Resistance',
#      'description': '''
# You can have resistance to various damage types, the incoming damage to these damage types is halved, rounded down.
#          '''
#     },
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
