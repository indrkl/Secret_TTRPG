story_teller_barbarian = {
    'MARTIAL': 4,
    'MAGE': 0,
    'SKILLED': 2,
    'Levels': {
        1: {
            'Innate_feat_martial': 'Versatile combatant',
            'Innate_feat_skilled': 'Skilled (Lore)',
            'Martial advancements': [
                'rage feat', '1 proficiency in 2 handed Swords',
            ],
            'Skilled advancements': [
                '2 profciency in Lore',
            ]
        },
        2: {
            'Martial advancements': [
                'enrage feat', '1 stamina recovery',
            ],
            'Skilled advancements': [
                '1 luck token',
            ]
        },
        3: {
            'Martial advancements': [
                '2 proficiency in 2 handed Swords', '2 in max stamina'
            ],
            'Skilled advancements': [
                '1 luck token',
            ]
        },
        4: {
            'Martial advancements': [
                '2 proficiency in 2 handed Swords', '2 in AC bonus'
            ],
            'Skilled advancements': [
                '2 profciency in Lore',
            ]
        },
        5: {
            'Innate_feat_martial': 'Vigorous / Life stealer',
            'Innate_feat_skilled': 'Lucky',
            'Martial advancements': [
                'Heavy armor feat'
            ],
            'Skilled advancements': [
                'Inspiring',
            ],
            'Summary at level 5': '''We have rage, and while we do so we have 8 stamina recovery and 9 maximum stamina.
                We can wear heavy armor, which provides us at least 5 additional AC, and we get 2 AC bonus from our martial advancement, totalling us +17 AC
                Considering that most enemies have +1 or +2 to hit at this level, this is quite OK. While we rage we can
                do an exerted rampage attack every other turn. Next level we will be able to do it every turn. And even 
                out of rage we can do normal enrage almost every turn. So we are a very scary beast. Finally we have 2 luck tokens,
                and we can either use it to be lucky in some of our attacks or to inspire our allies in skill checks.                
                '''

        },
    }
}
blood_mage = {
    'MARTIAL': 0,
    'MAGE': 4,
    'SKILLED': 2,
    'Levels': {
        1: {
            'Innate_feat_mage': 'Metamagician',
            'Innate_feat_skilled': 'Skilled (Survival)',
            'Mage advancements': [
                'Blood magic (illusion x2, False threats)', 'Enduring, large, tricky and distant magic for free'
            ],
            'Skilled advancements': [
                'Agent of chaos',
            ]
        },
        2: {
            'Mage advancements': [
                'advance in discord, 2 daily limit, shattering shriek',
            ],
            'Skilled advancements': [
                '2 x advance in survival',
            ]
        },
        3: {
            'Mage advancements': [
                'Mind expertise (disoriented), once in discord', '1 daily limit'
            ],
            'Skilled advancements': [
                '2 x advance in lore',
            ]
        },
        4: {
            'progression_feats': ['Mastery (illusion)', 'Resourceful'],
            'Mage advancements': [
                'Quick magic, mind expertise (crazed), Invisibility'
            ],
            'Skilled advancements': [
                'twice in will (gain ref and fort as well)',
            ]
        },
        5: {
            'Mage advancements': [
                'Trickster (illusion, ecnounter limit, side-step', 'learn painful hex'
            ],
            'Skilled advancements': [
                '1 x in luck, quick mind',
            ],
            'Summary at level 5': '''
                This trickster blood mage is a proper agent of chaos. Not only can he cast difficulty 8 (or 9 if sacrificing 2 hit dice)
                false threats making it check 3 times, boost it with metamagic to make the area larger or simply add to
                DC by tricky magic, and you can boost it even more once. Ending up with a DC of 10 + 6 (proficiency) +
                2 (trickster) + 1 or 2 (tricky magic) = 19-20 DC, 3 times. Few will succeed, any of them. Because of Mind
                expertise they even gain 1 extra. Together with Agent of chaos and a successful ambush, you can just
                start the combat with pervertedly strong advantage. Add quick magic casted of crazed, which checks twice
                but again with DC 20, and second mind expertise, the enemies action economy is fucked. They are fucked.
                Without magical aid, they will not recover :D . And since you probably don't want to spend too many hit
                dice you can just start preparing on a next vicious ploy to fuck the enemy over.
                '''
        },
    }
}

