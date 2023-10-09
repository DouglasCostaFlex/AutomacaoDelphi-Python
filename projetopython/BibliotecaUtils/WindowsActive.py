import pygetwindow as gw
import time

def is_window_active(window_title):
    try:
        # Obtém a janela ativa no momento
        active_window = gw.getActiveWindow()

        # Verifica se o título da janela ativa corresponde ao título desejado
        if active_window and active_window.title == window_title:
            return True
    except:
        pass

    return False

# # Exemplo de uso
# window_title = "FlexTotal - 12.11.3.3 - Retaguarda"
# while True:
#     if is_window_active(window_title):
#         print(f"A janela {window_title} está ativa.")
#     else:
#         print(f"A janela {window_title} não está ativa.")

#     time.sleep(1)