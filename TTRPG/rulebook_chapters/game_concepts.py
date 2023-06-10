from math import floor, ceil

from glossary import glossary as glossary_obj
from status_effects import status_effects as status_effects_obj
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak

from pdf_utils.styles import basic_paragraph_style, basic_list_style, minor_title, minor_subtitle, option_style


def prep_flowable(element):
    elements = []
    elements.append({'type': 'minortitle', 'content': element['name']})
    elements.append({'type': 'paragraph', 'content': element['description']})

    return elements

def get_game_concepts_chapter():

    elements = [
        {'type': 'title', 'content': 'All game concepts'},

    ]


    for element in glossary_obj:
        elements.extend(prep_flowable(element))
    elements.append(
        {'type': 'title', 'content': 'Status effects'},
    )

    for element in status_effects_obj:
        elements.extend(prep_flowable(element))

    return elements