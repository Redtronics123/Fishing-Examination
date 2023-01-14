from docx import Document
from docx.enum.section import WD_ORIENTATION
from office import table


class Doc:
    def __init__(self, date: str):
        self.doc = Document()
        self.date = date
        self.section = self.doc.sections[0]
        self.width = self.section.page_width
        self.height = self.section.page_height

    def create(self):
        self.section.orientation = WD_ORIENTATION.LANDSCAPE
        self.section.page_width = self.height
        self.section.page_height = self.width

        # set date
        date = self.doc.add_paragraph(self.date)
        date.alignment = 2

        # add headline
        self.doc.add_heading("Fischereischeinprüfung", 1)

        # generate tables
        table.Table(
            doc=self.doc
        ).create_table()

        # self.doc.save(f"Prüfung-{self.date}.docx")
