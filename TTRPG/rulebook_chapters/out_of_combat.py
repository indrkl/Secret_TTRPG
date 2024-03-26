from math import floor, ceil

def get_out_of_combat_chapter():

    return [
        {'type': 'title', 'content': 'Running the game out of combat'},
        {'type': 'paragraph',
         'content': """
The game out of combat is divided into campaign turns, the exact time frame of the campaign turn is agreed between the
GM and players. Each campaign turn starts with all players rolling their dice pool. That becomes the main resource to do
anything during that turn.

During campaign turns players get to roleplay, GM gets to describe the scene and what is happening. 
When players want to do something none-trivial, which either is time-consuming or even challenging then they need to use 
dice from their dice pool. If the nature of the activity is none-challanging but still time consuming, they need to 
spend any of the dice to do the activity in the sense that each dice represents a junk of time that they spend on the
activity during the scene. If the success of the activity is however not certain, then a target number between 1 and 6
is decided, and the player needs to muster that many dice with the given number. They can of course use their skill
proficiency to nudge dice, they may get assisted by their allies, they may try to roleplay in order to get an advantage,
and finally there is an option to use up to 3 of your dice to get risk dice, which can end up pushing you right past the
success (more on them later).

How do risk dice work? In order to get 1 risk die, you need to spend any die from your pool. You first choose between
how many risk dice you get (max 3), spend that many normal dice from your pool, then roll the risk dice. For each
result that is +-1 from the target number you get 1 success. Results that are within 2 away from the target number do
nothing and results that are 3 or more away from the target number do not harm the current task, but do create
complications for the future.

How to determine the target number? Just roll a 1d6 and the result determines the target number.

With regards to choosing the number of dice (challange difficulty), that is required for some action, then this is done 
solely by the GM and it follows the following logic:

1. The base-line is 3 dice unless specified otherwise.

2. The challenge can have various aspects, which make this more difficult, such as when intimidating someone, they can
be prideful, when crafting something, you are missing proper tools or a roof and it is windy. When negotiating with
someone but you don't speak their language and so on. Each aspect can have a severity ranging from 1 to 3. It is 
recommended to usually leave it to 1, but in some cases it can be increased higher. Each lvl of severity adds 1 dice
to the challenge.

3. Some aspects can be allowed to be tackled separately. For example another action might be precisely with regards to
removing an aspect from your ally. For example to shelter a friend, so that they can craft in peace not worrying about
the elements.

4. Some challanges can be tackeled by more than one person, like constructing a shelter, setting up camp, cross a river,
these are more difficult challanges, which may require 5, 6 or even more dice in total. In this case one of the players
must take the lead in the activity, they get to use their dice with 100 % efficiency. In addition the one who takes the
lead in these challanges can use their leadership proficiency instead of the challange's skill proficiency if that is
better. Other players need to first pay 1 dice of the target number to start contributing, but all the dice afterwards
contribute with 100 % efficiency. Players may choose to not participate in some particular group effort.
         
Players may aid each other. When aiding a player may provide 1 dice of the target number (can nudge using their
proficiency) to provide an additional nudge for the player doing the action. A player cannot be aided more times this
way than their own proficiency (so basically the number of nudges can in maximum double).

When either the scope of the campaign turn ends, or players all have spent their resources, then we can start a new
campaign turn. Either way the world also progresses, and even if the scene in it's core is the same, this is the time
for the GM to introduce new variable, maybe a new NPC, or to move the plot forward in some way.

One suggested way to really represent the world progressing or the the resources to matter, is for the GM to also
draw cards from a stacked deck of normal cards at the beginning of each campaign turn, which they can use to boost 
encounters, create complications etc. 
In addition, the complications attained by the risk dice can also be represented by additional cards during the next
turn. The exact usage of those cards should still be done in a role gamey wibe, but this is more to remind the GM, that
now is fair game to ramp up the difficulty and create some tension. You could stack the deck with 1 (ace), 2, 3 and 4-s 
mostly, with fewer 5 and maybe a single, 6, 7 or 8 for group challanges. 
"""},
    ]

