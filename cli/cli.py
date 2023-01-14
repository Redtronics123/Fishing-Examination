import cmd
from office import document


class Cli(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "[Exam]> "
        self.intro = "Fischereischeinprüfungsgenerator"

    @staticmethod
    def do_exit(args: str):
        exit()

    @staticmethod
    def do_exam(date: str):
        document.Doc(date=date).create()
