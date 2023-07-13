feats = {
    'Mage': [
        {'cost': 2,
         'name': 'Commune with animals',
         'effect': '''You are able to communicate with animals. To get desired communication, GM can provide you a dice
         target for the scene, and you can use nature school of magic proficiency to meet the target'''
         },
        {'cost': 2,
         'name': 'Adept attuner',
         'effect': '''You can attune to one additional magical item'''
         },
        {'cost': 4,
         'name': 'Talented attuner',
         'effect': '''You can attune to one additional magical item'''
         },
        {'cost': 2,
         'name': 'Enduring magic',
         'metamagic_option': {
             'difficulty': 'Ru.Ru',
             'effect': '''Can only be applied to concentration spells or spells with duration.
             Concentration spells without duration gain a duration of 3 rounds. Spells with duration increase their
             duration by 3 rounds or double it, whichever has greater effect''',
            },
         },
        {'cost': 2,
         'name': 'Large magic',
         'metamagic_option': {
             'difficulty': 'Ru',
             'effect': 'Increase spell radius, which has radius by 1 sq.',
            },
         },
        {'cost': 2,
         'name': 'Distant magic',
         'metamagic_option': {
             'difficulty': 'Ru',
             'effect': 'Increase spell distance by 6 sq. or double it, whichever has greater effect',
            },
         },
        {'cost': 4,
         'name': 'Twin magic',
         'metamagic_option': {
             'difficulty': 'Rp.Ru',
             'effect': '''Cast the spell twice using the same number of actions. You may choose new targets for second
                cast. Concentration spells share concentration for both casts.''',
             'L': 1,
            },
         },
        # {'cost': 6,
        #  'name': 'Hex master',
        #  'effect': '''You can apply max 2 hexes on a creature instead of only 1. Also advance in max mana and learn
        #  one discord spell''',
        #  },
        {'cost': 5,
         'name': 'Pyromancy',
         'effect': '''Whenever your spell applies at least 1 stack of burning onto an enemy, it applies one more stack
         of burning onto them.
            ''',
         },
        {'cost': 3,
         'name': 'Wielder of fire and ice',
         'effect': '''When burning or freezing applied to enemies by you cancel out the previous freezing or burning
         stacks, the enemy takes 3 damage for each stack cancelled out this way.
            ''',
         },
       # {'cost': 2,
       #   'name': 'Mind expertise',
       #   'effect': '''When taking this trait, choose one of the WILL status effects. ONCE PER ROUND, when applying the
       #   chosen status effect on an enemy, you can force them to check for that status effect once more. This trait can
       #   be taken multiple times, but different status effect must be chosen each time.
       #      ''',
       #   },
        {'cost': 3,
         'name': 'Trickster',
         'effect': '''
         Whenever you apply a level of disoriented or afraid, you also disrupt 1.
         ''',
         },
        {
            'cost': 5,
            'name': 'Iron concentration',
            'effect': '''You can spend any dice to maintain concentration, and concenctration does not reduce action 
            limit''',
        },
        {
            'cost': 5,
            'name': 'Dimension mastery',
            'requires': 'Expert dimension proficiency',
            'effect': '''
            When taking this feat you craft an object, a talisman of sorts, which, while you are attuned to it, you can
            cast spells from the point of that object.
            
            If you are are legendary in dimension magic, you can craft one additional such object.
            ''',
        },
        {
            'cost': 5,
            'name': 'Enchanter',
            'effect': '''
Enchantment spells cost 1 less power dice to cast. When the concentration cost is higher than 1 power dice, then that
too costs 1 less power dice.
            ''',
        },
    #     {
    #         'cost': 8,
    #         'name': 'Holy bonds',
    #         'effect': '''
    # You can attune to any number of your party members instead of items. When casting spells that only target the
    # attuned players or their weapons, you can target any number of other attuned players or their weapons to also
    # receive the benefits of the spell.
    # This does not increase the cost or concentration requirement for that spell.
    #
    # For spells which the target is self, you can instead cast it targeting up to 1 attuned player.
    #
    # The minimum range for these spells becomes 5 sq.
    #         ''',
    #     },
    #     {
    #         'cost': 8,
    #         'name': 'Blood magic',
    #         'effect': '''
    # You may cast spells using your hit dice instead of mana. Each hit dice you spend makes a spell 5 mana cheaper and
    # increases the max difficulty of the spell by 1.
    #
    # Advance twice in any school of magic and learn 1 spell.
    #         ''',
    #     },
    #     {
    #         'cost': 5,
    #         'requires': 'Blood magic',
    #         'name': 'Blood magic expertise',
    #         'effect': '''
    # You can use the hit dice of other willing allies within 4 m. of you or enemies who have are either frozen or
    # paralized, or have at least 4 levels of disoriented or afraid on them. Note however that few enemies have more than
    # a single hit dice. You can however combine your own, willing ally's and confused enemies hit dice to cast spells.
    #         ''',
    #     },
    #     {
    #         'cost': 8,
    #         'name': 'Shackles of suffering',
    #         'effect': '''
    # When gaining this ability, choose between afraid, disoriented or crazed. You gain an action, which binds between
    # 2 and 4 enemies. Whenever these enemies gain a level of chosen status effect caused by your spell effect, the other
    # bounded enemies also get it. However the WILL used to defend against such status effects is the highest WILL value
    # amongs the bounded enemies.
    #
    # You know the Will saving throws of all enemies intuitively.
    #
    # Advance in any school of magic, twice in maximum mana and learn 1 spell.
    #         ''',
    #         'action': {
    #             'roll target': '1-3AP',
    #             'target': '2-4 enemies',
    #             'range': '20 m',
    #             'duration': '3 rounds',
    #             'effect': '''The AP cost depends on the number of enemies you want to bind. 1 AP for 2 enemies, 2 AP for
    #             3, and 3 AP for 4 enemies. Binds these enemies into shackles of suffering. Their will save against
    #             chosen status effect caused by your spells becomes the highest amongst them and whenever one of them
    #             receives a status effect caused by your spells, the others also receive it.''',
    #         },
    #     },
    #     {
    #         'cost': 3,
    #         'requires': 'Shackles of suffering',
    #         'name': 'Prolonged shackles',
    #         'effect': '''
    # Shackles of suffering lasts 1 more round
    # ''',
    #     },
    ],
    'Martial': [
        # {'cost': 1,
        #      'name': 'Basic dodging',
        #      'effect': '''You gain +1 max dodge tokens and the dodge ability: whenever you would get hit by an attack
        #         or as a reaction to anything you may spend 1 dodge token and 2 STA or when failing a reflex save,
        #         to move 2 m. and completely negate the effects from the attack or pass the reflex save,
        #         for other effects you are just considered to be in the new location.
        #         If the attack would have been a critical hit or if you failed your reflex save critically, you need to
        #         spend 2 dodge tokens and 3 STA instead.
        #         You can only use this ability while wearing Light armor or no armor''',
        #  'action': {
        #      'roll target': '3A',
        #      'target': 'self',
        #      'effect': '''recover all dodge tokens''',
        #     },
        # },
#         {'cost': 2,
#          'requires': 'Basic dodging',
#          'name': 'Advanced dodging',
#          'effect': '+1 max dodge token',
#         },
#         {'cost': 2,
#          'requires': 'Advanced dodging',
#          'name': 'Extreme dodging',
#          'effect': '+1 max dodge token',
#         },
#         {'cost': 3,
#          'requires': 'Extreme dodging',
#          'name': 'Legendary dodging',
#          'effect': '+1 max dodge token',
#         },
        {'cost': 2,
             'name': 'Medium armor proficiency',
             'effect': '''Remove the penalty of -1 action limit when wearing medium armor''',
         },
        {'cost': 3,
             'name': 'Heavy armor proficiency',
             'effect': '''While wearing heavy armor you only get -1 action limit instead of -2.
                ''',
         },
        {'cost': 2,
             'name': 'Defensive stance',
             'effect': '''If you have not attacked or cast an offensive spell since the beginning of your last turn
             you have an additional +2 maximum defense while guarded.''',
         },
#         {'cost': 2,
#              'name': 'Accuracy',
#              'effect': '''With ranged weapons, reduce enemy cover category by 1. If enemy has no cover, you have
#              advantage.''',
#          },
#
        {
            'cost': 3,
            'name': 'Menace',
            'effect': '''When you damage an enemy with a melee attack, then until the start of your next turn, they have
            disadvantage when attacking your allies''',
        },
        {
            'cost': 3,
            'name': 'Power strike',
            'effect': '''When making an attack with 2 handed melee weapon you can spend 1 stamina to deal 2 additional
            damage''',
        },
        {
            'cost': 3,
            'name': 'Opportunist',
            'effect': '''
                You have advanatege with attacks against enemies that have damaged your allies but not you since the 
                end of your last turn.
            '''
        },
#         {
#             'cost': 3,
#             'name': 'Pinner',
#             'action': {
#                 'roll target': '1A',
#                 'range': 'melee/spear',
#                 'target': 'single',
#                 'base_cost': '1 STA',
#                 'effect': '''Pin a single target. Your allies have advantage when attacking them. You can only pin one
#                 enemy at a time. When you attack another enemy, or another enemy attacks you, the pin is broken. When
#                 pinned target attempts to move away from you, you're reaction attack against him has advantage. If you
#                 hit, the enemy must make a REF saving throw equal to half the damage rounded up. On a fail, they stop
#                 their movement and remain within your range.''',
#             }
#         },
        {'cost': 5,
             'name': 'Two weapon fighter',
             'effect': '''
                Your maximum defense is increased by 1 while wielding two weapons.
                
                When wielding two melee weapons which sum of power dice is less than or equal to 6, then you can use R6
                from your dice pool as a power dice for attacks with both weapon (and it only consumes a single action
                limit).
                ''',
        },
        {'cost': 5,
             'requires': 'Two weapon fighter',
             'name': 'Two weapon master',
             'effect': '''
Whenever you attack with both weapons in a round you gain a flow token.

You can use the flow tokens in following ways, flow tokens are reset to 0 at the end of an encounter:

* When you would get a level of negative status effect, you can spend a flow token to prevent that.

* Spend 2 flow tokens to instantly go to your maximum defense

* Spend 1 flow token to move yourself up to 2 sq. after finishing an attack action.
                ''',
        },
        {'cost': 7,
             'requires': 'lvl 5.',
             'name': 'Master of defenses',
             'effect': '''
Defend action now requires only R2. You can also use Defend action as a reaction once between your turns after being
attacked.
                ''',
        },
#         {'cost': 8,
#              'name': 'Blade dancer',
#              'effect': '''
# Attacks with one handed swords do not increase stamina cost for further attacks. Advance 4 times with
# one handed swords.
#
# You gain additional difficulty options for one handed swords:
#
# 2: When you critically hit, you recover a dodge token
#
# 4: As long as you don't critically miss, target gains 1 level of vulnerable against you only.
#
# 3: when an enemy attacks you, spend your reaction to first attack them. If you succeed, you stop their
# attack
#
# 5: Your critical hits do double damage.
#
#                 ''',
#         },
        {'cost': 5,
             'name': 'Savage Axe',
             'effect': '''
             
You gain 1 savagery token per stamina spent. These tokens must be used in the current round. When you
attack with an axe you can spend savagery points to deal 1 additional damage per savagery point.

You gain additional difficulty adjustment options for two handed axes:

RU: Spend 2 savagery tokens to add a level of afraid to the enemy

RU: Spend 2 savagery tokens to add 1 level of vulnerable to the enemy. 
                ''',
        },
        {'cost': 5,
         'name': 'Sentinel',
         'effect': '''
When wielding a polearm, you get a zone of control around you of 2 sq. Enemies that want to move through your ZoC or
want to enter within 1 sq. of you need to provide a R6 phsyique roll in order to do that.

Enemies entering your ZoC give you a attack reaction opportunity.

First reaction attack with a polearm in between your turns has double advantage, the rest have simple advantage.
         ''',
         },
#         {'cost': 2,
#          'name': 'Cleave',
#          'effect': '''
#          You have a new difficulty options for melee weapons:
#
# 3: You attack all enemies around you, but the attack costs 3 additional STA and 1 additional AP.
#          ''',
#          },
#          {'cost': 1,
#          'name': 'Fierce',
#          'effect': '''
# You have a new difficulty options for melee weapons:
#
# 1: When you score a critical hit, target needs to check for afraid.
#          ''',
#          },
#          {'cost': 2,
#          'name': 'Double strike',
#          'effect': '''
# You have a new difficulty options for melee weapons:
#
# 4: The attack costs 3 additional STA, but you attack twice, making 3d6 check both times, and receiving all other hit
# effects both times.
#          ''',
#          },
        {'cost': 5,
         'name': 'Rage',
         'effect': '''
            Gain rage action.
         ''',
         'action': {
             'roll target': '1A',
             'target': 'self',
             'limit': 'once per encounter',
             'duration': '5 rounds',
             'effect': '''You go into rage where you stay for 5 rounds or until you go unconscious. If you are wearing 
                heavy armor, rage lasts for 2 fewer rounds.
                While raging you are immune to confusion and disruption.
                
                You lose all your defense and cannot recover any defense. However you still roll all the dice that were
                set aside because of damage and scarred dice can be used for targets 4, 5 and 6 as well.
                ''',
            }
         },
        {'cost': 7,
         'requires': 'Rage',
         'name': 'Fury',
         'effect': '''
When raging then enemies within 5 sq. of you who choose to attack someone other than you or someone 
else who is raging suffer 1 confusion. When you are damaged, then for every 2 points of damage rounded up, you gain
1 fury token. When successfully hitting an enemy you can spend any number of fury tokens to add 
following buffs to that attack:

* 1 damage per fury token. If you have proficiency in elemental school of magic, you can convert all your
physical damage into fire damage.

* 1 confusion per fury token.

* Push them away from you forcing them to check for unbalanced for each fury token. The push distance is 1 sq.
per fury token used this way.
         
         ''',
         },
        {'cost': 2,
         'requires': 'Rage',
         'name': 'Prolonged rage',
         'effect': '''
         Your rage lasts 3 additional rounds, or 2 additional rounds if wearing heavy armor.
         ''',
         },
        # {'cost': 6,
        #  'name': 'Hex arrow',
        #  'effect': '''When taking this feat, also advance 3 times with bows. Also, choose a {hex spell} of difficulty 1.
        #     Whenever you critically hit with this attack, apply that hex, or a hex you can cast yourself to the target.
        #     If you choose to apply a hex you can cast yourself, you do have to spend your mana to do so.
        #     No concentration costs are necessary to maintain that hex, normal hex limits apply.
        #     When you reach level 5/10/15/20, the chosen hex is upcasted to difficulty 3/5/7/9.''',
        #  'action': {
        #      'roll target': '1A',
        #      'range': 'ranged',
        #      'target': 'single',
        #      'base_cost': '2 STA',
        #      'effect': 'Reduce critical threshold by 1. On a critical strike apply the Hex on the target.',
        #      'restrictions': 'Bows',
        #     }
        #  },
        {'cost': 3,
         'requires': 'Heavy armor proficiency',
         'name': 'Fortress',
         'effect': '''You can use fortitude proficiency against afraid and disoriented conditions instead of will.
         ''',
         },
        {'cost': 4,
         'name': 'Backstabber',
         'effect': '''When attacking someone with a one handed melee weapon from behind or while the opponent is unaware
         of your presence, you have double advantage.''',
        },
        {
            'cost': 3,
            'name': 'Shadow',
            'effect': '''You are able to take maximum advantage of disoriented foes. Foes who have at least 1 level
    of disorientation, have disadvantage for attacks against you. You have advantage with attacks against foes
    who have at least 2 levels of disoriented. When taking a move action, then one target creature with at least
    2 levels of disoriented loses track of you and become unaware of your presence.''',
        },
#         {'cost': 2,
#          'name': 'Toxicologist',
#          'effect': '''The DC of each consecutive potion increases by 1 instead of 2. You have +1 to fort saves against
#          poison, and +3 to fort saves against alcohol.''',
#          },
#         {'cost': 6,
#          'name': 'Commander',
#          'effect': '''Leadership becomes a martial skill.
#
#          At the beginning of combat encounters roll for leadership. For every 10 points, the entire party gains
#          +1 to their initiative.
#
#          Gain the coordination action.
#          ''',
#          'action': {
#              'roll target': '1A',
#              'range': '30 ft.',
#              'target': '2 allies (can be yourself)',
#              'effect': '''
#              Coordinate the assault of 2 of your allies. Roll for leadership with a DC check of 11. If you succeed then
#              until the start of your next turn if one of the allies deals damage or applies a negative status effect on
#              some enemy, then the other ally gets advantage against these enemies (whoever were damaged or received
#              a negative status effect).
#              ''',
#          }
#          },
#         {'cost': 3,
#          'name': 'Improved coordination',
#          'requires': 'Commander',
#          'effect': '''Coordination action can target 1 additional ally.
#          ''',
#          },
        {'cost': 5,
         'name': 'Blessed warrior',
         'effect': '''
Increase your maximum defense by 1. Whenever you hit an enemy with an attack involving at least 4 power dice
you may choose 1 option:

* remove one level of negative status effect from you or one of your allies.

* recover 1 stamina

* spend 1 mana to deal an additional 3 damage. (requires mage path)
         ''',
         },
#         {'cost': 6,
#          'requires': 'Blessed warrior',
#          'name': 'Blessed Champion',
#          'effect': '''Choose from amongst the following spells: Unity, Guardian, Valor, Force field.
#          You have the selected spell's buff permanently on you. It's max difficulty is based on the martial path.
#          You can readjust it's exact effect (which difficulty modifiers to use) on each level up.
#          ''',
#          },
#         {'cost': 8,
#          'requires': 'Blessed Champion',
#          'name': 'Blessed commander',
#          'effect': '''The chosen buff also applies to all your allies within 20 m. of you.
#          ''',
#          },

    ],
    'Skilled': [
        {'cost': 5,
         'name': 'Offer them to surrender',
         'effect': '''
         You gain the offer enemy to surrender ability.
         ''',
         'action': {
             'roll target': 'R5.R5',
             'range': '3 sq.',
             'target': 'single',
             'effect': '''
An enemy with 3 moral or less will surrender. If they have more than 3 but less than 6 moral remaining they will be
get 2 confusion.
             ''',
             'difficulty_options': [
                 {
                     'adjustment': 'R5',
                     'effect': '''Increase the moral threshold for surrendering and confusion by 1''',
                 },
                 {
                     'adjustment': 'R3.R3',
                     'effect': '''Target one additional target with this ability''',
                 },
             ]
            }
        },
        {'cost': 5,
         'name': 'Natural leader',
         'effect': '''
         You gain the coordinate action, which can used both during combat and out of combat.
         ''',
         'action': {
             'roll target': 'R3.R3',
             'range': '6 sq.',
             'target': '2 allies',
             'effect': '''
Targeted allies may give up to 1 dice to the other ally to be used temporarily (that dice preserves it roll). The dice
is returned after using it.
             ''',
             'difficulty_options': [
                 {
                     'adjustment': 'R3',
                     'effect': '''They can give up to 1 additional dice''',
                 },
             ]
            }
        },
        {'cost': 4,
         'name': 'Master plan',
         'effect': '''
         You gain the master plan action, which can be used during scene. This is a leadership action.
         ''',
         'action': {
             'roll target': 'R3.R3.R3',
             'range': '6 sq.',
             'target': '3 allies',
             'effect': '''
Targeted allies roll 1 extra temporary dice into their dice pool for this scene.
             ''',
             'difficulty_options': [
                 {
                     'adjustment': 'R3.R3',
                     'effect': '''They roll one additional dice''',
                 },
             ]
            }
        },
        {'cost': 5,
         'name': 'Agent of chaos',
         'effect': '''
         Causing chaos comes naturally to you. You can make ploys to disorient a group of enemies before the battle.
         You can use diplomacy, survival or lore as the main skill to check for it's success. You must still describe
         how you are going to do it and how using that skill makes sense. 
         
         A new roll target is added to combat initiation phase with R5.R5.R3.R3, that you may complete. If you succeed
         then all enemies start the combat with 1 level of disoriented. For an additional +R5 they start the combat
         with 2 levels of disoriented instead. Use the chosen skill to achieve this.
         ''',
        },
#         {
#             'cost': 3,
#             'name': 'Quick mind',
#             'effect': '''
#             You come up with vicious ploys on the spot. You still must come up with the ploy, but during combat, if you
#             are able to act 3 rounds undisturbed, you can deploy a ploy to have an impact. They need to check 3 times
#             against some condition that is fitting for the ploy against a skill check that makes sense and if they fail
#             at least 2 times, then they in addition lose their next round in combat.
#
#             Depending on the role play quality of the ploy, GM can give advantage or dis-advantage to these checks.
#             '''
#         },
        {'cost': 3,
         'name': 'Lucky finder',
         'effect': '''When rolling loot table, you can spend 2 luck token to be presented with 2 options
            , you still pick only 1.''',
         },
        {'cost': 3,
         'name': 'Planner',
         'effect': '''Choose a {skill}. If your party doesn't have that skill related group focus, then you can start an
                extra group focus related to that skill, it is not counted towards the 1 group focus limit.''',
         },
#         {'cost': 2,
#          'name': 'Knowing when to shut up',
#          'effect': '''When you use lore to try to aid your allies, critical failures do not cause dis-advantage''',
#          },
        {'cost': 5,
         'name': 'Inspiring',
         'effect': '''Grants you the ability to inspire others by spending luck tokens. Gain 2 max luck tokens.

         Inspire action uses leadership skill.
         ''',
         'action': {
             'roll target': 'R3.R3',
             'range': '12 m.',
             'target': '1 creature',
             'additional_costs': '1 Luck token',
             'effect': '''target gains inspiration''',
             'difficulty_options': [
                 {
                     'adjustment': 'R6',
                     'effect': '''They lose 1 level of Will related status effects''',
                 },
                 {
                     'adjustment': 'R6.R6',
                     'effect': '''They lose 3 level of Will related status effects''',
                 },
                 {
                     'adjustment': 'R3.R3',
                     'effect': '''They gain 1 additional temporary dice that they can use until their next roll''',
                 },
                ]
            }
         },
        {
            'cost': 7,
            'name': 'Inspiring leader',
            'requires': 'Inspiring',
            'effect': '''When using the inspire ability, you can spend 1 additional luck token so that all your party
            members except fo your gain inspiration and other benefits of the inspire action. Gain 2 max luck tokens.
            ''',
        },
#         {
#             'cost': 7,
#             'name': 'Luck bringer',
#             'requires': 'Inspiring',
#             'effect': '''When your ally uses inspiration provided by you, their roll is also lucky. Advance twice
#             in luck.
#             ''',
#         },
#         {
#             'cost': 2,
#             'name': 'Expert of pawn sacrifices',
#             'effect': '''During a resolution of the plan, when giving disadvantage to a check to give advantage to
#             another check, you can give advantage to one additional check. Advance 1 times in leadership''',
#         },
        {'cost': 2,
         'name': 'Foresight',
         'action': {
             'roll target': '-',
             'additional_costs': '1 Luck token',
             'effect': '''Once every time after visiting a settlement with shops, you can take out a common item
                from your backpack, which you as a player actually had not bought from the settlement, but consider it
                having been bought (subtract the gold cost of the item from your balance).'''
            }
        },
#         {'cost': 3,
#          'name': 'Hunter',
#          'effect': '''
#          When you score a critical success while tracking someone, you learn a piece of information about them (feat,
#          level, stamina level, spells that they know, GM-s discretion). Advance twice in survival skill.
#          ''',
#          'action': {
#              'roll target': '1 AP',
#              'effect': '''Appraise a none magical opponent (beast, martial humanoid) and learn about their stamina, HP,
#              AC and wielded weapon proficiency (or attack proficiency for beasts).'''
#             }
#          },
#         {'name': 'Grenade maker',
#          'cost': 6,
#          'effect': '''
# You can make grenades using gunpowder and various chemicals with differing effects.
#
# Grenades have by default 2m. effect radius. Each grenade also has a potency. Potency affects the effect amplitude.
#
# Possible effects and their base cost:
#
# 1d12 damage per potency: 15 gp
#
# Covers the area in smoke, blinding everyone in it for potency number of turns,
# the area radius for this effect is tripled: 40 gp
#
# Affected check for disoriented for times equal to potency: 10 gp
#
# When attempting to craft a grenade, choose the target potency, potency cannot be larger than your effective crafting
# level. The cost is base cost * potency. In addition at potencies of 5 and 10 increases the cost by 50 %.
#
# In addition you can adjust the radius by 2 m. Each adjustment increases the cost by 50%. You can do so twice.
# (all increases are summed up before applied to the base cost).
#
# You and anyone at least adept in the martial path are able to throw these grenades accurately for up to 20 m.
# Talented martials can throw them for 30 m and legendary martials for 40 m.
# Others' can throw them for only 6 m.
#
# Grenades available in the shops in the game world are usually at least twice to three times more expensive compared to
# those available through this feat.
#          '''
#          },
        {'name': 'Lore weaver',
         'cost': 5,
         'effect': '''
        By spending 1 luck token , you can use the "is there such a thing in the game-world" option one additional time
        per scene. When taking this feat advance 4 times in luck.
            '''
        },
        {
            'cost': 5,
            'name': 'Excellent instructor',
            'effect': '''By spending 30 min. to prepare someone in a skill you are proficient in, you can have them
            meet 1 roll target with your effective proficiency bonus in that skill within the next 12 h.
            You can use this ability twice a day.
''',
        },
        {
            'cost': 7,
            'requires': 'Excellent instructor',
            'name': 'Master',
            'effect': '''For each party member you can choose one skill. Their effective proficiency bonus in that
            skill is equal to yours. That skill can be changed once a month in game time.
''',
        },
    ],
    'Mage/Martial': [
    #     {'cost': 10,
    #      'name': 'Blade enchanter',
    #      'effect': '''Weapon enchantment spells that have only been applied to a weapon you wield do not require
    # AP to be spent on concentration, they still cost mana as normal. The max
    # difficulty for these enchantments is as if you were Legendary in Mage path. Advance once in encounter limit,
    # once in one school of magic, learn a spell, advance in 1 weapon and once in maximum stamina and stamina recovery''',
    #      },
    #     {'cost': 10,
    #      'name': 'Spell blade (or bow)',
    #      'effect': '''
    #      Whenever you critically hit an enemy you can also cast a spell that targets a single enemy (the one that got
    #      hit), that does not require concentration with a difficulty, which are free to cast for you (costs 0 mana, and
    #      not replaced by any other cost like with Blood magic).
    #      ''',
    #      },
    ],
    'Mage/Skilled': [
#         {
#             'cost': 6,
#             'name': 'Potion maker',
#             'effect': '''You can make magical potions, which have the effects of spells you know how to cast, and
# which difficulty requirements you meat. These potions have however certain constraints:
#
# 1. They target is the person who drinks the potion. Spells with area of effect lose the area component.
#
# 2. Spell effects that have additional targets, like a location, cannot be made into a potion. The potion
# can only effect the creature drinking the potion.
#
# 3. When these potions have a concentration effect, instead they simply last 3 iterations (normally this
# is 3 rounds, but if a spell duration is otherwise 5 rounds, that is extended to 15 rounds instead and so on)
#
# In order to make these potions there is a baseline cost for ingredients that is based on difficulty. Maximum
# difficulty for potions is 10.
# Through role play, group focuses etc. these may be reduced.
# D0: 5 gp, D1: 15 gp, D2: 30 gp. D3: 50 gp, D4: 75 gp, D5: 105 gp, D6: 150 gp, D7: 250 gp, D8: 400 gp,
# D9: 600 gp, D10: 1000 gp.
#
#
# It is also possible to increase the duration of those potions to 5 iterations, which would double the cost.
#
# It is also possible to combine 2 spells into 1 potion, but they would add up their difficulties. This option
# would also double the cost.
#
# Potions are also available through shops in the game world, however their prices would be around twice
# higher.
# ''',
#         },
    ],
    'Martial/Skilled': [
#         {'name': 'Poison specialist',
#          'cost': 6,
#          'effect': '''
# You can prepare poison coatings and coat weapons with poison. In order to prepare poisons you
# need to gather poison glands or procure necessary raw materials from the marketplace. Both of them
# requires you to choose them as your personal focus. Depending on the situation it could require gathering,
# diplomacy, roguery and would also have a different difficulty, plus may require some extra cost such as gold.
#
# By default a coating of 3 stacks of following poisons on a melee weapon or 2 stack a single arrow costs that
# much money, this can be reduced with role-play,group focuses:
#
# 1d6 damage per stack at the beginning of target's turn: 20 gp
#
# 1d8 damage per stack at the beginning of target's turn: 40 gp
#
# 1d10 damage per stack at the beginning of target's turn: 75 gp
#
# 1d12 damage per stack at the beginning of target's turn: 150 gp
#
# stack of disoriented: 50 gp
#
# stack of afraid: 40 gp
#
# stack of crazed: 100 gp
#
# stack of freezing: 200 gp
#
# The price doubles if you want to apply 5 stacks on a melee weapon or 3 stacks on a single arrow. And doubles
# again when wanting to apply 7 stacks on a melee weapon or 4 stacks on a single arrow.
#
# By adding 100 gp to the base price, you can increase the DC to 13, and by adding an additional 300 gp to the
# base price, you can increase the DC to 14.
#
# A successful melee attack made with the weapon moves 1 stack of poison onto the hit target. A successful attack
# with an arrow moves all stacks of poison from the arrow onto the target.
#
# At the beginning of the turn and after the poison stacks have taken effect, target throws a FORT save of DC 12.
# On success they remove 1 stack of poisons from them, on critical success they remove 3 stacks of poison from
# them.
#
# Stacks of disoriented, crazed, afraid, and freezing cannot be reduced normally even though their effects
# work the same as having the same levels of the these status effects.
#
# Poison cannot be applied to enchanted weapons.
# '''
#          },
    ],
    'General': [
        {'cost': 12,
         'name': 'Legendary magic item user',
         'effect': '''You can attune to one additional magical item. You can double one numerical effect of 1 magical 
item you wear / wield. You can change the item/effect at the beginning of each of your rounds.
If you have the blade enchanter feat, you can use this ability on the enchanted weapon you wield.
'''
         },
    ]
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style
from reportlab.lib import colors
import re

def prep_feat_flowable(feat):
    elements = []
    elements.append(Paragraph(feat['name'], style=minor_title))
    elements.append(Paragraph(f"Advancement point cost: {feat['cost']}", style=minor_subtitle))

    if feat.get('requires'):
        elements.append(Paragraph('Requires: %s'%feat['requires'], style=minor_subtitle))



    if feat.get('effect'):
        for para in feat['effect'].split('\n\n'):
            para = para.replace('\n', ' ')
            elements.append(Paragraph(para, style=basic_paragraph_style))

    if feat.get('metamagic_option'):
        meta_option = feat.get('metamagic_option')
        data = [[f"Roll: {meta_option['difficulty']}", f"Use limit: {meta_option.get('L', 'unlimited')}",
                 Paragraph(meta_option['effect'], basic_paragraph_style)]]
        table = Table(data, colWidths=[100, 100, 280])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)

    if feat.get('action'):
        action = feat['action']
        data = [
            [f"Stamina cost: {action.get('base_cost', '-')}", f"Other attacks cost increase: {action.get('next_attack_cost_increase', '-')}",
                f"Other costs: {feat.get('additional_costs', '-')}"],
            [f"Roll target: {action.get('roll target', '-')}", f"Target: {action.get('target', '-')}", f"Duration: {action.get('duration', '-')}"],
            [f"Limit: {action.get('limit', '-')}", f"Restrictions: {action.get('restrictions', '-')}", ""],
            [Paragraph(action['effect'], basic_paragraph_style)]
        ]

        table = Table(data, colWidths=[160]*3)
        table.setStyle(TableStyle([
                                   ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                   ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
                                   ('SPAN', (0, -1), (-1, -1)) # merge last row into a single cell
        ]))
        elements.append(table)
        if action.get('difficulty_options'):
            elements.append(Paragraph('Difficulty adjustment options:', style=minor_subtitle))
            data = []
            for option in action.get('difficulty_options'):
                description = re.sub('\s+', ' ', option['effect'])
                data.append([f"Difficulty adjustment: {option['adjustment']}",
                             Paragraph(description, basic_paragraph_style)])
            table = Table(data, colWidths=[160, 320])
            table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
            elements.append(table)


    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements


def get_normal_feats_chapter():
    elements = [
        {'type': 'title', 'content': 'Normal feats'},
        {'type': 'paragraph',
         'content': """
Feats in this chapter are gained using your level up advancement points. Feats are spread out between the paths. For
example mage feats can only be taken using mage advancement points. Mixed feats can be taken by combining the 2 path
advancement in any way you like. 
            """},
    ]
    first = True
    for path_name, path_feats in feats.items():
        if not first:
            elements.append({'type': 'flowables', 'content': [PageBreak()]})
        else:
            first = False
        elements.append({'type': 'subtitle', 'content': path_name})


        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
