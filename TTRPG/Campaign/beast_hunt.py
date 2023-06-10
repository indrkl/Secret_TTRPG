story = """
Shape-shifters Miranda and Grot are sister and brother. One day Grot is presented a cursed amulet, that would give him
the power to possess any beast, however that power comes at a cost, of giving up his ability to turn into his spirit
beast. That drives him power hungry and mad, conflict with his sister, and soon after he dissapears. He starts 
experimenting on beasts, giving them extra powers, magically enhancing them, possessing them, and then getting bored
of them and moving away to another project. Some of those discarded projects however start to cause havoc in the 
country-side. Miranda suspects that this may be connected with his lost brother, and seeks the help of a group of 
adventurers, hoping that perhaps he can still be saved from this madness, but no, this is too late. 

The story first starts with Miranda seeking out help from the heroes. She offers an hefty some of money for anyone who
would take care of a beast, and return with all the necessary details about the beast for her "research". 
"""

beasts = [{
    'description': '''Wolf''',
    'feats': ['Fast beast', 'Leaping attack', 'Claw attacks', 'Bite grappling'],# 10 cost worth of feats
    'stamina': 5 + 3 * 4,# 3 points
    'proficiency': "6 capped at +3",#3 points
    'AC': 15,
    'HP': 50,
    'lvl2': '''Lose fast beast, 1 stamina, 1 proficiency''',
    'additional_ideas': """
blink strike
Howl that makes everyone check for concentration and afraid
Fade away to make a strong attack next round.
When one of them dies, the other one rages.
    """
}]

remnant_mage = {
    'MAGE': 2,
    'MARTIAL': 2,
    'lvl': 2,
    'spells': ['pain hex', 'frost bite'],
    'daily_cast_limit': 8,
    'proficiencies': ['discord', 'elements'],
    'AC': 14,
    'HP': 18 + 4 * 10,
    'REFLEX': +2,
    'FORTITUDE': +2
}
remnant_mage_leader = {
    'MAGE': 2,
    'MARTIAL': 4,
    'lvl': 1,
    'innate_mage': 'Raw caster',
    'innate_martial': 'Nimble',
    'spells': ['False threats'],
    'daily_cast_limit': 8,
    'proficiencies': ['illusion 2', 'axe 4'],
    'AC': 14,
    'HP': 48 + 18,
    'REFLEX': +3,
    'FORTITUDE': 0,
    'stamina_recovery': 1,
    'stamina': 8,
}

heavy_armored_fuck = {
    'MARTIAL': 3,
    'AC': 14,
    'HP': 27 + 27,
    'max_stamina': 11,
    'proficiencies': ['2 handed mallet 2'],
}
cursed_archer = {
    'MARTIAL': 3,
    'AC': 12,
    'HP': 27,
    'feats': ['Hex arrow (Pain hex)'],
    'max_stamina': 5,
    'proficiencies': ['bows 6'],
    'weapon': 'Composite bow (+1 AP to attack, +2 to hit, +3 with hex arrow)'
}

archer = {
    'MARTIAL': 2,
    'AC': 12,
    'HP': 27,
    'max_stamina': 5,
    'proficiencies': ['bows 8'],
    'weapon': 'Long bow'
}



squire = {
        'MARTIAL': 2,
        'Advances': [{
            'lvl': 1,
            'shield': 3,
            'max stamina': 1
        },
        {'lvl': 2,
         'AC': 1, 'sword': 1,
        },
        {'lvl': 3,
          'max stamina': 2
        },
        ],
    },


