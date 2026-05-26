origin = """
players are from Amarkand. Castle name: Al'Ernus
"""



badlands = """
A region in the western part of the desert is badlands. An ambitious wizard in the past tried to create artificially
a similarly powerful magical node than the ones in the center, but this eventually back fired badly. Before it backfired
he did accumulate a lot of wealth, and a lot of it is spread around the castles, secret lairs and abandoned mansions. 
Now it has turned unstable. The area is infested now by various desert devils, elementals and other nasty creatures
that feed on the dark and chaotic energy of the node. The plants in the node are poisonous for individual driving them
mad and disorienting them.
"""

objective = """
There is a castle rather in the edge of the badlands controlled by some sand devils. There is some nice loot, like
heavy armor of the scarabus, which allows you to borrow in sand, sabre of tracking, if you draw blood with it, then
you know the whereabouts of the target for 7 days, ring of luck-burn, which allows you to spend 2 luck per turn instead
of one.

The objective is to clear the castle of the sand devils.
"""


sand_devils = {
    'pawn': '''camel faced sabre wielding ass holes with shields. They have 4 HP, 1 DR, 2 DMG, 4 MV''',
    'knight': '''Sand demons who can move through sand as fast as normally. They have a scorpion face and they strike
    with poison. 7 HP, 10 MV, 4 DMG or 1 DMG and 2 stacks of poison, that disorients 1''',
    'bishop': '''Fire elemental like creatures that cast fireball with 1 turn of preparation. But the fireball has 2 sq.
    radius. 6 HP, 5 MV, range 8''',
    'queen': '''R'Haal, the master of shadows. She can either cast false threats with 1 proficiency and she has 3 mana
    total. Or she can strike with her sabre and dagger having the Shadow feat. All her blades are also poisoned, that
    add disoriented stacks. She like her knights can also borrow in the sand'''
}

castle_rooms = [
    {
        'key': 'Entry hall and the old defense line',
        'description': '''
This is a narrow opening inside the western part of rock formation, it used to have a gate but that is long been 
destroyed and unmaintained. The old rusted gate is just lying there in the side. So the entrance is open.

The entrance used to be a murder hole, but the bars are long destroyed, but there are pathways left and right to
actually get to observation points that can be used to shoot invaders. The small holes are all around the castle, and
this pathway actually circles the whole castle, from there you can also get to the barracks if you go 120 degrees to
the left.

If you take the forward path from the entrance then first you go through 20 m. of narrow passage, which can be targeted
from above, and then you arrive to a large courtyard, where the plants grow naturally.
        
        '''
    },
    {
        'key': 'Water reservoir',
        'description': '''
This is in the southern side of the fortress and in the dungeon floor. It is connected with the main courtyard
and also the dungeons themselves.
        
        '''
    },
    {
        'key': 'The plant courtyard',
        'description': '''
Not strategically brilliant, but right after the entrance the plants are growing. That was decided by nature, so here we 
are. From the top you see sun light shining, and there are nice holes for the sun to get through throughout the day, so 
the courtyard is pretty lit during day. Since the sun is shining from the north mostly, then the plants grow in the
southern side and in terrace formation, so to have more area for them.

That means that if you enter then the plants are to the right. There is a passage between the plants that leads to the
water reservoir, but this leads down.

In addition a stair case leads to barracks, and there is a hard to climb opening to the stockpile, but it is more so
that people in the stockpile can access the courtyard more easily. Finally even higher up there is another window, that
is basically the leadership quarters, so that the leaders can see what is going on inside here.
        '''
    },
    {
        'key': 'The barracks or living quarters',
        'description': '''
This is able to comfortably house 40 soldiers + 5 sergeants. But in times of need it can be doubled, or if you really
want, then even triple. There are 4 rooms for soldiers and 2 for officers. Soldier rooms have bunk beds with simple
sand bags to soften the sleep.
The barracks can access easily dungeons, the outer defensive layer and the courtyard. So to quickly react and reach all
strategic locations. In addition they can access the armory and through that there is another defensive line that
surrounds the inner courtyard. Finally stair leads up to the leadership area.        
        '''
    },
    {
        'key': 'The leadership area',
        'description': '''
This is one big room, with a window to outside and the inner courtyard.
        
        '''
    },
    {
        'key': 'Stockpile, armory',
        'description': '''
In the east side of the barracks floor, from 180 to 270 degrees is the stockpile area, where currently old equipment is
being held, but also food and so on. This can be accessed only through the barracks and is pathed by the inner defensive
line. There is an opening to jump down if a battle would be taking place in the courtyard.        
        '''
    },
    {
        'key': 'Dungeon, prison area',
        'description': '''
The dungeons are in the northern side of the dungeon floor. There are cells, a guard room, and the cells fo 3 floors
deep, first one having 6 cells, second one 4, and last deepest floor only a single cell, with torture equipment, that
is slightly rusty. The dungeon connects with the water reservoir through a narrow passage, and also stairs lead up
to barracks. The doors to the barracks are still functional.
        
        '''
    },
]

what_are_the_current_inhabitants_upto = """
So they definitly need to eat, so the pawns are ordered to also tend to the plants. In general however, since they are
demons they are all rather lazy, so doubt there is any proper guard duty since they are not expecting anyone. They
probably have put a trap in the entrance to alarm them.

They probably sleep in the barracks, play some gambling and dice games for gold coins. And they may occasionally go to
some raids and try to raid some caravans or some shit like that. Very rarely there are some other bad land factions
trying to mess with them.

There are a total of 15 pawns, 4 knights, 2 bishops and the queen in the fortress currently, so they are quite cozy. So
the players definitely need to think how to split them up. In the dungeon they currently have a few stolen natives from
recent raid to a caravan, rescuing them, if party manages to heal, provide them weapons and feed them, they can actually
be of use in the fight. There is 4 of them in second floor and 1, a powerful harmony mage paladin in the torture floor.

Someone might be in the prison having fun of course. 

Another 6 of their comrades have already died in the dungeon.

Remember, sand is only in the courtyard, all other rooms are made of stone.
"""