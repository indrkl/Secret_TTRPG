from math import floor, ceil

def get_character_creation_chapter():

    return [
        {'type': 'title', 'content': 'Design philosophy'},
        {'type': 'paragraph',
         'content': """
Pillars:

1. Mage, Martial and Skilled paths should feel extremely distinct, by having clearly defined strengths and weaknesses.
Less so perhaps for Mage, where the identities are actually managed in the schools of magic themselves and not so much
by the path.

1.a Martials are clear, they excel in combat, and their main resource: stamina recovers easily, meaning they provide
clear value reliably and without cost.

1.b Skilled is also clear, they excel out of combat, by having access to all the skills. In addtion they have the
luck resource, which is the most effective in achieving your results whenever, but also the most limited in it's
recovery.

1.c Mage is tricky, they are mostly involved in combat, but magic can also be used out of combat. I think their
identity is that mana is somewhat limited, and it has a price to it. Spells are worse than attacks when mana is not used
but when you start using mana they quickly go on par and surpass attacks. Mana is like a get what you want resource,
which costs money. It is power, but at a cost. Also they open up a whole fantasy element, as depending on which school
of magic someone chooses, they can use it in unique ways in the story. 

2. Each level up should feel exciting, and impactful, as you try to manage taking the necessary feats for your build,
improving defenses, upgraded proficiencies, or gaining more resources to be able to sustain more powerful actions.

3. Make only weapons and spells that are mechanically distinct. For spells there are vast scaling options, so it is
actually intended that you cast low level spells in higher level. For example there is only 1 healing spell for the
entire game. But since you can alter it, and ramp up it's power as you level up, that is actually enough. That means
less spells, but each spell is much more reusable in different builds and throughout your character progression. It
might be completely viable to pick up a first level spell at level 10 to upcast it to a version you actually intend to
use.


Let's talk about offensive and defensive scaling.

For all of those numbers I consider the Legendary variant.

Offenses:

Each power dice is roughly 1 to 1.5 damage with low dice numbers and can go up to 1.5 to 2 damage when you add fifth
and sixth power dice. So the early game per turn damage output is usually 3-4 for players. But can spike to more than
that.


Defenses:

HP, Defenses, Willpower, Reflex and Fortitude.

HP - Each dice you have represents a health pool of 2 + toughness. Maximum toughness is 4. So since you have 6 dice,
you have between 12 and 36 health points. In practice, taking any damage is detrimental, since you do lose a dice, 
I think losing up to 2 dice let's you still be in the fight, but once you lose your third one, you should really
consider fleeing or find a way to heal yourself.

Defense - This represents your posture, position, ability to block and parry. Whenever you get attacked you first negate
the damage using defense, but then that defense is lost. Losing defense does not lower your fighting capacity like
losing life does. In addition Defense is easily recoverable resource. You only need to take the recover defenses action,
which costs R2.R2. The efficiency of this depends on your maximum defense however, which depends on your armor, and
other defensive capabilities.

Reflex - When being hit by an AoE spell you can roll 2 additional dice and use your reflex proficiency to dodge it and
take half damage. In addition the same applies when you would take a stack of burning. Proficiency resets at the start
of your turn.

Willpower and fortitude - they can be used to remove disoriented and afraid (willpower), or poisoned and freezing status
effects (fortitude). These both use the dice in your dice pool.




Status effects

Pillars

1. Status effects are there to create a sense of dread and danger that is alternative to the out right damage and dying.

2. Have multiple levels for all status effects. that way you avoid the from 0 to full lock down immediately which will
feel bad. If the status effects take small but slowly increasing bites from players power, the urgency starts to build,
and it won't feel cheap.

3. Always have default things that players can do something about them. However it should be a choice of do you spend
some time in your turn or do you instead gamble and hope it won't be a problem.

4. They are there to add flavor and story to the fights. To really help bring the visuals to the imagination.

5. 2 routes, add small extra status effects on top of existing damage. Or focus heavily on the status effect meaning
that there should be fair chance for it to bring some tempo or control advantage significantly faster than just killing
the enemies out-right.

6. They must always answer the question: why not just deal more damage instead if that is an option?


Bonuses / Debuffs

Pillars

1. Have a fixed set of bonuses you can have that modify the outcome. You have proficiency, 
advantage / disadvantage, luck and inspiration.


Mana / magic

Spell slots is too long of a term. just use mana. The problem is, should we separate encounter mana, or daily mana?
Or how should mana be recovered?

Let spells be Over powered. And instead have have mana be a limited resource. Have normal mana recovery be even slower
than a day and instead have pricey food addons that boost the mana recovery for the long rest.

"""},
    ]