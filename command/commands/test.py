import sys
from command.base import Command

# Новая комманда Test. Для создания мы наследуем обьект Command по пути command.base
class Test(Command):
    def __init__(self,name: str):
        super().__init__(type=name)
    
    def execute(self,args: dict):
        sys.stdout.write(str(args)+"\n")