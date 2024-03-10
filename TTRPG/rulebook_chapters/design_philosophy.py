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


Balancing

The core of the gameplay is to get as many dice of the desired number to get to do what you want in a spectacular
manner. How to think of that?
So there is a near 100 % chance for any pair when you roll dice. There is around 37 % chance for a triple. That is the
base line. For a specific pair however it is 25 and 6 % respectively.

However if you only care about a specific number and how many dice you get of that number with a roll, then the base
line is actually 1 dice on average. 

Let's consider all of these as a way to get dice and let's see how effective they are:

1. proficiency - Biggest increase is from 0 to 1, which is in most cases almost 1. From then on it goes to 0.7, 0.5, 0.4
But for 1 and 6, it is actually even worse: 0.7, 0.5, 0.4, 0.3. Proficiency is target number dependent.

2. luck tokens - This increases it always by 1. So using a luck token is as good as going from 0 to 1 proficiency or 2
to 4 proficiency. It is also much better for 1 and 6 number targets.

3. additional dice - This is surprisingly ineffective, it does increase your action economy though, but for increasing
your most powerful move, it is effectively around 0.1-0.2 per dice with no proficiency and goes up to 0.3-0.4 at high
proficiencies. Surprisingly doesn't matter weather the target number is 1 or a 2

4. having two valid options instead of 1 - surprisingly a measly 0.5-0.7 dice only.

5. being happy with an easier roll - With no proficiency doesn't matter, but with proficiency it can go up to 0.6 and if
you combine it with having two valid options it can be a whopping 1.

6. Advantage is a simple 1, getting advantage for multiple things is 1 each time, so that's kinda powerful.

Risk dice are interesting however:

If we need to increase the number of dice by 1, then our odds are following:
Using 1 dice for target number 1 the odds are 0.33
Using 2 dice for target number 1 the odds are 0.22
Using 3 dice for target number 1 the odds are 0.29
Using 1 dice for target number 2 the odds are 0.50
Using 2 dice for target number 2 the odds are 0.42
Using 3 dice for target number 2 the odds are 0.54
Using 1 dice for target number 3 the odds are 0.50
Using 2 dice for target number 3 the odds are 0.58
Using 3 dice for target number 3 the odds are 0.67

If we need to increase the number of dice by 2, then our odds are following:

Using 1 dice for target number 1 the odds are 0.00
Using 2 dice for target number 1 the odds are 0.11
Using 3 dice for target number 1 the odds are 0.09
Using 1 dice for target number 2 the odds are 0.00
Using 2 dice for target number 2 the odds are 0.25
Using 3 dice for target number 2 the odds are 0.25
Using 1 dice for target number 3 the odds are 0.00
Using 2 dice for target number 3 the odds are 0.25
Using 3 dice for target number 3 the odds are 0.38

That means that for simpler targets the odds of the risk paying off is significant, up to 67 % for 1 dice, and if you
need 2 dice, it can still be 1 in 4 or up to 38 %!! Which is significant boost.

What do we all learn here? By diversifing, being less picky, having 1 proficiency we easily hit the 2.5 - 3.5 mark.
This is significant. With 4 proficiency and applying the same things we are 4.5 - 5.5 range.

If you have luck and advantage, then even tasks which require 6 or 7 dice are plausible. And then when you need to
push your luck, then we are talking about 8-9 dice as being the hardest of challanges which are still doable. Of course
when you add more dice, then it goes up to something like 10.

So a godly challange is 10, while things that should not be taken for granted can be around 6-7. 3 for baseline makes
sense, and increasing it to 4 or 5 relatively early on for tougher challanges is actually quite fair.



"""},

    ]