ideas = [
    '''some farm boy who lost his father to a beast offers help, you can get some aid in the battle, but he can also
    die and then there will be a sad scene.''',

    '''Hunting the wolves has a risk of splitting the party, the wolves will try to seek a good opportunity to attack 
    the players''',

    '''Offer a skilled player to sacrifice their luck tokens to luckily stumble onto a corpse with some nice loot, but
    they miss the start of the fight''',

    '''When tracking, chasing, keeping the party together, protecting some fool NPC, trying to achieve an advantage
    over your pray, offer to make trade offs, gaining advantage in 1 and disadvantage in another.''',

    '''A shifter druid scouts you, shaped as a raven, just curious. If you figure it out you might be able to talk to
    him, maybe he even offers to help you out. Though he doesn't much care for the wolves, or the villagers, he just
    likes some company, and wine. A chubby, curious fucker, so to speak.''',

    '''The village has some agents of remnants, who are also manipulating the rest of the villagers.''',

    '''The wolves were abandoned by Grot, because the other one would not cooperate with Grot, if he only possessed one
    The first kill was done by Grot out of spite, the second killings of the mob, which was gathered, by the wolves for
    self defense.''',

    '''Miranda gets kidnapped, by the remnants for sniffing around too much''',

    '''There is a local remnant initiate leading a criminal gang loosely associated with Myriad. They have some 
    connections to get weapons, and they mostly get their money by extorting locals, robbing travelers, and faking
    taxing data. The gang consists of around 12 men, the village has around 250 people. Their mayor is under the thumb
    of the gang. Also the tax collector is also with the Myriads, and the mayor has no other connections.''',

    '''The gang runs their operations from 2 bigger houses, owned by some of the members. and most of them spend their
    nights in one of them. The initiate (discord and illusion mage) and 4 smarter soldiers are in the biggest building,
    the alfa brute is with 5 proper grunts in the other building. Then the accountant, fixer is living alone in his
    house. He also does the torturing, while the villagers know about the others, they don't know that he is part of the
    gang. And finally there is the town bard, who is jolly, and very seductive, and inviting to gossip and gossips 
    himself.
    ''',

    '''
    When the players want to know about what is going on in the village, I request how they approach their socialization
    and communication.
    ''',

    '''When you try to speak to anyone, they turn away, some beg not to request anything from them and just leave them
    alone, other's pretend you don't exist. You recognise fear, shame, hopelessness in various faces, as you try to ask
    about Miranda from one house after another. How persistent are you?''',

    '''The innkeeper is ordered to notify the gang immediately if new foreigners arrive.''',

    '''Miranda is kept alive because Remnant wants to use her as leverage over Grot.''',

    '''Jasmin gets drugged during the evening Miranda is captured, to avoid her getting involved. The night of 
    kidnapping has a huge party to keep everyone distracted''',

    '''The party allowed Miranda to learn something she shouldn't have that triggered a very hasty capture of her.''',

    '''So there is 1 mage, 11 fighters, 1 accountant torturer and 1 bard trying to control a village of 250 people.
    Obviously they need to be worried of a massive up rising. Fear is used, but if someone ignites hope, that can be
    dangerous. That means they cannot allow to sit out in their fortified homes, even if they are fortified. So the
    moment they learn that the party is posing a risk to them and not just looking around for Miranda, they would need
    to act. So if everyone falls upon the heroes then they would be fucked. What are the advantages that they could
    pursue? Help from villagers, they could seek tactical advantage, they could try to make a decoy attack and real
    attack.
    ''',

    '''They may go into a more investigative route. The innkeeper is still going to notify, but if they don't try to
    ignite a rebellion then the crime lord will also prefer to get rid of the party discretely. There are a few clues,
    Jasmin's headache, the blundering of Miranda's room, missing money. No journal or notes for the time she had been
    here. Still only way to figure anything out is to talk with the citizens, who saw something, but most would not 
    speak, not voluntarily, some may hint to just leave. However even sniffing around and then leaving, especially if
    the group may have some connections in the realm, is also a bad outcome for them. ''',

    '''The dungeon where Miranda is being kept has also some spiders made with beast-craft, a dark technique for
    creating monstrosities. Apparently Grot made the spiders before he vanished and the Remnants lost contact with him.
    ''',

    '''What things can go wrong? what are the vectors of loss asides from complete party wipe? Losing 1 party member,
    getting somewhat beat up in the fight, losing villagers, some villains, together with a lot of money getting away.
    Needing to retreat.''',

    '''Some players met already on the road, they had some fights with some bandits, and got merry already''',

    '''To get the wibe, there are some drunks in the front of the inn, the maid is cleaning puke from the last night,
    it seems to have been wild for such a small town. If the query, then it was an actually wilder than usual party.
    Some characters, the maid, innkeeper may appear to be a little startled, especially if Miranda is mentioned.''',

    '''The accountant doing to book keeping for the fucks is the son of a noble who got lost and who Rolf is looking 
    for. So he is young, and stupid and rebellious, got mixed with the wrong crowd. Will pretend as if he was forced to
    work for them, but that is bull shit, because he was shit to Miranda. He just wanted to be part of something big.
    He is greedy and power hungry little prick.
    ''',
]


