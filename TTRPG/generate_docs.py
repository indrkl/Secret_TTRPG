from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, ListFlowable, ListItem, PageBreak, \
    BaseDocTemplate, PageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from pdf_utils.styles import basic_paragraph_style, basic_list_style, basic_para_title_style, basic_para_sub_title_style, minor_title

first = True


class MyDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        template = PageTemplate('normal', [Frame(2.5 * cm, 2.5 * cm, 15 * cm, 25 * cm, id='F1')])
        self.addPageTemplates(template)

    # Entries to the table of contents can be done either manually by
    # calling the addEntry method on the TableOfContents object or automatically
    # by sending a 'TOCEntry' notification in the afterFlowable method of
    # the DocTemplate you are using. The data to be passed to notify is a list
    # of three or four items countaining a level number, the entry text, the page
    # number and an optional destination key which the entry should point to.
    # This list will usually be created in a document template's method like
    # afterFlowable(), making notification calls using the notify() method
    # with appropriate data.

    def afterFlowable(self, flowable):
        "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            entry = None
            if style == 'Heading1':
                entry = [0, text, self.page,]
            if style == 'Heading2':
                entry = [1, text, self.page,]
            if entry:
                bn = getattr(flowable, '_bookmarkName', None)
                if bn is not None:
                    entry.append(bn)
                self.notify('TOCEntry', tuple(entry))


def prep_elements_from_chapter(chapter):
    from hashlib import sha1

    elements = []
    global first
    for ele in chapter:
        if ele['type'] in ['title', 'subtitle']:
            bn = sha1(str(ele['content'] + ele['type']).encode('utf-8')).hexdigest()
        if ele['type'] == 'paragraph':
            for para in ele['content'].split('\n\n'):
                para = para.replace('\n', ' ')
                elements.append(Paragraph(para, style=basic_paragraph_style))
        elif ele['type'] == 'title':
            elements.append(PageBreak())
            elements.append(Paragraph(ele['content']+'<a name="%s"/>' % bn, style=basic_para_title_style))
        elif ele['type'] == 'subtitle':
            elements.append(Paragraph(ele['content']+'<a name="%s"/>' % bn, style=basic_para_sub_title_style))
            elements[-1].keepWithNext = True
        elif ele['type'] == 'minortitle':
            elements.append(Paragraph(ele['content']+'<a name="%s"/>' % bn, style=minor_title))
            elements[-1].keepWithNext = True
        elif ele['type'] == 'table':
            data = ele['content']
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                       ('GRID', (0, 1), (-1, -1), 1, colors.black)]))
            elements.append(table)
        elif ele['type'] == 'list':
            pdf_list = []
            for list_ele in ele['content']:
                pdf_list.append(ListItem(Paragraph(list_ele, style=basic_list_style)))
            elements.append(ListFlowable(pdf_list, bulletType='1', start='1'))
        elif ele['type'] == 'flowables':
            elements.extend(ele['content'])
        if ele['type'] in ['title', 'subtitle']:
            elements[-1]._bookmarkName=bn
    return elements


def build_pdf_file():
    from rulebook_chapters.character_creation import get_character_creation_chapter
    from rulebook_chapters.skills import get_skill_related_chapter
    from general_actions import get_general_actions_chapter
    from rulebook_chapters.game_concepts import get_game_concepts_chapter
    from rulebook_chapters.intro import get_intro_chapter
    from monster_chapter import get_monsters_chapters
    from Spells import get_spells_chapter
    from Innate_feats import get_innate_feat_chapter
    from progression_feats import get_progression_feat_chapter
    from Normal_feats import get_normal_feats_chapter
    from weapons import get_weapons_chapter
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(fontName='Helvetica-Bold', fontSize=20, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=10,
           leading=16),
        ParagraphStyle(fontName='Helvetica',fontSize=18, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),
    ]
    elements = [toc]
    elements.extend(prep_elements_from_chapter(get_intro_chapter()))
    elements.extend(prep_elements_from_chapter(get_character_creation_chapter()))
    elements.extend(prep_elements_from_chapter(get_game_concepts_chapter()))
    elements.extend(prep_elements_from_chapter(get_skill_related_chapter()))
    elements.extend(prep_elements_from_chapter(get_general_actions_chapter()))
    elements.extend(prep_elements_from_chapter(get_innate_feat_chapter()))
    elements.extend(prep_elements_from_chapter(get_progression_feat_chapter()))
    elements.extend(prep_elements_from_chapter(get_normal_feats_chapter()))
    elements.extend(prep_elements_from_chapter(get_weapons_chapter()))
    elements.extend(prep_elements_from_chapter(get_spells_chapter()))
    elements.extend(prep_elements_from_chapter(get_monsters_chapters()))
    return elements


pdf_file = MyDocTemplate("rulebook.pdf", pagesize=letter)
pdf_file.multiBuild(build_pdf_file())
