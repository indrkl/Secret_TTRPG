weapon_classes = ['dagger', 'bow', 'sword', 'axe', 'mace', '2H sword', '2H axe', '2H mace', 'spear', 'shield']

equipment = {
    'dagger': {
        'action': {
            'cost': 'R2.R2',
            'damage': 2,
            'range': 'melee',
            'extra_options': [
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
                    'effect': 'Additional 1 damage',
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
    'shortbow': {
        'action': {
            'cost': 'R6.R6',
            'damage': 3,
            'range': '8 squares',
            'extra_options': [
                {
                    'cost': 'R6',
                    'effect': 'bypass damage reduction',
                },
                {
                    'cost': 'R6',
                    'effect': 'Additional 2 damage',
                },
                {
                    'cost': 'R6.R6',
                    'effect': 'Additional 5 damage',
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
            'extra_options': [
                {
                    'cost': 'R3',
                    'effect': 'Additional 2 damage',
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
            'extra_options': [
                {
                    'cost': 'R5',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R3',
                    'effect': 'Additional 1 damage',
                },
                {
                    'cost': 'R3.R3',
                    'effect': 'Additional 3 damage',
                },
            ]
        }
    },
    'sword': {
        'action': {
            'cost': 'R5.R5',
            'damage': 2,
            'range': 'melee',
            'extra_options': [
                {
                    'cost': 'R3',
                    'effect': 'Recover 1 defense',
                },
                {
                    'cost': 'R5',
                    'effect': 'Additional 1 damage',
                },
                {
                    'cost': 'R5.R5',
                    'effect': 'Additional 3 damage',
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
            'extra_options': [
                {
                    'cost': 'R4',
                    'effect': 'Additional 1 damage',
                },
                {
                    'cost': 'R4.R4',
                    'effect': 'Additional 3 damage',
                },
                {
                    'cost': 'R2',
                    'effect': 'Confuse 1',
                },
                {
                    'cost': 'R2',
                    'effect': 'Reposition yourself within 1 squares freely',
                },
            ]
        }
    },
    '2 handed sword': {
        'action': {
            'cost': 'R5.R5',
            'damage': 3,
            'range': 'melee',
            'extra_options': [
                {
                    'cost': 'R2',
                    'effect': 'Recover 2 defense',
                },
                {
                    'cost': 'R5',
                    'effect': 'Additional 2 damage',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Confuse 4',
                },
                {
                    'cost': 'R2',
                    'effect': 'Reposition yourself within 2 squares freely',
                },
            ]
        }
    },
    '1 handed mace': {
        'action': {
            'cost': 'R3.R3',
            'damage': 2,
            'range': 'melee',
            'extra_options': [
                {
                    'cost': 'R4',
                    'effect': 'Bypass enemy damage reduction',
                },
                {
                    'cost': 'R3',
                    'effect': 'Additional 1 damage',
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
            'extra_options': [
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
                    'effect': 'Additional 2 damage',
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
    '2 handed axe': {
        'action': {
            'cost': 'R5.R5',
            'damage': 3,
            'range': 'melee',
            'extra_options': [
                {
                    'cost': 'R5',
                    'effect': 'Remove guarded status effect',
                },
                {
                    'cost': 'R5',
                    'effect': 'Additional 2 damage',
                },
                {
                    'cost': 'R2.R2.R2',
                    'effect': 'Apply 1 level of afraid onto enemy',
                },
                {
                    'cost': 'R2.R2',
                    'effect': 'Apply 1 level of vulnerable onto enemy',
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
            'extra_options': [
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
Instead you have 2 additional normal spell options and 1 signature spell option. The signature spell has advantage'''
    },
    'simple leather armor': {
        'effect': '''
Provides 2 maximum defense
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
    }
}
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak
from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style
from reportlab.lib import colors
import re


def prep_equipment_flowable(weapon, name):
    elements = []
    elements.append(Paragraph(name, style=minor_title))
    if weapon.get('effect'):
        elements.append(Paragraph(weapon.get('effect'), style=basic_paragraph_style))

    if weapon.get('action'):
        action = weapon.get('action', {'cost': '-', 'damage': '-'})
        data = [
            [f"Roll: {action['cost']}", f"Base damage: {action['damage']}", f"Range: {action.get('range', '-')}"],
        ]
        table = Table(data, colWidths=[160] * 3)
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.gray)]))
        elements.append(table)

        if action.get('extra_options'):
            elements.append(Paragraph('Extra options:', style=minor_subtitle))
            data = []
            for option in action.get('extra_options', []):
                description = re.sub('\s+', ' ', option['effect'])
                data.append([f"Roll: {option['cost']}",
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


def get_equipment_chapter():
    elements = [
        {'type': 'title', 'content': 'Equipment'},
    ]

    for name, weapon in equipment.items():
        elements.append({'type': 'flowables', 'content': prep_equipment_flowable(weapon, name)})

    return elements
