from generate_docs import MyDocTemplate, prep_elements_from_chapter

from reportlab.lib.pagesizes import letter

def build_pdf_file():
    from Characters import get_player_character_chapter
    elements = []

    elements.extend(prep_elements_from_chapter(get_player_character_chapter()))

    return elements


pdf_file = MyDocTemplate("characters.pdf", pagesize=letter)
pdf_file.multiBuild(build_pdf_file())