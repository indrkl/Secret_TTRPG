feats = {
    'Racial': [
        {
            'name': 'Extraordinary senses',
            'description': '''
Acquinted: You can see 6 sq. in the dark, and 12 sq. in low light

Adept: You can see 25 sq. in the dark and 50 sq. in low light

Talented: In addition to the adept feature, you have blind sight in 2 sq around you.

Legendary: You can see in the dark as well as in the light. You have blind sight in 6 sq around you.
            ''',
        },
        {
            'name': 'Wings',
            'description': '''
Acquinted: You don't take any falling damage as long as you are wearing light armor.

Adept: You don't take any falling damage as long as you are wearing light armor and are not carrying more than
1/5th of your carry weight, and when falling from great heights
you can glide, falling 6 sq. per round and moving 6 sq. per round at any direction.

Talented: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your carry weight, then you can fly as your move action. If you do, move 2 less squares.

Legendary: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your carry weight, then you can fly at your move speed.
            ''',
        },
        {
            'name': 'Natural armor',
            'description': '''
You can only have the maximum defensive benefits from the armor you wear or this feat, they do not stack.

You can lower the bonus of the natural armor by 2 to receive the no armor bonus.

Acquinted: Your maximum defense from natural armor is 2.

Adept: Your maximum defense from natural armor is 3.

Talented: Your maximum defense from natural armor is 4.

Legendary: Your maximum defense from natural armor is 5.

Natural armor bonus increases by 1 at levels 7 and 14

Also when you are talented or legendary, then you get the option to take the heavy armor penalty (cannot take both this
and no armor bonus) in order to get 1 damage reduction. This increases to 2 damage reduction at level 7 and to 3 damage
reduction at level 14
            ''',
        },
        {
            'requires': 'Adept',
            'name': 'Claws',
            'description': '''
You have claws. They can be used to attack. They use claw proficiency which can be upgraded using either Martial path
or the path which innate feat is replaced by this one.

Adept: You have claws which enable you to do a simple claw attack when unarmed. They use claw proficiency
and R2 as the power dice. Check the claw statistics under equipment.

Talented: Your left hand claw uses R4 as the power dice, check the secondary claw statistics.

Legendary: Your claw proficiency is not shared between the two hands.
            ''',
        },
        {
            'requires': 'Legendary',
            'name': 'Four hands',
            'description': '''
You have four hands, meaning you can hold 4 one handed items, 2 two handed items or any combination in between.
            ''',
        },
    ],
    'Background': [
        {
            'requires': 'Legendary',
            'name': 'Royalty',
            'description': '''
You belong to one of the well-known houses in the realm. That grants you access to places commoners don't have access to
and guards and many other officials are more forgiving for various problems you may cause. You start the game with 
2000 additional gp. and always have a castle to stay in at least one of the major cities. But in most cities there is
often someone who is willing to host you for free in a very quality lodging (another house member, allied house member,
simply someone who wants favor from your house etc.)
    ''',
        },
    ],
    'Mage': [
        # {
        #     'name': 'Favoured magic',
        #     'description': '''Choose 1 school of magic. Your max difficulty and spell DC for spells in that school is as
        #         if you were talented in the mage path.''',
        # },
        {
            'requires': 'Talented',
            'name': 'Metamagician',
            'description': '''Metamagic feats cost 2 less to learn but no less than 1. You can apply 1 level of large or 
            distant magic to a spell for free without increasing the difficulty, mana cost or metamagic limit.''',
        },
        {
            'requires': 'Adept',
            'name': 'Shifter',
            'description': '''You have a beastly form, that levels up as you do. In the beastly form, you cannot
            speak, don't benefit from any of your normal form advancements in any path, but you can level up using the
            beast path (used to make all the mighty beasts in the game). The level of your beastly path is equal to
            your magic path. Beastly form has the ability to turn back into your regular form. To turn into your
            beastly form you need to spend 1 mana per your character level and if you are in combat then also meet
            R5.R5.R5 roll target using nature magic. Your equipment merges
            into your body and loses it's magical effect until you return to your normal form. Scarred, damaged and
            wounded dice carry over when transforming to the other form.''',
        },
        {
            'name': 'Divine protector',
            'description': '''
            You can advance toughness using both mage and martial path. You can transfer a scarred dice from an ally
            to yourself (their scarred dice becomes normal, 1 of your normal dice become scarred) twice a day outside
            of combat.
            When your mage path is talented, When a dice would become scarred, roll it. On a 6, it stays normal.
            When your mage path is legendary, then it also doesn't become scarred on a 5. This effects also the dice
            you transfer from allies to yourself.
            '''
        },
        {
            'name': 'Raw caster',
            'requires': 'Talented',
            'description': '''
            You cannot cast concentration spells, or spells which cast time is greater than 1 round. You also cannot
            initiate rituals nor spend your mana for rituals.            
            
            Reroll the dice that you used to cast the first spell during the combat and return them to the dice pool.
            You do not reroll any virtual dice you gained by using mana, advantage or anything else.
            
            Recover that ability at the third, sixth and tenth round of combat.
            '''
        },
        {
            'name': 'Duality',
            'requires': 'Talented',
            'description': '''
Choose 2 schools of magic with different power dice values. You can only learn those two schools of magics. You share
the proficiency between those schools of magics (you need to progress only once, and spells from both of the schools
share proficiency using during combat and scenes).

The school with the lower power dice is called the lower school, and the other one the higher.

You can use the power dice from both schools to cast either school spells as long as the balance wouldn't tip by more
than 2 into either direction because of doing so. Outside of combat you can only use it once per scene.

When you spend a lower school's power dice to cast higher school spells your balance tips towards calm, and if you spend 
higher school's power dice to cast lower school spells your balance tips towards rage.
'''
        },
#         {
#             'name': 'Ritualist',
#             'requires': 'Adept',
#             'description': '''
# Downside is can only cas rituals and nothing else, implement later, when we have more rituals in the game,
# '''
#         },
        {
            'name': 'Savant',
            'requires': 'Adept',
            'description': '''
Choose 1 school of magic, you can only cast spells from that school of magic, and you can only gain proficiency with
that school of magic. The proficiency upgrade cost are halved (rounded up) and you can go to 4 proficiency even as an
adept mage.

If you are talented or legendary in the Mage path, then in addition you always have advantage when casting spells from
that school. 
'''
        },
    ],
    'Martial': [
        {
            'requires': 'Legendary',
            'name': 'Warcaster',
            'description': '''You can use stamina instead of mana for spellcasting.''',
        },
        {
            'requires': 'Legendary',
            'name': 'Mastery over body',
            'description': '''
Your body is your weapon. You have made a vow to give up using weapons, armor and magical items, instead you have
focused in making your body a supreme weapon. Now and during the level-ups you receive a progression feat, you can
pick one additional martial progression feat, but you cannot use weapons, shields, armors nor attune to any magical 
item.
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Bulwark',
            'description': '''
Enemies within 3 sq. of you that attack your allies have disadvantage. If you are legendary in martial then
you can spend stamina and mana to reduce damage taken by 1 per stamina or mana spent to you and you can use luck to 
reduce damage dealt to you by 3.
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Defiant',
            'description': '''
When your martial path is talented, When a dice would become scarred, roll it. On a 6, it stays normal.
When your martial path is legendary, then it also doesn't become scarred on a 5.

At the beginning of each round, if you have at least 3 damaged dice, you may choose one of the following:

* Heal 1 damaged dice and recover 1 stamina.

* Deal additional damage with one attack equal to the number of damaged dice.

* Roar, all enemies within 5 sq. radius get 1 level of afraid per 3 damaged dice on you rounded down. 
            ''',
        },
        # {
        #     'requires': 'Legendary',
        #     'name': 'Nimble',
        #     'description': '''Your action limit increases by 1''',
        # },
        {
            'requires': 'Talented',
            'name': 'Tough',
            'description': '''If you are talented, then every turn negate the first damage you receive. If you are
            legendary, then negate the first 2 damage you receive.''',
        },
        {
            'requires': 'Adept',
            'name': 'Natural killer',
            'description': '''
When you first time damage each enemy dice, gain a blood token that can be used during this encounter. If you are
talented or legendary, whenever you gain at least one blood token, gain one additional one.

Whenever you make an attack, you can use one and only one of those options once to boost that attack:

* spend 2 blood tokens to gain advantage or upgrade advantage to double advantage
 
* Spend 5 blood tokens to gain double advantage
 
* spend 1 blood token to deal 1 additional damage
 
* spend 2 blood tokens to disrupt 1 
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Anti mage',
            'description': '''You cannot be the target of spells (including those of your allies), nor can you cast 
                spells, nor can spells have any none-damaging effect on you. When you attack a spell caster, they lose 
                1 mana for every 3 unmitigated damage (that damages their dice)''',
        },
        # {
        #     'requires': 'Talented',
        #     'name': 'Life stealer',
        #     'description': '''You cannot be healed using nature magic. Heal 1d6 -1 life for each damage dice you deal in
        #         melee combat. Heal 1d6 instead, if your martial path is legendary.''',
        # },

        {
            'name': 'Harmonious body',
            'description': '''Whenever you advance in REFLEX or FORTITUDE saving throws. Advance in the other one as 
                well. If you are talented or legendary in martial, also advance in Will proficiency. You cannot advance
                in will proficiency from mage path in this case.''',
        },
    #     {
    #         'name': 'Favored weapon',
    #         'description': '''Choose 1 weapon category. In that weapon your MAX level is as if your PATH
    # level in Martial was 1 higher (cannot exceed Legendary).
    #     ''',
    #     },
    ],
    'Skilled': [
        {
            'requires': 'Legendary',
            'name': 'Wild magic',
            'description': '''You can cast any spell with the speed of at most 1 round not requiring concentration using 
1 luck token, even if you do not know that spell. Power dice for these spells are always D6 and
utility dice are always D5.''',
        },
        {
            'name': 'Specialist',
            'description': '''Choose 1 skill. You have an extra +1 for that skills proficiency. Note it does not 
            increase the cost of acquiring proficiency with this skill and also allows the skill to reach +5 proficiency
''',
        },
        {
            'name': 'Lucky',
            'description': '''When you spend a luck token, you cannot have disadvantage until the start of your next
            turn or until the scene ends. If you are talented/legendary in skilled path increase your maximum number of 
            luck tokens by 50 %.  
''',
        },
        {
            'name': 'Good fortune',
            'description': '''You can allow other party members to use your luck tokens. If you are talented/legendary
            in skilled path increase your maximum number of luck tokens by 50 %.  
''',
        },
        {
            'requires': 'Adept',
            'name': 'Prodigy',
            'description': '''At second level gain double the amount of advancements in skilled path (so at legendary
            skilled you gain 16 advancement points).
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Well connected',
            'description': '''Whenever you need some service, vendor or someone who knows stuff there is a chance you
            know someone in the current location who could help. In cities it is 50 % chance, in towns it is 25 % chance
            , in hamlets it is 10 % chance.
            
            Just because you know someone doesn't mean that they provide that service for free. They may have a positive
            disposition and maybe provide a small discount, but that is up to GM-s discretion. 
            ''',
        },
    ]
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style




def prep_feat_flowable(feat, name_addon=''):
    elements = []

    elements.append(Paragraph(feat['name'] + name_addon, style=minor_title))
    if feat.get('requires'):
        elements.append(Paragraph(f"Requires: {feat['requires']}", style=minor_subtitle))

    for para in feat['description'].split('\n\n'):
        para = para.replace('\n', ' ')
        elements.append(Paragraph(para, style=basic_paragraph_style))

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements


def get_innate_feat_chapter():
    elements = [
        {'type': 'title', 'content': 'Innate feats'},
        {'type': 'paragraph',
         'content': """
Innate feats are something you get as you create your character, granting you unique powers not available later on.
These are usually very unique or special effect. You get an innate feat for each path you have assigned a point into.
However if you have put more points into the path, then the innate feat is that much stronger. In addition, if you
are of some unique race, which would be able to for example have dark vision, or flying or something else, then refer
to the races innate feats. When taking one or more races innate feats you must give up a feat in one of the paths.
The power of the racial feat depends on the level of the path, which feat you gave up.

Finally I added one background feat, and may add more in the future. These can also be replaced by one of the path feats
similarly to racial feats.
        """},
    ]

    for path_name, path_feats in feats.items():
        elements.append({'type': 'subtitle', 'content': path_name})

        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
