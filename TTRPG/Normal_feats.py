feats = {
    'Mage': [
        {'cost': 'small',
         'name': 'Adept attuner',
         'effect': '''You can attune to one additional magical item'''
         },
        {'cost': 'small',
         'name': 'Enduring magic',
         'metamagic_option': {
             'difficulty': 'Rp.Rp',
             'effect': '''Can only be applied to concentration spells or spells with duration.
     Concentration spells without duration gain a duration of 3 rounds. Spells with duration increase their
     duration by 3 rounds or double it, whichever has greater effect''',
         },
         },
        {'cost': 'small',
         'name': 'Large magic',
         'metamagic_option': {
             'difficulty': 'Rp',
             'effect': 'Increase spell radius, which has radius by 1 sq.',
         },
         },
        {'cost': 'small',
         'name': 'Distant magic',
         'metamagic_option': {
             'difficulty': 'Rp',
             'effect': 'Increase spell distance by 6 sq. or double it, whichever has greater effect',
         },
         },
        {'cost': 'small',
         'name': 'Commune with animals',
         'effect': '''You are able to communicate with animals. To get desired communication, GM can provide you a dice
 target for the scene, and you can use nature school of magic proficiency to meet the target'''
         },
        {'cost': 'medium',
         'name': 'Talented attuner',
         'effect': '''You can attune to one additional magical item'''
         },
        {'cost': 'medium',
         'name': 'Twin magic',
         'metamagic_option': {
             'difficulty': 'Rp.Rp',
             'effect': '''Cast the spell twice. You may choose new targets for second
        cast. Concentration spells share concentration for both casts.''',
             'L': 1,
         },
         },
        {'cost': 'medium',
         'name': 'Hex master',
         'effect': '''You can apply max 2 hexes on a creature instead of only 1''',
         },
        {'cost': 'medium',
         'name': 'Fire and ice',
         'effect': '''When burning or freezing applied to enemies by you cancel out the previous freezing or burning
         stacks, the enemy takes 3 damage for each stack cancelled out this way. This bypasses defense and damage 
         reduction.
            ''',
         },
        {'cost': 'medium',
         'name': 'Trickster',
         'effect': '''
 Whenever you apply a level of burning, disoriented or afraid, or when you make the enemy prone, you also 
 disrupt 1.
         ''',
         },
        {
            'cost': 'medium',
            'requires': 'Ritual master',
            'name': 'Improved Ritual master',
            'effect': '''
You are more skilled at including others in your rituals. Nobody who joins your ritual has disadvantage, even if they
don't know the ritual.
            ''',
        },

        {'cost': 'major',
         'requires': 'Commune with animals',
         'name': 'An useful pet',
         'effect': '''
You have a pet that is useful both in combat and outside of it. Choose a physical form, and then a out of combat 
ability:

Physical forms:

The pet is a small creature, either flying, or jumping around, they are super agile and so enemies usually cannot hit
them easily and therefore ignore them. AoE abilities still knock them out. In combat, they can be ordered to disrupt one 
enemy each turn. Small pet has 1 HP.

The pet is a large predator who acts like a minion meaning they always do fixed damage of 2 and have fixed HP of 5.
Their downside is that they can be taken out by the enemy.

The pet is a mount, who you can ride on. In combat whenever you use a dice for movement you can move 2 extra squares.
The mount has 6 HP. When you or the mount are attacked you can choose who defends the attack / takes the damage. AoE
effects still effect both of you.

When a pet is knocked out, they require time, care and 20 gp worth of medical herbs to fix them up. If they are knocked
out but take additional damage, either because the enemy is sadistic or there is some AoE damaging effect, they die,
and your character is devastated by the fact. However it is possible to find a new pet over time as you get over it.

Outside combat bonuses. Choose 1 for the pet:

1. Outside combat you have advantage for survival checks when detecting ambushes, traps and other threats.

2. Outside of combat they give you advantage when tracking or chasing someone.

3. Outside of combat the pet increases your prestige, and thus can give you an advantage in diplomacy checks where 
appropriate.
         '''
         },
        {'cost': 'medium',
         'name': 'Hex master',
         'effect': '''You can apply max 2 hexes on a creature instead of only 1''',
         },
        {'cost': 'medium',
         'name': 'Fire and ice',
         'effect': '''When burning or freezing applied to enemies by you cancel out the previous freezing or burning
         stacks, the enemy takes 3 damage for each stack cancelled out this way. This bypasses defense and damage 
         reduction.
            ''',
         },
        {'cost': 'medium',
         'name': 'Trickster',
         'effect': '''
 Whenever you apply a level of burning, disoriented or afraid, or when you make the enemy prone, you also 
 disrupt 1.
         ''',
         },
        {
            'cost': 'medium',
            'requires': 'Ritual master',
            'name': 'Improved Ritual master',
            'effect': '''
You are more skilled at including others in your rituals. Nobody who joins your ritual has disadvantage, even if they
don't know the ritual.
            ''',
        },
        {'cost': 'major',
         'name': 'Pyromancy',
         'effect': '''Whenever your spell applies at least 1 stack of burning onto an enemy, it applies one more stack
         of burning onto them.
            ''',
         },
        {'cost': 'major',
         'requires': 'Pyromancy',
         'name': 'Fire mastery',
         'effect': '''Whenever a stack of burning is removed that was applied by you, gain a temporary flame token that
         lasts until end of combat.
         
You can spend flame tokens to fuel your spells and attacks:

3 Flame tokens: Apply burning on one of the target's of the spell or attack

5 Flame tokens: Remove a negative status effect from yourself and move it onto the target of the spell or attack.

7 flame tokens: At the end of your attack or spell remove all stacks of burning from the target dealing 3 damage per
removed stack. If that kills the target, refresh your dice pool. The cost of this ability increases
by 5 for the duration of this encounter.
            ''',
         },
        {'cost': 'major',
         'name': 'Will breaker',
         'effect': '''
As you apply disoriented or afraid onto enemies, your ability to effect the battlefield becomes increasingly stronger
based on the total levels of these conditions that you have applied during this combat

At least 2 levels per remaining number of enemies: Enemies with disoriented or afraid cannot attack you and have their 
damage reduced by 1 for each level of disoriented and afraid.

At least 4 levels per remaining number of enemies: Enemies with disoriented or afraid get disadvantage to will checks. 
Mobs recover from disoriented and afraid twice as slow.

At least 7 levels per remaining number of enemies: Enemies with at least 3 combined levels of disoriented and afraid 
will stop fighting and just fall prone and give up. This may not effect enemy heroes, but in this case the enemy hero 
gets disadvantage for all their spells and attacks. 

At least 10 levels per remaining number of enemies: All your allies gain advantage with all their offensive spells and 
attacks.
         ''',
         },
        {
            'cost': 'major',
            'name': 'Iron concentration',
            'effect': '''You can spend any dice to maintain concentration''',
        },
        {
            'cost': 'major',
            'name': 'Dimension mastery',
            'requires': 'Expert dimension proficiency',
            'effect': '''
            When taking this feat you craft an object, a talisman of sorts, which, while you are attuned to it, you can
            cast spells from the point of that object.
            
            If you are are legendary in dimension magic, you can craft one additional such object.
            ''',
        },
        {
            'cost': 'major',
            'name': 'Enchanter',
            'effect': '''
Enchantment spells cost 1 less power dice to cast. When the concentration cost is higher than 1 power dice, then that
too costs 1 less power dice.
            ''',
        },
        {
            'cost': 'major',
            'name': 'Holy bonds',
            'effect': '''
You can attune to any number of your party members instead of items.

Whenever attuned party member receives a negative status effect you can instead move it to yourself.

For spells which the target is self, you can instead cast it targeting one of the attuned party members.

The minimum range for these spells becomes 5 sq.

Other spells targeting attuned party members have advantage
            ''',
        },
        {
            'cost': 'major',
            'name': 'Ritual master',
            'effect': '''
You are more skilled at including others in your rituals. All casters who join your ritual, their minimum proficiency
is your proficiency - 1.
            ''',
        },

        {
            'cost': 'major',
            'name': 'Blood magic',
            'effect': '''
You may spend your life points the same way you can spend your mana to make spells cheaper. By doing that you take
damage directly to your life bypassing defense and damage reduction.
    
For 1 damage reduce the spell cost by 1 dice, for 3 damage, by 2 dice, for 6 damage by 3 dice and for 10 damage by 4 
dice. You can combine this with mana, and the maximum reduction using your life points is equal to your spell school
proficiency. However the combined total reduction with reduction from mana is your proficiency + 2. So if your
proficiency is 4, then you could spend 10 life points and 3 mana to reduce the cost by 6 dice, but you cannot spend
10 life points and 6 mana to reduce it by 7 any more.

Also, you cannot be healed by the heal spell (that includes healing potions which apply the spell on you).
            ''',
        },
    #     {
    #         'cost': 'major',
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
    #             'cost': '1-3AP',
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
    #         'cost': 'medium',
    #         'requires': 'Shackles of suffering',
    #         'name': 'Prolonged shackles',
    #         'effect': '''
    # Shackles of suffering lasts 1 more round
    # ''',
    #     },
    ],



    'Martial': [

        {'cost': 'small',
            'name': 'Kick',
            'effect': '''Kick is a special unarmed move, which can be used as long as you have light or no armor. You
             may be wielding weapons. It does use a unarmed (mental) slot.''',
            'action': {
             'cost': 'R5.R5.R5',
             'proficiency': 'unarmed',
             'additional_costs': '1 stamina',
             'effect': '''Push an enemy 2 squares, apply 2 unabalanced''',
             'difficulty_options': [
                 {
                     'cost': 'R5',
                     'effect': '''Send them flying 2 additional squares and have them take 2 more levels of unbalanced''',
                 },
                 {
                     'cost': 'R5',
                     'effect': '''+1 damage''',
                 },
             ]
            },
        },
        {'cost': 'small',
             'name': 'Medium armor proficiency',
             'effect': '''Remove the penalty of -1 physique proficiency when wearing medium armor''',
        },
        {'cost': 'small',
         'name': 'Defensive stance',
         'effect': '''If you have not attacked or cast an offensive spell since the beginning of your last turn
         you have an additional +2 maximum defense while guarded.''',
         },
        {
            'cost': 'small',
            'name': 'Power strike',
            'effect': '''When making an attack with 2 handed melee weapon you can spend 1 stamina to deal 2 additional
damage''',
        },
        {'cost': 'small',
         'requires': 'Rage',
         'name': 'Prolonged rage',
         'effect': '''
        Your rage lasts 3 additional rounds, or 2 additional rounds if wearing heavy armor.
        ''',
         },
        {'cost': 'small',
         'requires': 'Heavy armor proficiency',
         'name': 'Fortress',
         'effect': '''You can use fortitude proficiency against afraid and disoriented conditions instead of will.
''',
         },
        {'cost': 'small',
         'name': 'Toxicologist',
         'effect': '''When drinking potions, only every other potion adds an R3 to fortitude checks for drinking
  potions instead of every potion. You have +1 to proficiency against poison, and +2 proficiency to fort saves 
  against alcohol.''',
         },
        {'cost': 'medium',
             'name': 'Heavy armor proficiency',
             'effect': '''Wearing heavy armor only applies a -1 physique proficiency penalty instead of -2
                ''',
         },
        {'cost': 'medium',
         'name': 'Dodging',
         'effect': '''Whenever you would receive damage you can react with a R5 physique dice to negate that damage.
     This cost goes up by 1 X R5 every time you use this ability during encounter. You can take the recover
     action to reset it to 1 dice again.

     Dodging requires no or light armor''',
         'action': {
             'cost': 'R5.R5.R5',
             'proficiency': 'physique',
             'additional_costs': '1 stamina',
             'target': 'self',
             'effect': '''reset the dodging reaction dice cost to 1 dice''',
            },
        },
        {
            'cost': 'medium',
            'name': 'Menace',
            'effect': '''When you damage an enemy with a melee attack, then until the start of your next turn, they have
            disadvantage when attacking your allies''',
        },
        {
            'cost': 'medium',
            'name': 'Opportunist',
            'effect': '''
                You have advanatege with attacks against enemies that have damaged your allies but not you since the 
                end of your last turn.
            '''
        },
        {'cost': 'medium',
         'name': 'Backstabber',
         'effect': '''When attacking someone with a one handed melee weapon from behind or while the opponent is unaware
     of your presence, you have double advantage.''',
         },
        {
            'cost': 'medium',
            'name': 'Shadow',
            'effect': '''You are able to take maximum advantage of disoriented foes. Foes who have at least 1 level
of disorientation, have disadvantage for attacks against you. You have advantage with attacks against foes
who have at least 2 levels of disoriented. When taking a move action, then one target creature with at least
2 levels of disoriented loses track of you and become unaware of your presence.''',
        },
        {
            'cost': 'medium',
            'name': 'War shout',
            'effect': '''You can spend 2 natural R5 or R4 to make a proper shout, that would apply 1 level of afraid
            into all enemies within 4 sq. of you, or 2 natural R6 to make an even more powerful bone-shattering shout,
            that applies 1 level of afraid into all enemies within 2 sq. of you and 1 additional level of afraid into
            enemies within 5 sq. of you''',
        },
        {'cost': 'major',
             'name': 'Two weapon fighter',
             'effect': '''
                Your maximum defense is increased by 1 while wielding two weapons.
                
                When wielding two melee weapons which sum of power dice is less than or equal to 6, then you can use R6
                from your dice pool as a power dice for attacks with both weapon (and it only consumes a single action
                limit).
                ''',
        },
        {'cost': 'major',
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
        {'cost': 'major',
             'requires': 'lvl 5.',
             'name': 'Master of defenses',
             'effect': '''
Defend action now requires only R2. You can also use Defend action as a reaction once between your turns after being
attacked.
                ''',
        },
        {'cost': 'major',
             'name': 'Savage Axe',
             'effect': '''
             
You gain 1 savagery token per stamina spent. These tokens must be used in the current round. When you
attack with an axe you can spend savagery points to deal 1 additional damage per savagery point.

You gain additional difficulty adjustment options for two handed axes:

Rp: Spend 2 savagery tokens to add a level of afraid to the enemy

Rp: Spend 2 savagery tokens to add 1 level of vulnerable to the enemy. 
                ''',
        },
        {'cost': 'major',
         'name': 'Sentinel',
         'effect': '''
When wielding a polearm, you get a zone of control around you of 2 sq. Enemies that want to move through your ZoC or
want to enter within 1 sq. of you need to provide a R6 phsyique roll in order to do that. When a pawn enters your ZoC
they end their turn, when rook or knight need to pay R6 then they do, but they end their turn after finishing the
maneuver, bishops don't enter your ZoC. When a rook ends their turn next to you, the sentinel feat becomes disabled.

Enemies entering your ZoC give you a attack reaction opportunity.

First reaction attack with a polearm in between your turns has double advantage, the rest have simple advantage.
         ''',
         },
        {'cost': 'major',
         'name': 'Rage',
         'effect': '''
            Gain rage action.
         ''',
         'action': {
             'cost': 'R6',
             'proficiency': 'fortitude',
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
        {'cost': 'major',
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

        {'cost': 'major',
         'name': 'Hex arrow',
         'effect': '''When taking this feat, choose a {hex spell}
            Whenever you hit an enemy roll 2d6, if the sum is lower than the damage you dealt with this attack also
            apply chosen hex or a hex spell you know onto that enemy. No concentration is required to maintain that hex.
            ''',
         },
        {'cost': 'major',
         'name': 'Commander',
         'effect': '''Leadership becomes a martial skill.

         Gain the coordination action.
         ''',
         'action': {
             'cost': 'R3.R3.R3',
             'range': '6 sq..',
             'target': 'One enemy',
             'proficiency': 'leadership',
             'effect': '''
             Once an ally damages the targeted enemy all other allies gain advantage for all attacks and spells
             targeting that enemy. This lasts until the end of turn.
             ''',
             'difficulty_options': [
                 {
                     'cost': 'R3.R3',
                     'effect': '''Once two allies have damaged targeted enemy, all other allies gain double advantage
                     for all attacks and spells targeting that enemy.''',
                 },
             ]
         }
         },
        # {'cost': 'medium',
        #  'name': 'Improved coordination',
        #  'requires': 'Commander',
        #  'effect': '''Coordination action can target 1 additional ally.
        #  ''',
        #  },
        {'cost': 'major',
         'name': 'Blessed warrior',
         'effect': '''
Increase your maximum defense by 1. Whenever you hit an enemy with an attack involving at least 4 power dice
you may choose 1 option:

* remove one level of negative status effect from you or one of your allies.

* recover 1 stamina

* spend 1 mana to deal an additional 2 damage. (requires mage path)
         ''',
         },
        # {'cost': 'major',
        #  'requires': 'Blessed warrior',
        #  'name': 'Blessed Champion',
        #  'effect': '''At the start of combat you get an extra round where you can only cast buff spells on yourself.
        #  Alternatively you could have a single base-line buff from "Guardian",
        #  ''',
        #  },
#         {'cost': 8,
#          'requires': 'Blessed Champion',
#          'name': 'Blessed commander',
#          'effect': '''The chosen buff also applies to all your allies within 20 m. of you.
#          ''',
#          },

    ],
    'Skilled': [
        {'cost': 'small',
         'name': 'Knowing when to shut up',
         'effect': '''During the diplomacy checks, one bad result from risk dice has no effect.''',
         },
        {'cost': 'small',
         'name': 'Deep apology',
         'effect': '''
         When your or your parties past deeds cause a diplomacy challange to become harder, then once per NPC, you can
         offer a deep apology to reduce the penalty by 1 dice. 
         ''',
        },
        {
            'cost': 'small',
            'name': 'Intimidating presence',
            'effect': '''
You can use twos in the dice pool for diplomacy roll targets regardless of the roll target. You cannot nudge dice to
become twos though, and when you do use this ability, the diplomacy action gets a intimidation aspect to it. You will
succeed, BUT!

You must declare when using this ability.
''',
        },
        {'cost': 'small',
         'name': 'Foresight',
         'action': {
             'cost': '-',
             'additional_costs': '1 Luck token',
             'effect': '''Once every time after visiting a settlement with shops, you can take out a common item
                from your backpack, which you as a player actually had not bought from the settlement, but consider it
                having been bought (subtract the gold cost of the item from your balance).'''
         }
         },
        {'name': 'Lore weaver',
         'cost': 'small',
         'effect': '''
        By spending 1 luck token , you can use the "is there such a thing in the game-world" option one additional time
        per scene.
            '''
         },
        {'cost': 'small',
         'name': 'Lucky finder',
         'effect': '''
When rolling loot table, you can spend 2 luck token to be presented with 2 options, you still pick only 1.''',
         },
        {'cost': 'medium',
         'name': 'Insightful',
         'effect': '''
Whenever you spend at least 3 dice for lore related activities, you can ask a yes / no / yes and no / uncertain question
, which the GM will answer based on the evidence which can be found in the scene or if you are having a conversation
with someone, that someone is able to provide.''',
         },
        {'cost': 'medium',
         'name': 'Master plan',
         'effect': '''
         You gain the master plan action, which can be used during scene. This is a leadership action.
         ''',
         'action': {
             'cost': 'R3.R3.R3',
             'target': '3 allies',
             'proficiency': 'leadership',
             'effect': '''
Targeted allies roll 1 extra temporary dice into their dice pool for this scene. These dice can be traded between
players on a 1 to 1 basis.
             ''',
             'difficulty_options': [
                 {
                     'cost': 'R3.R3',
                     'effect': '''They roll one additional dice''',
                 },
             ]
            }
        },
        {'cost': 'medium',
         'name': 'Tinkerer',
         'effect': '''
You have the ability to come up and craft all sorts of crazy gadgets. You carry materials with you, and during
campaign turns, if you can explain how a wild gadget could help you solve a challange, you can use the crafting
proficiency instead. the cost in materials depends on the challenge difficulty:


3 dice: 15 gp


4 dice: 30 gp


5 dice: 50 gp


6 dice: 80 gp


From there on it doubles every dice.
         
Also by doubling the gadget cost, you gain an advantage.
         ''',
        },
        {'cost': 'medium',
         'name': 'Inspiring',
         'effect': '''Grants you the ability to inspire others by spending luck tokens.

         Inspire action uses leadership skill.
         ''',
         'action': {
             'cost': 'R3.R3',
             'range': '12 m.',
             'target': '1 creature',
             'additional_costs': '1 Luck token',
             'effect': '''target gains inspiration''',
             'difficulty_options': [
                 {
                     'cost': 'R6',
                     'effect': '''They lose 1 level of Will related status effects''',
                 },
                 {
                     'cost': 'R6.R6',
                     'effect': '''They lose 3 level of Will related status effects''',
                 },
                 {
                     'cost': 'R3',
                     'effect': '''They gain 1 additional temporary dice that they can use until their next roll''',
                 },
                ]
            }
         },
        {
            'cost': 'medium',
            'requires': '3 proficiency in leadership',
            'name': 'Expert of sacrifice',
            'effect': '''When assigning dice to scene roll target's, you can give one of those advantage at the cost
            of another a disadvantage. The one that is given disadvantage must be one that would be passed if not
            given disadvantage to (and the dice for passing must still be commited).''',
        },

        {'name': 'Sir, know it all',
         'cost': 'medium',
         'effect': '''

         ''',
         'action': {
             'cost': 'R5',
             'target': '1 ally',
             'proficiency': 'lore',
             'effect': '''
Targeted ally is assisted by your knowledge and gets advantage in another skill check of your choosing.
    ''',
             'difficulty_options': [
                 {
                     'cost': 'R5.R5',
                     'effect': '''Also provide them double advantage''',
                 },
             ]
         }
         },
        {'cost': 'major',
         'name': 'Offer them to surrender',
         'effect': '''
         You gain the offer enemy to surrender ability.
         ''',
         'action': {
             'cost': 'R5.R5',
             'range': '3 sq.',
             'target': 'single',
             'effect': '''
An enemy with 3 moral or less will surrender. If they have more than 3 but less than 6 moral remaining they will be
get 2 confusion.
             ''',
             'difficulty_options': [
                 {
                     'cost': 'R5',
                     'effect': '''Increase the moral threshold for surrendering and confusion by 1''',
                 },
                 {
                     'cost': 'R3.R3',
                     'effect': '''Target one additional target with this ability''',
                 },
             ]
            }
        },
        {'cost': 'major',
         'name': 'Natural leader',
         'effect': '''
         You gain the coordinate action, which can used both during combat and out of combat.
         ''',
         'action': {
             'cost': 'R3.R3',
             'range': '6 sq.',
             'target': '2 allies',
             'effect': '''
Targeted allies may give up to 1 dice to the other ally to be used temporarily (that dice preserves it roll). The dice
is returned after using it.
             ''',
             'difficulty_options': [
                 {
                     'cost': 'R3',
                     'effect': '''They can give up to 1 additional dice''',
                 },
             ]
            }
        },
        {'cost': 'major',
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
        {
            'cost': 'major',
            'name': 'Inspiring leader',
            'requires': 'Inspiring',
            'effect': '''When using the inspire ability, you can spend 1 additional luck token so that all your party
            members except fo you gain inspiration and other benefits of the inspire action.
            ''',
        },
        {
            'cost': 'major',
            'name': 'Fortunate',
            'effect': '''
When negotiating for rewards, finding treasure, selling something unique, 
you can meet a roll target of R5.R5.R5 for values lower than 500 gp. or R5.R5.R5.R5
for values larger than that but lower than 5000 gp or R5.R5.R5.R5.R5 for even larger values to increase the gold gains
by 50 %. You can use diplomacy skill for these checks. This roll target needs to be met
during the same scene, so it still competes where the whole interaction happens.''',
        },
        {
            'cost': 'major',
            'name': 'Excellent instructor',
         'action': {
             'cost': 'R5.R5',
             'target': '1 ally',
             'proficiency': 'lore',
             'effect': '''
             Targeted ally gains your level of proficiency in a skill of your choice for the duration of this turn /
             scene.
             ''',
             'difficulty_options': [
                 {
                     'cost': 'R5',
                     'effect': '''You can have another ally gain the same proficency for this scene / turn.''',
                 },
             ]
            }
        },
        {
            'cost': 'major',
            'requires': 'Excellent instructor',
            'name': 'Master',
            'effect': '''For each party member you can choose one skill. Their effective proficiency bonus in that
            skill is equal to yours. That skill can be changed during down time.
''',
        },
    ],
    'Mage/Martial': [
        {'cost': 'medium',
         'name': 'Blade enchanter',
         'effect': '''Weapon enchantment spells that are applied to the weapons you wield don't require concentration
         as long as you hit something with that weapon every round after it has been applied.
         ''',
         },
        {'cost': 'major',
         'name': 'Spell blade (or bow)',
         'effect': '''
         When you hit an enemy with a blade you can cast a single target spell that targets that enemy that costs no
         more than the number of power dice you used for the attack. Spend 1 mana for each dice cost for that spell.
         ''',
         },
        {'cost': 'major',
         'name': 'Magical protection',
         'effect': '''
         Whenever you cast a buff spell on yourself that used at least 4 power dice, also do the Defend action for free.
         
         Gain +1 maximum defense.
         ''',
         },
        {'cost': 'major',
         'name': 'Torturer',
         'effect': '''
For each different type of negative status effect you have applied onto an enemy that they have not yet removed, they
have 1 level of vulnerable, which is only removed by removing negative status effects that cause it.
         ''',
         },
    ],
    'Mage/Skilled': [
        {
            'cost': 'major',
            'name': 'Potion maker',
            'effect': '''You can make magical potions, which have the effects of spells you know how to cast, and
which difficulty requirements you meat. These potions have however certain constraints:

1. They target is the person who drinks the potion. Spells with area of effect lose the area component.

2. Spell effects that have additional targets, like a location, cannot be made into a potion. The potion
can only effect the creature drinking the potion.

3. When these potions have a concentration effect, instead they simply last 3 iterations (normally this
is 3 rounds, but if a spell duration is otherwise 5 rounds, that is extended to 15 rounds instead and so on)

In order to make these potions there is a baseline cost for ingredients that is based on difficulty. Difficulty is based
on the number of dice that the spell, which effect is applied to the potion. Maximum number of dice is 6.
Through role play, group focuses etc. these may be reduced.

DX means that the underlying spell requires X dice.

D2 and less - 20 gp
D3 - 50 gp
D4 - 150 gp
D5 - 400 gp
D6 - 1000 gp


It is also possible to increase the duration of those potions to 5 iterations, which would double the cost.

It is also possible to combine 2 spells into 1 potion, but they would add up their difficulties. This option
would also double the cost.

Potions are also available through shops in the game world, however their prices would be around twice
higher.
''',
        },
    ],
    'Martial/Skilled': [
        {'name': 'Poison specialist',
         'cost': 'major',
         'effect': '''
You can prepare poison coatings and coat weapons with poison. In order to prepare poisons you
need to gather poison glands or procure necessary raw materials from the marketplace. Both of them
requires you to choose them as your personal focus. Depending on the situation it could require gathering,
diplomacy, survival and would also have a different difficulty, plus may require some extra cost such as gold.

By default a coating of 3 stacks of following poisons on a melee weapon or 2 stack a single arrow costs that
much money, this can be reduced with role-play,group focuses:

1 damage per stack at the beginning of target's turn: 20 gp

2 damage per stack at the beginning of target's turn: 100 gp

stack of disoriented: 50 gp

stack of afraid: 80 gp

stack of freezing: 200 gp

The price doubles if you want to apply 5 stacks on a melee weapon or 3 stacks on a single arrow. And doubles
again when wanting to apply 7 stacks on a melee weapon or 4 stacks on a single arrow.

By adding 100 gp to the base price, it takes one more dice to remove a stack of poison from oneself, and by adding an 
additional 300 gp to the base price, it takes another dice to remove a stack of poison from oneself.

A successful melee attack made with the weapon moves 1 stack of poison onto the hit target. A successful attack
with an arrow moves all stacks of poison from the arrow onto the target.

At the beginning of the turn and after the poison stacks have taken effect, poisoned target can meet a R5 fortitude
check to remove a stack of poison from themselves. 

Stacks of disoriented, crazed, afraid, and freezing cannot be reduced normally even though their effects
work the same as having the same levels of the these status effects.

Enchanted weapons cannot be coated with poison.
'''
         },
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
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style, add_dice_images
from reportlab.lib import colors
import re

def prep_feat_flowable(feat):
    elements = []
    elements.append(Paragraph(feat['name'], style=minor_title))
    elements.append(Paragraph(f"Feat level: {feat['cost']}", style=minor_subtitle))

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
            [Paragraph(f"Base cost: {add_dice_images(action['cost'])}", style=basic_paragraph_style), f"Proficiency: {action.get('proficiency', '-')}", f"Other costs: {feat.get('additional_costs', '-')}"],
            [f"Target: {action.get('target', '-')}", f"Duration: {action.get('duration', '-')}", f"Limit: {action.get('limit', '-')}", ],
            [f"Restrictions: {action.get('restrictions', '-')}", f"", f""],
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
                data.append([Paragraph(f"+ {add_dice_images(option['cost'])}", style=basic_paragraph_style),
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