nasty_barbarian = {
    'MARTIAL': 4,
    'MAGE': 2,
    'SKILLED': 0,
    'Levels': {
        1: {
            'Innate_feat_mage': 'Divine Protector (actually quite an undivine protector)',
            'Innate_feat_martial': 'Defiant',
            'Mage advancements': [
                'Mind expertise (afraid)'
            ],
            'Martial advancements': [
                'Rage (2 handed sword, max stamina, stamina recovery)',
            ]
        },
        2: {
            'Mage advancements': [
                'Will, lore',
            ],
            'Martial advancements': [
                '4 x 2 handed sword',
            ]
        },
        3: {
            'Mage advancements': [
                'daily limit, heal'
            ],
            'Martial advancements': [
                'Medium armor, max stam',
            ]
        },
        4: {
            'progression_feats': ['', 'Stamina related'],
            'Mage advancements': [
                'Speak with animals'
            ],
            'Martial advancements': [
                'stam recovery, double strike',
            ]
        },
        5: {
            'Mage advancements': [
                'adept atuner, nature magic x 2'
            ],
            'Martial advancements': [
                'Fury, 2 x max stamina',
            ],
            'Summary at level 5': '''
                You're a beast. Your survivability really comes from defiance, and hopefully some of your allies. Even
                if you are not super tanky, the enemy will have really fucked up choices. Damage you and provide you
                fury tokens, or attack someone else and end up being afraid by your intimidation. Either way you are 
                going to come hard on them during your turn as you waste you burn your stamina on double strikes and 
                normal attacks. You start with 25 stamina, and recover 6 while raging. Ally that is able to rejuvenate 
                you is super valuable, since that effect gets doubled. Either way, wouldn't want to face you.
                When playing together with trickster, consider taking Shadow instead of medium armor for added offense
                and alternate defenses :P .
                '''
        },
    }
}

Hexer_archer = {
    'MARTIAL': 3,
    'MAGE': 3,
    'SKILLED': 0,
    'Levels': {
        1: {
            'Innate_feat_martial': 'Favored weapon (bow)',
            'Innate_feat_mage': 'Versatile magician',
            'Martial advancements': [
                'hex archer feat (enfeeble hex)'
            ],
            'Mage advancements': [
                'Hex master feat',
            ],
        },
        2: {
            'Martial advancements': [
                '1 in bow proficiency, 1 in stamina recovery'
            ],
            'Mage advancements': [
                '1 in discord proficiency, 1 in daily cast limit (also get encounter cast limit), learn Pain hex',
            ]
        },
        3: {
            'Martial advancements': [
                'light armor proficiency, Accuracy feat'
            ],
            'Mage advancements': [
                '1 in discord proficiency, 2 in daily cast limit (also get encounter cast limit)',
            ]
        },
        4: {
            'Martial advancements': [
                '2 bow proficiency, 1 maximum stamina'
            ],
            'Mage advancements': [
                '2 in discord proficiency, 1 in WILL saving throws',
            ]
        },
        5: {
            'Innate_feat_martial': 'Harmonious body',
            'Innate_feat_mage': 'Dual magic (discord and dimensionality)',
            'Martial advancements': [
                '1 bow proficiency, 2 fortitude saving throw'
            ],
            'Mage advancements': [
                '2 in daily cast limit, learn blink jump spell',
            ],
            'Summary at level 5': '''Character is proficient with bow, off-setting the composite-bow -6 penalty. 
                While doing the special hexing attack, they get another +5, and then a +2 making critical hits against
                everyone but mostly heavily defended opponents very likely. He has 3 stamina recovery, and 7 max stamina
                meaning he can try to make a normal attack and 2 hex strikes the first round, if lucky hexing the enemy completely,
                and he can continue doing a normal attack and hex strike in consequintive rounds. Since he doesn't need to concentrate on hexes,
                he can spam them also on secondary enemies, providing control through enfeeble hex and damage with his critical strikes and maddening hex.
                Finally by choosing dual magic, he becomes proficient with dimension magic as well, allowing him to blink jump, gaining range
                on anyone trying to approach him.'''
        },
    }
}

