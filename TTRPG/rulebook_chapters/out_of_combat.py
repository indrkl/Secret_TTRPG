from math import floor, ceil

def get_out_of_combat_chapter():

    return [
        {'type': 'title', 'content': 'Out of combat roleplaying / campaign pillars'},
        {'type': 'paragraph',
         'content': """
1. There has to be a chance for things to go wrong? To get partial successes, complications, or trying and then actually
failing and ending up in a dangerous situation because of it.

2. A simple way to abstract time passing. Time and pace are important for considering that the world around them also
changes. An idea is to separate into 3 different time categories. Smallest one is considered equivalent to tens of 
minutes. When in this time abstraction, GM only considers NPC actions in a very local
level. In the second category, each instance is around 6-10 hours. GM can consider NPC actions throughout the settlement
or in the wider vicinity in nature when it comes to whether or not they start interacting with the situation players are
part in. The largest time scale is long actions considered to be taking like a week or 2. These can be sailing to
some place far away, travelling some place far away on foot, smithing, really proper long rest, construction, building
defenses for an upcoming siege etc. etc. In this time scale the activities of all actors in the campaign are considered,
and they move forward in their strategic plans.

3. Interacting with the world, lore, and caring about the minute details of the world should be rewarded, role playing
should be rewarded.
"""},
        {'type': 'title', 'content': 'Running the game'},
        {'type': 'paragraph',
         'content': """
The general openness of role playing games apply here as well. Players can do anything in the game world, that makes
sense for GM and other players. In a way role playing is collaborative sense making. GM describes the environment,
how NPC-s react to PC-s, and answers various clarifying questions to the players. Players describe how their character
behaves, what is their intent with considered actions, and whether or not they do those considered actions.

When operating within the game world, players need to spend time and effort. Also, some actions may not be guaranteed,
in this case there needs to be a resolution mechanism. IN 6d6 we use again, our 6 d6s.

Resolution mechanism:


1. First the general idea of what players want to achieve and the time scale they want to operate in is agreed.
Everyone roll their 6 dice as usual.

2. Things that GM needs to resolve are:

 * Can an activity be done within the agreed upon time-scale.
 
    * If an activity can be done within a smaller time-scale, do we play it through or just assume that it succeeds to
    
    a result, which suits both players and GM
    
 * How much time and effort does an action / activity take? This is measured between 1 to 6 dice.
 
 * Is it possible to fail the action / activity. What would it look like? What would complications regarding the 
 activity look like.
 
    * If yes, then how difficult should the action /activity be.
    
    * Can there be complications?
    
    * Can there be boons as extra bonuses? Recommended to only consider these in special activities. Not all things
    need boons.
    
    
Skill check rules:


GM decides Effort E and how many dice he rolls to decide to determine the what result beats the challange. 

 * Difficulty is average, then the number of dice rolled is equal to E and challange is represented as E / E
 
 * Difficulty is above average then the number of dice rolled is larger than E, and the E largest results are chosen
 to become the challenge target. Challenge is represented as "E / D hard" where D is the number of dice.
 
 * Difficulty is below average, then the number of dice rolled is larger than E, but the lowest E results are chosen
 to become the challenge target. Challenge is represented as "E / D easy"
 
 
Example:

GM says that the challange is "3 / 5 hard". That means the attempting player has to present 3 dice, then GM throws
 5 dice and chooses 3 largest values, then they are compared with the player's dice and if all player dice are larger
 or equal to the challange dice, then it is a clean success. For each dice that the presented dice is only 1 lower than
 challange dice, there can be either 1 complication per such dice, or a one suitable bigger complication for all such
 dice, but otherwise the challange is still considered as success and players get what they want with a "BUT". In all
 other cases challange fails, and complications are handed out as appropriate.

Player interactions with the skill difficulty

 * Players can use their proficiency to nudge the presented dice to be higher than they are. Normal proficiency rules
 apply. Proficiency is used before comparing but after the presented dice and challange dice are decided.
 
 * Players can invoke some elements in the world, or by explaining why they should have an advantage, or roleplay, to nudge
 the difficulty by 1. Hard difficulties can be nudged multiple times, until they are average. Average and easy
 difficulties can be nudged once this way. For really hard difficulties, some roleplay aspect could nudge it more
 than 1 dice, for example when difficulty is "6 / 20 hard", then it could reduce it to 6 / 18 or 6 / 17 immideately.
 
 * Players can push the challange by spending dice to reduce the difficulty by 1. That does reduce the number of dice
 available for them for this campaign turn
 
 * Players may assist other players by spending dice to reduce the difficulty by 1. When assisting however, the assisted
 dice has to at least a 4. Assisting player can use their proficiency however to achieve that condition.
 
Terms:

 * Challange - an activity or action that players do in order to achieve a goal they set out.
 
 * Effort - number of dice needed to be presented for a challange
 
 * Difficulty - Represented either easy, average or hard and by the number of dice the GM throws.
 
 * Easy difficulty - GM throws more dice than effort E, and chooses the smallest results for challange dice.
 
 * Hard difficulty - GM throws more dice than effort E, and chooses the largest results for challange dice.
 
 * Presented dice - Effort number of dice that player presents, which are then checked against the challange dice to
 determine success, success with complications or failure.
 
 * Challange dice - The final Effort number of dice that GM rolls based on the difficulty.
 
 * Comparing - Each dice from presented dice is compared against the corresponding Challange dice. Highest dice from
 both sides are compared first, then second, third and so on.
 
 * Success - Each presented dice is equal to or higher to the compared challange dice.
 
 * Success with complications - Each presented dice is equal or higher than the compared challange dice minus one, and
 some of them are equal to challange dice minus one.
 
 * Failure - Some dice is smaller than challange dice minus 1.
 
 * Success with boon - Each presented dice is equal to or higher to the compared challange dice + 1, then it is
 considered success with a boon. Not all challanges can have a boon. But for those that do, proficiency can be used
 to increase the presented dice to 7 if necessary.
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