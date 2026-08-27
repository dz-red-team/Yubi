from script.base import Script
from command.manager import Manager as CommandManager

# Менеджер для скриптов
class Manager:
    script_storage = []
    def __init__(self,commandManager: CommandManager):
        self.commandManager = commandManager

    def add(self,script: Script):
        self.script_storage.append(script)

    def execute(self,titul: str):
        for i in self.script_storage:
            if i.titul == titul:
                for cmd in i.cmds:
                    self.commandManager.execute(cmd)
                    break