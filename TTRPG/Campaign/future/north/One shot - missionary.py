text = """
You live in the continent of Crescent. It is shaped like a waxing crescent moon phase, which has an ocean between it's shores
and outside of them. The eastern area is filled with a vast mountain range, while the northern areas are mostly cold
tundra, the southern areas split between a wild jungle, wilder plains and a state by a giant river ruled by a God King.

Between the center part of the mountains and the western shores is the middle empire, most progressed empire, that is
where you are from. In addition the empire controls many cities in the shores of various places, but none yet in the
inlands of the plains, jungles or tundra.

You are members of the church of Progress, it's symbol is the wheel and sails. You originate from the central empire, 
but have been
sent to a missionary mission to the tundras in the north. The north is a poor land, inhabited by shamanistic tribes,
the truth is that the central empire has little interest in the north, and most of the missionary expeditions have
little results, or at least they didn't gather much attention. You have been sent there because you have wronged
someone, perhaps annoyed someone, but not to the extent that you could be commited to prison or executed. You were sent
there, to get you out of sight, out of the way. What was it?

Remember, just because you are clergy, doesn't mean you actually are good at prophesizing, you can still be good at
magic, practice fighting, in fact, since you were sent to the north you are very likely not good a prophesizing, even
though your official mission is to spread the gospel of progress in a small village called Yorg in the middle of 
nowhere.

Think:

Why are you part of the church of progress, did you join voluntarily? Where you naive, coerced, fanatical, you had debt
and the church paid the debt for your service?

What did you do wrong to be sent to the north on a pointless mission? 
"""

Scenes = [
"""

Intro:

(Explain the reasons why each of you were sent to the north).

So now you have been sent to the norther lands of Tundra to do "missionary" work in the small village of Yorg. The
voyage starts from the harbor city Tresburg, where your church community resides. You travel by ship to one of the few
small trade hubs, Raxarc, controlled by the central empire, that reside by the inward northern shores.

Before we continue with this however we do a quick flash back of how you prepped for this expedition.
""",
    """
Prep scene: 

1. Sink - Lore - to learn about the north in more details from books: 

2. Normal - Diplomacy 2 - get help from brother Geoffrey: He is a hiker and knows about surviving in the north. Gives you
tips and tricks for survival and makes sure you have some warm furs with you. That does set you back a lot of money
though.

3. Normal - Diplomacy 3 - get help from brother Brian: He is a theorist and knows about the local customs, his tips
gives you a "Know northern customs" aspect which makes simple diplomacy scenes easier by lowering the difficulty by 1
dice. He also mentsions to make sure to have some nice gifts, and first impression is very important!

4. Normal - Diplomacy 4 - get help from brother Henry: He is a grumpy old guy. Once you get him to talk to you, he
reveals that the mission is a bust, but if you ever want to return with something of use, then figure out where they
grow the spice in their lands. It is believed that they have small deposits not worth bothering much, but that does
not add up with some of the records about the shamanistic rituals that they have performed in the past, so he believes
that if you find a big enough magic spice source, then you could actually progress your careers instead of wasting it.

5. Scaling - Survival 2/3/4 - prepare yourself to survive in the north. Get 1 / 2 / 3 times during the expedition an
advantage to some aspect of survival in the north, weather it be cold, wild-life, getting food, etc. 

    """,
"""
Prep scene 2:

Now that you have finished preparations, let's skip slightly closer to present. The voyage took several weeks, the ship,
that carried you, a small trade ship bringing metal tools and ready made clothes to Raxarc. The
crew is around a dozen men strong, you are the guests. As monks of the holy order, you are left alone, but deep down
they know, you are almost as if exiled from the civilization, the looks and glimpses betray men, wondering, what is
wrong with you, ignorant judgement of men who think they know more than they do. Today, you have spent 7 hours in
silence, but soon, one of you will finally break it, by starting a discussion about what do you expect from the north,
what do you plan to do, how is your attitude towards missionary work, your whole situation, 
and what kind of rumors have you heard while on boat from the crew, who knows, perhaps some of them are true? 
Now, break the silence.

""",
"""
Starting scene 3:

You land in Raxarc, this is a really small village, it has a warehouse, a dock, an inn and a few dozen of houses.

You meet Roy, the local innkeeper, who supplies you with a wagon and 2 Beefalos to carry the wagon with you and your
burdens. These beasts move slowly, around the pace of your walking speed. The journey to Yorg is 2 weeks long. Do you
want to do anything before you head out? 
""",
    """
Meeting villagers:

To get help from the villagers, or to achieve some goal regarding them, we can agree for a roll target, which is 
probably a hard diplomacy check. However, we can generate aspects and there are several opportunities.

First introduction, do you know their language? Roleplay can give you advantage. How it goes, depends on players.
Did you bring gifts? Maybe you do a small or quite a large favor for them. 

    """,
]