alternative_idea = """

So instead of having all the different options to use the dice for, we have moves, similar to spells for the mage path
but instead there are moves, each move being associated with a skill, each moving having a wide range of creative
applications, they are thematically sensible, in the sense that these are things that are realistic and happen in the
real world, and they still carry the underlying philosophy of each skill doing concrete thing, diplomacy alters
behaviour of NPC-s, lore reveals knowledge about the game-world, crafting creates objects to aid you on your journey
and so on.

Each time you take a proficiency upgrade you also get a move associated with that proficiency. Moves are things like:

For diplomacy:

Build a polite and elegant argumentation for your case.

Intimidate someone to do your bidding using threats.

Taunt someone to attack you, gaining disadvantage when attacking others.

Approach someone with a very friendly way, making them feel warmly towards your goals.

So basically all the options are taken apart and made into moves, as you build your character you add more moves, and
similar to spells you can also take additional moves for advancement points.

Now moves explain the part of players and their proactivity. But GM also may want to push obstacles of things that
hinder players, threaten or what not. This can actually be easily tied to campaign turns. 

Firstly when GM wants to create a threat or obstacle, they simply introduce it to the scene at any time, then he
provides the difficulty and target number picking the target number using the same already provided theme. And finally
he needs to think what happens on failure and success, both of them needs to be interesting.

In addition, to make the GM-s job easier GM simply needs to draw from a deck of cards, where the numbers on the card
dictate the difficulty. And so during the campaign turn, GM should find a use for these cards and create an obstacle to
really match the card that was drawn. This helps dictate the tempo of the game.

"""