Dirty_rogue = {
    'MARTIAL': 3,
    'MAGE': 0,
    'SKILLED': 3,
    'Levels': {
        1: {
            'Innate_feat_martial': 'Favored weapon (dagger)',
            'Innate_feat_skilled': 'Everything is connected (roguery and treasure finding)',
            'Martial advancements': [
                'backstab'
            ],
            'Skilled advancements': [
                'Planner (treasure hunting), 1 luck token',
            ],
        },
        2: {
            'Martial advancements': [
                '1 in dagger proficiency, 1 in stamina recovery'
            ],
            'Skilled advancements': [
                '1 roguery proficiency, 1 luck token',
            ]
        },
        3: {
            'Martial advancements': [
                '1 AC, 1 dagger proficiency, 1 max stamina'
            ],
            'Skilled advancements': [
                'Lucky finder',
            ]
        },
        4: {
            'Martial advancements': [
                'medium armor proficiency'
            ],
            'Skilled advancements': [
                '2 fortitude save, 1 reflex save',
            ]
        },
        5: {
            'Innate_feat_martial': 'Versatile (gain 2 AC, 1 luck token',
            'Innate_feat_skilled': 'Lucky',
            'Martial advancements': [
                '1 stamina recovery, 1 max stamina'
            ],
            'Skilled advancements': [
                'Foresight', '1 fortitude save'
            ],
            'Summary at level 5': '''Character is a dangerous disorienting back stabber in combat. Out of combat,
                he is a sneaky rogue, who is constantly planning for the group how to find the next big treasure.
                Also, he has great foresight, and whenever party find needing to have some very specific items little
                item, it turns out he had thought of that beforehand.
                '''
        },
    }
}

Wise_man = {
    'MARTIAL': 0,
    'MAGE': 2,
    'SKILLED': 4,
    'Levels': {
        1: {
            'Innate_feat_mage': 'Dual magic (Nature, Harmony)',
            'Innate_feat_skilled': 'Wild magic',
            'Mage advancements': [
                '1 in nature, 1 in daily limit, learn unity and rejuvenation'
            ],
            'Skilled advancements': [
                'Planner (diplomacy), 1 luck token',
            ],
        },
        2: {
            'Mage advancements': [
                '1 daily limit, 1 encounter limit'
            ],
            'Skilled advancements': [
                'Advance 1 in lore, 1 in crafting, 1 luck token',
            ]
        },
        3: {
            'Mage advancements': [
                '1 nature, learn heal'
            ],
            'Skilled advancements': [
                'Advance 2 in lore, 1 luck token',
            ]
        },
        4: {
            'Mage advancements': [
                '1 daily limit, 1 encounter limit'
            ],
            'Skilled advancements': [
                'Advance 1 in lore, 1 in crafting, 1 luck token',
            ]
        },
        5: {
            'Innate_feat_mage': 'Favoured magic (harmony)',
            'Innate_feat_skilled': 'Lucky',
            'Mage advancements': [
                '1 in nature, learn clarity'
            ],
            'Skilled advancements': [
                'Advance 1 in diplomacy, 1 in crafting, 1 luck token'
            ],
            'Summary at level 5': '''This character is lucky, and can use his luck to cast variety of spells using
                Wild magic. That is of course a very limited and expensive resource. He can also use simple harmony
                and nature magic. But where he really shines is his out of combat skill sets. He is exception diplomat,
                but has become very learned in the lore of land, and finally has connections with various crafter guilds.
            '''
        },
    }
}

Priest_warrior = {
    'MARTIAL': 3,
    'MAGE': 2,
    'SKILLED': 1,
    'Levels': {
        1: {
            'Innate_feat_mage': 'Favoured magic (nature)',
            'Innate_feat_marital': 'Versatile',
            'Innate_feat_skilled': 'Specialist (diplomacy)',
            'Mage advancements': [
                '1 in nature, 2 in encounter limit, learn heal'
            ],
           'Martial advancements': [
                'medium armor proficiency, shield proficiency, 1 max stamina, 1 in swords'
            ],
            'Skilled advancements': [
                '1 in diplomacy, Offer them to surrender',
            ],
        },
        2: {
            'Mage advancements': [
                '1 encounter limit, 1 in nature'
            ],
            'Martial advancements': [
                '1 max stamina, double strike feat, 1 AC'
            ],
            'Skilled advancements': [
                '1 in diplomacy',
            ],
        },
        3: {
            'Mage advancements': [
                '1 will and 1 encounter limit'
            ],
            'Martial advancements': [
                '1 AC, 1 in sowrds, Quirky fighter'
            ],
            'Skilled advancements': [
                '1 in fortitude',
            ],
        },
    }
}

Priest_warrior2 = {
    'MARTIAL': 4,
    'SKILLED': 2,
    'Levels': {
        1: {
            'Innate_feat_marital': 'Versatile',
            'Innate_feat_skilled': 'Lucky',
           'Martial advancements': [
                'medium armor proficiency, shield proficiency, 1 max stamina, 2 in swords, 1 in AC'
            ],
            'Skilled advancements': [
                '1 in diplomacy, Offer them to surrender', '1 luck token'
            ],
        },

    }
}