clues = [
    '''Miranda on kadunud''',
    '''Jasmin on mürgitatud''',
    '''Miranda ruum on tühjaks tehtud''',
    '''Rahvas on hirmus, keegi ei räägi midagi''',
    '''Inn keeper on veidi närvis, kui uued külalised saabuvad, ja eriti kui Mirandat mainitakse''',
    '''Kui Miranda toast tagasi tullakse on kõrtsi üks tööline kadunud''',
    '''Osadel majadel on märgistus, mis on ühe kindla kabali hoiatus sümbol''',
    '''Raamatupidajal on ledger, kus on kõik tõendid kirjas''',
    '''Miranda on raamatupidaja keldris, mis on ühenduses bossi keldriga''',
    '''Küla ekspordib puitu, aga ka vibusid. Võib olla keegi teab, et tegelt vibud, mis siin toodetakse on päris hinnas.
    ''',
    '''Inimesed näevad vaesed välja''',
    '''Osad hooned näevad konkreetselt paremad siiski välja. Ning mõned hooned on siuksed kesk-klassi hooned.
    Raamatupidaja, Pandede boss ja teises küla otsas Jõhkardite juht on kõik väga ilusates majades. Neil on külast
    teenijad, kes siis koristavad nende maja ümbrust näiteks.
    
    Lisaks külapea elab küla keskel, ja tal on OK maja, samuti on OK majad küla kahel vibu meistril ja saekoja juhil.
    
    Saekoja juhil on aga üks käsi puudu. Kuid see tegelt on lõike haav ja mitte sae haav, kuid kas seda pandakse tähele?
    ''',
]


player_hooks = [
    '''agent of the clasp is a friend of Miranda, she asked for someone who is willing to work for gold. But could they
    have alternative motive?''',

    '''An initiative in the Library of Cobalt soul was sent to aid Miranda. ''',

    '''Mercenary who saw a note in the board.''',

    '''An elf from Syngorn, who knows Miranda from childhood, they know that Miranda is a shifter.''',
]

links = [
    'https://watabou.github.io/village-generator/?seed=1343656716&tags=uncultivated,large,organic,sparse&name=Lorwey&pop=253',
    'https://watabou.github.io/village-generator/?seed=333933546&tags=large,sparse',
    'https://watabou.github.io/village-generator/?seed=26555168&tags=large',
    'https://watabou.github.io/one-page-dungeon/?seed=788841165&tags=backdoor,small,dangerous,crumbling,secret',
    'https://watabou.github.io/',
]


Session_1_scenes = [
    'Coming to the Inn and trying to contact Miranda',
    'Requesting information from the innkeeper, encounter with the bard',
    'Investigation in the city',
    'Preparing for the confrontation with the crime lords',
    'Ambushing the crime lord themselves',
    'Searching the house of the crime lord',
    'Entering the dungeon of the Accountant',
    'Encounter with the spiders',
    'Rescuing Miranda',
    'Burials and conclusion',
]