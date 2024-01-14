schools = {
    'Force': {
        'spells': [
            {
                'name': 'Telekinesis',
                'effect': '''You can move objects with your mind for various effects. Move a bucket of hot water on top
                of your enemies, a key from the guard to you for escape, etc.                
                This is a creative spell so please refer to the creative spell section in the glossary                
''',
                'difficulty': 'R3.??',
            },
            {
                'name': 'Push/pull',
                'range': '8 sq.',
                'effect': '''Move target away from you or towards you for 2 sq. Halve the distance for large creatures
                and those wearing heavy armor. Huge and larger creatures cannot be moved this way.''',
                'target': 'single',
                'difficulty': 'R3.R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': '''increase the move distance by 2 sq. The target needs to make an 
                    additional check for balance'''},
                    {'D': 'R3', 'description': '''For the purposes of moving the target and balance checks the creature is 
                    considered to not be wearing heavy armor and also to be one size smaller'''},
                ],
            },
            {
                'name': 'Explosive force',
                'range': '8 sq.',
                'effect': '''A force pushes everyone around target point 2sq. away from the point and they must check
                for balance 4 times''',
                'target': 'point',
                'radius': '1 sq',
                'difficulty': 'R3.R3.R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': '''The force pushed them 2 additional sq. further away and they need to 
                    check for balance twice more'''},
                ],
            },
            {
                'name': 'Wall of force',
                'range': '12 sq.',
                'effect': '''Create a 2 sq. long wall. arrows that would fly through this area, lose their speed and
                fall on the ground. It takes 3 sq. worth of movement to go through the wall of force''',
                'concenctration': 'R3',
                'difficulty': 'R3.R3.R3',
                'scaling': [
                    {'D': 'R2', 'description': '''increase the length by 4 m.'''},
                    {'D': 'R2', 'description': '''At the beginning of each of your rounds you can move the position of the
                    wall'''},
                    {'D': 'R3', 'description': '''It requires 2 additional sq. worth of movement to go through the wall
                    of force'''},
                ],
            },
            {
                'name': 'Force field',
                'range': 'touch',
                'target': 'self',
                'duration': '5 rounds',
                'concenctration': 'R3',
                'effect': '''Increase your maximum defense to 2 (note, this does not stack with armor and is only
                useful if you don't have maximum defense from other sources..
                ''',
                'difficulty': 'R3.R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': '''
                        The maximum defense provided by this spell is increased by 1
                    '''},
                    {'D': 'R3.R3', 'description': '''Gain 1 damage reduction'''},
                    # {'D': 'R4.R4', 'description': '''Choose fire, cold, lightning or physical, gain resistance to the chosen
                    # damage type.'''},
                ]
            },

        ]
    },
    'Nature': {
        'spells': [
            {
                'name': '''Nature's bounty''',
                'effect': '''After learning this spell, when trying to find food, or otherwise survive in the 
                wilderness, you can use your nature proficiency instead of survival proficiency to make the checks.'''
            },
            {
                'name': 'Heal',
                'speed': '2A',
                'range': 'touch',
                'effect': '''This is a heal. Target recovers 1 damaged dice or removes all damage from wounded dice, or
                removes 1 level of burning, poison or freezing.''',
                'target': 'single',
                'difficulty': 'R1.R1.R1',
                'scaling': [
                    {'D': 'R1', 'description': 'This heal recovers 1 additional damaged dice'},
                    {'D': 'R1', 'description': 'remove a level of poison'},
                    {'D': 'R1', 'description': 'remove a level of burning'},
                    {'D': 'R1', 'description': 'remove a level of freezing'},
                ],
            },
            {
                'name': 'Grant luck',
                'range': 'touch',
                'target': 'single',
                'effect': '''Target can change the result of one dice in the dice pool when you cast and each time
                you concentrate on it
                ''',
                'difficulty': 'R1.R1.R1',
                'concentration': 'R1.R1.R1',
                'scaling': [
                    {'D': 'R1.R1', 'description': '''Target can change another dice in their dice pool'''},
                ],
            },
            {
                'name': 'Entangling roots',
                'range': '6 sq',
                'radius': '2 sq',
                'target': 'area',
                'effect': '''Requires being in the wild. Roots grow from the ground and entangle anyone. 
                    Anyone starting their round or entering the area of effect gain 2 levels of entangled''',
                'difficulty': 'R1.R1.R1.R1',
                'concentration': 'R1.R1',
                'scaling': [
                    {'D': 'R1', 'description': '''Anyone starting their round or entering the area of effect gain 
                    additional 1 level of entangled'''},
                    {'D': 'R1',
                     'description': '''Anyone starting their round or entering the area of effect take 2 piercing 
                        damage'''},
                ],
            },
        ]
    },
    'Harmony': {
        'special_rules': [
            """You can use harmony proficiency instead of diplomacy when
                interacting with large crowds, or individuals who are neither evil, power hungry nor emotionless."""
        ],
        'spells': [
            {
                'name': 'Guardian',
                'speed': '2 AP',
                'target': 'self',
                'radius': '1 sq.',
                'effect': '''When you have the guarded buff, then allies standing within radius. of the target also
                have that buff.
            ''',
                'difficulty': 'R3.R3.R3',
                'concentration': 'R3',
                'scaling': [
                    {'D': 'R4', 'L': 1, 'description': '''This spell can target others. Gaining the range of touch.'''},
                    {'D': 'R3', 'L': 1, 'description': '''Increase maximum defense of the target by 1'''},
                    {'D': 'R4.R4', 'L': 1, 'description': '''If the target is willing, he may direct an attack onto 
                    them for all attacks made to an ally within this spells radius.'''},
                ],
            },
            {
                'name': 'Clarity',
                'speed': '2 AP',
                'target': '1 creature',
                'effect': '''Remove 1 lvl from all negative status effects related to WILL saving throws.
            ''',
                'difficulty': 'R3.R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': '''Remove one additional level from those status effects'''},
                ],
            },
            {
                'name': 'Bless',
                'range': '5 sq.',
                'target': 'up to 3 allies',
                'effect': '''
                Target has an additional bless dice to be used in roll dice and for actions. One can have bless dice
                only from one source. 
        ''',
                'difficulty': 'R3.R3.R3.R3',
                'concentration': 'R3',
                'scaling': [
                    {'D': 'R3.R3', 'description': '''Provide one additional bless dice for targets'''},
                ],
            },
            {
                'name': 'Harmony of souls',
                'target': 'Up to 8 willing participants',
                'effect': '''
                Harmony of souls is a ritual that connects the souls of the participants in a way that they sense each
                other's concerns, desires, feelings, excitement, and even though they don't hear each other's thoughts
                they get glimpses and a sense of some of the thoughts especially if those thoughts make a lot of sense
                to them or if they have similar thoughts themselves.
                
                This allows players to assist each other by using only 2 dice. Assist provides 1 dice for a roll target,
                attack, spell, action etc.
        ''',
                'difficulty': '10 X R3',
                'duration': '1 day',
                'concentration': 'X / 2 mana',
                'scaling': [
                    {'D': '8 X R3', 'description': '''
                    Participants may make will actions instead of other participants. They may also do the recover
                    defenses action for other participants. 
                    '''},
                ],
            },
        ]
    },
    'Elemental': {
        'special_rules': [
            """Elements are fire, water, earth and air. In addition to the combat spells this school provides. One can
            manipulate the elements out of combat, by describing what they want to achieve and GM then setting a roll
            target for that, so that they get to use elemental proficiency when attempting to meet it. You need to
            have some elemental proficiency to even have the option however."""
        ],
        'spells': [
            {
                'name': 'Fireball',
                'difficulty': 'R6.R6.R6',
                'range': '8 sq.',
                'effect': 'Deal 2 fire damage to everyone in the area.',
                'save': 'REFLEX',
                'target': 'area',
                'radius': '1 sq.',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'Deal additional 3 damage'},
                    {'D': 'R1', 'description': '1 target enemy within radius gets a level of burning'},
                ],
            },
            {
                'name': 'Chain lightning',
                'difficulty': 'R6.R6.R6',
                'range': '8 sq.',
                'effect': '''Deal 4 lightning damage to a target enemy, and then it jumps to another target enemy,
                dealing 2 less damage, until it can do no more damage''',
                'save': 'REFLEX',
                'target': 'area',
                'radius': '1 sq.',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'Deal additional 2 damage'},
                    {'D': 'R1.R1', 'description': 'Everyone hit by chain lightning get 1 level of disoriented'},
                ],
            },
            {
                'name': 'Tremor',
                'difficulty': 'R6.R6',
                'range': '6 sq.',
                'effect': '''everyone in the target area  gain 2 levels of unbalanced. At the beginning of your round,
                when you continue to concentrate on this spell, you may move the center of tremor up to 2 sq. When you 
                are outside the range of the tremor you lose concentration.''',
                'target': 'area',
                'concentration': 'R6.R6',
                'radius': '2 sq.',
                'scaling': [
                    {'D': 'R6', 'description': 'The gain an additional level of unbalanced'},
                ],
            },
            {
                'name': 'Frostbite',
                'range': '8 sq.',
                'effect': '''Target enemy gets one level of freezing''',
                'target': 'single target',
                'difficulty': 'R6.R6.R6.R6',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'Target gets another level of freezing'},
                    {'D': 'R1', 'description': 'You get to choose which of the dice are frozen'},
                ],
            },
            {
                'name': 'Rune trap ritual',
                'range': '8 sq.',
                'effect': '''Make a trap that when triggered casts either fire-ball, chain lightning or freezing
                upon the target. The cost of this spell scales depending on the dice cost of the target spell. Let the
                target spell cost be X*R6''',
                'target': 'single target',
                'difficulty': '2X*R6',
                'scaling': [
                ],
            },
            {
                'name': 'Elemental weapon',
                'range': 'touch',
                'effect': '''Choose fire, cold or lightning. Enchant target not enchanted weapon. Target weapon deals 
                1 extra damage of the chosen damage type with every attack made with this weapon.
                ''',
                'target': 'single weapon',
                'difficulty': 'R6.R6.R6.R6',
                'duration': '3 rounds',
                'concentration': 'R6.R6',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'target weapon deals an additional 1 damage of the chosen type'},
                    {'D': 'R6.R6.R6', 'L': 1, 'description': '''You need to have chosen cold. Convert all physical 
                        damage target weapon does to cold damage. Each time that weapon hits an enemy the enemy gets
                        one level of freezing
                    '''},
                    {'D': 'R6', 'L': 1, 'description': '''You need to have chosen lightning. Convert all physical damage 
                        target weapon does to lightning damage. Each time that weapon hits an enemy, the enemy
                        gets 2 confusion.
                    '''},
                    {'D': 'R6.R6', 'L': 1, 'description': '''You need to have chosen fire. Convert all physical damage 
                        target weapon does to fire damage. Each time that weapon hits an enemy, the enemy gets one
                        level of burning.
                    '''},
                ],
            },
            {
                'name': 'Haste',
                'range': '6 sq.',
                'duration': '2 rounds',
                'effect': '''Target gets +1 action limit haste buff. Each character can have the haste buff from only 
                one source''',
                'difficulty': 'R6.R6.R6.R6',
                'target': 'single',
                'concentration': 'R6.R6',
                'scaling': [
                    {'D': 'R6.R6.R6', 'L': 1, 'description': '''Haste buff provides additional +1 action limit'''},
                ],
            },
            # {
            #     'name': 'Shatter rock',
            #     'speed': '2A',
            #     'range': '6 m.',
            #     'radius': '1 m.',
            #     'target': 'area',
            #     'effect': 'Break stone into small pieces in the radius of effect',
            #     'difficulty': 4,
            #     'scaling': [
            #     ],
            # },
            # {
            #     'name': 'Clean water',
            #     'speed': '1 minute',
            #     'range': 'touch',
            #     'target': 'vessel filled with water',
            #     'effect': '''Clean a water in a constrained vessel''',
            #     'difficulty': 0,
            #     'scaling': [
            #     ],
            # },
        ]
    },
    'Dimension': {
        'special_rules': [
            """School of dimension deals with overcoming great distances and moving between planes. Most things
            however, like teleportation, long distance communication or moving to other planes is a complex matter and
            requires rituals to be made."""
        ],
        'spells': [
            {
                'name': 'Pass object',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''Teleport a tiny object weighing no more than 1 kg. onto the possession of another willing 
                creature. You can place it on them wherever you would like.''',
                'difficulty': 'R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': '''Increase the max object weight by 1 kg'''},
                    {'D': 'R3', 'L': 1, 'description': '''When passing a potion onto a willing subject, they can also 
                    drink it and receive it's benefit immediately'''},
                    {'D': 'R3', 'L': 1, 'description': '''When passing a vial of poison onto a willing subject, you can
                    coat their melee weapon or next arrow with that poison vial instead'''},
                ],
            },
            # {
            #     'name': 'Communicate',
            #     'speed': '1 round',
            #     'range': '1 km.',
            #     'target': 'Anyone(known)',
            #     'effect': '''Send a short message over a long distance. If recipient is within the range of the spell, 
            #         they will hear that and may choose to reply shortly.''',
            #     'difficulty': 0,
            #     'scaling': [
            #         {'D': 1, 'description': 'double the range'},
            #         {'D': 4, 'L': 1, 'description': '''open a line of steady communication with the target, it stays 
            #         open as long as you concentrate 3, concentration does not consume additional mana'''},
            #         {'D': 3, 'L': 1, 'description': 'You can have another party member do the communicating.'},
            #     ],
            # },
            {
                'name': 'Blink jump',
                'range': '8 sq.',
                'target': 'empty space',
                'effect': '''Instantly disappear from your current location without provoking any attacks of opportunity
                    and reappear in the target location''',
                'difficulty': 'R3.R3.R3',
                'scaling': [
                    {'D': 'R3', 'description': 'Increase range by 8 sq.'},
                ],
            },
            {
                'name': 'Teleportation ritual',
                'range': '50 km.',
                'duration': '1 min.',
                'concentration': '8 mana',
                'effect': '''Create a temporary teleportation portal from which up to 10 normal sized creatures can go
                through to go to a target which is 50 km away. The ritual master or one of the participants must know
                this target location.
                
                The portal stays open for 1 minute or until 10 creatures go through it whichever happens first.
                ''',
                'difficulty': '9 X R3',
                'scaling': [
                    {'D': '7 X R3', 'L': 3, 'description': 'double the range'},
                    {'D': '10 X R3', 'L': 3, 'description': 'double the range'},
                ],
            },
            {
                'name': 'Communication ritual',
                'range': '10 km.',
                'duration': '1 hour',
                'concenctration': '3 mana',
                'effect': '''Create a temporary communication link between a mirror you can touch and a mirror one of 
                the participants knows in the world that is within the range of the ritual 
                ''',
                'difficulty': '3 X R3',
                'scaling': [
                    {'D': '3 X R3', 'L': 5, 'description': 'double the range'},
                    {'D': '5 X R3', 'L': 5, 'description': 'double the range'},
                ],
            },
            {
                'name': 'Step between dimensions',
                'target': 'self',
                'effect': '''You become corporeal becoming unaffected by all effects in the material plane.
                    By default you cannot attack, cast spells or concentrate on spells in a way that would affect anyone
                    in the material plane.''',
                'difficulty': 'R3.R3.R3.R3',
                'concentration': 'R3.R3',
                'scaling': [
                    {'D': 'R3.R3', 'description': '''Target may cast spells that would affect the material plane'''},
                    {'D': 'R3', 'description': '''This spell can target any willing creature. This spell gains a range 
                        of touch.'''},
                    {'D': 'R3.R3', 'description': '''This spell can target any creature. This spell gains a range 
                        of touch.'''},
                    {'D': 'R3.R3', 'description': '''Target may concentrate on spells that would affect the material 
                    plane'''},

                ],
            },
        ]
    },
    'Discord': {
        'special_rules': [
            """Regarding hexes. Each creature can by default have only 1 hex placed on them. This can be overwritten
        by certain feats. Any creature with a hex on them can make a R5.R5 remove hex action using Will proficiency
        for weak hexes, R5.R5.R5 for strong hexes and R5.R5.R5.R5 for extreme hexes. Hexes cannot be applied to 
        your allies to override hexes by your enemies. However if an ally has hexed a creature, then your hex would 
        override their hex(s), unless you are able to place multiple hexes on the enemy."""
        ],
        'spells': [
            {
                'name': 'Enfeeble hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''Each time target enemy rolls, you may change the outcome of 1 dice. It has to be a
                different dice than was changed by lucky condition, if the enemy was lucky and is done after the lucky
                dice is chosen.''',
                'difficulty': 'R1.R1.R1',
                'concentration': 'R1',
                'scaling': [
                    {'D': 'R1', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R1.R1', 'description': 'You may change the outcome of 1 additional dice'},
                ],
            },
            {
                'name': 'Pain hex',
                'speed': '1 AP',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''Whenever target is hit, they take 1 extra psychic damage. After that they may use a 
                reaction to remove this curse if they have the required dice''',
                'difficulty': 'R1.R1.R1',
                'concentration': 'R1',
                'scaling': [
                    {'D': 'R1', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R1.R1', 'description': 'Target takes 1 additional psychic damage when hit'},
                ],
            },
            {
                'name': 'Maddening hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''At the beginning of their turn, the hexed creature gets 1 level of either disoriented or 
                    afraid.
                    ''',
                'difficulty': 'R1.R1.R1.R1',
                'concentration': 'R1',
                'scaling': [
                    {'D': 'R1', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R1.R1', 'description': 'Hexed creature also gets 1 level of the other status effect'},
                ],
            },
            {
                'name': 'Mage bane hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''The mana cost for all spells is doubled
                    ''',
                'difficulty': 'R1.R1.R1',
                'concentration': 'R1',
                'scaling': [
                    {'D': 'R1', 'description': 'Increase the strength of this curse up 1 level'},
                ],
            },
            {
                'name': 'Shattering Shriek',
                'speed': '2 AP',
                'range': '12 sq',
                'target': '1 creature',
                'effect': '''A extremely loud shriek hits, heard loudest by the target. It deals 2 psychic damage and
                    the target has to give up concentration of 1 spell.
                    ''',
                'difficulty': 'R1.R1.R1.R1',
                'scaling': [
                    {'D': 'R1', 'description': 'deal additional 3 psychic damage'},
                ],
            },
            # {
            #     'name': 'Paranoia',
            #     'speed': '2 AP',
            #     'target': '1 creature',
            #     'duration': '1 minute',
            #     'effect': '''Target must make your spell DC check. On failure their disposition to one random ally
            #         changes to hostile. When target is still hostile to players, they may still choose to attack the
            #         players instead, but if presented with a convenient opportunity they may attack that ally instead.
            #         ''',
            #     'difficulty': 7,
            #     'scaling': [
            #         {'D': 5, 'L': 1, 'description': '''The ally is no longer random, but chosen by you'''},
            #     ],
            # },
            {
                'name': 'Weapon of horrors',
                'target': '1 weapon',
                'duration': '3 rounds',
                'effect': '''This weapon requires 1 less power dice to make an attack
                    ''',
                'difficulty': 'R1.R1.R1.R1',
                'concentration': 'R1.R1',
                'scaling': [
                    {'D': 'R1.R1', 'L': 2, 'description': '''When that weapon deals at least 6 damage with an attack, 
                    target enemy gets 1 level of afraid
                    '''},
                    {'D': 'R1.R1', 'description': '''Target weapon deals 1 additional psychic damage per power dice 
                    spent'''}
                ],
            },
        ]
    },
    'Illusion': {
        'special_rules': [
            """
            """
        ],
        'spells': [
            {
                'name': 'False threats',
                'target': 'area',
                'range': '6 sq.',
                'radius': '1 sq.',
                'effect': '''Pose an illusionary threat to enemies in the area, they gain 2 levels of disoriented
            ''',
                'difficulty': 'R4.R4.R4.R4',
                'scaling': [
                    {'D': 'R4.R4', 'L': 3, 'description': '''Everyone get 1 additional level of disoriented'''},
                    {'D': 'R4', 'L': 3, 'description': '''One target within radius gets 1 additional level of 
                    disoriented'''},
                ],
            },
            {
                'name': 'Side step',
                'speed': 'reaction',
                'target': '1 creature',
                'effect': '''When a hit would hit you, you may instead move 1 sq. to your chosen direction without
                provoking any attacks of opportunities and the attack misses.
            ''',
                'difficulty': 'R4.R4.R4',
                'scaling': [
                    {'D': 'R4.R4', 'L': 2, 'description': '''Target gains 1 level of disoriented'''},
                ],
            },
            {
                'name': 'Create illusionary images',
                'effect': '''You create illusionary images in the space around you, which can impress, surprise, deceive 
                etc. This is a creative spell so please refer to the creative spell section in the glossary                
            ''',
                'difficulty': 'R4.??',
            },
            # {
            #     'name': 'Mirror image',
            #     'speed': '2 AP',
            #     'target': 'empty space(s)',
            #     'range': '6 sq.',
            #     'duration': '5 rounds',
            #     'effect': '''A mirror illusion copy of you appears, who mirrors your actions and confuses enemies.
            #     They have an AC of 10 + your effective AC bonus from martial path. When someone attacks you there is a
            #     equal chance for them to attack a illusion instead of you. When they hit the illusion, the illusion
            #     disappears.
            # ''',
            #     'difficulty': 1,
            #     'scaling': [
            #         {'D': '2/3/5/7', 'L': 4, 'description': 'You summon an additional illusion'},
            #         {'D': 3, 'L': 1, 'description': ''''When you land a hit on an enemy, one illusion also lands an hit
            #             and the enemy must make your spell DC will save or suffer half your hit's damage as psychic
            #             damage. If he succeeds, the illusion disappears however'''},
            #     ],
            # },
            {
                'name': 'Invisibility',
                'target': 'self',
                'duration': '2 rounds',
                'concentration': 'R4.R4',
                'effect': '''You appear invisible as long as you are standing still. When you move, cast spells, attack
    or otherwise perform a action with rapid movement, there are ripples that hint others that there is somewhere there
    where you are and also the nature of the movement. Attacks against enemies that rely on sight have advantage, and
    attacks by enemies against you who rely on sight have disadvantage. This allows you to sneak in broad daylight.
    
    This can also be used as a creative spell during scenes. In this case the cost is RX.R?? where X is the dice used
    in the scene and R?? is the roll target.
            ''',
                'difficulty': 'R4.R4.R4.R4',
                'scaling': [
                    {'D': 'R4', 'L': 1, 'description': '''When you move at half speed, then no ripple is creating so you
                    have perfect invisibility. This allows you to sneak in broad daylight with advantage'''},
                    {'D': 'R4.R4', 'L': 1, 'description': '''Casting spells no longer creates ripples.'''},
                    {'D': 'R4.R4.R4.R4', 'L': 1, 'description': '''Attacking no longer creates ripples. This gives you
                    double advantage for attacks'''},
                    {'D': 'R4.R4', 'L': 1, 'description': '''You can select another ally as the target of this spell. This
                    spell gains the range of touch. To maintain the illusion the target must remain within line of sight
                    from you.'''},

                ],
            },
            {
                'name': 'Shattering presence',
                'target': 'self',
                'concentration': 'R4.R4.R4',
                'duration': '3 rounds',
                'effect': '''Your existance becomes questionable as you start to blur, and appear to be in multiple close places at once.
        It becomes hard to see target you. Any offensive spell or attack targeting you has a 50 % chance to 
        fail.
        ''',
                'difficulty': 'R4.R4.R4.R4.R4',
                'scaling': [
                    {'D': 'R4.R4', 'L': 1,
                     'description': 'You can target another creature. This spell gains a range of '
                                    '6 sq.'},
                ],
            },
            {
                'name': 'Hide large object',
                'target': 'Some object',
                'concentration': 'X/2 mana',
                'duration': '1 day',
                'effect': '''
        This is a ritual to hide, for eample a house, or an entrance to a cave, or if you go really wild, then even
        a castle. The idea is to create an illusion so that something doesn't appear to be there even though it is.
        
        The basic version can conceal an object that is no more than 5mx5mx5m in volume and requires 8 dice to
        succeed, however larger objects can be attempted to be concealed for more dice. Let the final resulting number
        of dice be X. That X is required for concentration cost
        ''',
                'difficulty': '8 X R4',
                'scaling': [
                    {'D': '3 X R4',
                     'description': 'increase the maximum length of one of the dimension by 5m'},
                ],
            },
        ]
    },
    'divination': {
        'spells': [
            {
                'name': 'Diviners advantage',
                'target': 'self',
                'effect': '''Increase your maximum defenses by 2 and recover all maximum defenses.''',
                'difficulty': 'R5.R5.R5.R5',
                'concentration': 'R5.R5',
                'duration': '2 rounds',
                'scaling': [
                    {'D': 'R5', 'L': 3, 'description': '''Increase maximum defense by another 2
                    '''},
                ],
            },
            {
                'name': 'Glimpse into future',
                'effect': '''During scene you can ask a question about the scene to which GM answers honestly either 
yes / no / yes and no / yet uncertain''',
                'difficulty': 'R5.R5.R5.R5',
                'scaling': [
                    {'D': 'R5.R5', 'L': 1, 'description': '''
                        Ask another follow-up question.
                    '''},
                ],
            },

        ]
    },
}
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style
from reportlab.lib import colors
import re
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def prep_spell_flowable(spell):
    elements = []
    elements.append(Paragraph(spell['name'], style=minor_title))
    data = [
        [f"Difficulty: {spell.get('difficulty')}", f"Target: {spell.get('target', '-')}", f"Range: {spell.get('range', '-')}", f"Area radius: {spell.get('radius', '-')}"],
        [f"Duration: {spell.get('duration', '-')}", f"Concentration: {spell.get('concentration', 'NO')}", "", ""]
    ]
    table = Table(data, colWidths=[120]*4)
    table.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)

    elements.append(Paragraph(spell['effect'], style=basic_paragraph_style))
    data = []
    # style = ParagraphStyle(name='Table Cell', fontSize=12, textColor='black', textWrap=True)
    for scaling in spell.get('scaling', []):
        description = re.sub('\s+', ' ', scaling['description'])
        data.append([f"Add cost: {scaling['D']}", f"Use limit: {scaling.get('L', 'unlimited')}", Paragraph(description, basic_paragraph_style)])
    if data:
        table = Table(data, colWidths=[100, 100, 280])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    table_overall = Table([[x] for x in elements], colWidths=[490])
    table_overall.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
    ]))


    return [KeepTogether([table_overall]), Spacer(480, 15)]
    # return [table_overall, Spacer(480, 15)]


def get_spells_chapter():
    elements = [
        {'type': 'title', 'content': 'Spells'},

    ]

    for name, school in schools.items():
        elements.append({'type': 'subtitle', 'content': name})
        for rule in school.get('special_rules', []):
            elements.append({'type': 'paragraph', 'content': rule})

        for spell in school['spells']:
            elements.append({'type': 'flowables', 'content': prep_spell_flowable(spell)})

    return elements
