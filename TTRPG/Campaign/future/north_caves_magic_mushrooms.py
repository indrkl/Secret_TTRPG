
rooms = [
    {
        'key': 'First hall',
        'description': '''You arrive to the entrance of the cave, it is rather wide, 10 m x 4 m. It quickly goes
        narrower, allowing a single orc to walk through at a time, and then opens up again into a wide space inside the
        mountain. It is pitch dark though. 
        
        If lit:
        
        In the front you can see a path leading downwards and turning left and another path going upwards
        and turning right, that crossing is 200 m. from the start of the room.
        
        When you look up:
        
        You see around 10 m. upwards an opening both in the left and in the right and a formation which as if formed
        a bridge, though not fully connecting, between those openings. 
        
        The path to the right turns around and ends up in the bridge that could be seen before. However it is physically
        quite exhausting to pass this path, as there are ups and downs, small chasms, and cliffs to climb up.
        
        The path to the left is much more smoother.
        '''
    },
    {
        'key': 'The hall of growth',
        'description': '''Finally you arrive to an enourmous open area, where the moss gives off light, there are 
        mushrooms, hundreds of different types of mushrooms, there is a definite magical aura in the room, the size
        500 m to the end, starts going wider being 30 m wide at it's peak, and there are multiple layers or floors,
        where the moss and mushroom grows in each of the layers.'''
    },
    {
        'key': 'Waterfall',
        'description': '''
        
        '''
    },
    {
        'key': 'Devils bed area',
       'description': '''

        '''
    },
    {
        'key': 'the area across the bridge - grove',
       'description': '''
        When you cross the "bridge", the path leads to a grove, where snow melts and the water turns into many streams
        that hide beneath the stone walls. In the center there are trees and flowers, the ceiling is open and you can
        see the night sky, or the blizzard but in the grove it is warm. The moss glows with vibrant colors. You see
        squirrels going about, as they see you they hide within trees, stones and other small hiding spots.
        
        One of the streams leads it's way to a path away from the grove, and that path starts leading downwards again.
        until you reach a cliff, which is 15 m. downwards, to a path, where you could take either left or right.
        ''',
    },
    {
        'key': 'The crossing',
       'description': '''
        When you take the path left from the start you arrive at a crossing, one turns right, the other turns left
        ''',
    },
    {
        'key': 'The pit path',
       'description': '''
        When you turn right from the crossing, then you come to a narrow path, which has chasms on the both sides, if
        you like down you see pit blackness. It is actually a dirt pit, which is pit dark that is only after falling 5
        m. The landing is soft, making you take only 1 damage, but moving in the pit is difficult. It costs 4 movements 
        to move. And 12 movement to climb out of the pit. Would be fun to have a fight here.
        ''',
    },
    {
        'key': 'The frontal camp',
       'description': '''
        After the pit path, unless players have encountered the first group of devils already, then one of the groups
        is staying en guard here. It is a place, where they campers have an advantage, they spot whoever comes earlier.
        They are camped in all the hidden corners, so there is an empty opening in the center. The path to their leads
        up for a moment, so it is really hard to spot if something is behind there. 
        ''',
    },


]

cards = {
    'devil': '''The group lead by Borg, the devil wielding two handed axe. He has 4 annoying imps and 10 throggar''',
    'emperor': '''The main group lead by devil Thrag, the master of contracts. He is not very strong, but he has
    14 throggar, 2 imps, and 2 trolls protecting him''',
    'fool': 'You meet the Sloth demon Lorki, he is high and offers you a special mushroom, which he has prepared.',
    'magician': '''The group runs into the group lead by Sham, the devil wielding frost spells. He has 10 throggar
    1 troll and 2 support casters.''',
    'page of cups': '''
    You accidently find a narrow passage, and you see something glimmering in the other side, however you don't seem to
    fit through, also, there is a threat of the wall falling in, making it inaccessible, but you still wonder what is
    on the other side.
    
    There is some treasure, rings and necklaces worth 120 gp, and also one magical necklace, which grants you protection
    against freezing. Every time you would gain a stack of freezing roll 1d6. On a 4, 5 or 6 you do not get it. It does
    require attuning.
    ''',

}

combat_encounters = [
    {
        'name': 'devils',
        'knight': 'Small imp, 1 HP, 1 dodge per turn, disrupt 1',
        'pawn': 'Throggar, 3 HP, 3 ATK, 4 MV',
        'bishop': 'Ice imp - casts freezing every other turn.',
        'rook': 'Troll, 10 HP, 6 ATK, 4 MV, occupies 2 x 2 squares, so create for blocking.',
        'queen1': '''A big fat brute wielding a two handed Axe. 6 dice, 4 toughness, 3 DEF. 2 physique, axe, fortitude.
        Savage Axe feat and 3 stamina. 
        ''',
        'queen2': '''
        A spell casting demon wielding a staff of freezing. 6 dice, 2 toughness, 2 DEF, 1 physique, will. 9 mana. 
        ''',
        'king': '''
        A fat demon, who is quite weak, 10 HP, but can order 3 throggar every turn to focus on someone specific.
        '''
    },

]