ideas = [
    """A squirrel druidess may join the party to spy their purpose when they feed her.""",
    """The cart is pulled by super furry beefalo like creatures. They are actually quite warm, can help survive the cold
    nights""",
    """A pack of wolves may try to hunt for the beefalos.""",
    """A village on the way to the final destination may provide help, but for anything more than basic help, they
    require service from you. They want you to clear some demons messing around in the nearby cavern.""",
    """Blizzard, which is a constant challange. It requires fortitude to prevent and remove freezing status effects.
    There are aspects that help, reduce the severeness of blizzard: fur clothes, special soup, elemental magic, some
    other creative ways?""",
    """The cavern has the magic source that enables recovery of mana, but since there are mushrooms and moss that grows
    there, they work a bit differently, they have alternative additional effects, I guess there is a reason middle
    empire grows specific spices in the mana sources.""",
    """""",
    """Shaman whispering to ear. Player character specific stuff""",
    """Hallucinations, visions, to guide players to their desires, traps and encounters.""",
    """Shamans of the north and devils have some kind of understanding. Devils roam the north because they have been
    summoned by some shaman for some purpose, which they have fulfilled. """,
    """The journey goes by the villages of Rygmund and Rhönd. Rhönd is on the road 4 days before Yorg and Rygmund is 5
    days from start. Rygmund is however half a day from the main road, and it goes inside some hills. """
]

combat_encounters = [
    {'name': 'wolves',
     'pawn': '4 HP, 2 ATK, 6 MV',
     'knight': '7 HP, 4 ATK, 9 MV',
     },
    {
        'name': 'demons',
        'knight': 'Small imp, 1 HP, 1 dodge per turn, disrupt 1',
        'pawn': 'Throggar, 3 HP, 3 ATK, 4 MV',
        'bishop': 'Ice imp - casts freezing every other turn.',
        'rook': 'Troll',
        'queen1': '''A big fat brute wielding a two handed Axe. 5 dice, 4 toughness, 3 DEF. 2 physique, axe, fortitude.
        Savage Axe feat and 3 stamina. 
        ''',
        'queen2': '''
        A spell casting demon wielding a staff of freezing. 
        ''',
        'king': '''
        
        '''
    },
    {
        'name': 'villagers',
        'pawn': '3 HP, 2 ATK, 4 MV',
        'rooks': '6 HP, 4 ATK, 4 MV',
        'queen': '''Druid - freezing, roots spells, can turn into a squirrel, once per combat can encourage troops, 
        3 troops can move with druid interrupting the players turn. 2 proficiency in elements, 6 dice, 2 toughness
        2 DEF.
        ''',
    }
]

harvesting_options = [
"""
Skin of wolves, also their teeth. Skin can be crafted into coats that provide greater protection against blizzard.

Teeth could be crafted into jewelry.
""",
"""
Various plants and herbs that might still grow during autumn, moss, mushrooms!

Some are poisonous however without proper cooking.

They can however find the rare fire-shroom, which can be crafted into warmth providing ration. They grow however inside
thick forests.
""",
"""
Skin of the greater devil could be crafted into a 4 DEF medium armor. 
"""
]

