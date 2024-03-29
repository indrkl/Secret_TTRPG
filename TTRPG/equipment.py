weapon_classes = ['dagger', 'bow', 'sword', 'axe', 'mace', '2H sword', '2H axe', '2H mace', 'spear', 'shield', 'unarmed']

equipment = {
    'dagger': {
        'action': {
            'cost': 'R2.R2',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R1',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Double damage',
                },
                {
                    'cost': 'R2',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R1',
                    'effect': 'Confuse 2',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Disrupt 2',
                },
            ]
        }
    },
    'unarmed': {
        'action': {
            'cost': 'R2',
            'damage': 1,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R2',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Disorient 1',
                },
                {
                    'cost': 'R6.R6',
                    'effect': 'Disrupt 2',
                },
            ]
        }
    },
    'shortbow': {
        'action': {
            'cost': 'R6.R6',
            'damage': 3,
            'range': '8 squares',
            'difficulty_options': [
                {
                    'cost': 'R6',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R6',
                    'effect': '+ 2 damage',
                },
                {
                    'cost': 'R6.R6',
                    'effect': '+ 5 damage',
                },
                {
                    'cost': 'R1',
                    'effect': 'Confuse 1',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Disrupt 1',
                },
            ]
        }
    },
    'spear': {
        'action': {
            'cost': 'R3.R3',
            'damage': 3,
            'range': '2 squares',
            'difficulty_options': [
                {
                    'cost': 'R3',
                    'effect': '+ 2 damage',
                },
                {
                    'cost': 'R6',
                    'effect': 'Disrupt 1',
                },
            ]
        }
    },
    'axe': {
        'action': {
            'cost': 'R3.R3',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R5',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R3',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R3.R3',
                    'effect': '+ 3 damage',
                },
            ]
        }
    },
    'sword': {
        'action': {
            'cost': 'R4.R4',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R3',
                    'effect': 'Recover 1 defense',
                },
                {
                    'cost': 'R4',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R4.R4',
                    'effect': '+ 3 damage',
                },
                {
                    'cost': 'R3.R3',
                    'effect': 'Confuse 3',
                },
            ]
        }
    },
    'sabre': {
        'action': {
            'cost': 'R4.R4',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R4',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R4.R4',
                    'effect': '+ 3 damage',
                },
                {
                    'cost': 'R2',
                    'effect': 'Confuse 1',
                },
                {
                    'cost': 'R2',
                    'effect': 'Reposition within 1 sq.',
                },
            ]
        }
    },
    '2 handed sword': {
        'action': {
            'cost': 'R5.R5',
            'damage': 3,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R2',
                    'effect': 'Recover 2 defense',
                },
                {
                    'cost': 'R5',
                    'effect': '+ 2 damage',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Confuse 4',
                },
                {
                    'cost': 'R2',
                    'effect': 'Reposition within 2 sq.',
                },
            ]
        }
    },
    '1 handed mace': {
        'action': {
            'cost': 'R3.R3',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R4',
                    'effect': 'Bypass enemy damage reduction',
                },
                {
                    'cost': 'R3',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R4.R4',
                    'effect': 'Confuse 3',
                },
                {
                    'cost': 'R4',
                    'effect': 'Confuse 1',
                },
            ]
        }
    },
    '2 handed mace': {
        'action': {
            'cost': 'R5.R5',
            'damage': 3,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R5',
                    'effect': 'Bypass enemy damage reduction',
                },
                {
                    'cost': 'R5',
                    'effect': 'Reduce defenses by 3 before doing damage',
                },
                {
                    'cost': 'R5',
                    'effect': '+ 2 damage',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Disrupt 2',
                },
                {
                    'cost': 'R1',
                    'effect': 'Confuse 2',
                },
            ]
        }
    },
    'two handed axe': {
        'action': {
            'cost': 'R5.R5',
            'damage': 3,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R5',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R5',
                    'effect': '+ 2 damage',
                },
                {
                    'cost': 'R2.R2.R2',
                    'effect': 'Apply 1 afraid',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Apply 1 vulnerable',
                },
            ]
        }
    },
    'Burning two handed axe of the devils': {
        'action': {
            'cost': 'R6.R6',
            'damage': 4,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R6',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R6',
                    'effect': 'Deal 1 fire damage and apply a stack of burning onto the enemy',
                },
                {
                    'cost': 'R1.R1',
                    'effect': 'Apply 1 afraid for every 3 stacks of burning on the enemy',
                },
                {
                    'cost': 'R1.R1.R1',
                    'effect': 'Apply 1 vulnerable for every stack of burning on the enemy',
                },
            ]
        }
    },
    'shield': {
        'effect':
            '''
When using the shield action, get guarded buff until the beginning of your next turn which increases your maximum 
defense by 2 and damage reduction by 1. Also recover 2 defense.
''',
        'action': {
            'cost': 'R2.R2',
            'damage': '-',
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R2.R2',
                    'effect': 'Gain an additional damage reduction',
                },
            ]
        }
    },
    'staff': {
        'effect':
            '''
Instead you have 2 additional normal spell slots and 1 signature spell slot. The spell used in the signature spell slot
has advantage. Signature spell cannot be switched out mid combat.'''
    },
    'staff of freezing': {
        'effect':
            '''
Instead you have 2 additional normal spell slots. In addition you have freezing spell as your signature spell, meaning
casting it has advantage.

Enables you to cast the freezing skill without elemental proficiency and knowing that spell. You may replace elemental
proficiency for casting it using this staff with your highest proficiency in any school minus one.'''
    },
    'simple leather armor': {
        'effect': '''
Light armor: Provides 2 maximum defense
        '''
    },
    'Heavy chain mail': {
        'effect': '''
This is a heavy armor that provides 4 maximum defense and 1 damage reduction     
        '''
    },
    'padded leather armor': {
        'effect': '''
This is medium armor that provides 4 maximum defense
        '''
    },
    'claw': {
        'effect':
            '''
This is not a weapon, but can be used when taking the unnatural limbs racial innate feat. Also used by beasts
''',
        'action': {
            'cost': 'R2.R2',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R1',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R2',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R1',
                    'effect': 'Apply 1 vulnerable',
                },
            ]
        }
    },
    'secondary claw': {
        'effect':
            '''
This is not a weapon, but can be used when taking the unnatural limbs racial innate feat. Also used by beasts
''',
        'action': {
            'cost': 'R4.R4',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R6',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R4',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R6',
                    'effect': 'Apply 1 vulnerable',
                },
            ]
        }
    },
    'bite': {
        'effect':
            '''
This is not a weapon, but can be used by beasts
''',
        'action': {
            'cost': 'R5.R5',
            'damage': 2,
            'range': 'melee',
            'difficulty_options': [
                {
                    'cost': 'R5',
                    'effect': '+ 1 damage',
                },
                {
                    'cost': 'R3.R3',
                    'effect': 'Apply 1 disoriented',
                },
                {
                    'cost': 'R3.R3',
                    'effect': '''Also get a level of upper hand as if you had done the wrestle action without spending
                    stamina.''',
                },
            ]
        }
    },
}

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style, add_dice_images
from reportlab.lib import colors
import re


