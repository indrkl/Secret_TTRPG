"""
It is recommended for groups to really decide what kind of campaign they want to have at session 0. It is also a good
idea to have a common origin, or some relations between the players to really give meaning to the role playing.

To help accomodate that, and also to help new players not avoid these lessons I want to have group types. Players decide
what kind of group they are, what kind of organization are they apart of. That also dictates the kind of adventures they
want to go to, what kind of things they want to pay attention to, and give a reason to already start the campaign
together.

When party gains experience, then the organization gains experience at 2/3 that rate. What does it do? Firstly when
one of the player characters retire or dies, and they roll a new character, that character starts with the organization's
experience points. Also, players who miss sessions can never be below the organizations experience level.

Secondly the organization also gains levels and earns advancement points, which can be used to give boosts to the
organization depending on its type. This is to really emphasise on the nature of what kind of group you are and what
kind of organization are you part of, so the party gets more invested in it, and their group effort.
"""


types = {
    'adventurers': """
The basic type, party has no specific goals, they just want to adventure and have fun, that means they don't have a base
of operations nor any specific goals. The reason why they are adventuring together is because they are simply friends,
who picked each other up along the way.

This is a vanilla choice, and players may choose to change to a different organization type during the campaign.

Group goals ideas (to earn exp):

1. Finish a quest.

2. Find loot in a dungeon or adventure.

3. Roleplay a jolly moment.
    """,
    'merchant caravan': """
Players are focused on being a merchant caravan which moves from town to town, they may get involved with various
adventures along the way, or they may be the scouts of the caravan, or the rebellious kids, who go out and get
themselves into all sorts of trouble. The point is, there is a caravan, which moves from place to place, and players
are somewhat attached to it. Also they will be involved in trading and hope to make an extra profit along the way.
Though keep in mind, that trade is not just profits, it is also risk, maintenance for all the other people in the
caravan, and all sorts of other costs.

Group goals ideas (to earn exp):

1. Earn profit in a trade

2. Roleplay a shrewd bargaining.

3. 
    """,
    'Scoundrels': """
A criminal gang, looking for loot and trouble. They may have a base of operation, or be part of a thieves guild, which
has a network of hideouts in various cities. They go on heists, or do assassination operations, or pick up some other
dubious tasks, but who knows, maybe they stumble upon something, that starts invoking even their morals which they
thought they didn't have.

Group goals ideas (to earn exp):

1. Complete a heist

2. Complete a complete encounter without being detected
    """,
    'Group of scholars': """
You are part of the old secret organization of scholars, which waned away a time ago, your generation has however
rediscovered your heritage. All party members are descendants of the same group of scholars, they have a secret hideout,
perhaps it has some magical properties, that it can portal to multiple cities, or that during the campaign you unlock
the portals from the hideout, as they all start dormant. Your party is obviously interested in gathering lore, knowledge
and learn about the game world more than on average, and rely on magic and secrets to get by and are materialistic
perhaps less ambitious.

What are the secrets your organization was guarding?

Did your organization have a secret purpose?

The assumption is that players who choose this group type are interested in world lore, story plot and want a game of
more mystery. Lore becomes the signature skill for these players. So the progression of the organization should
represent rebuilding the hideout, gathering knowledge, books, maybe get some wise old man to join your efforts.

How to get advancement points? Each level up grants 3 advancemnt points. In addition there are certain key lore
questions, for which to find an answer is a long process, and each time they find the answer to one of them, then they
get 1 additional advancement point for current and future levels. Each next question needs to be more signifant than
the previous.

What can you get for advancement points? Abilities?

You can rebuild the hideout of the secret organization with special rooms that grant boosts to the party. The maximum
level of each room is 5.

Rebuild library: first costs 1 advancement point. Increment future costs by 1. Improve library level by 1. Whenever
a player gains a lore token about a topic they can roll a d6. If the result is smaller or equal to library level they
gain an additional lore token, that they can use when they eventually get back to their central hideout.

Rebuild laboratory: First costs 1 advancement point. Increment future costs by. Improve laboratory level by 1. Potions
cost 10 % less per level. If a character hsa potion maker feat, then these too stack multiplicative.
So the maximum cost reduction is 75 %.

Rebuild medicine room: First costs 1 advancement point. Increment future costs by. Improve medicine room level by 1.
Recovering players from scarred dice costs 10 % less per level and recovery takes 10 % less time.

Group goals ideas (to earn exp):



    """,
    'A noble house': """
Players are part of a single noble house, which has been in decline for centuries, you still have an estate in poor
condition, and there are other noble houses hoping to get rid of you for once and for all. This is when players want
to choose a campaign, which in addition includes politics and intrigue. Here you will need to manage your reputation,
as you are still a noble house, you have the opportunity to gain in your reputation much faster than a commoner, but
when you lose it, then it's the end of your house. You could be punished by the king, you could lose your lands, by
outcast, after which you could simply continue the campaign as adventurers?


    """,
    'Holy order': """
Your players are part of the holy order and on a quest. Various churches and cathedrals can easily serve as your groups
hideouts or stopping places. You don't care for material things like gold, but instead you follow some greater purpose,
ideals, or a goal.

What is your mission?

What kind of holy order is it?

What are it's secrets?

What are you protecting the world from?
    """,
    'Cult': """
Players have started a small cult, they are the founders, and start out with a few followers already, they seek to say
secretive, mysterious and have some kind of slightly ominous agenda, or perhaps they just want to have a massive 
followers to satisfy the egos of the founders.

What are your goals?

How do you recruit?

What do you do with the followers?
    """,
    'Mercenaries': """
You are band of soldiers, fighters, perhaps mages for hire. You do tasks, for gold. You go where the gold takes you. It
is very simple life style. The player with the highest leadership is the leader of the bunch and the second highest
is the first lieutenant.

Special rules for the mercenary band is that you can find recruits. But beware, they cost money. Similarly to enemy mobs
your company members can either be pawns, knights, rooks or bishops. As the party gains more experience, so does your
ability to manage your mercenary band and upgrade your troops.

At start you can manage up to 4 troops in addition to your party and can only recruit pawns. From group level 4 onwards
you can start recruiting other troop types as well. Before that some of the pawns may still be upgraded through battle.

You get one upgrade when a battle was harrying (25 % of total hit pools was damaged), and 2 if it was against odds (50%
of total hit pools was damaged) (The total is based on troops hit points, and not player hit points, some are likely to
die due to that). 

Starting statistics of the troops:

Pawns - 3 HP+DEF, 2 ATK, 4 MV, 2 gold per day

Knight - 4 HP+DEF, 3 ATK, 8 MV, 5 gold per day

Rook - 6 HP+DEF, 3 ATK, 4 MV, 5 gold per day

Bishop - 3 HP+DEF, 3 ATK (RNG 5), 5 MV, 4 gold per day

All salaries are 20 x on a day with battle that is equal or dangerous, and 5 x on a day with a battle which was safe or
easy.

Over time you can upgrade all 3 of those factors. In addition knights, rooks and bishops can be specialised with special
abilities, which can be discussed with GM. But examples of what enemies have gotten, is poison blades for knights,
taunt ability for rooks, turn Bishops into a single spell casters. It is important to always keep the theme of those
soldiers.

When mercenary company gains a level up, then a strategy scene is played out in where the party decides the direction of
the company, training plans and so on. In the scene the captain and first lietenant get a X R3 leadership roll target,
where for every dice they can provide, organization gets one advancement point.

Advancement points can be spent following ways:

Increas HP+DEF by 1 for all troops: starts at 2 points, and increments by 1 each time it is picked.
Increas ATK by 1 for all troops: starts at 5 points, and increments by 2 each time it is picked.
Increas MV by 1 for all pawns, rooks and pishops and by 2 for knights: starts at 3 points, and increments by 3 each time 
it is picked.

Special rule: Every 15 points spent on these 3 traits (Increase HP+DEF/ATK/MV) increases the daily salary by 1 for all 
troops.

Increases maximum number of troops: starts at 1 points, and increments by 1 every other time to a maximum of 3.

Troop special abilities:

Taunt for rooks: Costs 5 points, rooks can take the taunt action, which can be broken by attacking them, if someone does
they retaliate with their attack damage. Until noone attacks them, then attacks against allies within 2 sq. of them have
disadvantage. Rooks also get +2 HP+DEF. Increase their daily salary by 2. 


    """,

}