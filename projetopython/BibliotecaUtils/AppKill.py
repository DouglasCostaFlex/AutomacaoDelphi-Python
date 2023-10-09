
import psutil

def kill_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                # Tenta encerrar o processo
                psutil.Process(process.info['pid']).terminate()
                print(f"Processo {process_name} encerrado com sucesso.")
            except psutil.NoSuchProcess as e:
                print(f"Erro: {e}")
            except psutil.AccessDenied as e:
                print(f"Erro: {e}")

# Substitua "automacao.exe" pelo nome real do processo que você deseja encerrar

