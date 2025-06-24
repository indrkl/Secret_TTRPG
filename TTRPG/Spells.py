# Force - 4
# Nature - 1
# Harmony - 2
# Elemental - 6
# Dimension - 3
# Discord - 5
# Illusion - 2
# Divination - 3

schools = {
    'Arcanum (intelligence)': {
        'spells': [
            {
                'name': 'Identify',
                'effect': '''A ritual to identify the magical properties of magical items. While some magical items
                might have obvious magical properties, like a flaming sword doing additional fire damage, others may
                have hidden or more complex properties that would need to be either studied, mathced with historic
                records, tested out blindly, or you could cast this ritual instead.          
                
                The final cost of the ritual depends on the complexity of the magical item.
                
                It costs 2xR1 to identify a simple but none obvious effect. It costs 4xR1 to identify more obscure 
                hidden effects, including if the item has a simple curse, that the creator tried to hide.
                
                It costs 10xR1 to identify legendary items, their properties, hidden properties and curses.
                
                It may not be obvious which kind of magical item it is. However if you spend at least 2xR1 you will
                know if it has as more obscure hidden effects. And if you spend at least 4xR1, then you you will know
                if the item is of legendary quality.
                
                Even for some legendary items you could learn some properties with either 2 or 4 xR1, but this is up
                to GM to decide.
                
                Also note that if a legendary item does not have this mid level effects, then one may not learn that
                there is more to reveal by only spending 2xR1.
        ''',
            },
            {
                'name': 'Transfer magic',
                'effect': '''A ritual to transfer magical properties from one item, to another item which could hold
                that magical property. So from a one handed weapon to another one handed weapon, or for example from
                one armor to another. You might want to do that if the weapon type of the origin weapon does not suit
                you, or if the base quality of the armor or weapon is better for the newer item. Or if you want to
                hide a magical effect by removing it from a recognised piece of jewelry to one no one knows about.
                
                Some magical effects could be weapon type or armor type specific, these in that case couldn't be moved
                to other types but to only items these properties are intended for.
                
                Doing this is a ritual costs 6xR1 for simple effects, 14xR1 for obscure effects but for legendary items,
                it costs 25xR1.
        ''',
            },
            {
                'name': 'Record memory',
                'effect': '''
                This is a magical technique where you can record what you think, feel, see, hear during the magical
                effect and store this into a cleanly cut large emerald stone costing at least 100 gp. 
                
                This can later be used to have someone else or yourself to relive these memories. 
                
                This magic is often used to record act of crime, or parts of investigation to then in the future present 
                this as evidence.
                
                The mana cost depends on the length of the campaign turn you want the recording to be done. 3 mana for
                quick turns, 6 for medium and 9 for strategic turns.
                
                Those who know this spell can also attempt to tamper these memories, though the process can either break
                the crystal, losing the memory entirely, or may be done in a way that it is clear that it has been 
                tampered with.
                
                Tampering costs twice as much mana as creating those memories in the first place, and you must roll for
                the quality of the tampering, whoever looks at those memories may attempt to roll against your quality
                in order to understand that this has been tampered with. Un suspecting NPC-s usually wouldn't do that,
                however judges or those who have reasons to not trust you will definitely do it.
        ''',
            },
            {
                'name': 'Detect magic',
                'range': '8 sq.',
                'effect': '''
            You know if there are active magical effects within range of you.
            
            The scaling of this spell is a bit more complicated. You can spend an additional R1 to be able to tell
            which school of magic the effects belong to. You can do it after you learn there are magical effects at all.
            
            You can spend an additional R1 to tell which exact spell this is.
            
            Finally you can spend another R1.R1 to learn exactly where the effect is, what it is attached to, how long
            ago it was cast, and if it has an duration, how long does it last.
            
            If you have paid all the costs then you can also tell when someone starts casting a spell within range.
            
            The additional costs don't have to be spent in the same round as initial cast.            
            ''',
                'difficulty': 'R1',
                'concentration': 'R1',
                'duration': '7 rounds',
                'scaling': [
                ],
            },
            {
                'name': 'Counterspell',
                'requires': 'Detect magic',
                'range': '8 sq.',
                'effect': '''
                In order to counter spells, you need to be detecting magic and having paid all the additional costs.
                
                When someone casts a spell, you can, as a reaction spend same amount of R1 as they spent on their spell
                to negate the effect of the spell. Both of you still spend their mana.

            ''',
                'difficulty': '?',
                'scaling': [
                    {'D': 'R1', 'L': 2, 'description': '''You get the caster of the spell to spend 2 additional mana
                    '''},
                ],
            },
            {
                'name': 'Dispel magic',
                'requires': 'Detect magic',
                'range': '8 sq.',
                'effect': '''
                In order to dispel spells, you need to be detecting magic and having paid all the additional costs.
                
                You can dispel magical effects, buffs and effects of rituals. The cost to dispel is equal to the
                cost of initial spell or ritual to cast it but in R1-s.
                
                You can dispel concentration spells / buffs / curses normally, without performing a ritual. And for
                rituals you need to perform a dispelling ritual. 
            ''',
                'difficulty': '?',
                'scaling': [
                    {'D': 'R1', 'L': 2, 'description': '''You get the caster of the spell to spend 2 additional mana
                    '''},
                ],
            },
            {
                'name': 'Control magical object usage',
                'target': 'one magical item',
                'effect': '''
                Add a zeal onto target magical item, that makes it completely unusable or permits it's use to one
                particular individual. If that individual were to die, then the zeal would simply make it unusable by
                anyone.
                
                To make the zeal, one has to perform a ritual and spend at least 3 x R1. However technically there is
                no ceiling.
                
                To break the zeal someone who knows this spell, could also perform a counter ritual, that would need
                to spend as many R1-s as was spent to make the original zeal.
                
                By initial inspection one could only tell if the number of R1 required is more or less than 10. Other
                wise as you start making the ritual, you will feel when you hit 25 %, 50 % and 75 % on your way to
                cracking the zeal. When you fail to crack the zeal and end the ritual, then 1 / 3 (rounded down) of
                the spent R1s still lower the zeals strength for future.
                
            ''',
            },
        ]
    },
    'Force (intelligence)': {
        'spells': [
            {
                'name': 'Telekinesis',
                'effect': '''You can move objects with your mind for various effects. Move a bucket of hot water on top
                of your enemies, a key from the guard to you for escape, etc.
                This is a creative spell so please refer to the creative spell section in the glossary.                
''',
            },
            {
                'name': 'Push/pull',
                'range': '8 sq.',
                'effect': '''Move target away from you or towards you for 2 sq. Halve the distance for large creatures
                and those wearing heavy armor. Huge and larger creatures cannot be moved this way.''',
                'target': 'single',
                'difficulty': 'R4',
                'scaling': [
                    {'D': 'R4', 'description': '''increase the move distance by 2 sq. Target also gets 1 level of
                    unbalanced'''},
                    {'D': 'R4.R4', 'description': '''For the purposes of moving the target and balance checks the creature is 
                    considered to not be wearing heavy armor and also to be one size smaller'''},
                ],
            },
            {
                'name': 'Explosive force',
                'range': '8 sq.',
                'effect': '''A force pushes everyone around target point 2sq. They also get 1 level of unbalanced''',
                'target': 'point',
                'radius': '1 sq',
                'difficulty': 'R4.R4',
                'scaling': [
                    {'D': 'R4', 'description': '''The force pushed them 2 additional sq.''',},
                    {'D': 'R4', 'description': '''They get 1 additional level of unbalanced.''',},
                ],
            },
            {
                'name': 'Wall of force',
                'range': '12 sq.',
                'effect': '''Create a 2 sq. long wall. arrows that would fly through this area, lose their speed and
                fall on the ground. It takes 3 sq. worth of movement to go through the wall of force''',
                'concenctration': 'R4.R4',
                'difficulty': 'R4',
                'scaling': [
                    {'D': 'R4', 'description': '''increase the length by 2 sq.'''},
                    {'D': 'R2', 'description': '''At the beginning of each of your rounds you can move the position of the
                    wall'''},
                    {'D': 'R4', 'L': 3, 'description': '''It requires 2 additional sq. worth of movement to go through the wall
                    of force'''},
                ],
            },
            {
                'name': 'Force field',
                'range': 'touch',
                'target': 'self',
                'duration': '3 rounds',
                'concenctration': 'R4.R4.R4',
                'effect': '''Increase your maximum defense to 2 (note, this does not stack with armor and is only
                useful if you don't have maximum defense from armor or natural armor).
                
                You can use force proficiency to take the defend basic action.
                ''',
                'difficulty': 'R4',
                'scaling': [
                    {'D': 'R4', 'description': '''
                        The maximum defense provided by this spell is increased by 1
                    '''},
                    {'D': 'R4.R4', 'description': '''Gain 1 damage reduction'''},
                    # {'D': 'R4.R4', 'description': '''Choose fire, cold, lightning or physical, gain resistance to the chosen
                    # damage type.'''},
                ]
            },

        ]
    },
    'Nature (cunning)': {
        'spells': [
            {
                'name': '''Nature's gifts''',
                'effect': '''After learning this spell, when trying to find food, or otherwise survive in the 
                wilderness, you can use your nature proficiency instead of survival proficiency to make the checks.
                Doing so costs no mana, and you cannot amplify this ability with mana.
                '''
            },
            {
                'name': '''Growth and Decay''',
                'effect': '''This is a creative spell. It accelerates the growth of plants for a short duration, letting
                them grow days or even weeks worth of growth within seconds. 
                
                However this comes at the expense of your health. You can restore your well being by having same or
                other plants decay at similar pace. The bio mass of the plants and severity of decay must match the
                bio mass and benefits of the growth part.'''
            },
            {
                'name': '''Strength''',
                'effect': '''This is a creative spell. You boost the strength of yourself or one of your allies. After
                learning this spell you can replace physique proficiency with nature proficiency when doing physique
                challenges requiring strength or endurance.'''
            },
            {
                'name': '''Speak with animals''',
                'effect': '''This is a creative spell. This allows you to commune with animals, and try to befriend,
                convince them, or ask them questions. They are still animals and can't understand concepts that would
                make no sense for animals, like religion, human factions, difference between human weapons etc.'''
            },
            {
                'name': 'Remove poison',
                'range': 'touch',
                'target': 'single',
                'difficulty': 'R1.R1',
                'effect': '''Remove a single stack of poison from the target''',
                'scaling': [
                    {'D': 'R1', 'description': 'remove a level of poison'},
                ],
            },
            {
                'name': 'Healing ritual',
                'range': 'touch',
                'effect': '''                
                This is a ritual. Target recovers 1 damaged die or removes all damage from wounded dice, or
                removes 1 level of burning, poison or freezing.
                
                Each act of healing that recovers dice, scars one of the recovered dice. You can recover dice through
                healing, if a none scarred dice is wounded. Scarred dice can still be recovered as the additional dice 
                with this spell. 
                ''',
                'target': 'single',
                'difficulty': '3X R1',
                'scaling': [
                    {'D': '5X R1', 'description': 'This heal recovers 1 additional damaged die'},
                    {'D': '5X R1', 'description': 'The same healing ritual applies to 1 additional target'},
                    {'D': 'R1', 'description': 'remove a level of freezing'},
                ],
            },
            {
                'name': 'Grant luck',
                'range': 'touch',
                'target': 'single',
                'effect': '''Target can change the result of one die in the dice pool when you cast and each time
                you concentrate on it
                ''',
                'difficulty': 'R1',
                'concentration': 'R1.R1.R1',
                'scaling': [
                    {'D': 'R1.R1.R1', 'description': '''Target can change another die in their dice pool'''},
                ],
            },
            {
                'name': 'Entangling roots',
                'range': '6 sq',
                'radius': '2 sq',
                'target': 'area',
                'effect': '''Requires being in the wild. Roots grow from the ground and entangle anyone. 
                    Anyone starting their round or entering the area of effect gain 2 levels of entangled''',
                'difficulty': 'R1.R1',
                'concentration': 'R1.R1',
                'scaling': [
                    {'D': 'R1', 'description': '''Anyone starting their round or entering the area of effect gain 
                    additional 1 level of entangled'''},
                    {'D': 'R1',
                     'description': '''Anyone starting their round or entering the area of effect take 2 piercing 
                        damage'''},
                ],
            },
            # {
            #     'name': 'Primal roar',
            #     'radius': '5 sq',
            #     'effect': '''You channel primal nature magic, to roar like a giant beast, causing all enemies within
            #     radius to gain 1 levels of afraid''',
            #     'difficulty': 'R1.R1.R1.R1',
            #     'scaling': [
            #         {'D': 'R1.R1', 'description': '''They get another level of afraid'''},
            #         {'D': 'R1.R1',
            #          'description': '''Your allies get advantage with their next attack'''},
            #     ],
            # },
        ]
    },
    'Harmony (social)': {
        'spells': [
            {
                'name': 'Harmonious voice',
                'effect': '''
                You encompass the essence of harmony, making you able to speak in a extremely calming, compassionate
                and convincing voice.
                This can for example help you sway large crowds, or people who are who are neither evil, power hungry 
                nor emotionless.
                
                This is a creative spell.            
''',
            },
            {
                'name': 'Guardian',
                'speed': '2 AP',
                'target': 'self',
                'radius': '1 sq.',
                'effect': '''When you have the guarded buff, then allies standing within radius. of the target also
                have that buff.
            ''',
                'difficulty': 'R2',
                'concentration': 'R2',
                'scaling': [
                    {'D': 'R4', 'L': 1, 'description': '''This spell can target others. Gaining the range of touch.'''},
                    {'D': 'R2', 'L': 1, 'description': '''Increase maximum defense of the target by 1'''},
                    {'D': 'R4.R4', 'L': 1, 'description': '''If the target is willing, he may direct an attack onto 
                    them for all attacks made to an ally within this spells radius.'''},
                ],
            },
            {
                'name': 'Clarity',
                'target': '1 creature',
                'effect': '''Remove 1 lvl from all negative status effects related to WILL saving throws.
            ''',
                'difficulty': 'R2',
                'scaling': [
                    {'D': 'R2', 'description': '''Remove one additional level from those status effects'''},
                ],
            },
            {
                'name': 'Bless',
                'range': '5 sq.',
                'target': 'up to 3 allies',
                'effect': '''
                Targets have advantage for refocus and recover actions. 
        ''',
                'difficulty': 'R2.R2',
                'concentration': 'R2.R2',
                'scaling': [
                    {'D': 'R2', 'L': 2, 'description': '''Targets have 1 additional maximum defense'''},
                    {'D': 'R2.R2', 'description': '''Targets remove 1 negative status effect at the beginning of
                     their turn for free'''},
                ],
            },
            {
                'name': 'Recover defenses',
                'range': '5 sq.',
                'target': 'area',
                'radius': '1 sq.',
                'effect': '''
All friendly allies in the targeted area recover their defenses to the maximum
        ''',
                'difficulty': 'R2.R2',
                'scaling': [
                    {'D': 'R2', 'description': '''They gain 1 temporary defense pushing their defense over their
                    maximum'''},
                ],
            },
            {
                'name': 'Harmony of souls',
                'target': 'Up to 8 willing',
                'effect': '''
                Harmony of souls is a ritual that connects the souls of the participants in a way that they sense each
                other's concerns, desires, feelings, excitement, and even though they don't hear each other's thoughts
                they get glimpses and a sense of some of the thoughts especially if those thoughts make a lot of sense
                to them or if they have similar thoughts themselves.
                
                This allows players to assist each other by spending 2 dice and one of those dice is added
                to a roll target, attack, spell, action etc. If it is added to spell then the normal 1 additional mana
                cost still applies.
        ''',
                'difficulty': '10 X R2',
                'duration': '1 day',
                'concentration': 'X / 2 mana',
                'scaling': [
                    {'D': '8 X R2', 'description': '''
                    Participants may make will actions instead of other participants. They may also do the recover
                    defenses action for other participants. 
                    '''},
                ],
            },
        ]
    },
    'Elemental (intelligence)': {
        'spells': [
            {
                'name': 'Stone speach',
                'effect': '''
                You can talk to stone and dirt in the earth, and command them to shape, shift, crumble, collapse or
                thicken. 

                This is a creative spell.            
''',
            },
            {
                'name': 'Fireball',
                'difficulty': 'R6.R6',
                'range': '8 sq.',
                'effect': 'Deal 2 fire damage to everyone in the area.',
                'save': 'REFLEX',
                'target': 'area',
                'radius': '1 sq.',
                'scaling': [
                    {'D': 'R6', 'description': 'Deal additional 2 damage'},
                    {'D': 'R6', 'description': '1 target enemy within radius gets a level of burning'},
                ],
            },
            {
                'name': 'Chain lightning',
                'difficulty': 'R6.R6',
                'range': '8 sq.',
                'effect': '''Deal 4 lightning damage to a target enemy, and then it jumps to another target enemy 
                within radius of the first target dealing 2 less damage. This jumping continues until next jump would
                 do no more damage (that means increasing the initial damage increases the number of jumps). 
                damage''',
                'save': 'REFLEX',
                'target': 'single target',
                'radius': '3 sq.',
                'scaling': [
                    {'D': 'R6', 'description': 'Increase initial damage by 2'},
                    {'D': 'R6', 'description': 'Everyone hit by chain lightning get 1 level of disoriented'},
                ],
            },
            {
                'name': 'Tremor',
                'difficulty': 'R6',
                'range': '6 sq.',
                'effect': '''everyone in the target area  gain 2 levels of unbalanced. At the beginning of your round,
                when you continue to concentrate on this spell, you may move the center of tremor up to 2 sq. When you 
                are outside the range of the tremor you lose concentration.''',
                'target': 'area',
                'concentration': 'R6',
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
                'difficulty': 'R6.R6',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'Target gets another level of freezing'},
                    {'D': 'R6', 'description': 'You get to choose which of the dice are frozen'},
                ],
            },
            {
                'name': 'Rune trap ritual',
                'range': '8 sq.',
                'effect': '''Make a trap that when triggered casts either fire-ball, chain lightning or frostbite
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
                'difficulty': 'R6.R6',
                'duration': '3 rounds',
                'concentration': 'R6.R6',
                'scaling': [
                    {'D': 'R6.R6', 'description': 'target weapon deals an additional 1 damage of the chosen type'},
                    {'D': 'R6.R6', 'L': 1, 'description': '''You need to have chosen cold. Convert all physical 
                        damage target weapon does to cold damage. Each time that weapon hits an enemy the enemy gets
                        one level of freezing
                    '''},
                    {'D': 'R6', 'L': 1, 'description': '''You need to have chosen lightning. Convert all physical damage 
                        target weapon does to lightning damage. Each time that weapon hits an enemy, the enemy
                        gets 1 levels of disoriented.
                    '''},
                    {'D': 'R6', 'L': 1, 'description': '''You need to have chosen fire. Convert all physical damage 
                        target weapon does to fire damage. Each time that weapon hits an enemy, the enemy gets one
                        level of burning.
                    '''},
                ],
            },
            # {
            #     'name': 'Haste',
            #     'range': '6 sq.',
            #     'duration': '2 rounds',
            #     'effect': '''Target gets +1 action limit haste buff. Each character can have the haste buff from only
            #     one source''',
            #     'difficulty': 'R6.R6.R6.R6',
            #     'target': 'single',
            #     'concentration': 'R6.R6',
            #     'scaling': [
            #         {'D': 'R6.R6.R6', 'L': 1, 'description': '''Haste buff provides additional +1 action limit'''},
            #     ],
            # },
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
    'Dimension (precision)': {
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
                'difficulty': 'R3',
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
                'difficulty': 'R3.R3',
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
                'difficulty': 'R3.R3.R3',
                'concentration': 'R3.R3',
                'scaling': [
                    {'D': 'R3.R3', 'description': '''Target may cast spells that would affect the material plane'''},
                    {'D': 'R3', 'description': '''This spell can target any willing creature. This spell gains a range 
                        of touch.'''},
                    {'D': 'R3.R3', 'description': '''This spell can target any creature. This spell gains a range 
                        of touch.'''},
                    {'D': 'R3', 'description': '''Target may concentrate on spells that would affect the material 
                    plane'''},
                ],
            },
        ]
    },
    'Discord (cunning)': {
        'special_rules': [
            """Regarding hexes. Each creature can by default have only 1 hex placed on them. This can be overwritten
        by certain feats. Any creature with a hex on them can make a R2.R2 remove hex action using Will proficiency
        for weak hexes, R2.R2.R2 for strong hexes and R2.R2.R2.R2 for extreme hexes. Hexes cannot be applied to 
        your allies to override hexes by your enemies. However if an ally has hexed a creature, then your hex would 
        override their hex(s) if their hex is weaker or equal to your hex's strength, unless you are able to place 
        multiple hexes on the enemy."""
        ],
        'spells': [
            {
                'name': 'Enfeeble hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''Now and each time target enemy rolls, you may change the outcome 1 dice. It has to be a
                different dice than was changed by lucky condition, if the enemy was lucky and is done after the lucky
                dice is chosen.''',
                'difficulty': 'R5',
                'concentration': 'R5',
                'scaling': [
                    {'D': 'R5', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R5.R5', 'description': 'You may change the outcome of 1 additional dice'},
                ],
            },
            {
                'name': 'Pain hex',
                'speed': '1 AP',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''Whenever target is hit, they take 1 extra psychic damage. After that they may use a 
                reaction to remove this curse if they have the required dice''',
                'difficulty': 'R5',
                'concentration': 'R5.R5',
                'scaling': [
                    {'D': 'R5', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R5.R5', 'description': 'Target takes 1 additional psychic damage when hit'},
                ],
            },
            {
                'name': 'Maddening hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''At the beginning of their turn, the hexed creature gets 1 level of either disoriented or 
                    afraid.
                    ''',
                'difficulty': 'R5.R5',
                'concentration': 'R5.R5.R5',
                'scaling': [
                    {'D': 'R5', 'description': 'Increase the strength of this curse up 1 level'},
                    {'D': 'R5.R5', 'description': 'Hexed creature also gets 1 level of the other status effect'},
                ],
            },
            {
                'name': 'Mage bane hex',
                'range': '6 sq.',
                'target': '1 creature',
                'effect': '''The mana cost for all spells is doubled
                    ''',
                'difficulty': 'R5.R5',
                'concentration': 'R5.R5',
                'scaling': [
                    {'D': 'R5', 'description': 'Increase the strength of this curse up 1 level'},
                ],
            },
            {
                'name': 'Shattering Shriek',
                'speed': '2 AP',
                'range': '12 sq',
                'target': '1 creature',
                'effect': '''A extremely loud shriek hits, heard loudest by the target. It deals 2 psychic damage and
                    the target has to give up concentration of 1 spell. This damage ignores defenses and damage 
                    reduction.
                    ''',
                'difficulty': 'R5.R5',
                'scaling': [
                    {'D': 'R5', 'L': 3, 'description': 'deal additional 2 psychic damage'},
                    {'D': 'R5', 'L': 1, 'description': 'Target loses concentration of one additional spell'},
                ],
            },
            {
                'name': 'Pain sharing',
                'range': 'touch',
                'target': '1 creature',
                'duration': '2 rounds',
                'effect': '''Buff an ally, so that when they take damage to their health, then whoever caused that
                damage takes the same amount of psychic damage. This psychic damage ignores damage reduction and 
                defense.
                    ''',
                'difficulty': 'R5.R5',
                'concentration': 'R5.R5.R5',

                'scaling': [
                    {'D': 'R5.R5.R5', 'description': '''The one dealing the damage also gets 1 levels of disoriented for 
                    every 2 damage dealt rounded up'''},
                    {'D': 'R5.R5', 'description': '''For each damage dealt, you siphon 1 mana back to yourself.'''},
                ],
            },
            {
                'name': 'Weapon of horrors',
                'target': '1 weapon',
                'duration': '3 rounds',
                'effect': '''Enchant a weapon, weapon cannot be magical or be otherwise enchanted with another effect.
                    This weapon requires 1 less power dice to make an attack.
                    ''',
                'difficulty': 'R5.R5',
                'concentration': 'R5.R5',
                'scaling': [
                    {'D': 'R5.R5', 'L': 2, 'description': '''When that weapon deals at least 6 damage with an attack, 
                    target enemy gets 1 level of afraid
                    '''},
                    {'D': 'R5.R5', 'description': '''Target weapon deals 1 additional psychic damage per power dice 
                    spent'''},
                    {'D': 'R5.R5', 'description': '''When the weapon kills a hexed enemy with this weapon, 
                    immediately cast the hex on another target'''},
                ],
            },
            {
                'name': 'Dread',
                'target': '1 enemy',
                'duration': '2 rounds',
                'effect': '''Target enemy gets 2 levels of afraid, when target is killed while under the effect of this
                spell, Another target of your choice gets all the levels of afraid of the killed enemy and becomes the
                new target of this spell.  
                    ''',
                'difficulty': 'R5.R5.R5',
                'concentration': 'R5.R5.R5',
                'distance': '6 sq.',
                'scaling': [
                    {'D': 'R5.R5', 'L': 2, 'description': '''When target is killed ,then 1 additional level of afraid
                    is passed to the new target
                    '''},
                    {'D': 'R5', 'description': '''Target gets an additional level of afraid'''},
                    {'D': 'R5', 'description': '''When you pay the concentration cost, also deal psychic damage to
                     the target equal to the number of levels of afraid on him.'''},
                ],
            },
            {
                'name': 'Darkness',
                'target': 'any square',
                'duration': '2 rounds',
                'range': '8 sq.',
                'radius': '2 sq.',
                'effect': '''
Darkness sweeps from the target point and all natural light gets vanquished in the target area. Only those with dark
vision can peer through. Those inside it are blinded unless they have dark vision or blind sight. In addition, while
inside the darkness, characters cannot remove hexes or remove disoriented or afraid stacks.

Every time you pay the concentration cost, you can move the cloud of darkness by up to 4 sq. from the original spot.
                    ''',
                'difficulty': 'R5.R5',
                'concentration': 'R5.R5.R5',
                'scaling': [
                    {'D': 'R5.R5', 'L': 1, 'description': '''Even those with dark vision cannot see through this
                    cloud of darkness and while being inside it, they are blinded. Only blind sight helps against this.
                    '''},
                    {'D': 'R5', 'L': 1, 'description': '''You can see hexed enemies inside the darkness and while being
                    inside the darkness, you are not treated as being blind against hexed enemies.
                    '''},
                ],
            },
        ]
    },
    'Illusion (cunning)': {
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
                'difficulty': 'R2.R2',
                'scaling': [
                    {'D': 'R2', 'L': 3, 'description': '''Everyone get 1 additional level of disoriented'''},
                    {'D': 'R2', 'L': 3, 'description': '''One target within radius gets 1 additional level of 
                    disoriented'''},
                ],
            },
            {
                'name': 'Block sight',
                'target': 'creature',
                'range': '6 sq.',
                'duration': '1 round',
                'effect': '''Block target's sight with an illusion making them effectively blind.
            ''',
                'difficulty': 'R2.R2',
                'concentration': 'R2.R2',
                'scaling': [
                    # {'D': 'R2.R2', 'L': 3, 'description': '''Everyone get 1 additional level of disoriented'''},
                ],
            },
            {
                'name': 'Side step',
                'speed': 'reaction',
                'target': '1 creature',
                'effect': '''When a hit would hit you, you may instead move 1 sq. to your chosen direction without
                provoking any attacks of opportunities and the attack misses.
                ''',
                'difficulty': 'R2.R2',
                'scaling': [
                    {'D': 'R2.R2', 'L': 2, 'description': '''Target gains 1 level of disoriented'''},
                ],
            },
            {
                'name': 'Create illusionary images',
                'effect': '''You create illusionary images in the space around you, which can impress, surprise, deceive 
                etc. This is a creative spell so please refer to the creative spell section in the glossary                
            ''',
                'difficulty': 'R2.??',
            },
            {
                'name': 'Disguise self',
                'effect': '''You use illusions to disguise yourself as someone else, in order to deceive other people
                into believing you are that person. In order to do that convincingly, you would still need to know
                what that person looks like, how they behave, what are their mannerism, how they talk and so on.
                
                This is a creative spell.         
            ''',
                'difficulty': 'R2.??',
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
                'concentration': 'R2.R2.R2',
                'effect': '''You appear invisible as long as you are standing still. When you move, cast spells, attack
    or otherwise perform a action with rapid movement, there are ripples that hint others that there is somewhere there
    where you are and also the nature of the movement. Attacks against enemies that rely on sight have advantage, and
    attacks by enemies against you who rely on sight have disadvantage. This allows you to sneak in broad daylight.
    
    This can also be used as a creative spell during campaign turns.
            ''',
                'difficulty': 'R2.R2.R2',
                'scaling': [
                    {'D': 'R2', 'L': 1, 'description': '''When you move at half speed, then no ripple is creating so you
                    have perfect invisibility. This allows you to sneak in broad daylight'''},
                    {'D': 'R2.R2', 'L': 1, 'description': '''Casting spells no longer creates ripples.'''},
                    {'D': 'R2.R2.R2', 'L': 1, 'description': '''Attacking no longer creates ripples. This gives you
                    double advantage for attacks'''},
                    {'D': 'R2.R2', 'L': 1, 'description': '''You can select another ally as the target of this spell. 
                    This spell gains the range of touch. To maintain the illusion the target must remain within line of 
                    sight from you.'''},

                ],
            },
            {
                'name': 'Shattering presence',
                'target': 'self',
                'concentration': 'R2.R2.R2',
                'duration': '3 rounds',
                'effect': '''Your existance becomes questionable as you start to blur, and appear to be in multiple 
                close places at once.
        It becomes hard to target you. Any offensive spell or attack targeting you has a 50 % chance to 
        fail.
        ''',
                'difficulty': 'R2.R2.R2',
                'scaling': [
                    {'D': 'R2.R2', 'L': 1,
                     'description': '''You can target another creature instead of yourself. This spell gains a range of
                    6 sq.'''},
                    {'D': 'R2.R2', 'L': 1,
                     'description': '''When a spell or attack does hit you, you can give up dice with a total sum of 6
                     to negate that after all.'''},
                ],
            },
            {
                'name': 'Hide large object',
                'target': 'Some object',
                'concentration': 'X/2 mana',
                'duration': '1 day',
                'effect': '''
        This is a ritual to hide, for example a house, or an entrance to a cave, or if you go really wild, then even
        a castle. The idea is to create an illusion so that something doesn't appear to be there even though it is.
        
        The basic version can conceal an object that is no more than 5mx5mx5m in volume and requires 8 dice to
        succeed, however larger objects can be attempted to be concealed for more dice. Let the final resulting number
        of dice be X. That X is required for concentration cost
        ''',
                'difficulty': '8 X R2',
                'scaling': [
                    {'D': '3 X R2',
                     'description': 'increase the maximum length of one of the dimension by 5m'},
                ],
            },
        ]
    },
    'divination (intelligence)': {
        'spells': [
            {
                'name': 'Diviners advantage',
                'target': 'self',
                'effect': '''Increase your maximum defenses by 2 and recover all defenses (defense is not
                recovered every round, only those rounds when concentration cost is paid).''',
                'difficulty': 'R3.R3.R3',
                'concentration': 'R3.R3.R3',
                'duration': '2 rounds',
                'scaling': [
                    {'D': 'R3.R3', 'L': 3, 'description': '''Increase maximum defense by another 1''',},
                    {'D': 'R3.R3.R3', 'L': 1, 'description': '''
                    Your attacks go through defense directly and cannot be dodged unless the enemy also has diviners
                    advantage.'''},
                ],
            },
            {
                'name': 'Divine sight',
                'target': 'self',
                'effect': '''Gain blind sight of 6 sq.''',
                'difficulty': 'R3',
                'concentration': 'R3',
                'duration': '1 rounds',
                'radius': '6 sq.',
                'scaling': [
                ],
            },
            {
                'name': 'Glimpse into future',
                'effect': '''During campaign turn you can ask a question about the campaign turn to which GM answers 
                honestly either yes / no / yes and no / yet uncertain''',
                'difficulty': 'R3.R3',
                'scaling': [
                    {'D': 'R3', 'L': 1, 'description': '''
                        Ask another follow-up question.
                    '''},
                ],
            },
            {
                'name': 'See beyond the veil',
                'difficulty': 'R3',
                'effect': '''
                Reveal the difficulty of some challenge in the future based on assumptions you have to list to GM.
                ''',
            },
            {
                'name': 'Divine guidance',
                'difficulty': 'R3.R3',
                'effect': '''
Think of an object or person, and get a sense of which direction you should go to get closer to the person / object.
It doesn't reveal the distance or place of the target, only the direction.
                ''',
            },
        ],
    'dreams (social)': [
        {
            'name': 'Sweet dreams',
            'effect': '''
                Ritual to enhance sleep of the target, making them rest real good, see good dreams, and awaken really
                well rested and energetic.
                
                Target gets various benefits for a medium turn after waking up. For starter, they get advantage with a 
                single ability of your choice.
            ''',
            'difficulty': '8 X R1',
                'scaling': [
                    {'D': '4 X R1', 'description': 'Gain advantage with one other additional ability of your choice',},
                    {'L': 3, 'D': '4 X R1', 'description': 'Have 2 additional stamine',},
                    {'L': 2, 'D': '4 X R1', 'description': '+1 defense',},
                ],
        },
        {
            'name': 'Sleep',
            'effect': '''
                Put someone to sleep for 8 h with a total remaining HP of at most 6, target is woken by taking further 
                damage.
            ''',
            'difficulty': 'R1.R1',
            'scaling': [
                {'D': 'R.1', 'description': 'Increase the HP limit by 4', },
                {'D': 'R1.R1.R1', 'description': 'Nothing can wake the target for the duration'}
            ],
        },
        {
            'name': 'Enter nightmare',
            'effect': '''
                Ritual to learn a vulnerability of someone by making them see their worst fears and you also witnessing
                it. The ritual cost scales by the power of the individual. For a commoner it starts at 6 dice, for
                stronger individuals like veteran soldiers, squad leaders, beginning mages, somewhat enduring 
                individuals it increases to 10 dice. 
                
                Against expert mages, strong leaders, heroes, mighty beasts it increases to 20 dice.
                
                Against legendary creatures, mages or heroes, mightiest of emperors, dragons etc. it increases to 50 
                dice.
                
                Against Gods and god-like mages it increases to 200 dice.
                
                Against mightier beings entering the nightmare can also pose risks and damage those part taking in the
                ritual, or even killing them.
            ''',
            'difficulty': '6 X R1',
        },
        {
            'name': 'Enter dream',
            'effect': '''
                Ritual to learn a what target wants, desires, dreams about.
                
                The ritual cost scales by the power of the individual. For a commoner it starts at 4 dice, for
                stronger individuals like veteran soldiers, squad leaders, beginning mages, somewhat enduring 
                individuals it increases to 8 dice. 
                
                Against expert mages, strong leaders, heroes, mighty beasts it increases to 17 dice.
                
                Against legendary creatures, mages or heroes, mightiest of emperors, dragons etc. it increases to 40 
                dice.
                
                Against Gods and god-like mages it increases to 140 dice.
                
                Against mightier beings you run the risk of not comprehending what is going on, while the risk of
                psychic damage is not severe usually, it may occur, confusion, disorientation, losing touch of reality
                may however be common occurrence when part taking this ritual.
            ''',
        },
        {
            'name': 'Commune with the unknown',
            'effect': '''
                Ritual
                You can state what you want to learn about, and then as you sleep, you enter a dream of someone
                you may not know, but can help you or guide you, and through that you learn something what you desire,
                but there are risks, since those you commune with will also learn about you. The ritual difficulty
                depends on what you want to learn.
                
                Something known to many commoners in the vicinity, even if not spoken publicly: 4 X R1
                
                Something known to few commoners in the vicinity, or a larger group of elite soldiers, mages, etc. 10 X R1
                
                Something known to only a few elite soldiers, mages, mighty lords: 20 X R1
                
                Something known to only 1 or 2 individuals in the world: 50 X R1.
                
                Be careful however, since if you enter a dream of a mightier being, a powerful mage, for example, they
                could learn about you, attempt to hide what they know still, deceive you, or even harm you in the dream
                world. Especially dangerous are other mages who understand the magic of dreams.
            ''',
        },
        {
            'name': 'Dream travel',
            'effect': '''
                Travel around the dream worlds of local inhabitants, it is all wierd and mushy, but if you do it
                regularly, you do learn if there is a shift in the air, either, if there is more hope, more fear,
                something specific impacting the psychy of the population, or if some silent sorcery is at play against
                the population.
                
                            
            ''',
        },
    ]
    },
}
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style, add_dice_images
from reportlab.lib import colors
import re
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def prep_spell_flowable(spell):
    elements = []
    elements.append(Paragraph(spell['name'], style=minor_title))
    data = [
        [Paragraph(f"Cost: {add_dice_images(spell.get('difficulty', ''))}", style=basic_paragraph_style), f"Target: {spell.get('target', '-')}", f"Range: {spell.get('range', '-')}", f"Area radius: {spell.get('radius', '-')}"],
        [f"Duration: {spell.get('duration', '-')}", Paragraph(f"Concentration: {add_dice_images(spell.get('concentration', 'NO'))}", style=basic_paragraph_style), "", ""]
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
        data.append([Paragraph(f"+ {add_dice_images(scaling['D'])}", style=basic_paragraph_style), f"Use limit: {scaling.get('L', 'unlimited')}", Paragraph(description, basic_paragraph_style)])
    if data:
        table = Table(data, colWidths=[70, 100, 310])
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
