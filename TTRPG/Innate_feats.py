feats = {
    'Racial': [
        {
            'name': 'Extraordinary senses',
            'description': '''
Acquainted: You can see 6 sq. in the dark, and 12 sq. in low light

Adept: You can see 25 sq. in the dark and 50 sq. in low light

Talented: In addition you have blind sight in 2 sq around you.

Legendary: You can see in the dark as well as in the light. You have blind sight in 6 sq around you.
            ''',
        },
        {
            'name': 'Wings',
            'description': '''
Acquainted: You don't take any falling damage as long as you are wearing light armor.

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
You can only have the maximum defensive benefits from the armor you wear or this foundation, they do not stack.

You can lower the bonus of the natural armor by 2 to receive the no armor bonus.

Acquainted: Your maximum defense from natural armor is 2.

Adept: Your maximum defense from natural armor is 3.

Talented: Your maximum defense from natural armor is 4.

Legendary: Your maximum defense from natural armor is 5.

Natural armor bonus increases by 1 at levels 5 and 10

Also when you are talented or legendary, then you get the option to take the heavy armor penalty (cannot take both this
and no armor bonus) in order to get 1 damage reduction. This increases to 2 damage reduction at level 5 and to 3 damage
reduction at level 10
            ''',
        },
        {
            'requires': 'Adept',
            'name': 'Claws',
            'description': '''
You have claws. They can be used to attack. They use claw proficiency (physique) which can be upgraded using either 
Martial path or the path which foundation is replaced by this one.

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
        {
            'requires': 'Talented',
            'name': 'Extreme temperature tolerance',
            'description': '''
Choose either fire or cold. If you choose fire, you are immunte to fire damage and burning condition. If you choose
cold, you are immunte to cold damage and freezing condition.

Legendary: Choose both of these options.
            ''',
        },
        {
            'requires': 'Adept',
            'name': 'Strong mind',
            'description': '''
You have immunity to afraid condition.

Talented: In addition you have immunity to disoriented condition

Legendary: In addition you cannot be confused or disrupted. 
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Poison secretion',
            'description': '''
You are immune to poison.
            
You naturally produce poison when stressed in battle. When picking this innate feat, choose the type of poison you make:
 * 1 damage at the beginning of each turns per stack
 * 1 levels of disoriented per stack
 * 1 levels of afraid per stack.
 When Legendary, you have one additional option:
 * 1 level of freezing.
 
To apply this poison to your next attack with weapon or bow, you need to spend a R4. 
You can do that at most once per turn, and this applies only 1 stack. 

If you are legendary you can instead spend R4.R4 to apply 2 stacks to the next attack with weapon or bow.
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
            'description': '''When learning a metamagic feat, learn a metamagic feat of same or lesser power. 
            You can apply 1 level of large or distant magic to a spell for free without increasing the dice cost or 
            metamagic limit.''',
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
            wounded dice carry over when transforming to and from the other form.''',
        },
        {
            'name': 'Divine protector',
            'description': '''
            You can advance toughness instead of spell school proficiency using mage path. 
            
            You can transfer a scarred dice 
            from an ally to yourself (their scarred dice becomes normal, 1 of your normal dice become scarred) twice
            during a strategic turn, while being outside of combat.
            
            When your mage path is talented, When a dice would become scarred, roll it. On a 6, it stays normal.
            When your mage path is legendary, then it also doesn't become scarred on a 5 as well. 
            This effects also the dice you transfer from allies to yourself.
            ''' # This is effectively almost a 50 % larger health pool for legendary mage.
        },
        {
            'name': 'Raw caster',
            'requires': 'Talented',
            'description': '''
            You cannot cast concentration spells, or spells which cast time is greater than 1 round. You also cannot
            initiate rituals nor spend your mana for rituals.            
            
            Reroll the dice that you used to cast the first spell during the combat and return them to the dice pool.
            You do not reroll any virtual dice you gained by using mana or through other means.
            
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
than 2 into either direction because of doing so. Outside of combat you can only use it once per turn.

When you spend a lower school's power dice to cast higher school spells your balance tips towards calm, and if you spend 
higher school's power dice to cast lower school spells your balance tips towards rage.

While at maximum calm you cannot be disoriented, while at maximum rage, you are immune to afraid condition.
'''
        },
#         {
#             'name': 'Ritualist',
#             'requires': 'Adept',
#             'description': '''
# Downside is can only cast rituals and nothing else, implement later, when we have more rituals in the game,
# '''
#         },
        {
            'name': 'Savant',
            'description': '''
Choose 1 school of magic, you can only cast spells from that school of magic, and you can only gain proficiency with
that school of magic. Proficiency advancement options all have max prof. 3 when acquainted and 4 otherwise, 
when advancing this school of magic.

If you are talented or legendary in the Mage path, then you get a free virtual power dice when casting spells with at
least 2 power dice without the virtual dice from that school.

When casting rituals from that school of magic, you get a free virtual power dice every round of ritual. 
The free power dice does not cost mana.
'''
        },
        {
            'name': 'Mana born',
            'requires': 'Legendary',
            'description': '''
You are a mana based being, even though you still have the humanoid form. You don't have blood and you only need to
consume mana infused foods. Each normal day of living uses 1 mana (or 1 medium turn, a normal strategic turn would spend
5 mana). In addition you can store mana in your dice equal to toughness amounts of mana per die.             

You don't have life, instead whenever you take damage you lose mana. You can give up your dice for toughness amounts of
mana and recover those dice for toughness amounts of mana. Meaning you can basically heal with the pace of recovering
mana. Whenever you have no mana, you die.

You have no blood, you are immune to poison. You cannot be healed using heal spell or healing potions, since you don't
lose dice, you simple release the mana stored in them as you need more mana, dice cannot become scarred.

You start the game with having maximum mana, and all your normal dice are fully stored with mana.  
'''
        },
    ],
    'Martial': [
        {
            'requires': 'Legendary',
            'name': 'Warcaster',
            'description': '''You can use stamina instead of mana for spellcasting during combat. You cannot use stamina 
            to cast spells outside of combat or for rituals.''',
        },
        {
            'name': 'Enduring',
            'description': '''
You start with 1/2/3/4 additional maximum stamina depending on the level in martial path. And in addition you can
use your stamina once more per round.

When you are at least talented you also recover 1 stamina every round during combat. When you are at
least legendary, then you recover 1 additional stamina every second round during combat. Recovery happens
during the rerolling of your dice pool.
            ''',
        },
        {
            'name': 'Defensive',
            'description': '''
You can choose to have disadvantage for your offensive actions this turn (attacks and offensive spells), in order to
get advantage to recovering defense. When you recover defense this way, your maximum defense is increased by
1 if your acquainted or adebt, or by 2 if you are talented or legendary.
            ''',
        },
        {
            'requires': 'Legendary',
            'name': 'Mastery over body',
            'description': '''
Your body is your weapon. You have made a vow to give up using weapons, armor and magical items, instead you have
focused in making your body a supreme weapon. At levels 1, 4, 8 and 12 you get to choose an additional major option
from your martial playcard (this option does not spend a check-box on the talent card), 
but you cannot use weapons, shields, armors nor attune to any magical item. 

In addition your unarmed strikes do 1 additional damage and you have 2 bonus maximum defense. Both  of those bonuses 
increases by 1 at levels 3, 6, 9 and 12.
            ''',
        },
        {
            'requires': 'Talented',
            'name': 'Bulwark',
            'description': '''
Enemies within 3 sq. of you that attack your allies have disadvantage. If they already would have disadvantage, it
becomes double disadvantage. 

If you are legendary in martial then
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

At the beginning of each round, for each die that was damaged for the first time this combat since your last turn choose 
1 of these options:

* Heal 1 damaged die and recover 3 stamina. This healing does scar a die though.

* Deal 3 additional damage with one of your attacks this turn.

* Roar, all enemies within 4 sq. radius get 1 level of afraid.
            ''',
        },
        {
            'requires': 'Legendary',
            'name': 'Nimble',
            'description': '''After using dice to move, dodge or recover defense, you can reroll those dice back into
            your dice pool. Up to 2 dice can be reused this way per round (this resets when you reroll your entire dice
            pool). This increases to 3 dice at level 5 and 4 dice at level 10.''',
        },
        {
            'requires': 'Talented',
            'name': 'Tough',
            'description': '''If you are talented, then every turn negate the first damage you receive. If you are
            legendary, then negate the first 2 damage you receive.
            
            This ability resets during the round if one of your dice loses all it's HP.
            ''',
        },
        {
            'requires': 'Adept',
            'name': 'Natural killer',
            'description': '''
When you damage an enemy first time this combat with a weapon, gain a blood token that can be used during this encounter.
Against enemy heroes, if they use defense action, then you can get blood token another time. 
If you are talented or legendary, whenever you gain at least one blood token, gain one additional one.

Once per round, whenever you make an attack, you can use one and only one of those options once to boost that attack:

* spend 1 blood tokens to gain advantage or upgrade advantage to double advantage
 
* Spend 2 blood tokens to gain double advantage
 
* spend X blood token to deal X additional damage
 
* spend 1 blood token to disrupt 1
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

        # {
        #     'name': 'Harmonious body',
        #     'description': '''Whenever you advance in REFLEX or FORTITUDE saving throws. Advance in the other one as
        #         well. If you are talented or legendary in martial, also advance in Will proficiency. You cannot advance
        #         in will proficiency from mage path in this case.''',
        # },
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
            'description': '''
You can cast any spell not requiring concentration using 1 luck token, even if you do not 
know that spell. For spell schools which power dice is either 4, 5 or 6 the power dice 
to use this ability becomes 6 and the utility dice becomes 5. For spell schools which power dice is 1, 2 or 
3, the power dice to use this ability becomes 1 and the utility dice becomes 2. This ability uses wild magic
proficiency, which you can advance instead of advancing in any school of magic or skill.
            
Each spell can however only be used once using this ability until your next "Time out and recover".''',
        },
        {
            'name': 'Specialist',
            'description': '''Choose 1 skill. You have an extra +1 for that skills proficiency. Note it does not 
            increase the max of acquiring proficiency with this skill using normal options and therefore allows
            the skill to potentially reach +5 proficiency.
            
            If you are talented or legendary, you can choose two skills instead.
''',
        },
        {
            'name': 'Lucky',
            'description': '''When you spend a luck token, you can choose 2 of the options instead of only 1. 
            If you are talented/legendary in skilled path increase your maximum number of luck tokens by 50 %.  
''',
        },
        {
            'name': 'Good fortune',
            'description': '''You can allow other party members to use your luck tokens. If you are talented/legendary
            in skilled path increase your maximum number of luck tokens by 50 %.
''',
        },
        {
            'name': '(Wo)Man of many talents',
            'description': '''
            Start the game with one additional "creative skill", which has a proficiency of 1.
            
            If you are talented/legendary in skilled path, start with one additional "creative skill" with a proficiency
            of 2.
''',
        },
        {
            'requires': 'Adept',
            'name': 'Prodigy',
            'description': '''
            From level 1 you can pick one major option from your skilled lvl 1-4 playcard and that does 
            not forbid you to take that option again. (meaning you could for example take 2 major skilled feats by level
            2 as Talented or Legendary in Skilled path). Repeat this at levels 5 and 9.
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
        {
            'requires': 'Adept',
            'name': 'Daredevil',
            'description': '''
Whenever you succeed with complications, you recover 1 luck token. If you are talented or legendary, then you recover
2 luck instead.
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
        {'type': 'title', 'content': 'Foundations'},
        {'type': 'paragraph',
         'content': """
Foundations are the second thing after choosing paths that players choose when creating a character. They grant unique
often build defining powers, that significantly define the wibe and nature of your character. Foundation powers are not
available later in the level ups.
You get a foundation for each path you have assigned a point into.
However if you have put more points into the path, then the foundation is that much stronger. In addition, if you
are of some unique race, which would be able to for example have dark vision, or flying or something else, then refer
to the races foundations. When taking one or more race foundations you must give up a foundation in one of the paths.
The power of the racial foundation depends on the level of the path, which foundation you gave up.

Finally I added one background foundation, and may add more in the future. These can also be replaced by one of the path 
foundations similarly to racial foundations.
        """},
    ]

    for path_name, path_feats in feats.items():
        elements.append({'type': 'subtitle', 'content': path_name})

        for feat in path_feats:
            elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements
