from command.base import Command

# Обьект Scipt
class Script:
    def __init__(self,titul: str,cmds: dict):
        self.titul = titul
        self.cmds = cmds