Priest_warrior3 = {
    'MARTIAL': 4,
    'MAGE': 2,
    'Levels': {
        1: {
            'Innate_feat_marital': 'Nimble',
            'Innate_feat_mage': 'Shifter?? HArmony, Divine protector??',
           'Martial advancements': [
                'shield proficiency, 1 max stamina, 2 in swords, 2 in AC'
            ],
            'Mage advancements': [
                'spells: guardian, unity, encounter cast limit, harmony proficiency',
                'other ideas: heal? raw caster, luck. Rejuvenation, heal.'
            ],
        },
    }
}

Priest_warrior4 = {
    'MARTIAL': 4,
    'MAGE': 2,
    'Levels': {
        1: {
            'Innate_feat_martial': 'Nimble',
            'Innate_feat_mage': 'Harmony',
           'Martial advancements': [
               'Holy warrior, 1 stamina recovery, (1 max stamina, 1 in swords)',
               '2 in swords, 2 in AC',
           ],
           'Mage advancements': [
               'spells: unity, 2 encounter cast limit, harmony proficiency',
               'spells: rejuvenation, 1 encounter cast limit'
           ],
        },
    }
}

Forgetful_mage = {
    'MAGE': 4,
    'SKILLED': 2,
    'Levels': {
        1: {
            'Innate_feat_mage': 'Advanced senses',
            'Innate_feat_skilled': 'Specialist (smth)',
            'Mage advancements': [
                '''1 in dimension, 1 in daily cast limit, 1 in communicate, 1 in lore, 1 in encounter cast limit'''
            ],
            'Skilled advancements': [
                '1 in luck, 1 in smth else',
            ],
        },
        2: {
            'Mage advancements': [
                '1 encounter limit, 1 in nature'
            ],
            'Martial advancements': [
                '1 max stamina, double strike feat, 1 AC'
            ],
            'Skilled advancements': [
                '1 in diplomacy',
            ],
        },
        3: {
            'Mage advancements': [
                '1 will and 1 encounter limit'
            ],
            'Martial advancements': [
                '1 AC, 1 in sowrds, Quirky fighter'
            ],
            'Skilled advancements': [
                '1 in fortitude',
            ],
        },
    }
}

