import sys
from command.base import Command

import libs.system as system 

class Fetch(Command):
    def __init__(self,name: str):
        super().__init__(type=name)
    
    def execute(self,args: dict):
        profile: system.profile.Profile = system.manager.getProfile()
        sys.stdout.write(f"User: {profile.user}\n")
        sys.stdout.write(f"Uptime: {system.manager.getUptime()}\n")