import sys

from command.manager import Manager as CommandManager
from script.manager import Manager as ScriptManager

from libs import color

def root() -> bool:
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
    scriptManager.add(Script("basescript",["fetch","test"]))
    scriptManager.execute("basescript")

    while True:
        try:
            user_input = input(f"{color.RED}>{color.RESET} ")
            if user_input.strip():
                    commandManager.execute(user_input)
                    
        except KeyboardInterrupt:
            sys.stdout.write(f"{color.LIGHT_BLACK}^C{color.RESET}\n")
            sys.stdout.flush()
            continue 
        
if __name__ == "__main__":
    root()