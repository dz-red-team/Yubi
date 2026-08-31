import sys
from command.base import Command

from libs import process as process

class Run(Command):
    def __init__(self,name: str):
        super().__init__(type=name)
    
    def execute(self,args: dict) -> str:
        if len(args) < 2:
            return "Argument not found! Example run yubi.txt\n"
        return str(process.run_process(args[1])) + "\n"