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
Skills

While playing during campaign turns, players may come to various challanges, and for all of them, there is at least
1 skill, which proficiency they can use to complete that challange, which is provided by the GM. Players
of course may try to convince the GM why they could also use another skill, or perhaps a creative spell from the school
of magic, or just one of the school of magic's proficiency instead, but at least one skill has to be first provided by 
GM.

Skills in this game are much more broad than in DnD or many other TTRPG-s. They are derived from asking the question,
what do players want to do, or what motivates them?

They want to learn about the game world, uncover secrets, solve mysteries? This is lore. They want to influence other
NPC-s to do something they wouldn't otherwise do? diplomacy, they want to survive or give themselves an edge to survive?
Survival. Hide information, scheme, plot? concealment. Be the party leader or a beacon of hope in general? leadership.

Each skill represents motivation and drive.
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


    for skill in skills_obj:
        elements.append({'type': 'flowables', 'content': prep_skill_flowable(skill)})

    return elements