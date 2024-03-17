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
        'name': 'Dice Roll',
        'description': """
During a dice roll, your entire dice pool is rolled at once. Afterwards you can pick and choose which dice to use on
which action.

Out of combat, dice rolls happens at the beginning of each scene.

In combat, dice rolls happen at the end of each players round. The players can use dice from the dice pool for reactions
in between their turns and for actions during their turn.
        """
    },
    {
        'name': 'Power dice and utility dice',
        'description': """
Each weapon type, school of magic and combat action has 2 dice, power dice, and utility dice. To activate the action
(attack, spell) and to boost it's raw power you need to get power dice. But to augment the action / spell in useful
ways, you need utility dice. For example, the power dice of swords is R5 (a dice that rolled a 5) and utility dice is
R2. 
        """
    },
    {
        'name': 'Reactions',
        'description': """
Some feats provide characters abilities for reactions under certain conditions outside their turn. These still consume 
dice in the dice pool.
        """
    },
    {
        'name': 'Roll target',
        'description': """
All actions have some certain roll target. For example R6.R6.R6 means that you need 3 dice with the 6 result in order
to perform this action. Also various outcomes in social encounters or campaign in general have roll targets, which have
to be met in order to get the desirable results, these are also called as challanges.
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

For example with a proficiency of 2 you can nudge the roll of two separate dice by 1, or a roll of a single dice by 2. 
You can only nudge the rolls of a dice used on the roll target that you actually use on the roll target.
        '''
    },
    {'name': 'Advantage and disadvantage',
     'description':'''
A character who has advantage against an enemy requires 1 less power dice for any attack against them. A character with
disadvantage requires 1 more power dice to do an attack.

Normal advantage and disadvanatage does not stack. However some effects can specifically provide double advantage or
double disadvantage, in which case it is 2 power dice that is needed less or more.
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

In combat however, The order is more strict. The surprise round may vary, but afterwards each round works as follows:
GM declares the threats and intentions of all the enemies. Players get to damage, move and disrupt the plans of the
enemies, and finally the remaining undisrupted threats resolve, meaning players get dealt damage and negative status
effects.

If the opposing side has a villain (powerful enemy), then he may interrupt players turns, or do his things with the
rest of the enemies. Either way he rolls XD6 as well and plays very closely to player characters.
        '''
    },
    {
        'name': 'Combat setup',
        'description': '''
You may know a lot of spells, or be able to do a lot of actions or use a lot of different weapons. However you can
use a limited number of them in combat decided by your combat setup. By default all players have 4 slots. One for
right hand, one for left hand, and two for mental. The action available for the right and left hand is decided by what
you wield. Mental slot can be filled with a spell, skill action etc. Also by freeing left or right hand you can
instead have an additional mental slot. Magical weapons like wands or staves also grant mental slots for spells.

By spending 2 dice from the dice pool, a player can switch what they are wearing in their hands with a backup setup,
the mental slots however cannot be changed.
        '''
    },
    {
        'name': 'taking damage and various defenses',
        'description': '''
If you take X damage then it is mitigated followingly:

1. First substract damage reduction from the damage

2. Then character's remaining defense mitigates it as much as possible. All mitigated damage lowers character's defense,
but not maximum defense.

3. The rest of the damage hits the character's "life pool", see next topic

Defense can be recovered by taking the Defense action, with which one recovers up to their maximum number of
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

7. Scarred dice always only mitigate 1 damage.
        '''
    },
    {
    'name': 'Healing and scarred dice',
     'description': """
Each time you receive healing and recover some of the set aside dice, one of those dice become scarred (try to have
them in different color, like red for example).

Scarred dice can only be used as 1, 2 or 3 in any roll target. You can still nudge them lower if they roll 4, 5 or 6.

To heal players must take time out and recover.

During recovery, by spending various resources like herbs, good food etc. one can change scarred dice back to normal 
dice.

To change a single dice back it costs 15 gp worth of resources, to change 2 dice back it costs 50 gp and to change 3 
dice back it costs 150 gp worth of resources. To recover all the dice, it coses 250 gp. 
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
When you have no more dice in your dice pool, you are incapacitated, cannot move normally nor do any actions, even if 
you have bonus actions or dice. Your character can still talk, and crawl 1 sq. per round.

Each damage turns one of the set aside dice into scarred dice (you can only receive healing by scarring a
not scarred dice).

If there are no dice left to scar when you take damage, you die.
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
8. For mobs losing half of their HP+DEF they lose 3 moral
     """,
    },
    {
    'name': 'Death',
     'description': """
When a creature, whose all dice are scarred takes damage, they die.

Death is permanent. So if this happens to a player, they simply discard that character and need to make a new one.
     """,
    },
    {
        'name': 'Resources',
        'description':"""
Each path has a specific resource associated with their path. Mages have mana, Martials have stamina and Skilled have
luck. Each resource is used for different effects and have different rules for recovering it. Mana is recovered during
long rest by consuming expensive spices and is used to cast spells. 
Stamina is recovered each encounter and can be used during combat to increase use scarred dice 
unconstrained and for some combat abilities, and luck tokens are recovered when a story arch finishes and are used to 
change the outcome of a single dice in a roll, or to gain advantage.
        """
    },
    {'name': 'Mana',
     'description': """
When advancing in the mage path, characters can increase their maximum mana. When casting spells, character may choose
to spend mana to reduce the number of dice required to cast that spell.

For 1 mana reduce the spell cost by 1 dice, for 3 mana, by 2 dice, for 6 mana by 3 dice and for 10 mana by 4 dice. You
cannot reduce the cost by more than your proficiency in the spell's school of magic. Note that this is for casting
spells during combat. When using magic in a scene, the mana cost is tripled with regards to lowering the dice
requirements to not trivialise most challanges.

Mana is recovered during rest by consuming quite pricy magical spices. You must spend enough resources to reach maximum
man, that means the more you consumed your mana during an encounter, the more pricy it will be. 

For the first 1 - 10 mana, the cost of spices is 3 gp per mana.

For the next 11 - 30 mana, the cost of spices is 5 gp per mana.

For all mana after that, the cost of spices is 10 gp per mana.

Suppose a spell caster with 100 maximum mana has spent 60 mana and now decides to rest. He can either not recover any
mana for now, or can spend 30 (first 10 mana) + 75 (next 20 mana) + 300 (last 30 mana) for a total of 405 gp to recover
their mana to full.
     """,
     },
    {'name': 'Stamina',
     'description': """
When advancing in the martial path, characters can increase their maximum stamina. Stamina can be used for following
effects:

Recover all defenses with just one R2 dice: 1 stamina

Deal 1 additional damage with your attack: 1 stamina

Double the movement of a single move action: 2 stamina

Only one of the previous options can be chosen per turn.

Another option to spend stamina on is to use a scarred dice ignoring the normal scarred dice limitation.

In additional some abilities may require stamina or provide means to recover stamina.

Stamina recovers after every encounter.
     """,
     },
    {'name': 'Luck tokens',
     'description': """
When advancing in the skilled path, characters can increase their maximum luck tokens. 

Luck tokens can be used in various ways, but each player can spend only 1 luck token per turn:

1 luck token: Get 2 additional nudges (in addition to your proficiency and aiding)

1 luck token: When throwing risk dice, negative results do nothing.

In addition some abilities may require Luck tokens to be used.


Luck tokens are recovered when the party chooses to take time out and recover.

     """,
     },
    {'name': 'Time out and recover',
     'description': """
When players are heavily scarred and run out of luck, they may find themselves needing to take time out and recover.
This should not be done lightly however, since in-game this can be several weeks to months. This means that this gives
time for adversaries to advance in their plans, for the situation to change, and for new challanges to be introduced.

In addition they need to find a proper lodging and this time out will cost them money, as they rest and don't earn any
money in the meanwhile.

Finally time out cannot be taken mid-session, as GM needs time to prepare and figure out how the world changes. It 
should be decided always at the end of a game session.

Note, there are costs associated with lodging, and recovering from scarred dice. Luck is recovered on it's own.
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

To use fortitude and will you need to spend your dice from the dice pool.
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
    {'name': 'Rituals',
     'description': """
Rituals are powerful spell effects which take a lot more time to cast and require much more mana than normal
spells. Like spells, the ritual caster needs to learn the ritual. However rituals can be casted by multiple spell
casters. Only one of them is required to know the ritual, but mages who do not know the ritual have dis-advantage when
casting the ritual.

How does it work? There are a certain number of dice that need to be met to complete the ritual. To complete these dice
casters need to roll their entire dice pool multiple times. Each time the mana cost to roll the pool increases but using
their proficiency they can progress in the ritual.

First roll costs 4 mana, then each consequent roll costs 2 additional mana. Players who have disadvantage, can 
contribute starting from the second dice that they meet for the target throughout the ritual, so when they roll the
second time and they met one roll in the first time they effectively no longer have disadvantage. 

Rituals can be used to prepare for combat against the odds.

Some rituals can have semi permanent effects, but they often have some daily mana cost. Meaning it is a constant
resource drain for the ritual caster.
     """
     },
    {'name': 'Magical potions',
     'description': """
Throughout the game-world players may find potions with magical effects and mages with the potion maker feat can make
them themselves. Potions however have limitations. The roll target for the first potion is RX, meaning any single dice will
do. The roll target for the second potions is RX for drinking the potion and R3 fortitude check to stomach that potion.
After that an additional R3 is added to the fortitude check each time.
     """
     },
    {'name': 'Stealth',
     'description': '''
There is no stealth skill in the game, instead either survival or concealment skill is used and depending on your 
familarity with the environment you may get a bonus or penalty. Still there are some things that refer to it, in the 
forms of penalties and bonuses etc.
     '''
     },
    {'name': 'Different armors',
     'description': '''
There are 3 different armor categories in the game. Light armor, Medium armor and heavy armor.

Armor provides maximum defense. Light armor provides 2-3 maximum defense. Medium armor provides 3-5 maximum defense.
Heavy armor also provides 3-5 maximum defense, but it also provides 1-2 damage reduction. The range depends on the
quality of the armor and better quality armor becomes available as players progress in the campaign.

However each armor has certain additional upsides / downsides.

Having light or no armor: You have access to dodge.

Having medium armor: No upside or downside with proficiency. You have -1 physique proficiency penalty without medium
armor proficiency. You cannot wear any armor if your physique proficiency would go negative as a result.

Having heavy armor: You have -1 physique proficiency penalty if you have heavy armor proficiency. You have -2 physique 
proficiency penalty without heavy armor proficiency.You cannot wear any armor if your physique proficiency would go 
negative as a result.
         '''
    },
    {'name': 'Shields',
     'description': '''
Shields can be used to provide additional defensive actions. In addition they also provide 1-2 maximum defense. 
         '''
    },
#     {'name': 'Resistance',
#      'description': '''
# You can have resistance to various damage types, the incoming damage to these damage types is halved, rounded up.
#          '''
#     },
    {'name': 'Attunement',
     'description': '''
In order for characters to make use of magical items they need to attune to them. There are also some other effects
that require attunement. By default all players can attune to up to 3 items, but some feats in the mage path allow
for increased attunement.
         '''
    },
#     {'name': 'Story beat / scene',
#      'description': '''
# The story is divided into scenes or beats. Each scene has a setup and description by the GM and they can serve as
# normal story progression scenes, where players do stuff, or tactical scenes, where players are presented a problem,
# or problems, or they can spot even more potential problems, and they need to describe a strategy or tactics how they
# try to solve those problems. Then they decide who does which roles, who aids who, and then they roll the necessary
# skill checks and the combination of presented problems, hidden problems, their tactics and strategy, and the skill
# checks presents an outcome moving the story forward.
#     '''
#     },
#     {'name': 'Scene dice target',
#      'description': '''
# Each scene has a specific dice target. All roll targets, that are created by the scene require that target, but
# obviously has different skill proficiencies. Player spells and abilities are however unaffected by this dice target.
#
# The target is decided by the nature and atmosphere of the scene.
#
# 1 - cold, but not hostile, when professionalism or clear etiquette is expected. Audience with a king, negotiations with
# shrewd merchant, talking with spies. You are not in danger, but also gaining what you want is difficult.
#
# 2 - Friendly atmosphere, a party, talking with people with good will towards you, calm, slow movement. No physical
# activity, no energy is required.
#
# 3 - Friendly atmosphere, but a more active activity. Travelling in friendly territory, trading actively. Taking part
# of a competition etc.
#
# 4 - Neutral to cold atmosphere, could turn hostile, but not currently.
#
# 5 - Hostile atmosphere, but the possible opponents are not very harsh or sharp, or when the fight is still not evident.
# Moving in hostile territory, facing a group of bandits, who demand money, climbing a mountain.
#
# 6 - Hostile, dangerous atmosphere, which is also very difficult, the situation may end up as combat any second now,
# any mistake could have damaging consequences.
#
# Note, that 1 and 6 are the hardest dice, so they represent difficulty. Choosing them is not just extreme friendly
# or hostile, these are reserved for 2 and 5, they represent difficulty of the situation.
#
# When the atmosphere changes, then so do the dice targets. For example we have a friendly scene, and then players insult
# deeply someone, and all of sudden the scene target changes to 4 or 5, which obviously consequences to the story as well.
#     '''
#     },
#     {'name': 'Is there such a thing in the game-world',
#      'description': '''
# During each of the encounters and story beats, each player may ask the GM if there is some thing in the game-
# world, which the GM didn't describe beforehand but which might sound plausible. When making the request, it
# is recommended to also ask for the functionality that they imagine they would want to get out of it. This
# allows the GM to provide something that is more plausible but with similar functionality.
# The GM sets the base DC (3, very likeyly, 7, plausible, 13, unlikely, 18, very unlikely, 20, nearly impossible)
# and rolls a d20. If the result is higher than DC then GM describes a way this can exist, and how they can achieve what
# they want using this knowledge.
#      '''
#      },
#     {'name': 'Group focuses',
#      'description': '''
# At all times the group can have 1 group focus active, which let's them progress towards a goal that the players have
# completely set themselves. This is in addition to the main quest that GM is presenting. Usually a story beat progresses
# either the main quest or one of the group focuses. Group focuses are often tied to some skill, meaning that these skills
# are often most important in achieving these goals, but of course not solely used.
# '''
#      },
    {'name': 'Creative spells',
     'description': '''
Some spells may leave a lot of room for creativity. In this case it is important to have a way to balance it. It is
perfectly alright, if the illusion magician creates whatever kind of illusionary image, question becomes what do they
want to achieve with it, what do they think the effect should be on other people? Here is a general balance idea of what
various effects should cost in power dices. Keep in mind that a good idea should given an advantage, and perfect ideas
even double advantage, while none-sensical ideas can either be dis-allowed or allowed with disadvantage. And of course
there can be staples in between, like disorienting with illusion, something your character always does, this can be
allowed without advantage or disadvantage. But when a creative opportunity arises and the player notices, then you can
reward the player with advantage or more. The goal is to create cool story moments with fun explanations which are still
somewhat constrained by balance (RP in following context is power roll, this depends on your school of magic which the
creative spell or ability belongs to).

1 RP: 2 damage
1 RP: 1 level of vulnerability, entangled, unbalanced or confusion
2 RP: 1 level of disoriented, afraid, prone, burning or disruption
3 RP: blinded, 1 level of frozen
2 RP: Aid an ally to give them advantage, or upgrade advantage to double advantage
X RP: Meet a scene roll-target, X is number of dice required in the roll-target. The dice used for roll-target also
override the spell's own power dice.

The default range for effecting someone is 6 sq.
     '''

    },
    {
        'name': 'Combat',
        'description': '''
Combat has usually 2 sides. The player characters and their allies, and the enemy. The combat turns are simple. First
the players move in turn order decided by their leader (leader is chosen at each game session based on leadership 
skill). Then all the mobs move by the following order: Bishops > Pawns > Rooks. Knights can be used in any of the other
pieces turns. For each piece type enemy mobs move first, and then allied mobs move second.

The combat is designed so that, you can easily add more than twice as many enemies against the heroes, and they would
still be able to win the fight with some wounds, resulting in more epic, and brutal cinematic fights.
        '''
    },
    {
        'name': 'Mobs',
        'description': '''
To make the combat flow quicker, then all enemies except for special characters have fixed attack damage, movement range 
and HP. There are 4 types of mobs, and each opposing encounter composition has the same statistics within a single type.
To make it simpler, they are represented by famous chess pieces, which is nice, since you can take them from your
chess game laying around and you already have the correct pieces to represent enemy units:

Pawns: the back bone and core of any encounter. They don't have special abilities, and have least HP, ATK and MV. Their
tactics usually involve simply attacking the nearest enemy.

Knights: Fast moving, high maneuverable units, they have slightly more HP, ATK than pawns and the most MV out of any of
the units. Their tactics involve attacking the weakest links, high aggro targets or someone who is already vulnerable.

Bishops: Ranged supporters, either archers, support spell casters, cyclops throwing stones etc. They often have high ATK
but are comparable to pawns with regards to HP and MV.

Rooks: Tanks, high HP units with better ATK than pawns but not necessarily better movement.

In addition, when heroes apply status effects to Mobs, then they disrupt their turns, so that they don't do their move
or attack action, but shrug of some of the negative status effects.

While pawns and bishops have disoriented or afraid, they skip their turn and lose 1 level of those. If they have 3
levels of those, they give up and flee the fight. If they have any levels of burning, they take the damage, skip their
turn and lose all of them. If they are poisoned by a damaging effect, they simply do their turn and take the damage.
If they have any levels of freezing they are removed from combat.

Knights and rooks can lose up to 2 levels of disoriented or afraid or all of burning (still take the damage). If they
only lose 1 level of those, they take their turn partially by doing half movement and half damage or either movement or
damage, halving is rounded down. If they have 2 levels of freezing, they are also removed from combat, or when they have
5 levels of combined disoriented and afraid. If they have 1 levels of freezing, then they act as if removing one level
of some negative effect every turn (without removing it) and can only remove 1 levels of disoriented/afraid.

When a mob is prone, then they need to give up either their entire movement or their entire attack, but they do stand
up.

In addition if a mob takes at least half of their hit points in damage they are also shocked and they skip their next
turn.

This gives you the baseline. In different line ups, like for example when fighting a tribe of giants, this may differ.
Also you could have an elite army, and all encounters against them, even the pawns would feel a lot tougher, and could
have much stronger defensive and offensive capabilities.

Disadvantage for mobs halves their damage. And advantage gives them up to 2 extra damage but no more than 50 % of their
original damage
        '''

    },
]
