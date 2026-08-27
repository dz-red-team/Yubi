from command.manager import Manager as CommandManager
from script.manager import Manager as ScriptManager

from libs import color

"""
    Инициализация менеджеров
"""
commandManager: CommandManager = CommandManager()
scriptManager: ScriptManager = ScriptManager(commandManager)



"""
    Ниже представлено добавление скрипта ,тоесть набор комманд
    Тут ему не место ,но для теста он тут
"""
from script.base import Script
scriptManager.add(Script("basescript",["test"]))
scriptManager.execute("basescript")

while True:
    user_input = input(f"{color.RED}>{color.RESET}")
    commandManager.execute(user_input)  