from command.base import Command

class Info(Command):
    def __init__(self,name: str):
        super().__init__(type=name)
    
    def execute(self,args: dict):
        print("Патом")