feats = {
    'Racial': [
        {
            'name': 'Extraordinary senses',
            'description': '''
Acquinted: You can see 12 m. in the dark, and 25 m. in low light

Adept: You can see 50 m. in the dark and 100 m. in low light

Talented: In addition to the adept feature, you have blind sight for 10 feet around you.

Legendary: You can see in the dark as well as in the light. You have blind sight for 30 feet around you.
            ''',
        },
        {
            'name': 'Wings',
            'description': '''
Acquinted: You don't take any falling damage as long as you are wearing light armor.

Adept: You don't take any falling damage as long as you are wearing medium armor, and when falling from great hights
you can glide, falling 6 sq. per round and moving 6 sq. per round at any direction.

Talented: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your carry weight, then you can fly at your move speed.

Legendary: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your carry weight, then you can fly at twice your move speed.
            ''',
        },
#         {
#             'name': 'Natural armor',
#             'description': '''
# With regards to natural armor bonus, this competes with the regular armor and all other kind of armor bonuses. Meaning
# only the highest one of the armor bonuses has any effect on you. You can still wear armor and get the magical effects
# of the armor and still benefit from the natural armor bonus, just not get the armor bonus from the armor.
# Acquinted: you get a +1 natural armor bonus. At levels 7 it increases to +2.
#
# Adept: you get a +2 natural armor bonus. At levels 7 it increases to +3. You cannot dodge.
#
# Talented: you get a +2 natural armor bonus. At levels 7 it increases to +3. Choose between the ability to dodge, +1 AC
# or +1 AC and being considered wearing heavy armor with it's downsides and benefits (as if having the heavy armor trait).
#
# Legendary: you get a +3 natural armor bonus. At levels 7 it increases to +4. Choose between the ability to dodge, +1 AC
# or +1 AC and being considered wearing heavy armor with it's downsides and benefits (as if having the heavy armor trait).
#             ''',
#         },
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
            'description': '''Metamagic feats cost 2 less to learn but no less than 0. You can apply 1 level of large or 
            distant magic to a spell for free without increasing the difficulty, mana cost or metamagic limit.''',
        },
        {
            'requires': 'Adept',
            'name': 'Shifter',
            'description': '''You have a beastly form, that levels up as you do. In the beastly form, you cannot
            speak, don't benefit from any of your normal form advancements in any path, but you can level up using the
            beast path (used to make all the mighty beasts in the game). The level of your beastly path is equal to
            your magic path. Beastly form has the ability to turn back into your regular form. To turn into your
            beastly form you need to spend 1 mana per your character level and if you are in combat then also meat
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
            When your mage path is talented, When a dice would become scarred, roll it. On a 5 or 6, it stays normal.
            When your mage path is legendary, then it also doesn't become scarred on a 3 and 4.
            '''
        },
        {
            'name': 'Raw caster',
            'description': '''
            You cannot cast concentration spells, or spells which cast time is greater than 1 round. You also cannot
            initiate rituals nor spend your mana for rituals.            
            However you have an extra raw caster dice, which you roll each round. This can be used to cast spells and
            it doesn't spend action limit.
            '''
        },
    ],
    'Martial': [
        # {
        #     'requires': 'Legendary',
        #     'name': 'Warcaster',
        #     'description': '''You can cast spells using your stamina instead of mana.''',
        # },
        {
            'requires': 'Talented',
            'name': 'Defiant',
            'description': '''
When your martial path is talented, When a dice would become scarred, roll it. On a 5 or 6, it stays normal.
When your martial path is legendary, then it also doesn't become scarred on a 3 and 4.

At the beginning of each round, if you have any damaged dice, you may choose one of the following:

* Heal 1 damaged dice.

* Deal additional damage with one attack equal to the number of damaged dice.

* Roar, all enemies within 5 sq. radius get 1 level of afraid per 3 damaged dice on you rounded down. 
            ''',
        },
        {
            'requires': 'Legendary',
            'name': 'Nimble',
            'description': '''Your action limit increases by 1''',
        },
        {
            'requires': 'Talented',
            'name': 'Versatile',
            'description': '''All feats cost 1 less but no less than 1 to take.''',
        },
        {
            'requires': 'Talented',
            'name': 'Anti-mage',
            'description': '''You cannot be the target of spells (including those of your allies), nor can you cast 
                spells, nor can spells have any none-damaging effect on you. When you attack a spell caster, they lose 
                1 mana for every unmitigated damage (that damages their dice)''',
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
                well''',
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
your luck tokens instead of mana, even if you do not know that spell. Power dice for these spells are always D6 and
utility dice are always D5.''',
        },
        {
            'name': 'Specialist',
            'description': '''Choose 1 skill. The MAX proficiency bonus for that skill is as if you were 1 level higher 
            in Skilled PATH (but cannot exceed Legendary).
''',
        },
        {
            'name': 'Lucky',
            'description': '''Whenever you spend a luck token and still fail the check, you recover that luck token.
            When you have disadvantage on a roll where you have spent a luck token on, negate disadvantage completely.
''',
        },
        {
            'name': 'Good fortune',
            'description': '''You can allow other party members to use your luck tokens. If you are talented/legendary
            in skilled path increase your daily number of luck tokens by 50 %.  
''',
        },
        {
            'requires': 'Adept',
            'name': 'Prodigy',
            'description': '''At first level gain double the amount of advancements in skilled path (so at legendary
            skilled you gain 16 advancement points).
            ''',
        },
    ]
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style


def prep_feat_flowable(feat):
    elements = []
    elements.append(Paragraph(feat['name'], style=minor_title))
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
        """},
    ]

    for path_name, path_feats in feats.items():
        elements.append({'type': 'subtitle', 'content': path_name})

        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