xd6_characters = [
    {
        'name': 'assassin',
        'MAGE': 2,
        'MARTIAL': 4,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Shifter',
                'Innate_feat_marital': 'Advanced senses',
                'Mage advancements': [
                    '''first illusion proficiency, false threats spell'''
                ],
                'Martial advancements': [
                    'first and second knife proficiency, first toughness proficiency',
                ],
            },
            2: {
                'Mage advancements': [
                    '''2 mana, second illusion proficiency'''
                ],
                'Martial advancements': [
                    'Shadow feat, Two weapon fighter feat',
                ],
            },
            3: {
                'Mage advancements': [
                    '''first will proficiency, 1 mana'''
                ],
                'Martial advancements': [
                    'Backstabber feat',
                ],
            },
        },
        'equipment': ['axe', 'dagger', '2 MD leather armor'],

    },
    {
        'name': 'elementalist',
        'MAGE': 4,
        'SKILLED': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Raw caster',
                'Innate_feat_skilled': 'Natural armor',
                'Mage advancements': [
                    '''first elemental proficiency, second elemental proficiency, fireball spell'''
                ],
                'Skilled advancements': [
                    'first lore proficiency, 1 luck',
                ],
            },
            2: {
                'Mage advancements': [
                    '''Pyromancy feat, first dimension proficiency, pass object spell, 1 mana'''
                ],
                'Skilled advancements': [
                    'Second lore proficiency, 2 luck',
                ],
            },
            3: {
                'Mage advancements': [
                    '''third elemental proficiency, 1 mana'''
                ],
                'Skilled advancements': [
                    'first will proficiency, first fortitude proficiency',
                ],
            },
        },
        'equipment': ['staff', 'robes (no armor)', '2 healing potions'],

    },
    {
        'name': 'Mastermind',
        'MAGE': 4,
        'SKILLED': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Raw caster',
                'Innate_feat_skilled': 'Specialist (leader',
                'Mage advancements': [
                    '''first and second discord proficiency, 'Weapon of horrors' spell'''
                ],
                'Skilled advancements': [
                    'first leadership proficiency, 1 luck',
                ],
            },
            2: {
                'Mage advancements': [
                    '''Enchanter feat, first elemental proficiency, 1 mana, enchant weapon spell'''
                ],
                'Skilled advancements': [
                    'Mastermind',
                ],
            },
            3: {
                'Mage advancements': [
                    '''second elemental proficiency, chain lightning, 1 mana'''
                ],
                'Skilled advancements': [
                    'Second leadership proficiency',
                ],
            },
        },
        'equipment': ['staff', 'robes (no armor)', '2 healing potions'],

    },
    {
        'name': 'Paladin',
        'MARTIAL': 4,
        'MAGE': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Divine protector',
                'Innate_feat_martial': 'Warcaster',
                'Mage advancements': [
                    '''1 harmony proficiency, guardian spell'''
                ],
                'Martial advancements': [
                    'Heavy armor proficiency, first sword proficiency',
                ],
            },
            2: {
                'Mage advancements': [
                    '''first and second toughness proficiency, 1 mana'''
                ],
                'Martial advancements': [
                    'Holy warrior feat, first shield proficiency, second sword proficiency',
                ],
            },
            3: {
                'Mage advancements': [
                    '''2 mana'''
                ],
                'Martial advancements': [
                    'first physique proficiency, second shield proficiency, 1 stamina',
                ],
            },
        },
        'equipment': ['sword', 'shield', '2 MD leather armor'],
    },
    {
        'name': 'Holy savage',
        'MARTIAL': 4,
        'MAGE': 2,
        'Levels': {
            1: {
                'Innate_feat_mage': 'Divine protector',
                'Innate_feat_martial': 'Defiant',
                'Mage advancements': [
                    '''first toughness proficiency, first will proficiency'''
                ],
                'Martial advancements': [
                    'first and second two handed axe proficiency, 1 stamina',
                ],
            },
            2: {
                'Mage advancements': [
                    '''second toughness and will proficiency'''
                ],
                'Martial advancements': [
                    'Savage axe and power strike feats',
                ],
            },
            3: {
                'Mage advancements': [
                    '''first force proficiency and push/pull'''
                ],
                'Martial advancements': [
                    '3 stamina, first physique proficiency',
                ],
            },
        },
        'equipment': ['Two handed axe', '2 MD leather armor'],
    },
    {
        'name': 'Inspiring leader',
        'SKILLED': 4,
        'MARTIAL': 2,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Prodigy',
                'Innate_feat_martial': 'Advanced senses',
                'Skilled advancements': [
                    '''first and second leadership proficiency, first diplomacy proficiency'''
                ],
                'Martial advancements': [
                    'first bow proficiency and first fortitude proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Inspiring, Inspiring leader, first survival proficiency, 3 luck'''
                ],
                'Martial advancements': [
                    'second bow proficiency and first toughness and physique proficiency',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''third leadership proficiency, 1 luck'''
                ],
                'Martial advancements': [
                    'second toughness proficiency',
                ],
            },
        },
        'equipment': ['axe', 'shield', '3 MD, 1 DR padding and chain mail heavy armor combo'],
    },
    {
        'name': 'Trickster',
        'SKILLED': 3,
        'MAGE': 3,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Lucky',
                'Innate_feat_mage': 'Raw caster',
                'Skilled advancements': [
                    '''first and second survival proficiency'''
                ],
                'Mage advancements': [
                    'first illusion proficiency, 1 mana, false threats',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Agent of chaos, 1 luck'''
                ],
                'Mage advancements': [
                    'Trickster feat, maddening hex spell, second illusion proficiency',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''3 luck'''
                ],
                'Mage advancements': [
                    'first and second discord proficiency' ,
                ],
            },
        },
        'equipment': ['staff', '2 MD leather armor'],
    },
    {
        'name': 'Sentinel',
        'SKILLED': 2,
        'MARTIAL': 4,
        'Levels': {
            1: {
                'Innate_feat_skilled': 'Specialist (survival)',
                'Innate_feat_martial': 'Defiant',
                'Skilled advancements': [
                    '''first survival and diplomacy proficiency'''
                ],
                'Martial advancements': [
                    'first polearm proficiency and second polearm proficiency, 1 stamina',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''Foresight, 1 luck, first physique proficiency'''
                ],
                'Martial advancements': [
                    'Sentinel and heavy armor feat',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''Second survival proficiency'''
                ],
                'Martial advancements': [
                    'third polearm proficiency, 1 stamina' ,
                ],
            },
        },
        'equipment': ['spear', '3 MD, 1 DR padding and chain mail heavy armor combo'],
    },
]

player_characters = [
    {
        'name': 'Jack of all trades',
        'SKILLED': 2,
        'MARTIAL': 2,
        'MAGE': 2,
        'defense': 4,
        'Innate_feat_skilled': 'Lucky',
        'Innate_feat_martial': 'Extraordinary senses',
        'Innate_feat_mage': 'Shifter',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): diplomacy''',
                    '''proficiency (first): lore''',
                    # '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    'proficiency (first): illusion',
                    'spell: Side step',
                ],
                'Martial advancements': [
                    'feat: Medium armor proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (first): crafting''',
                    '''proficiency (first): treasure hunting''',
                    '''feat: Foresight'''

                ],
                'Mage advancements': [
                    'feat: Commune with animals',
                    '''proficiency (first): will''',
                    '''1 mana'''

                ],
                'Martial advancements': [
                    'feat: Medium armor proficiency',
                    '''proficiency (first): sword''',
                    '1 stamina'

                ],

            },
            3: {
                'Skilled advancements': [
                    '''2 luck'''
                ],
                'Mage advancements': [
                    'proficiency (second): illusion',
                ],
                'Martial advancements': [
                    '''proficiency (second): sword''',
                ],
            },
        },
        'equipment': ['sword', 'padded leather armor',],
    },
    {
        'name': 'Quigly the demon hunter',
        'SKILLED': 2,
        'MARTIAL': 3,
        'MAGE': 1,
        'defense': 5,
        'Innate_feat_skilled': 'Specialist(lore)',
        'Innate_feat_martial': 'Anti mage',
        'Innate_feat_mage': 'Divine protector',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (second): lore''',
                    '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    '''proficiency (first): lore''',
                ],
                'Martial advancements': [
                    'feat: Heavy armor proficiency',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (third): lore''',
                    '''proficiency (first): survival''',
                ],
                'Mage advancements': [
                    '''proficiency (first): will''',
                    '''1 mana'''

                ],
                'Martial advancements': [
                    'feat: Blessed warrior',
                    '''proficiency (first): sword''',

                ],

            },
            3: {
                'Skilled advancements': [
                    '''proficiency (second): survival''',
                ],
                'Mage advancements': [
                    'proficiency (first): toughness',
                ],
                'Martial advancements': [
                    '''proficiency (second): sword''',
                    '''1 stamina'''
                ],

            },
        },
        'equipment': ['sword', 'Heavy chain mail',],
    },
    {
        'name': 'Esmeralda the warden of silver bats',
        'SKILLED': 2,
        'MAGE': 4,
        'Innate_feat_skilled': 'Specialist(lore)',
        'Innate_feat_mage': 'Divine protector',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): will''', '''proficiency (first): lore''',
                    '''proficiency (extra): lore'''
                ],
                'Mage advancements': [
                    'proficiency (first): elemental', 'proficiency (second): elemental', 'spell: fireball',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (second): lore''', '2 luck'
                ],
                'Mage advancements': [
                    'proficiency (first): nature', 'proficiency (second): nature', 'feat: iron concentration',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''2 luck'''
                ],
                'Mage advancements': [
                    'spell: heal', 'spell: grant luck', 'spell: Elemental weapon', '1 mana'
                ],
            },
        },
        'equipment': ['staff'],
    },
    {
        'name': 'Fred the Forgetful mage',
        'SKILLED': 2,
        'MAGE': 4,
        'Innate_feat_skilled': 'Specialist(treasure hunting)',
        'Innate_feat_mage': 'Raw caster',
        'Levels': {
            1: {

                'Skilled advancements': [
                    '''proficiency (first): treasure hunting''', '''proficiency (first): lore''',
                    '''proficiency (extra): treasure hunting'''
                ],
                'Mage advancements': [
                    'proficiency (first): force', 'proficiency (second): force', 'spell: push/pull',
                ],
            },
            2: {
                'Skilled advancements': [
                    '''proficiency (second): treasure hunting''', '2 luck'
                ],
                'Mage advancements': [
                    'proficiency (first): dimension', 'proficiency (second): dimension', 'proficiency (third): force',
                    'spell: pass object', '1 mana',
                ],
            },
            3: {
                'Skilled advancements': [
                    '''2 luck'''
                ],
                'Mage advancements': [
                    '4 mana',
                ],
            },
        },
        'equipment': ['a single lucky broken beer mug'],
    },

    {
        'name': 'Ralf the Troll diplomat',
        'SKILLED': 4,
        'MARTIAL': 2,
        'defense': 5,
        'Innate_feat_skilled': 'Natural armor(heavy armor)',
        'Innate_feat_martial': 'Extraordinary senses',
        'Levels': {
            1: {
                'Skilled advancements': [
                    '''proficiency (first): diplomacy''', 'proficiency (second): diplomacy', '1 luck'
                ],
                'Martial advancements': [
                    'proficiency (first): toughness', 'proficiency (first): physique',
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Offer them to surrender', 'proficiency (third): diplomacy'
                ],
                'Martial advancements': [
                    'proficiency (second): toughness', 'proficiency (second): physique',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (first): lore', '3 luck'
                ],
                'Martial advancements': [
                    '2 stamina',
                ],
            },
        },
        'equipment': [],
        'normal_actions': ['Wrestle'],
    },
    {
        'name': 'Tom the religious gansta poet',
        'SKILLED': 2,
        'MARTIAL': 4,
        'defense': 3,
        'Innate_feat_skilled': 'Prodigy',
        'Innate_feat_martial': 'Extraordinary senses',
        'Levels': {
            1: {
                'Skilled advancements': [
                    'proficiency (first): crafting', 'proficiency (first): survival'
                ],
                'Martial advancements': [
                    'proficiency (first): dagger', 'proficiency (second): dagger', 'proficiency (first): toughness'
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Agent of chaos', 'proficiency (second): survival', 'proficiency (first): diplomacy'
                ],
                'Martial advancements': [
                    'feat: Shadow', 'feat: Two weapon fighter',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (second): crafting'
                ],
                'Martial advancements': [
                    'feat: Backstabber',
                ],
            },
        },
        'equipment': ['1 handed mace', 'dagger', 'simple leather armor'],

    },
    {
        'name': 'Deadeye the Gang leader',
        'SKILLED': 3,
        'MARTIAL': 3,
        'defense': 2,
        'Innate_feat_skilled': 'Prodigy',
        'Innate_feat_martial': 'Natural killer',
        'Levels': {
            1: {
                'Skilled advancements': [
                    'proficiency (first): leadership', 'proficiency (second): leadership'
                ],
                'Martial advancements': [
                    'proficiency (first): bow', 'proficiency (second): bow',
                ],
            },
            2: {
                'Skilled advancements': [
                    'feat: Natural leader', 'proficiency (first): survival', 'proficiency (third): leadership'
                    , '2 luck', 'proficiency (first): will',
                ],
                'Martial advancements': [
                    'feat: Shadow', 'proficiency (first): toughness', 'proficiency (first): sword',
                    'proficiency (first): fortitude',
                ],
            },
            3: {
                'Skilled advancements': [
                    'proficiency (second): survival', '1 luck'
                ],
                'Martial advancements': [
                    'proficiency (third): bow',
                ],
            },
        },
        'equipment': ['shortbow', 'sword', 'simple leather armor'],

    },
]



import re
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, KeepTogether, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, spell_block_style
from reportlab.lib import colors


spell_schools = ['']

def split_data_into_columns(data, column_number):
    rows = []
    indx = 0
    row = []
    for i in range(len(data)):
        row.append(data[i])
        indx += 1
        if indx == column_number:
            rows.append(row)
            row = []
            indx = 0
    if indx > 0:
        while indx < column_number:
            row.append('')
            indx+=1
        rows.append(row)
    return rows

def find_feat_object(name, all_feats):
    for path in all_feats:
        for feat in all_feats[path]:
            if feat['name'].lower() == name.lower():
                return feat

def find_general_action(name, all_general_actions):
    for action in all_general_actions:
        if action['name'] == name:
            return action

def find_spell_object(name, all_spells):
    for school in all_spells:
        for spell in all_spells[school]['spells']:
            if spell['name'].lower() == name.lower():
                return spell

def generate_character_flowable(character):
    from Innate_feats import prep_feat_flowable as prep_innate_feat_flowable
    from Innate_feats import feats as all_innate_feats
    from Normal_feats import feats as all_normal_feats
    from Normal_feats import prep_feat_flowable as prep_normal_feat_flowable
    from Skills import skills
    skill_names = [x['name'] for x in skills]

    from Spells import schools
    from Spells import prep_spell_flowable as prep_spell_flowable

    spell_school_names = [key.lower() for key in schools]

    from equipment import weapon_classes, prep_equipment_flowable
    from equipment import equipment as all_equipment

    innate_feats = [{'name': character[key], 'path': key[12:]} for key in ['Innate_feat_skilled', 'Innate_feat_mage', 'Innate_feat_martial'] if key in character]
    feats = []
    proficiencies = {}
    spells = []
    stats = {'mana': 0, 'stamina': 0, 'luck': 0, 'toughness': 2, 'will': 0, 'fortitude': 0, 'reflex': 0}

    for indx in character['Levels']:
        level = character['Levels'][indx]
        for key in level:
            for advancement in level[key]:
                proficiency = re.search('proficiency \((first|second|third|fourth|extra)\): ([a-z ]*)', advancement)
                if proficiency:
                    proficiency = proficiency[2]
                    proficiencies[proficiency] = proficiencies.get(proficiency, 0) + 1
                    continue

                spell = re.search('spell: ([A-Za-z \/]*)', advancement)
                if spell:
                    spells.append(spell[1])
                    continue
                feat = re.search('feat: ([A-Za-z ]*)', advancement)
                if feat:
                    feats.append(feat[1])
                    continue
                stat = re.search('([0-9]*) (mana|stamina|luck)', advancement)
                if stat:
                    stats[stat[2]] += int(stat[1])
                    continue

                raise Exception(advancement + ' is unhandled')

    stats['toughness'] += proficiencies.get('toughness', 0)
    stats['will'] += proficiencies.get('will', 0)
    stats['fortitude'] += proficiencies.get('fortitude', 0)
    stats['reflex'] += proficiencies.get('reflex', 0)

    mana_multiplier = 2

    stats['mana'] = stats['mana'] * mana_multiplier

    elements = []
    elements.append(Paragraph(character['name'], style=minor_title))
    data = [
        [f"Martial: {character.get('MARTIAL', 0)}", f"Mage: {character.get('MAGE', '0')}", f"Skilled: {character.get('SKILLED', '0')}"],
        [f"Stamina: {stats.get('stamina')}", f"Mana: {stats.get('mana')}", f"Luck: {stats.get('luck')}"],
        [f"Toughness: {stats.get('toughness')}", f"Defense: {character.get('defense', 0)}", f""],
        [f"Will: {stats.get('will')}", f"Fortitude: {stats.get('fortitude', 0)}", f"Reflex: {stats.get('reflex')}"],
    ]

    skill_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in skill_names]

    print(skill_proficiencies)

    print(split_data_into_columns(skill_proficiencies, 3))

    data.extend(split_data_into_columns(skill_proficiencies, 3))

    spell_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in spell_school_names]

    print (spell_proficiencies)

    data.extend(split_data_into_columns(spell_proficiencies, 3))

    weapon_proficiencies = [f'{prof}: {proficiencies[prof]}' for prof in proficiencies if prof in weapon_classes]

    data.extend(split_data_into_columns(weapon_proficiencies, 3))

    table = Table(data, colWidths=[160]*3)
    table.setStyle(TableStyle([
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)




    elements.append(Paragraph('Feats', style=minor_subtitle))

    path_mapping = {1: 'Acquinted', 2: 'Adept', 3: 'Talented', 4: 'Legendary'}

    for feat in innate_feats:
        feat_name = re.search('(^[A-Za-z ]*)', feat.get('name'))[1]
        feat_obj = find_feat_object(feat_name, all_innate_feats)
        path_power = character.get(feat['path'].upper())
        name_addon = ' (%s)'%(path_mapping[path_power])
        elements.extend(prep_innate_feat_flowable(feat_obj, name_addon=name_addon))

    for feat in feats:
        feat_obj = find_feat_object(feat, all_normal_feats)
        elements.extend(prep_normal_feat_flowable(feat_obj))

    elements.append(Paragraph('Spells', style=minor_subtitle))

    for spell in spells:
        spell_obj = find_spell_object(spell, schools)
        elements.extend(prep_spell_flowable(spell_obj))

    if character.get('normal_actions'):
        from general_actions import actions as general_actions
        from general_actions import prep_action_flowable
        elements.append(Paragraph('General actions', style=minor_subtitle))

        for action in character.get('normal_actions'):
            action_obj = find_general_action(action, general_actions)
            elements.extend(prep_action_flowable(action_obj))


    elements.append(Paragraph('Equipment', style=minor_subtitle))

    for equipment in character.get('equipment', []):
        if equipment in all_equipment:
            elements.extend(prep_equipment_flowable(all_equipment[equipment], equipment))
        else:
            elements.append(Paragraph(equipment, style=minor_subtitle))


    return elements

def get_player_character_chapter():
    elements = [
        # {'type': 'title', 'content': 'Player characters'},
    ]
    first = True
    for character in player_characters:
        if not first:
            elements.append({'type': 'flowables', 'content': [PageBreak()]})
        else:
            first = False
        elements.append({'type': 'flowables', 'content': generate_character_flowable(character)})


    return elements

def get_player_character_chapters():

    for character in player_characters:
        elements = [{'type': 'flowables', 'content': generate_character_flowable(character)}]
        yield (elements, character['name'])
