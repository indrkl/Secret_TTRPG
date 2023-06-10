weapons = {
    'Short bow': {
        'base_damage': '2d6',
        'range': '24 m.',
        'base_difficulty': '0',
        'melee_penalty': -2,
        'difficulty_adjustment_options': [
            {
                'difficulty': '3',
                'effect': 'Deal 1d6 additional damage',
            },
            {
                'difficulty': '5',
                'limit': 1,
                'effect': 'Lower critical threshold by 1',
            },
            {
                'difficulty': '2',
                'limit': 1,
                'effect': 'Double the range of the weapon',
            }
        ]
    },
    'Composite bow': {
        'base_damage': '3d6',
        'base_difficulty': '3',
        'melee_penalty': -2,
        'range': '40 m.',
        'difficulty_adjustment_options': [
            {
                'difficulty': '3',
                'effect': 'Deal 1d6 additional damage',
            },
            {
                'difficulty': '5',
                'limit': 1,
                'effect': 'Lower critical threshold by 1',
            },
            {
                'difficulty': '2',
                'limit': 1,
                'effect': 'Double the range of the weapon',
            }
        ]
    },
    'Long bow': {
        'sneak_penalty': -1,
        'base_damage': '4d6',
        'base_difficulty': '6',
        'range': '100 m.',
        'melee_penalty': -3,
        'difficulty_adjustment_options': [
            {
                'difficulty': '3',
                'effect': 'Deal 1d6 additional damage',
            },
            {
                'difficulty': '5',
                'limit': 1,
                'effect': 'Lower critical threshold by 1',
            },
            {
                'difficulty': '3',
                'limit': 1,
                'effect': 'Double the range of the weapon',
            }
        ]
    },
    'Dagger': {
        'base_damage': '2d6',
        'base_difficulty': '0',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {
                'difficulty': '2',
                'effect': '''On a critical hit target must check for disoriented''',
            },
            {
                'difficulty': '3',
                'limit': 1,
                'effect': '''Reduce critical threshold by 1''',
            },
            {
                'difficulty': '4',
                'effect': '''On a critical hit target takes an additional 10 damage'''
            },
            {
                'difficulty': '3',
                'effect': '''On a critical hit move all the remaining poison stacks from the weapon onto the target.'''
            }
        ]
    },
    '1 handed axe': {
        'base_damage': '2d6',
        'base_difficulty': '0',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {
                'difficulty': '2',
                'effect': '''On a miss, but not on a critical miss, the enemy must make a FORT save against your
                weapon proficiency + 8 or lose "raise shield". If they don't have raise shield they gain 2 levels
                of unbalanced.''',
            },
            {
                'difficulty': '3',
                'effect': 'Deal 1d6 additional damage',
            },
        ]
    },
    'Short sword': {
        'base_damage': '2d6',
        'base_difficulty': '0',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {
                'difficulty': '3',
                'effect': '''Use your reaction to retaliate to a hit that critically missed you with advantage.''',
            },
            {
                'difficulty': '3',
                'effect': 'Deal 1d6 additional damage',
            },
        ]
    },
    'Long sword': {
        'base_damage': '3d6',
        'base_difficulty': '2',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {
                'difficulty': '2',
                'effect': '''Deals an additional 1d6 damage''',
            },
            {
                'difficulty': '3',
                'effect': '''Use your reaction to retaliate to a hit that critically missed you with advantage.''',
            },
        ]
    },
    '2 handed sword': {
        'sneak_penalty': -2,
        'base_damage': '3d6',
        'base_difficulty': '1',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {

                'difficulty': '2',
                'effect': '''After attacking with this attack, as long as you don't critically miss you can move away 
                from the target this turn without provoking attack of opportunity from him.''',
            },
            {
                'difficulty': '3',
                'effect': '''Deals an additional 2d6 damage''',
            },
        ]
    },
    '2 handed axe': {
        'sneak_penalty': -2,
        'base_damage': '3d6',
        'base_difficulty': '1',
        'range': 'melee',
        'difficulty_adjustment_options': [
            {

                'difficulty': '3',
                'effect': '''If you miss your initial target and there are other targets next to both of you, you can
                roll to attack again to try to hit the other enemy.''',
            },
            {
                'difficulty': '3',
                'effect': '''Apply 1 levels of vulnerable to target enemy(ies) if you miss, unless you critically miss.
                ''',
            },
            {
                'difficulty': '2',
                'effect': '''Deals an additional 1d6 damage''',
            },
        ]
    },
    '2 handed spear': {
        'sneak_penalty': -1,
        'base_damage': '2d8',
        'base_difficulty': '1',
        'range': '4 m.',
        'melee_penalty': -1,
        'difficulty_adjustment_options': [
            {
                'difficulty': '1',
                'effect': '''When this attack hits the enemy during an opportunity of attack, it stops their movement 
                for this AP''',
            },
            {
                'difficulty': '2',
                'effect': '''This adjustment allows you to do an attack of opportunity for an enemy that enters your 
                weapon reach.''',
            },
            {

                'difficulty': '1',
                'effect': '''After attacking with this attack, as long as you don't critically miss you can move away 
                from the target this turn without provoking attack of opportunity from him.''',
            },
            {
                'difficulty': '2',
                'effect': '''Deals an additional 1d6 damage''',
            },
        ]
    },
    '2 handed mallet': {
        'sneak_penalty': -2,
        'base_damage': '4d6',
        'base_difficulty': '0',
        'range': 'melee.',
        'difficulty_adjustment_options': [
            {
                'difficulty': '2',
                'effect': '''Armor bonus is capped at +2 and shield bonus is capped at +1''',
            },
            {
                'difficulty': '6',
                'effect': '''Armor bonus is capped at +1 and shield bonus is capped at +1''',
            },
            {
                'difficulty': '2',
                'effect': '''Enemy checks for disoriented''',
            },
            {
                'difficulty': '2',
                'effect': '''Deals an additional 1d6 damage''',
            },
        ]
    },
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style
from reportlab.lib import colors
import re


def prep_weapon_flowable(weapon, name):
    elements = []
    elements.append(Paragraph(name, style=minor_title))
    data = [
        [f"Base damage: {weapon['base_damage']}", f"Range: {weapon.get('range', '-')}",
         f"Melee penalty: {weapon.get('melee_penalty', '-')}"],
        [f"Proficiency penalty: {weapon.get('base_difficulty', 0)}",
         f"Sneak penalty: {weapon.get('sneak_penalty', '0')}", ""]
    ]
    table = Table(data, colWidths=[160] * 3)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
    elements.append(table)
    if weapon.get('difficulty_adjustment_options'):
        elements.append(Paragraph('Difficulty options:', style=minor_subtitle))
        data = []
        for option in weapon.get('difficulty_adjustment_options'):
            description = re.sub('\s+', ' ', option['effect'])
            data.append([f"Difficulty: {option['difficulty']}",
                         f"Limit: {option.get('limit', '-')}",
                         Paragraph(description, basic_paragraph_style)])
        table = Table(data, colWidths=[90, 70, 320])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)

    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements


def get_weapons_chapter():
    elements = [
        {'type': 'title', 'content': 'Weapons'},
    ]

    for name, weapon in weapons.items():
        elements.append({'type': 'flowables', 'content': prep_weapon_flowable(weapon, name)})

    return elements
