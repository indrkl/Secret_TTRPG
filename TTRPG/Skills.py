skills = [
    {'name': 'diplomacy',
     'description': '''
Diplomacy is used to influence the behaviour of NPC-s with an advantage. This means to haggle for a better price,
get someone to do you a favor, get someone to give up a secret, give you access to another important NPC 
or negotiate a peace deal between warring 
nations, or to simply behave in a court of nobles when you have not grown up in this environment. 

It is important to note, that you can often by pass diplomacy by simply paying money, since most things has a price,
and so NPC is perfectly willing to do many things for that coin. Diplomacy only comes into play when you want a deal,
where the NPC by default would find it lacking.

The forms of how you act out diplomacy may vary. It can take the form of persuasion, negotiation, listening and
sympathising, or instead intimidation, coercion or something else entirely?

The form of diplomacy you choose will of course have an impact on the story, and character consistency is of course
something one should take into account, but since that is such a complex topic, there are no mechanical limitations
and this is more up to GM to reward and encourage consistent play and for the player, to really come up with the
nuances of their character.

The challenge difficulty of diplomacy challanges depend on 2 factors. 

The cost to the NPC to accomodate the player's wish, and the hierarchical difference between the NPC and player. 
        '''
     , 'group focuses': [
        ]
    },
    {'name': 'lore',
     'description': '''
Lore is used to get information about the plot, game-world, scene, mysteries etc. A player who picks proficiency in lore
states with that, that they intend to engage with the story hard, they want to know everything, and uncover all secrets.

This can be used to study a topic in a library, to pick up key information through conversations or interrogation, to
deduce (GM can say that your character deduced the killer, by noticing scratch marks, and the skin under the victims
nails for example), to investigate some scene for clues, or to simply observe and pay attention to interesting details.

Regarding observation, both survival and lore skill can be used to perceive things but their motivation is different.
Lore is used to notice things that reveal something about the plot, NPCs, the world, while survival is used to perceive
threats.

Simply put, when player says I want to know an answer to some question, then most likely lore skill is the most
relevant for this challenge.

''',
     'group focuses': [],
     },
    {'name': 'leadership',
     'description': '''
Leadership skill is an interesting one. This is used to lead the group. For one, the player with the highest leadership
decides the play order in the battle field. In addition leadership skill can be used in group challenges by the leading
player instead of the challange's main skill. There can be also situations when the situation requires leading larger
groups of NPCs, villagers, or to inspire hope in large masses, then again leadership can be used.

While the motivation of leadership is to take charge and bring the group behind a common goal, all players should
remember that in this game everyone want to have fun and want spot light in the game. So when picking this skill, make
sure you are encompassing positive leadership, where you listen at least as much as you speak.
     '''
     , 'group focuses': []
    },
    {
        'name': 'survival',
        'description': '''
Survival skill is used by players who are motivated by surviving themselves and making sure their party also survives.
This is for detecting traps, avoiding ambushes, getting a tactical advantage for battle, but also avoiding detection
from guards, escaping from threats, and also surviving in the wilds, or streets, or when you are in a royal court full
of intrigue, then surviving all sorts of threats that can come from that.

Basically having proficiency in survival implies that your character has a constructive and useful dose of paranoia. Or
they could simply be very aware of their surroundings, either way they take surviving seriously.
    ''',
        'group focuses': []
    },
    {
        'name': 'intrigue',
        'description': '''
If your motivation is to make some mean plots yourself, and need to withhold information, mis-direct, manipulate, 
etc. this is the skill you require.

Note that it is perfectly possible for a group to play their whole campaign without using this skill. This is 
specifically a niche skill, but does represent the potential motivation of doing some crazy scheme to put the even the
BBEG to shame.
    ''',
        'group focuses': []
    },
    {
        'name': 'crafting',
        'description': '''This skill involves crafting yourself, knowing crafters, knowing good crafters,
            and anyways knowing what to do in order to craft great items for the party. Crafting for a specific item
            is easier than finding it, but harder than finding any item of similar power level.''',
        'group focuses': []
    },
    {
        'name': 'harvesting',
        'description': '''This is harvesting for specific materials, knowing where to get them, also knowing where
            to buy them. It also involves knowing how to extract magical, but also none magical materials from slain 
            beasts.''',
        'group focuses': [],
        'notes': [],
    },
    {
        'name': 'physique',
        'description': '''
This is used for making all sort of checks requiring bodily accuracy, like when performing
acrobatic feats, climbing, having balance while crossing a narrow path, being able to endure long journey,
wrestling, martial arts, dancing.

Having proficiency in physique represents your character being strong, agile, trained. In addition to have application
during campaign, this proficiency is also used to recover defense and to boost your movement during combat. This is also
why this is a mandatory skill for martials.

The design philosophy behind this is, to naturally provide martials to be better at dealing with challanges that rely
on physical prowess and to make it cost effective for them to achieve it.
        ''',
        'group focuses': [],
    },
]


activities = [
    'climbing', #physique
    'dancing', #physique
    'jumping', #physique
    'wrestling', #physique
    'unarmed fighting', #physique
    'enduring physical hardship', #physique
    'accuracy challange', #physique
    'chase someone', #physique
    'ride horse', #physique
    'persuasion', #diplomacy
    'improving relations', #diplomacy
    'negotiations', #diplomacy
    'haggling', #diplomacy
    'selling', #diplomacy
    'hiring', #diplomacy
    'inspire', #leadership
    'ignite hope', #leadership
    'incite a revolution', #leadership
    'lead troops', #leadership
    'ambush', #leadership
    'hunt', #survival
    'track', #survival
    'forage', #survival
    'hide campsite', #survival
    'camouflage', #survival
    'flee', #survival
    'detect ambush', #survival
    'detect traps', #survival
    'pickpocket for survival', #survival
    'sneak', #survival
    'lock-pick', #survival
    'lie', #concealment
    'withhold information', #concealment
    'deceive', #concealment
    'misdirect', #concealment
    'study', #lore
    'investigate scene', #lore
    'learn language', #lore
    'decipher', #lore
    'find information from books', #lore
    'search for clues, pick up hints', #lore
    'extract information in a conversation', #lore / diplomacy*
    'extract information through torture', #lore / diplomacy*
    'converse', #lore
    'medical related', #lore / survival
    'craft an item', #crafting
    'evaluate worth of an item', #crafting
    'know the best crafters', #crafting
    'gather resources', #harvesting
    'extract resources from slain beasts', #harvesting
]