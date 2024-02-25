from math import floor, ceil

def get_out_of_combat_chapter():

    return [
        {'type': 'title', 'content': 'Running the game out of combat'},
        {'type': 'paragraph',
         'content': """
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
interrogation. You get to pose a yes no question and receive an
answer of yes, no, maybe, uncertain. In case of yes, GM may comment further. This requires 1 dice, but may be used 
multiple times during scene. The answer still depends on what is possible for you to find in this scene.



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

"""},
    ]