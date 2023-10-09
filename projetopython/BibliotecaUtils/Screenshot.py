import pyautogui
import os


# Para usar é facil, apenas chame a função e primeiro adicione o "nome do arquivo." e "o lugar onde vc vai guardar as fotos"
def save_screenshot(image_name, folder_path):
  
        # Tira a captura de tela
        screenshot = pyautogui.screenshot()

        # Cria o caminho completo do arquivo
        image_path = os.path.join(folder_path, image_name)

        # Salva a captura de tela no local especificado
        screenshot.save(image_path)

        print(f"Captura de tela salva em: {image_path}")
   
   