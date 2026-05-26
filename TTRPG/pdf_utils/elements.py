from reportlab.platypus import Flowable, Paragraph, Table, TableStyle
from reportlab.lib import colors


class InteractiveCheckBox(Flowable):
    def __init__(self, text='A Box', offset=0):
        Flowable.__init__(self)
        self.text = text
        self.boxsize = 12
        self.offset = offset

    def draw(self):
        self.canv.saveState()
        form = self.canv.acroForm
        form.checkbox(checked=False,
                      buttonStyle='check',
                      name=self.text,
                      tooltip=self.text,
                      relative=True,
                      x=self.offset,
                      fillColor=colors.beige,
                      size=self.boxsize)
        self.canv.restoreState()
        return


class IniteractiveTextBox(Flowable):
    def __init__(self, text='A Box', offset=0, width=100):
        Flowable.__init__(self)
        self.text = text
        self.boxsize = 12
        self.offset = offset
        self.width = width
        self.light_grey = colors.Color(red=(247.0 / 255), green=(247.0 / 255), blue=(247.0 / 255))  # 247, 247, 247

    def draw(self):
        self.canv.saveState()
        form = self.canv.acroForm
        form.textfield(fontSize=8,
                       name=self.text,
                       tooltip=self.text,
                       relative=True,
                       x=self.offset,
                       width=self.width,
                       height=12,
                       fillColor=self.light_grey,
                       borderWidth=0)
        self.canv.restoreState()
        return