old = """



The game out of combat is divided into campaign turns. During campaign turns players get to roleplay, GM gets to
describe the scene and what is happening. When players want to do something none-trivial, which either is time-consuming
or even challenging then they need to use dice from their dice pool, which they can nudge using the proficiency of the
challenge. The dice target is chosen by the player who attempts to do that action, but it must fit the characteristics
of that dice number (more on that later), but the challenge difficulty is determined by the GM. Then through role playing
of doing this action, players may gain either advantage, when their role playing makes sense for the situation, or earn
risk dice (they can choose from 1 to 3 risk dice) to determine weather or not it helps them or hinders them (more on
them later).

Each campaign turn starts with all players rolling their dice pool. That becomes the main resource to do
anything during that turn. 

As players want to do something, which success is not obvious, then the target number, proficiency and difficulty needs
to be agreed with the GM.

How to decide the roll target? There are 2 dimensions to it. First is the target number, ranging from 1 to 6 and second
is the difficulty, the number of dice of the target number required to succeed and get a result that is desired.

The target number should be proposed by the player and GM will simply need to validate that it makes sense considering
the following rules:

How to decide the target number?
 
In general lower numbers represent calm, intelligence, slowness, friendliness while higher numbers represent speed,
aggression, loudness, hostility, energeticness. In addition 1 and 6 are reserved for complicated and harder challanges,
1 is like a 2 or 3, but stronger, and 6 is like a 4 or 5, but stronger.

But here are more concrete ways to approach some of the skills:


For lore:

1 - getting knowledge from books or friendly and cooperative NPC-s. You get to pose a question, the question difficulty
may vary, base-line is 3. The answer still depends on the available books and NPC-s and what they know.

2 - getting knowledge from books or friendly and cooperative NPC-s. You get to pose a question, but instead of actual
answer, you get a hint, this requires 2 dice, but may be used multiple times during scene. The answer still depends on 
the available books and NPC-s and what they know.

3 - getting knowledge from books or friendly and cooperative NPC-s. You get to pose a yes no question and receive an
answer of yes, no, maybe, uncertain. In case of yes, GM may comment further. This requires 1 dice, but may be used 
multiple times during scene. The answer still depends on the available books and NPC-s and what they know.

4 - Getting knowledge from active investigation, searching of the room, observation of those around you, intense
interrogation. You get to pose a yes no question and receive an
answer of yes, no, maybe, uncertain. In case of yes, GM may comment further. This requires 1 dice, but may be used 
multiple times during scene. The answer still depends on what is possible for you to find in this scene.

5 - Getting knowledge from active investigation, searching of the room, observation of those around you, intense
interrogation. You get to pose a question, but instead of actual
answer, you get a hint, this requires 2 dice, but may be used multiple times during scene. The answer still depends on 
what is possible for you to find in this scene.

6 - Getting knowledge from active investigation, searching of the room, observation of those around you, intense
interrogation. You get to pose a question, the question difficulty
may vary, base-line is 3. The answer still depends on what is possible for you to find in this scene.



For diplomacy:

1 - To make an elegant and polite attempt at persuasion with coherent thoughts and a clear vision for mutual 
benefits.

2 - A polite and friendly persuasion which keeps within the boundaries of personal space.

3 - Overly friendly attempt to persuade someone. It can backfire if the friendship is not reciprocated.

4 - A lousy intimidation, but good enough against cowards.

5 - A stronger intimidation, might work as long as your demands are not too big, or they are cowards

6 - To make a really strong intimidation.



For crafting:

1 - You are crafting something which requires create detail and care. It assumes you have time enough to finish it. 
Item will have 1 boon

2 - You are crafting something without hurry, relaxed. The quality will be ok on success.

3 - You are crafting something without hurry, relaxed, but it will have 1 flaw

4 - You craft something much faster than usually, but it will have 2 flaws

5 - You craft something much faster than usually, but it will have 1 flaw

6 - You craft something much faster than usually, without the quality suffering



Survival is always 5 or 6 when dealing with active threats like hostile enemies, natural disasters, the situation is
at hand. It is 1 or 2 when preparing for threats in the future, it is regard planning for example going to extreme
environments, like mountain climbing, just generally very cold or very hot weather, or to forest with poisonous fauna,
or dangerous animals. Choosing 1 or 6 and succeeding will grant you a positive aspect regarding the challenge.



For physique skill, 1 represents something which requires intense accuracy and control, while 6 represents something
that requires great effort and strength. 2 and 3 suffer some sort of negative aspect when succeeding, or can be used for
things which require some accuracy and control but are easier and don't require effort or strength. And 4 and 5 relate
similarly to 6.



For harvesting, 1 represents gathering rare things, and 6 represents gathering a lot of things. Those inbetween are
half-assed versions of either 1 or 6.


With regards to choosing the number of dice, that is required for some action, then this is done solely by the GM and
it follows the following logic:

1. The base-line is 3 dice unless specified otherwise.

2. The challenge can have various aspects, which make this more difficult, such as when intimidating someone, they can
be prideful, when crafting something, you are missing proper tools or a roof and it is windy. When negotiating with
someone but you don't speak their language and so on. Each aspect can have a severity ranging from 1 to 3. It is 
recommended to usually leave it to 1, but in some cases it can be increased higher. Each lvl of severity adds 1 dice
to the challenge.

3. Some aspects can be allowed to be tackled separately. For example another action might be precisely with regards to
removing an aspect from your ally. For example to shelter a friend, so that they can craft in peace not worrying about
the elements.

Players may aid each other. When aiding a player may provide 1 dice of the target number (can nudge using their
proficiency) to provide an additional nudge for the player doing the action. A player cannot be aided more times this
way than their own proficiency (so basically the number of nudges can in maximum double).

It is possible that some tasks are simply time consuming and not challenging, in this case GM can allow players to give
up any X dice and they succeed automatically in this action. This still limits the number of things that player can do
during the campaign turn while not creating unnecessary and boring hindrances.

When casting spells during the campaign, then mana may be used, but they require
3 times more mana to get the desired benefits (more virtual dice of the right number essentially).

Finally the risk dice: when player earns risk dice through role playing, then they can choose between 1 to 3 d6. They
roll them, for each dice that rolls within 1 range from the number target, the challenge becomes easier by 1 dice 
and for each die that rolled further than 2 range from the number target, challenge becomes more difficult by 1 dice. 
For example, if the number target is 6, you need 3 dice, but only had 2, but now you rolled 3 risk dice.
Then each of them, that rolls 5 or 6 helps you succeed, and each of them that rolls 3, 2 or 1 brings you closer to fail.
Result of 4 would do nothing. Suppose you rolled 5, 6 and 3. Then you get 2 successes and 1 fail, so the challenge
becomes easier and you only needed 2 dice, which you have and you succeed. Note that risk dice are on average a lot 
favorable when the number target is 3 or 4, somewhat favorable when number target is 2 or 5 and 
unfavorable to you if the dice target is 1 or 6.

When either the scope of the campaign turn ends, or players all have spent their resources, then we can start a new
campaign world. Either way the world also progresses, and even if the scene in it's core is the same, this is the time
for the GM to introduce new variable, maybe a new NPC, or to move the plot forward in some way.

"""