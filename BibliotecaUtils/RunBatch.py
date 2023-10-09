import subprocess

def run_batch_file(batch_file_path):
    try:
        # Executa o arquivo batch
        subprocess.run([batch_file_path], shell=True, check=True)
        print("Arquivo batch executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o arquivo batch: {e}")

# Exemplo de uso
caminho_do_batch = "C:/AbrindoNotepad.bat"
run_batch_file(caminho_do_batch)
