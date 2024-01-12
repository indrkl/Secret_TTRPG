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
clear value reliably.

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

1. Your accuracy mainly improves with your proficiency in that weapon. From lvl. 1 to 10 it can scale from +4 to +11.
In addition you can get various bonuses from feats. I'm considering, is that too much? Once the bonuses increase above
average AC-s, you will start to hit every hit, except for nat 1s. And your crit chance will easily go above 50 %. That
may be too much.

2. Your damage. 3 attacks per round, with basic attacks and 2 handed weapons can be like 9d6 damage, this is 30 damage.
Of course hitting is not guaranteed, but critical hits are also a possibility. The first 2 STA should increase the 
number of average attacks by 1 per AP. For a third effective attack, it should be 3 STA. Also both increases all future
attack STA costs by 1 or 2 respectively. Or if you did a 2 AP attack, then even 2-5.
So 3 regular attacks consumes 3 STA.
3 double strikes consumes 3 + 4 + 5 STA = 12 STA. That requires 4 levels investment in stamina to sustain, but increases
your damage output from 30 to 60. This can be expected by level 6-7 earliest for Legendary martial builds, or earlier
with some support or when dealing with barbarian. However if they intent to invest in some defenses as well, then it may
be viable to do more like 1 + 3 + 4 = 8 STA spenditure for 5 attacks instead of 6, which already saves 3 whole levels.



Defenses:

HP
So players start with 36 HP + 3 per level in martial. SO full martials start with 48 HP. Each additional level gives
another 12 - 16 hp.

Against attacks:
1. AC - armor class, you gain that from armor that you are wearing, and from your martial class. Your base AC is 10.
If we consider that light armor provides from 2-3 AC, medium armor from 4-5, and heavy armor from 6-8 AC, that means
most tanky characters can get up to 26 AC. Also, why would anyone ever wear not heavy armor, or how could medium armor
be viable? To overcome STA penalty you need to invest 12 points to STA regen to make up for it. That is actually a lot.
Or 6 points if you are raging. That is 3 levels to be as effective offensively as someone in light armor, or 1 and half 
levels to be as effective as someone in light armor. So to actually get all out of heavy armor you need to invest 
6 legendary levels in martial. That is fucking lot. And for that you get 26 AC. Based on that I don't think attack 
bonuses above +16 make much sense. I lowered it slightly. It goes to +14 instead of previous +18.
Still, consider that if you use a shield, and you use the raise shield action then you can get an additional +3 +3
though that requires another 1 level of investment, though your STA demand by using a shield probably reduces, so maybe
that is not entirely fair comparison. Medium armor goes about to AC 20 and light armor will get fucked and go only up to
16. They also require the least investment.
2. Dodge - So if you are wearing light armor, or no armor, you get access to dodge. This is a series of feats, which
get progressively more expensive. Basic dodging, Skilled dodging, Extreme dodging and Legendary dodger. Each feat grants
you dodge points, and they cost a total of 10 points, which is still 2 and half levels. Dodge tokens can be used to
completely negate an attack and move 2 m. in any direction. To negate a critical strike you need to spend 2 dodge 
tokens. By spending 3 AP you can recover all your dodge tokens, that action also doubles your STA recover for that turn.
 To use each dodge token does require 2 STA. Dodging doesn't cost reactions, but since you eventually run out of dodge
tokens, then you will be fucked if you get overwhelmed by multiple enemies.
3. So light armor has their strength, heavy armor has their strength. What is the strength of medium armor? You still
get some STA penalty which you need to overcome, and to max out in medium armor you need to spend 6 points on STA 
recovery, 6 on AC. and almost entire level on the feat, that is still 3.75 levels, compared to the 6.25 for heavy armor.
Well for heavy armor it actually is more like 7, because you also need to increase MAX STA. You get a solid +20 AC
Here's what we do. Since light armor gets dodge, medium armor loses the +1 STA cost per attack and that cost is moved to
the lack of proficiency penalty. And the AC penalty is lowered to -1 for the lack of proficiency penalty.

Against AoE attacks and spells (Reflex). However this is mostly against damage and avoiding being knocked prone. You
can also counteract it by having high HP pool. Also heavy armor has a chance to not gain unbalanced levels. 

Against Status effects (Will and Fortitude)

There is a major problem with those. You only need to bi-line in one offensive capability. But to defend against all 
potential offenses, you need to invest into multiple areas. One way to balance for that is to give defenses an edge
in their maximum potential, meaning you would also need to invest into multiple offensive options in order to make use
of weaknesses in defense.


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

1. Have a fixed set of bonuses you can have that change the hit and success chances. You have proficiency, 
advantage / disadvantage, luck to improve the dice odds, but it doesn't improve the maximum potential, inspiration,
and one magical bonus.

2. For armor you have Armor bonus, shield bonus and magical bonus. Proficiency cannot go higher than those.


Mana / magic

mana is too long of a term. just use mana. The problem is, should we separate encounter mana, or daily mana?
Or how should mana be recovered?

Let spells be Over powered. And instead have have mana be a limited resource. Have normal mana recovery be even slower
than a day and instead have pricey food addons that boost the mana recovery for the long rest.

Combat casting is achieved with reducing the mana cost of spells allowing for more powerful spells to be cast for free.

"""},
    ]