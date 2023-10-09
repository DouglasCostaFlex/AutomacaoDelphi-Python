import psutil

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

# # Exemplo de uso
# process_name = "automacao.exe"
# if is_process_running(process_name):
#     print(f"O processo {process_name} está em execução.")
# else:
#     print(f"O processo {process_name} não está em execução.")