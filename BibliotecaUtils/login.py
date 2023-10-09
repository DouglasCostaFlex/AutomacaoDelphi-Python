## BLIBIOTECAS QUE O CODIGO USA ## NÃO MODIFICAR POIS PODE DAR PROBLEMA. 
from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
import pyautogui
import time
from psycopg2 import sql
import sys
sys.path.append('c:/Users/flexmobile/Documents/projetopython')

from  BibliotecaUtils.WindowsActive import is_window_active 
## IMPORTAÇÃO DE OUTRAS PASTAS
from Fontes.Dados import usuarioF , usuarioS , password , CaminhoExecutavel , tela_home
from Consultas.ultimo_pedido_303 import obter_nr_pedido
##TIME QUE O CODIGO IRA RODAR .  O.5 SEGUNDOS.


def login_correto():
    
        pyautogui.PAUSE = 0.5

        pyautogui.hotkey('winleft','d') 

        # Inicie o aplicativo
        CaminhoTrunk = (CaminhoExecutavel)
        app = Application().start(CaminhoTrunk)

        #Logando ERP
        time.sleep(7)  # espero abrir o ERP
        pyautogui.write(password)
        pyautogui.press('Enter')
        time.sleep(5)
        pyautogui.press('Enter') # clico no aviso de certificado digital

        print('Logando no ERP...')

        # Aguarde até que a janela principal esteja pronta
        janela_principal = app.window(title=tela_home)
        #Verifica se a tela está visivel e pronta para usar.
        janela_principal.wait('ready')  
        time.sleep(2)

pass