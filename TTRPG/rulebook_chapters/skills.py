from math import floor, ceil

from Skills import skills as skills_obj
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak

from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style


def prep_skill_flowable(skill):
    elements = []
    elements.append(Paragraph(skill['name'], style=minor_title))
    elements.append(Paragraph(skill['description'], style=basic_paragraph_style))
    elements.append(Paragraph('Group focuses:', style=minor_subtitle))
    pdf_list = []
    for list_ele in skill['group focuses']:
        pdf_list.append(ListItem(Paragraph(list_ele, style=option_style)))
    elements.append(ListFlowable(pdf_list, bulletType='bullet', start='*', leftPadding=20))
    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements

def get_skill_related_chapter():

    elements = [
        {'type': 'title', 'content': 'Skills'},
        {'type': 'paragraph',
         'content': """
The struggle I had is to think of Skilled path feats and abilities. The problem there is that, they are supposed to
be strong in the most creative part of the game, out of combat roleplay. The thing is, that part really should not be
constrained by making a finite set of feats or moves or what not as the vastness of play in TTRPG is impossible to
support with this approach.

What I want to achieve is players to both unleash their creative potential when creating characters, while at the same
time willingly limit what their characters can do, constrains are fun, as long as you have enough tools to figure out
a way.

So what I am leaning towards, is a creative way to say, that your character has a particular background, or a particular
set of skills, or knows how to do something very specific and unique.

So, in addition to basic skills like physique and leadership, there are limitless number of creative skills, which
players can gain proficiency in, and can also invoke in their adventures. But how to go about making these skills?

How to make sure they are balanced, both in the sense that they are not too obscure that never come up, and also that
it wouldn't cover pretty much every single situation?

For that there are some guide lines for how big of a scope could a such a skill have:

1. Each skill is related to a specific ability (see glossary). This also constrains the nature of the skill. For example
if your creative skill is working in a trading caravan. If the related ability is social, then you can use it to
negotiate or barter intensely. If however the related ability is intelligence, then perhaps you know all the trade 
routes and what kind of goods are moved around. If the related ability is cunning, then it could explain your ability
to spot ambushes, or spot scams, understand when some piece of item is fake etc.

2. It could be the core skill sets required for a profession, in this case, the skill set would be trading, blacksmith,
city guard etc. In this case you could use the proficiency of this skill set to do activities that these jobs would do
daily. You could try to invoke it with a dis-advantage for situations, which can come up during the line of work, but
are not the main activity. For example if you are a trader, you negotiate a lot, but that doesn't mean you know how to
negotiate with nobility, it also doesn't mean you could convince someone to aid you for no money. But you would be able
to buy anyone's services who is interested in money, and use your proficiency to barter the best price. As a blacksmith
you know how to forge weapons and armor, but couldn't craft leather, or you might be able to negotiate and barter your raw
resources and for the price of your own craft, but not other things. 

3. It is limited to a terrain type or certain cut of society. Like for example, you could be expert in the wild, but
you would be only expert in terrain familiar to you. For example, you could separate different major terrains as desert,
steppes, forests, mountains and sea. It can also be differentiated by the social class with whom you interact with:
nobles, religious, artisans, commoners, criminals. The exact relevant social classes may vary from culture to culture
and depend on the setting, and same with terrain, talk it through with the GM.

4. It is tied to a certain culture. For example, you have read a lot of books, but only from a certain culture. So you
can only know what that culture knows. You may know vaguely about heroes or happenings of other cultures, but even then 
you would only know about them from the perspective of that culture.

5. It is about specializing. For example, you are a sword blacksmith, you have studied all the swords from all around
the world, and can therefore make the best swords. Or you have specialized in a topic, such as warfare logistics, and
therefore you have read texts about it and know about from different cultures also from their persepctive. Or you could
be a magical spice merchant, so you would know where this is grown, where there is high demand, can tell the quality,
fakeness of the spice and so on and on. But by specializing you would limit yourself to not be able to do adjacent stuff
or have a significant disadvantage doing so.

General rule of thumb is that, each trait should consist of a profession / background / general character wibe, that
would allow it to be invoked in various situations, and at least 1 limitation (in addition to being constrained by an
ability), that would give it more character.

The limitation may make some things that the trait could otherwise allow to make it impossible, or make it so, that you
can attempt to do those things with disadvantage or severe disadvantage.

Examples of traits + limitation:


1. Trader (profession), limitation examples: spice merchant, deals with stolen goods in the underworld, has been leading 
caravans over desert.


2. Grew up helping his father hunt (back ground), limitation examples: In forest, In mountains, Specialized in traps.


3. Has read a lot of books and knows stuff, limitation examples: Books made by specific culture, Books about magic, Only 
the most obscure and rare books.


Also, when it comes to learning new skills during the campaign, it is also limited by the fact weather or not you can do
the activity. So you cannot all of a sudden become a trader while you do 0 trading during your journeys. You could
however read a whole bunch of books and become an theoretical expert of Dragons.

Each character starts the game with already 2 preexisting traits, And both of them have at least +1 proficiency, as
stated in creating your character chapter.
""",
# 'commented': """
#
# In addition if players want to pursue some specific goal or achieve something, either to learn about something, get an
# item, improve relations with a lord etc. they can start a group focus. Group focus consists of a goal, a progress
# tracked by GM, and fail conditions tracked by GM. When
#
# Party can have only 1 group focus active at a time, but Skilled path characters get access to a Planner feat, that let's
# them start another one. Even with the planner feats, the maximum number of group focuses is 3, and only 1 extra group
# focus can be initiated per player.
#
# Group focus progresses together with the main story line or whatever the players choose to do, and consists of skill checks
# after certain well signalled conditions have been met.
#
# Crtitical successes move the progress forward twice, while critical failures have some chance for negative consquences (GM discretion).
#
# The first check can be done when the goal is set.
#
# Using group focuses it is clear to the GMs what the players hope to get, and what they care about most,
# and at the same time lowers the amount of "let's try to squeeze lemonade out of anything".
#
# An example:
#
# Players' want to improve relations with the merchants in the town in order to get better prices when buying items.
# GM asks, how would they like to go about that, and how big of a discount are they aiming for. The players say 20 %.
# GM decides this should take some while and sets the requirement for this group focus to be 7 steps. The players think,
# that since they actually want to focus on the main quest, they could just try get along nicely with the merchants, maybe
# they could seek out some specific things during their travels?
#
# And so the GM decides that fine, they can make the first diplomacy check now as introduction. And each time when they
# return to town they can make another check if they spend at least a certain amount of gold in the market square. In
# addition he rolls some few random merchants, who do have some requests, so the players can look out for, certain herbs
# in the wilderness, or some venom from specific spiders, etc.
#
# So when questing in the wilderness, players get another gathering check to find the herbs. Or maybe they find  cave
# where those spiders could be and they have a fight encounter. All of these things give a diplomacy check opportunity and
# on a success or even better a critical success the thing progress. Eventually the wibe between the merchants and your
# group becomes so friendly, that they start giving you that 20 % discount. And maybe the herbalist who you supplied the
# herbs with gives you a even more special 35 % discount. When you choose to complete a quest for one of the merchants,
# you can also offer rewards for some of the steps in addition to progressing towards the longer goal.
# """
         },
    ]


    # for skill in skills_obj:
    #     elements.append({'type': 'flowables', 'content': prep_skill_flowable(skill)})

    return elements