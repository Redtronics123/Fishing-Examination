import docx
from algorithmen import nums
from database import connect


class Table:
    def __init__(self, doc: docx.Document):
        self.doc = doc

    def create_table(self):
        connection = connect.Database().connect()
        cursor = connection.cursor()

        table = self.doc.add_table(rows=1, cols=4)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Frage'
        hdr_cells[1].text = 'Antwort 1'
        hdr_cells[2].text = 'Antwort 2'
        hdr_cells[3].text = 'Antwort 3'

        counter = 1
        while counter < 6:
            numbers = nums.Nums().generate()

            while len(numbers) > 0:
                # data = cursor.execute(f"SELECT Question, AnswerA, AnswerB, AnswerC FROM Brandenburg WHERE NR={numbers[-1]} AND SG={counter}")
                cursor.execute(
                    f"SELECT Question, AnswerA, AnswerB, AnswerC FROM Brandenburg WHERE NR=1 AND SG=1")

                data = cursor.fetchone()
                numbers.pop()

                row_cells = table.add_row().cells
                row_cells[0].text = str(data[0])
                row_cells[1].text = str(data[1])
                row_cells[2].text = str(data[2])
                row_cells[3].text = str(data[3])

            counter += 1
