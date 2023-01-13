import cmd


class Cli(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "[Exam]> "
        self.intro = "Fischereischeinprüfungsgenerator"

    @staticmethod
    def do_exit(args: str):
        exit()
