import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("E:\Jetbrains Projekts\PyCharm\examinationFishing\\ressourcen\databases\\brandenburg.db")

    def connect(self):
        return self.connection

