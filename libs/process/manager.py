import subprocess

# Получить все процессы
def get_processes() -> dict:
    proc_list = []
    try:
        output = subprocess.check_output("tasklist", shell=True).decode('cp866')
        lines = output.splitlines()[3:]
        for line in lines:
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 2:
                name = parts[0]  
                pid = parts[1]  
                proc_list.append({"pid": pid, "name": name})
    except Exception as e:
        print(f"Ошибка чтения процессов: {e}")
    return proc_list

# Убить процесс по PID
def kill_process(pid_or_name: str) -> bool:
    try:
        if pid_or_name.isdigit():
            cmd = f"taskkill /F /PID {pid_or_name}"
        else:
            cmd = f"taskkill /F /IM {pid_or_name}"
        subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return True
    except:
        return False

# Запуск процесса
def run_process(path: str) -> bool:
    try:
        subprocess.run(path,shell=True)
        return True
    except:
        return False
