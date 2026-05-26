from math import floor, ceil

def get_intro_chapter():
    return [
        {'type': 'title', 'content': 'Intro'},
        {'type': 'paragraph',
         'content': """
Why develop my own TTRPG?

1. I wanted the impact and excitement of DnD character progression while having sound pillars for balance.

2. I wanted to create a feeling, where all characters feel OP. Obviously when everyone is OP, and the villains are OP
then no-one is OP. However I do believe this feeling can be created by allowing characters to really shine in a few 
things, so the feeling of OP-ness ends up being a rotational, as situations and circumstances change.

3. I wanted a system which supports GM and makes his life easier. The idea here is to bake the best practices already
into the rules somehow, since the philosophy is that, simple rules often simply hide the complexity inside the execution
of these rules. I want to move some of the cost of running the game into learning the rules.

4. The goal of this particular setting is to facilitate a game, with limitations, time pressure, a campaign where the
world is at some cross roads, and players are rewarded from squeezing the maximum out of every opportunity.  

5. Just because, fun :)

What is still the same?

1. Roleplaying, it's still a open fantasy world, players can state what they want to achieve, and what they can or
cannot do is determined by the narrative, common sense of the GM and dice.

2. Grid based combat. Measurement unit is 1 sq. (square) though

So what is different?""",
},
        {'type': 'list',
         'content': [
"""6 X d6 system, where players have 6 X d6 dice. In this game players first roll their dice, and then spend them
during their combat turn to do actions, or during campaign turns to attempt to do actions. 

During combat each action requires a specific combination of dice, 
and also to upcast spells or to add weapon abilities onto your attack, it requires you to get even
more difficult combinations. But basically those Xd6 dice that you roll each turn, become your
action economy and success checks at the same time. Also when you take damage you start losing some of those dice making
you increasingly weaker until you are healed. But same goes to the enemy. Because of that significantly damaged enemies
are much more incentivised to flee or surrender than to continue fighting.""",
"""Very little stat stacking. Your character is mostly defined by their proficiencies. What school of magic they know, 
what weapons they are good at, what skills have they mastered. You don't specifically put points into general abilities
such as strength, instead if you are proficient with an axe, you also are equally strong and being good at axe basically
helps you do simple tasks that would require strength.""",
"""No races in a mechanical point of view. You can choose your own race, and if that race is supposed to have some
special ability like dark vision, or flying, then there is a trade-off system for these features, and that comes at
the expense of your other level 1 powers. Again, that takes away the need to pick a race to get a few numbers advantage 
for the build and instead you can focus on the role playing, background, flavour aspect of any race (I mean let's face
it, that's what custom lineages are for, and now everyone want to have that free feat at level 1 for everyone, so we
might as well do away with races).""",
"""No traditional classes, and therefore no multi-classing, but with a caveat""",
"""Instead players get to define their innate ability among 3 paths - mage, martial and skilled. Mages can cast spells,
and are really only defined by their school of magics they choose to focus on, but basically they can do stuff noone
else can, martials excel in combat, both in being
able to take a punch but also excel in their sustained damage dealing potential. Skilled excel in campaign progression,
creative solutions to all sorts of problems, and generally in everything out of combat. Heroes get to spread out 6
points when creating their character among the 3 paths. The maximum in each path, one can assign is 4 points, giving
them a legendary innate ability in that path. That means every hero is somewhat acquainted in at least 2 of the 3 paths.
The end result of this is that even though there are no classes, the choice of how you distribute the 6 path points really
defines what your character can be built as, in a way there are 19 meta classes (the number of ways these 6 points can
be distributed).""",
"""There is a simple advancement system. Each level-up you get to advance in your innate paths depending your initial
point distribution. Both general things like being able to cast more spells, capping your proficiency in some school
of magic, weapon or skill and character defining things like picking feats is used by a 
shared pool of advancements. The advancement options, and also feat options are different for each path.""",
"""Weapon choice matters. Both because each weapon requires investment to become proficient in it, so you can't be
master with all weapons, but also because each weapon can have multiple awesome abilities. The abilities have been made
significantly more impactful, but with a caveat. You need to spend some of the dice to use these special abilities""",
"""Your mage is defined by your schools of magic you choose to focus on. Again, to become proficient and be able to cast
the most powerful spells in some school of magic, you need to have spent those precious advancement points on those
schools of magic, meaning you cannot have all the spells, and the choices you make really define your character.""",
"""Less spells is more spells. Instead of having 10 spells that do the same thing but with different numbers, there are
less spells, usually each spell is very unique and provides a unique ability or mechanic not achievable through other
spells. Instead there are a lot more scaling options for spells. A spell can have 1 or more scaling options. In addition
all spells can be augmented by taking one of the many metamagic feats providing additional scaling options. So when you
gain the ability to cast more difficult spells, you actually gain the ability to cast your existing spells with
additional power. And yes, there is only a single heal spell in the game. It is called heal. One gets access to it at 
level 1, and you can scale it, in very many ways.""",
"""Time advancement is abstracted. Campaign is played in campaign turns, they can be quick turns, medium turns and
strategic turns. This abstraction does away with considerations like how many minutes is a short rest, or what time it
is. A good day of work consists of either 1 or 2 medium turns. So when players complete a medium turn that started
in the morning, then it is now late afternoon. Each turn consists of rolling the 6 d6 once and spending them to do 
things.""",
"""We did away with skills, and instead players choose creative skill traits, that are associated with one of the 6
general abilities. This creative skills have proficiencies, and players can get better at these skills. These 
proficiencies are on the same level of abstraction as weapon proficiencies, and school of magic proficiencies.
""",
    ]},
]
