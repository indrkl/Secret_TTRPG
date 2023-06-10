from math import floor, ceil

def get_intro_chapter():

    return [
        {'type': 'title', 'content': 'Intro'},
        {'type': 'paragraph',
         'content': """
Why develop my own TTRPG?

1. This is not all new. Most is still stolen from DnD or Pathfinder, so no worries.

2. I wanted the impact and excitement of DnD character progression while having sound pillars for balance.

3. Just because, fun

4. I wanted to create a feeling, where all characters feel OP. Obviously when everyone is OP, and the villains are OP
then no-one is OP. However I do believe this feeling can be created by allowing characters to really shine in a few 
things, so the feeling of OP-ness ends up being a rotational, as situations and circumstances change.

What is still the same?

1. Skills and skill checks to see what happens

2. Combat still has initiative order, 6 second rounds, using pathfinder's 3 Action points per round system, all players 
have move action and basic attack action. You also do special attacks, use abilities and cast spells using APs. 

3. Players have Armor class, they add a bonus to their skill checks, attack rolls.

4. Some effects force one to make checks, where they need to pass a certain threshold or they get a status effect etc.

5. Grid based combat, 12 m. move speed for most characters.

So what is different?

1. No attributes. Your character is strictly defined simply by their proficiencies. What school of magic they know, 
what weapons they are good at, what skills have they mastered. Attributes offered very few interesting choices, and
usually were more of an hindrance to creative combinations. 

2. No races in a mechanical point of view. You can choose your own race, and if that race is supposed to have some
special ability like dark vision, or flying, then there is a trade-off system for these features, and that comes at
the expense of your other level 1 powers. Again, that takes away the need to pick a race to get a few numbers advantage 
for the build and instead you can focus on the role playing, background, flavour aspect of any race (I mean let's face
it, that's what custom lineages are for, and now everyone want to have that free feat at level 1 for everyone, so we
might as well do away with races).

3. No traditional classes, and therefore no multi-classing, but with a caveat.

4. Instead players get to define their innate ability among 3 paths - mage, martial and skilled. Mages can cast spells,
and are really only defined by their school of magics they choose to focus on, but basically they can do stuff noone
else can, martials excel in combat, both in being
able to take a punch but also excel in their sustained damage dealing potential. Skilled excel in campaign progression,
creative solutions to all sorts of problems, and generally in everything out of combat. Heroes get to spread out 6
points when creating their character among the 3 paths. The maximum in each path, one can assign is 4 points, giving
them a legendary innate ability in that path. That means every hero is somewhat acquainted in at least 2 of the 3 paths.
The end result of this is that even though there are no classes, the choice of how you distribute the 6 points really
defines what your character can be built as, in a way there are 19 meta classes (the number of ways these 6 points can
be distributed).

5. There is a simple advancement system. Each level-up you get to advance in your innate paths depending your initial
point distribution. Both general things like being able to cast more spells, capping your proficiency in some school
of magic, weapon or skill, capping your AC potential and character defining things like picking feats is used by a 
shared pool of advancements. The advancement options, and also feat options are different for each path.

6. Weapon choice matters. Both because each weapon requires investment to become proficient in it, so you can't be
master with all weapons, but also because each weapon can have multiple awesome abilities. The abilities have been made
significantly more impactful, but with a caveat. They have a difficulty penalty, so when choosing to use some weapon
ability, if you still want to strike at your proficiency maximum for your level, then you need to spend those precious
advancement points to off/set that difficulty.

7. Your mage is defined by your schools of magic you choose to focus on. Again, to become proficient and be able to cast
the most powerful spells in some school of magic, you need to have spent those precious advancement points on those
schools of magic, meaning you cannot have all the spells, and the choices you make really define your character.

8. Less spells is more spells. Instead of having 10 spells that do the same thing but with different numbers, there are
less spells, usually each spell is very unique and provides a unique ability or mechanic not achievable through other
spells. Instead there are a lot more scaling options for spells. A spell can have 1 or more scaling options. In addition
all spells can be augmented by taking one of the many metamagic feats providing additional scaling options. So when you
gain the ability to cast more difficult spells, you actually gain the ability to cast your existing spells with
additional power. And yes, there is only a single heal spell in the game. It is called heal. One gets access to it at 
level 1, and you can scale it, in very many ways.

9. Group and personal focuses: Often players want to trick the GM to get rolls for things that are super powerful,
super wild, or it may simply feel like getting too much for a single roll of dice. Instead of saying yes or no, you say
OK, eventually. Group can choose a cool thing that they care about, and that becomes their focus, either getting an
item, learning about a secret, getting discount with all the merchants etc. and depending on how wild the thing they
want is, there are a certain amount of progress steps that GM decides needs to be achieved, before they get what they
want and to spice things up there can be fail conditions along the way etc.

10. Less skills, and more options to use those skills in various situations, allowing for much more intended overlap.
Talking with a charismatic pirate leader you can use both roguery or diplomacy skill to gain his favor, but the story
may unwrap differently depending on which one you choose.

11. Using only d6. Instead of d20 skill checks we use 3d6. The base check is 10, and difficulty ranges from +1 to +7.
"""},
]
