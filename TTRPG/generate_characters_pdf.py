from generate_docs import MyDocTemplate, prep_elements_from_chapter

from reportlab.lib.pagesizes import letter

def build_pdf_file():
    from Characters import get_player_character_chapters



    for elements, name in get_player_character_chapters():
        pdf_content = prep_elements_from_chapter(elements)

        pdf_file = MyDocTemplate("%s.pdf"%(name), pagesize=letter)
        pdf_file.multiBuild(pdf_content)



build_pdf_file()