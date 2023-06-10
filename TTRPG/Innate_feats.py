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
you can glide, falling 12 m. per round and moving 12 m. per round at any direction.

Talented: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your body weight, then you can fly at your move speed.

Legendary: You don't take any falling damage. If you are wearing light or no armor, and are not carrying more than
1/5th of your body weight, then you can fly at twice your move speed.
            ''',
        },
        {
            'name': 'Natural armor',
            'description': '''
With regards to natural armor bonus, this competes with the regular armor and all other kind of armor bonuses. Meaning
only the highest one of the armor bonuses has any effect on you. You can still wear armor and get the magical effects
of the armor and still benefit from the natural armor bonus, just not get the armor bonus from the armor.
Acquinted: you get a +1 natural armor bonus. At levels 7 it increases to +2.

Adept: you get a +2 natural armor bonus. At levels 7 it increases to +3. You cannot dodge.

Talented: you get a +2 natural armor bonus. At levels 7 it increases to +3. Choose between the ability to dodge, +1 AC
or +1 AC and being considered wearing heavy armor with it's downsides and benefits (as if having the heavy armor trait).

Legendary: you get a +3 natural armor bonus. At levels 7 it increases to +4. Choose between the ability to dodge, +1 AC
or +1 AC and being considered wearing heavy armor with it's downsides and benefits (as if having the heavy armor trait).
            ''',
        },
    ],
    'Mage': [
        {
            'name': 'Favoured magic',
            'description': '''Choose 1 school of magic. Your max difficulty and spell DC for spells in that school is as
                if you were talented in the mage path.''',
        },
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
            beastly form you need to spend 3 AP and 1 mana per your character level. Your equipment merges
            into your body and loses it's magical effect until you return to your normal form. When you take damage
            in your beastly form, it carries over to your normal form when you return. If you go down to 0 HP, you
            return to your normal form automatically.''',
        },
        {
            'name': 'Divine protector',
            'description': '''
            You're hit dice can be determined by your mage path instead of martial if your mage path is greater.
            You're mage path grants you 4 HP per mage path levels instead of 2 (similarly to Warrior path).
            Using 2 AP, you can transfer any number of your hit dice to one other creature. They cannot go over their
            maximum number of hit dice this way. When your mage path is talented, you always recover all your hit dice
            when you finish your daily rest. When your mage path is legendary, you have 50 % more maximum hit dice.
            '''
        },
        {
            'name': 'Raw caster',
            'description': '''
            You cannot cast concentration spells, or spells which cast time is greater than 1 round. You also cannot
            initiate rituals nor spend your mana for rituals.            
            However increase your maximum level in schools of magic by 1. If you are at least talented in mage path, 
            then spells also cost 1 mana less to cast.
            
            These bonuses increase by an additional 1 at levels 7 and 14.
            '''
        },
    ],
    'Martial': [
        {
            'requires': 'Legendary',
            'name': 'Warcaster',
            'description': '''You can cast spells using your stamina instead of mana.''',
        },
        {
            'requires': 'Talented',
            'name': 'Defiant',
            'description': '''
If you are legendary, then you have 50 % more hit dice.

Each round when you are below half of your hit points you can roll a hit dice, heal rolled
amount of life and choose 1 additional benefit:

* Recover 2 stamina per level

* heal additional Xd6, where X is your level / 2 rounded up.

* Gain 1 bonus AP this turn. At level 11, instead gain 2 bonus AP this turn.

* The next 2 attacks you make are lucky. This increases by 1 at levels 5, 10 and 15.

* Roar, forcing all enemies in 10 m. radius to check for afraid X times, where X is your level / 3 rounded
up.

If after that you are still below 25 % of your hit points, you can roll another hit dice, heal rolled amount
and choose another effect.
            ''',
        },
        {
            'requires': 'Legendary',
            'name': 'Nimble',
            'description': '''Your base AP per round is 4''',
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
                1 mana for every damage dice you roll against them.''',
        },
        {
            'requires': 'Talented',
            'name': 'Life stealer',
            'description': '''You cannot be healed using nature magic. Heal 1d6 -1 life for each damage dice you deal in 
                melee combat. Heal 1d6 instead, if your martial path is legendary.''',
        },

        {
            'name': 'Harmonious body',
            'description': '''Whenever you advance in REFLEX or FORTITUDE saving throws. Advance in the other one as 
                well''',
        },
        {
            'name': 'Favored weapon',
            'description': '''Choose 1 weapon category. In that weapon your MAX level is as if your PATH 
    level in Martial was 1 higher (cannot exceed Legendary).
        ''',
        },
    ],
    'Skilled': [
        {
            'requires': 'Legendary',
            'name': 'Wild magic',
            'description': '''You can cast any spell with the speed of at most 1 round not requiring concentration using 
your luck tokens instead of mana, even if you do not know that spell. Your max difficulty is determined by the 
Skilled PATH instead of MAGE path and assumes you having max level in the school of magic. 
Your spell DC is still determined by your actual proficiency bonus in that school.''',
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
