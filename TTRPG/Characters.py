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
            'progression_feats': ['Mastery (illusion)', 'Resourceful']
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
            'progression_feats': ['', 'Stamina related']
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
                    '1 stamina, third sword proficiency',
                ],
            },
        },
        'equipment': ['sword', 'shield', '2 MD leather armor'],
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
                    'second bow proficiency and first toughness proficiency and 1 stamina',
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
        'MARTIAL': 3,
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
]