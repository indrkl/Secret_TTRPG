schools = {
    'Force': {
        'spells': [
            {
                'name': 'Push/pull',
                'speed': '2A',
                'range': '24 m.',
                'effect': '''Move target away from you or towards you for 4 m. Halve the distance for large creatures
                and those wearing heavy armor. Huge and larger creatures cannot be moved this way. After being moved
                the target needs to check for balance.''',
                'target': 'single',
                'difficulty': 0,
                'scaling': [
                    {'D': '1/1/2/2/3/3', 'L': 6, 'description': '''increase the move distance by 4 m. The target needs to make an 
                    additional check for balance'''},
                    {'D': 3, 'description': '''For the purposes of moving the target and balance checks the creature is 
                    considered to not be wearing heavy armor and also to be one size smaller'''},
                ],
            },
            {
                'name': 'Explosive force',
                'speed': '2A',
                'range': '24 m.',
                'effect': '''A force pushes everyone around target point 2 m. away from the point and they must check
                for balance 4 times''',
                'target': 'single',
                'radius': '2m',
                'difficulty': 3,
                'scaling': [
                    {'D': 1, 'L': 4, 'description': '''Have them check for balance one more time'''},
                    {'D': 3, 'description': ''''''},
                ],
            },
            {
                'name': 'Wall of force',
                'speed': '2A',
                'range': '24 m.',
                'effect': '''Create a 4 m. long wall. arrows that would fly through this area, lose their speed and
                fall on the ground. It takes 4 m. worth of movement and 2 stamina to go through the wall of force''',
                'concenctration': 1,
                'difficulty': 2,
                'scaling': [
                    {'D': 1, 'description': '''increase the length by 4 m.'''},
                    {'D': 2, 'description': '''At the beginning of each of your rounds you can move the position of the
                    wall'''},
                    {'D': 3, 'description': '''It requires 4 additional m. worth of movement and 2 stamina to go 
                    through the wall
                    of force'''},
                ],
            },
            {
                'name': 'Force field',
                'speed': '2A',
                'range': 'touch',
                'target': 'self',
                'duration': '5 rounds',
                'concenctration': 1,
                'effect': '''Increase your AC proficiency by 1
                ''',
                'difficulty': 0,
                'scaling': [
                    {'D': '1/1/2/2/3/3', 'L': 6, 'description': '''
                        Gain an armor bonus of at least 2/3/4/5/6/7
                    '''},
                    {'D': 1, 'description': '''increase AC proficiency by 1.'''},
                    {'D': 3, 'description': '''Choose fire, cold, lightning or physical, gain resistance to the chosen
                    damage type.'''},
                ]
            },

        ]
    },
    'Nature': {
        'spells': [
            {
                'name': '''Nature's bounty''',
                'effect': '''After learning this spell, when trying to find food, or otherwise survive in the 
                wilderness, you can use your nature proficiency instead of survival skill to make the checks.'''
            },
            {
                'name': 'Heal',
                'speed': '2A',
                'range': 'touch',
                'effect': '''A willing target rolls 1 of their hit dice and an additional 1d8 and heals that much HP.
                If the target does not roll 1 of their hit dice, this spell has no effect.''',
                'target': 'single',
                'difficulty': 0,
                'scaling': [
                    {'D': 1, 'description': 'Heal additional 1d8'},
                    {'D': 1, 'description': 'remove a level of poison'},
                    {'D': 1, 'description': 'remove a level of burning'},
                    {'D': 1, 'description': 'remove a level of freezing'},
                ],
            },
            {
                'name': 'Grant luck',
                'speed': '2A',
                'range': 'touch',
                'target': 'single',
                'effect': '''Until the beginning of your next round all attacks the target makes are lucky
                ''',
                'difficulty': 2,
                'scaling': [
                    {'D': 2, 'description': 'All attacks made against the target are unlucky'},
                    {'D': 3, 'description': 'All status effect checks target makes are lucky'},
                ],
            },
            {
                'name': 'Rejuvenation',
                'speed': '1A',
                'range': 'touch',
                'effect': 'Target gains 1 stamina recovery',
                'target': 'single',
                'difficulty': 0,
                'concentration': 1,
                'scaling': [
                    {'D': 2, 'description': 'Target gains 1 additional stamina recovery'},
                ],
            },
            {
                'name': 'Enhance poison',
                'speed': '2A',
                'range': 'touch',
                'effect': '''This enhancement can be applied to weapons which are coated with poison. Target weapon 
                which is coated with poison applies 1 additional stack per attack that hits, this additional stack does 
                not spend a poison stack from the weapon.''',
                'target': 'single',
                'duration': '3 rounds',
                'difficulty': 3,
                'concentration': 1,
                'scaling': [
                    {'D': 5, 'description': 'Apply an additional stack per attack that hits.'},
                ],
            },
            {
                'name': 'Entangling roots',
                'speed': '2A',
                'range': '12m',
                'radius': '2m',
                'target': 'area',
                'effect': '''Requires being in the wild. Roots grow from the ground and entangle anyone. 
                    Anyone starting their round or entering the area of effect gain 2 levels of entangled''',
                'difficulty': 1,
                'concentration': 2,
                'scaling': [
                    {'D': '1/2', 'L': 2, 'description': 'Increase radius by  2 m'},
                    {'D': '2', 'L': 5, 'description': '''Anyone starting their round or entering the area of effect 
                        gains 1 additional levels of entangled'''},
                    {'D': 1,
                     'description': '''Anyone starting their round or entering the area of effect take 1d6 piercing 
                        damage'''},
                ],
            },
        ]
    },
    'Harmony': {
        'special_rules': [
            """You can use harmony proficiency instead of diplomacy when
                interacting with large crowds, or individuals who are not evil, power hungry or emotionless."""
        ],
        'spells': [
            {
                'name': 'Guardian',
                'speed': '2 AP',
                'target': 'self',
                'effect': '''When target has the raised shield status, that shield AC bonus applies also to their allies
        within 2 m. of the target. (creature can have only 1 active shield AC bonus).
            ''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 3, 'L': 1, 'description': '''This spell can target others. Gaining the range of touch.'''},
                    {'D': 2, 'L': 2, 'description': '''Increase the shield AC bonus range by 2 m.'''},
                    {'D': 5, 'L': 1, 'description': '''If the target is willing, he may direct an attack onto them for
            all attacks made to an ally with this spell's shield AC bonus.'''},
                    {'D': 4, 'L': 2, 'description': '''Increase target's shield AC bonus by 1'''},

                ],
            },
            {
                'name': 'Valor',
                'speed': '2 AP',
                'target': 'touch',
                'effect': '''When target successfully hits an enemy, they recover 1 stamina, but no more than their maximum 
        stamina.
            ''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 2, 'description': '''Target recovers one additional stamina per hit'''},
                    {'D': 3, 'L': 1, 'description': '''Target gains inspiration on a critical hit'''},
                    {'D': 5, 'L': 1, 'description': '''When target hits critically, his next attack is lucky'''},

                ],
            },
            {
                'name': 'Clarity',
                'speed': '2 AP',
                'target': '1 creature',
                'effect': '''Remove 1 lvl from all negative status effects related to WILL saving throws.
            ''',
                'difficulty': 3,
                'scaling': [
                    {'D': 2, 'L': 2, 'description': '''Remove one additional level from those status effects'''},
                    {'D': 3, 'description': 'target one additional creature'},
                ],
            },
            {
                'name': 'Clear mind',
                'speed': '1 AP',
                'target': '1 creature',
                'range': '6 m.',
                'duration': '10 min',
                'effect': '''Remove hexes from the target, the next time target would be unlucky doing d20 check, make the 
        check normal instead
            ''',
                'difficulty': 2,
                'scaling': [
                    {'D': 3, 'description': 'target one additional creature'},
                ],
            },
            {
                'name': 'Unity',
                'speed': '1 AP',
                'range': '10 m',
                'target': '1 creature',
                'effect': '''Target has a +2 magical bonus to attacks and spell DCs against creatures that damaged any 
        target's ally since the beginning of target's last turn.
        ''',
                'difficulty': 0,
                'concentration': 1,
                'scaling': [
                    {'D': 2, 'L': 2, 'description': '''Increase the bonus by additional +1'''},
                    {'D': 2, 'description': 'target one additional creature'},
                ],
            },
            {
                'name': 'Clear heart',
                'speed': '1 AP',
                'target': '1 creature',
                'range': '10 m.',
                'duration': '1 hour',
                'effect': '''Target's diplomacy check get +5 magical bonus. The target has to be someone other than you.
            The target can only use this bonus when trying to persuade, or otherwise engage in friendly and 
            cooperative diplomacy.''',
                'difficulty': 7,
                'concentration': 'full',
                'scaling': [
                    {'D': 4, 'description': 'Increase the bonus by additional +1'},
                    {'D': 3, 'description': '''This bonus may be used on any diplomacy check, however if it doesn't meet the 
                initial requirements, there is a 50% chance that you lose concentration and may not cast any harmony 
                spells until the next day. The bonus still applies for that check.'''},
                ],
            },
        ]
    },
    'Elemental': {
        'spells': [
            {
                'name': 'Fireball',
                'speed': '2A',
                'range': '24 m.',
                'effect': 'Deal 1d8 fire damage to everyone in the area. Then they check for burning.',
                'save': 'REFLEX',
                'target': 'area',
                'difficulty': 0,
                'radius': '5ft',
                'scaling': [
                    {'D': 1, 'description': 'Deal additional 1d8 fire damage'},
                    {'D': 2, 'description': 'They check for burning an additional time'},
                ],
            },
            {
                'name': 'Tremor',
                'speed': '2A',
                'range': '12 m.',
                'effect': '''everyone in the target area check for unbalanced twice. At the beginning of your round,
                when you continue to concentrate on this spell, you may move the center of tremor up to 4 m. Then
                the unbalanced checks are done for all creatures in the new area of effect. When you are outside the 
                range of the tremor you lose concentration.''',
                'target': 'area',
                'difficulty': 0,
                'concentration': 1,
                'radius': '5ft',
                'scaling': [
                    {'D': 1, 'description': 'They need to check for unbalanced an additional time'},
                ],
            },
            {
                'name': 'Frostbite',
                'speed': '2A',
                'range': '24 m.',
                'effect': '''Target needs to check for freezing twice''',
                'target': 'single target',
                'difficulty': 1,
                'scaling': [
                    {'D': 1, 'description': 'Deal additional 1d6 cold damage'},
                    {'D': 3, 'L': 3, 'description': 'Target must make an additional freezing check'},
                ],
            },
            {
                'name': 'Enchant weapon',
                'speed': '2A',
                'range': 'touch',
                'effect': '''Choose fire, cold or lightning. Enchant target not enchanted weapon. 
                Target weapon deals 1d6 extra damage of the chosen damage type with every attack that it hits''',
                'target': 'single weapon',
                'difficulty': 1,
                'duration': '3 rounds',
                'concentration': 1,
                'scaling': [
                    {'D': 3, 'description': 'target weapon deals an additional 1d6 damage'},
                    {'D': 9, 'L': 1, 'description': '''You need to have chosen cold. Convert all physical damage target weapon
                        does to cold damage. Each time that weapon hits an enemy. They must check for freezing against
                        your spell DC for each damage dice added by this spell.
                    '''},
                    {'D': 7, 'L': 1, 'description': '''You need to have chosen lightning. Convert all physical damage 
                        target weapon does to lightning damage. Each time that weapon hits an enemy, the enemy must
                        check for disoriented against your spell DC for each damage dice added by this spell.
                    '''},
                    {'D': 5, 'L': 1, 'description': '''You need to have chosen fire. Convert all physical damage 
                        target weapon does to fire damage. Each time that weapon hits an enemy, the enemy must
                        check for burning against your spell DC for each damage dice added by this spell.
                    '''},
                ],
            },
            {
                'name': 'Haste',
                'speed': '2A',
                'range': '12 m.',
                'effect': '''Target gains an additional AP in their turns. 
                    Only 1 buff can grant additional APs to a character.''',
                'difficulty': 3,
                'target': 'single',
                'concentration': 2,
                'scaling': [
                    {'D': 6, 'L': 1, 'description': 'Upgrades the buff to grant 2 APs instead'},
                ],
            },
            {
                'name': 'Shatter rock',
                'speed': '2A',
                'range': '6 m.',
                'radius': '1 m.',
                'target': 'area',
                'effect': 'Break stone into small pieces in the radius of effect',
                'difficulty': 4,
                'scaling': [
                ],
            },
            {
                'name': 'Clean water',
                'speed': '1 minute',
                'range': 'touch',
                'target': 'vessel filled with water',
                'effect': '''Clean a water in a constrained vessel''',
                'difficulty': 0,
                'scaling': [
                ],
            },

        ]
    },
    'Dimension': {
        'spells': [
            {
                'name': 'Pass object',
                'speed': '1 AP',
                'range': '12 m.',
                'target': '1 creature',
                'effect': '''Teleport a tiny object weighing no more than 1 kg. onto the possession of another willing 
                creature. You can place it on them whereever you would like.''',
                'difficulty': 0,
                'scaling': [
                    {'D': 1, 'description': '''Increase the max object weight by 1 kg'''},
                    {'D': 1, 'L': 1, 'description': '''When passing a potion onto a willing subject, they can also drink
                    it and receive it's benefit immediately'''},
                    {'D': 3, 'L': 1, 'description': '''When passing a vial of poison onto a willing subject, you can
                    coat their melee weapon or next arrow with that poison vial instead'''},
                ],
            },
            {
                'name': 'Communicate',
                'speed': '1 round',
                'range': '1 km.',
                'target': 'Anyone(known)',
                'effect': '''Send a short message over a long distance. If recipient is within the range of the spell, 
                    they will hear that and may choose to reply shortly.''',
                'difficulty': 0,
                'scaling': [
                    {'D': 1, 'description': 'double the range'},
                    {'D': 4, 'L': 1, 'description': '''open a line of steady communication with the target, it stays 
                    open as long as you concentrate 3, concentration does not consume additional mana'''},
                    {'D': 3, 'L': 1, 'description': 'You can have another party member do the communicating.'},
                ],
            },
            {
                'name': 'Blink jump',
                'speed': '2 AP',
                'range': '16 m.',
                'target': 'empty space',
                'effect': '''Instantly disappear from your current location without provoking any attacks of opportunity
                    and reappear in the target location''',
                'difficulty': 2,
                'scaling': [
                ],
            },
            {
                'name': 'Teleport',
                'speed': '30 minutes',
                'range': '1 km.',
                'effect': '''Teleports a none disoriented person within your touch range to a place within range 
                that you know or can imagine. If this place is not a teleportation circle, then they need to make a 
                DC 12 fortitude save, if they fail, they get 2 levels of disoriented, this effect can only be removed by 
                doing a long rest.''',
                'difficulty': 3,
                'scaling': [
                    {'D': 2, 'description': 'double the range'},
                ],
            },
            {
                'name': 'Step between dimensions',
                'speed': '3 AP',
                'target': 'self',
                'effect': '''You become corporeal becoming unaffected by all effects in the material plane.
                    By default you cannot attack, cast spells or concentrate on spells in a way that would affect anyone
                    in the material plane.''',
                'difficulty': 5,
                'concentration': 1,
                'scaling': [
                    {'D': 4, 'description': '''You may cast spells that would affect the material plane'''},
                    {'D': 5, 'description': '''This spell can target any willing creature. This spell gains a range 
                        of touch.'''},
                    {'D': 8, 'description': '''This spell can target any creature. This spell gains a range 
                        of touch.'''},
                    {'D': 3, 'description': '''You may concentrate on spells that would affect the material plane'''},

                ],
            },

        ]
    },
    'Discord': {
        'special_rules': [
            """Regarding hexes. Each creature can by default have only 1 hex placed on them. This can be overwritten
        by certain very rare feats. Any creature with a hex on them may spend 1 AP to attempt to remove that hex from 
        them, make a Will check against spell casters DC, if successful the hex is removed. Hexes cannot be applied to 
        your allies to override hexes by your enemies. However if an ally has hexed a creature, then your hex would 
        override their hex(s), unless you are able to place multiple hexes on the enemy"""
        ],
        'spells': [
            {
                'name': 'Enfeeble hex',
                'speed': '1 AP',
                'range': '12 m.',
                'target': '1 creature',
                'effect': '''Target's hit rolls are unlucky. Whenever exactly one of their dice would succeed on an
                unlucky roll (other than saving throw against this hex), they may roll a WILL saving throw against spell 
                DC to break this hex.''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 4, 'description': 'Their damage rolls are also unlucky'},
                    {'D': 6, 'description': 'Their saving throws are unlucky'},
                ],
            },
            {
                'name': 'Pain hex',
                'speed': '1 AP',
                'range': '12 m.',
                'target': '1 creature',
                'effect': '''Whenever target is hit, they take 1d6 extra psychic damage and they may spend 
                    their reaction to roll a WILL saving throw  against spell DC to break this hex. If they succeed they 
                    still take the damage for this time.''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 3, 'description': 'Increase the damage they take by 1d6'},
                ],
            },
            {
                'name': 'Maddening hex',
                'speed': '1 AP',
                'range': '12 m.',
                'target': '1 creature',
                'effect': '''At the beginning of their turn, the hexed creature gets 1 level of either disoriented,
                    afraid or crazed. To reduce 1 level of any effects gained through this hex, they can spend 1 AP to
                    make a WILL saving through against your spell DC. On a critical success they lose 3 levels divided 
                    by any of these effects as they choose.
                    ''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 3, 'L': 1, 'description': 'It takes 2 AP to attempt to remove this hex'},
                    {'D': 5, 'L': 2, 'description': 'Hexed creature also gets 1 level of one of the other effects'},
                ],
            },
            {
                'name': 'Mage bane hex',
                'speed': '1 AP',
                'range': '12 m.',
                'target': '1 creature',
                'effect': '''The mana cost for all spells is increased by 2
                    ''',
                'difficulty': 1,
                'concentration': 1,
                'scaling': [
                    {'D': 3, 'L': 1,  'description': 'It takes 2 AP to attempt to shake this hex off'},
                    {'D': 1, 'description': 'The mana cost for all spells is increased by additional 1'},
                ],
            },
            {
                'name': 'Shattering Shriek',
                'speed': '2 AP',
                'range': '24 m.',
                'target': '1 creature',
                'effect': '''A extremely loud shriek hits, heard loudest by the target. It deals 1d8 psychic damage and
                    the target has to make your spell DC WILL save or give up concentration of 1 spell.
                    ''',
                'difficulty': 0,
                'scaling': [
                    {'D': 3, 'L': 1, 'description': 'The target makes a DC WILL save for each spell they are concentrating on'},
                    {'D': 1, 'description': 'deal additional 1d8 psychic damage'},
                ],
            },
            {
                'name': 'Shattering presence',
                'speed': '1 AP',
                'target': 'self',
                'concentration': 1,
                'duration': '3 rounds',
                'effect': '''Your existance becomes questionable as you start to blur, and appear to be in multiple close places at once.
                    It becomes hard to see target you. Any offensive spell or attack targeting you has a 50 % chance to 
                    fail.
                    ''',
                'difficulty': 5,
                'scaling': [
                    {'D': 5, 'L': 1, 'description': '''Concentration doesn't consume APs'''},
                    {'D': 5, 'L': 1, 'description': 'You can target another creature. This spell gains a range of 12 m.'},
                ],
            },
            {
                'name': 'Paranoia',
                'speed': '2 AP',
                'target': '1 creature',
                'duration': '1 minute',
                'effect': '''Target must make your spell DC check. On failure their disposition to one random ally 
                    changes to hostile. When target is still hostile to players, they may still choose to attack the 
                    players instead, but if presented with a convenient opportunity they may attack that ally instead.
                    ''',
                'difficulty': 7,
                'scaling': [
                    {'D': 5, 'L': 1, 'description': '''The ally is no longer random, but chosen by you'''},
                ],
            },
            {
                'name': 'Weapon of horrors',
                'speed': '2 AP',
                'target': '1 weapon',
                'duration': '3 rounds',
                'effect': '''Critical threshold for attacks with the target weapon is reduced by 3
                    ''',
                'difficulty': 3,
                'scaling': [
                    {'D': '2/3', 'L': 2, 'description': '''Critical threshold is further reduced by 1'''},
                    {'D': '5', 'L': 2, 'description': '''When you hit target critically, they must check once for 
                    disoriented or afraid, your choice
                    '''},
                    {'D': 2, 'description': '''Critical hits deal additional 2 damage'''}
                ],
            },
        ]
    },
    'Illusion': {
        'special_rules': [
            """You can use illusion proficiency when doing sneak and other
                stealth requiring checks."""
        ],
        'spells': [
            {
                'name': 'False threats',
                'speed': '2 AP',
                'target': 'area',
                'range': '12 m.',
                'radius': '2m.',
                'effect': '''Pose an illusionary threat to enemies in the area, who must check once for disoriented
            ''',
                'difficulty': 1,
                'scaling': [
                    {'D': '2/3/4', 'L': 3, 'description': '''Check for disoriented an additional time.'''},
                ],
            },
            {
                'name': 'Side step',
                'speed': 'reaction',
                'target': '1 creature',
                'effect': '''When a hit would hit you, you may instead move 2 m. to your chosen direction without
                provoking any attacks of opportunities and the attack misses.
            ''',
                'difficulty': 3,
                'scaling': [
                    {'D': 3, 'L': 2, 'description': '''Target must check for disoriented.'''},
                ],
            },
            {
                'name': 'Mirror image',
                'speed': '2 AP',
                'target': 'empty space(s)',
                'range': '12 m.',
                'duration': '5 rounds',
                'effect': '''A mirror illusion copy of you appears, who mirrors your actions and confuses enemies.
                They have an AC of 10 + your effective AC bonus from martial path. When someone attacks you there is a 
                equal chance for them to attack a illusion instead of you. When they hit the illusion, the illusion 
                disappears. 
            ''',
                'difficulty': 1,
                'scaling': [
                    {'D': '2/3/5/7', 'L': 4, 'description': 'You summon an additional illusion'},
                    {'D': 3, 'L': 1, 'description': ''''When you land a hit on an enemy, one illusion also lands an hit
                        and the enemy must make your spell DC will save or suffer half your hit's damage as psychic
                        damage. If he succeeds, the illusion disappears however'''},
                ],
            },
            {
                'name': 'Create illusions',
                'speed': '2 AP',
                'target': 'empty space(s)',
                'range': '24 m.',
                'duration': '1 min.',
                'concentration': 1,
                'effect': '''Ceate a static illusion within range occupying 2 m. cube area
            ''',
                'difficulty': 0,
                'scaling': [
                    {'D': 3, 'L': 1, 'description': '''Illusions can be animated and you can alter their position
                    during your turn.'''},
                    {'D': 2, 'description': '''Create 1 additional static illusion within range occupying 2mx2mx2m of 
                    space'''},
                    {'D': 3, 'L': 1, 'description': '''Each illusion can instead occupy a 10x10x10 feet cube's space'''},
                    {'D': 3, 'L': 1, 'description': '''The duration is instead 1 hour'''},
                ],
            },
            {
                'name': 'Invisibility',
                'speed': '2 AP',
                'target': 'self',
                'duration': '1 min.',
                'concentration': 1,
                'effect': '''You appear invisible as long as you are standing still. When you move, cast spells, attack
    or otherwise perform a action with rapid movement, there are ripples that hint others that there is somewhere there
    where you are and also the nature of the movement. Attacks against enemies that rely on sight have advantage, and
    attacks by enemies against you who rely on sight have disadvantage. This allows you to sneak in broad daylight.
            ''',
                'difficulty': 3,
                'scaling': [
                    {'D': 3, 'L': 1, 'description': '''When you move at half speed, then no ripple is creating so you
                    have perfect invisibility. This allows you to sneak in broad daylight with advantage'''},
                    {'D': 5, 'L': 1, 'description': '''Casting spells no longer creates ripples.'''},
                    {'D': 4, 'L': 1, 'description': '''You can select another ally as the target of this spell. This
                    spell gains the range of touch. To maintain the illusion the target must remain within line of sight
                    from you.'''},

                ],
            },
        ]
    },
    # 'divination': {
    #     'spells': [
    #         {
    #             'name': 'Diviners advantage',
    #             'speed': '2 AP',
    #             'target': 'self',
    #             'effect': '''Gain a magical 1 AC bonus. (you can have only 1 magical bonus to AC)''',
    #             'difficulty': 1,
    #             'concentration': 1,
    #             'scaling': [
    #                 {'D': 3, 'L': 3, 'description': '''Increase this bonus by 1
    #                 '''},
    #                 {'D': 5, 'L': 1, 'description': '''At the start of every turn gain a dodge token if you have none.
    #                 '''},
    #
    #             ],
    #         },
    #         {
    #             'name': 'Glimpse into future',
    #             'speed': 'reaction',
    #             'effect': '''This can be cast as a reaction to when GM has someone in your party to roll a skill check.
    #             Learn the DC of the skill check''',
    #             'difficulty': 2,
    #             'scaling': [
    #                 {'D': 3, 'L': 1, 'description': '''Learn of the negative consequences when failing the skill check
    #                 '''},
    #                 {'D': 5, 'L': 1, 'description': '''Grant advantage to the skill check'''},
    #
    #             ],
    #         },
    #         {
    #             'name': 'Tell fortune',
    #             'speed': '5 minutes',
    #             'target': 'group focus',
    #             'effect': '''Learn of the number of progress steps completed and total required to complete the group
    #             focus
    #         ''',
    #             'difficulty': 3,
    #             'scaling': [
    #                 {'D': 5, 'L': 1, 'description': '''Gain advantage on the next progress check, this can be used only
    #                     3 times per group focus'''},
    #                 {'D': 5, 'L': 3, 'description': '''Learn of one fail state for the group focus'''},
    #             ],
    #         },
    #     ]
    # },
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
        [f"Cast time: {spell.get('speed', '-')}", f"Duration: {spell.get('duration', '-')}", f"Concentration: {spell.get('concentration', 'NO')}", ""]
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
        data.append([f"Difficulty cost: {scaling['D']}", f"Use limit: {scaling.get('L', 'unlimited')}", Paragraph(description, basic_paragraph_style)])
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