def prep_equipment_flowable(weapon, name):
    elements = []
    elements.append(Paragraph(name, style=minor_title))
    if weapon.get('effect'):
        elements.append(Paragraph(weapon.get('effect'), style=basic_paragraph_style))

    if weapon.get('action'):
        action = weapon.get('action', {'cost': '-', 'damage': '-'})
        if 'base_effect' in action:
            effect = f"Base effect: {action['base_effect']}"
        else:
            effect = f"Base damage: {action['damage']}"
        data = [
            [Paragraph(f"Base cost: {add_dice_images(action['cost'])}", style=basic_paragraph_style), effect, f"Range: {action.get('range', '-')}", ""],
        ]
        if action.get('difficulty_options'):
            odd = True
            for option in action.get('difficulty_options', []):
                description = re.sub('\s+', ' ', option['effect'])
                option = [Paragraph(f"+ {add_dice_images(option['cost'])}", style=basic_paragraph_style),
                             Paragraph(description, basic_paragraph_style)]
                if odd:
                    data.append(option)
                    odd = False
                else:
                    data[-1].extend(option)
                    odd = True
            if not odd:
                data[-1].extend(["", ""])

        table = Table(data, colWidths=[100, 140, 100, 140])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)



    for i in range(0, len(elements)-1):
        elements[i].keepWithNext = True

    return elements


def get_equipment_chapter():
    elements = [
        {'type': 'title', 'content': 'Equipment'},
    ]

    for name, weapon in equipment.items():
        elements.append({'type': 'flowables', 'content': prep_equipment_flowable(weapon, name)})

    return elements
