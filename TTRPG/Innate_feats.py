feats = {
    'Racial': [
        {
            'name': 'Extraordinary senses',
            'description': '''
Acquinted: You can see 6 sq. in the dark, and 12 sq. in low light

Adept: You can see 25 sq. in the dark and 50 sq. in low light

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
            When your mage path is legendary, then it also doesn't become scarred on a 5.
            '''
        },
        {
            'name': 'Raw caster',
            'requires': 'Talented',
            'description': '''
            You cannot cast concentration spells, or spells which cast time is greater than 1 round. You also cannot
            initiate rituals nor spend your mana for rituals.            
            However you have an extra raw caster dice, which you roll each round. This can be used to cast spells and
            it doesn't spend action limit.
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
        {
            'requires': 'Legendary',
            'name': 'Nimble',
            'description': '''Your action limit increases by 1''',
        },
        {
            'requires': 'Legendary',
            'name': 'Nimble',
            'description': '''
            
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Anti-mage',
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
1 luck token per power dice, even if you do not know that spell. Power dice for these spells are always D6 and
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
            turn or until the scene ends. If you are talented/legendary in skilled path increase your daily number of 
            luck tokens by 50 %.  
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
            'description': '''At second level gain double the amount of advancements in skilled path (so at legendary
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
