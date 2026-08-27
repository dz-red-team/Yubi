
# Обьект Command
class Command:
    def __init__(self,type: str):
        self.type = type
    
    def execute(self,args: dict):
        print(args)