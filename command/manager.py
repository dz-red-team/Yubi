import command.commands as commands_package

# Менеджер для комманд
class Manager:
    def __init__(self):
        self.commands_storage = []
        self.commands_storage.append(commands_package.test.Test("test"))
        self.commands_storage.append(commands_package.fetch.Fetch("fetch"))

    def execute(self,line: str):
        parts = line.split()
        for i in self.commands_storage:
            if i.type == parts[0]:
                i.execute(parts)
                break
