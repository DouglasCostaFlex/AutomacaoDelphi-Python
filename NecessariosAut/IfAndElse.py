
## BLIBIOTECAS QUE O CODIGO USA ## NÃO MODIFICAR POIS PODE DAR PROBLEMA. 
from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
import pyautogui
import time
from psycopg2 import sql
import sys
sys.path.append('c:/Users/flexmobile/Documents/projetopython')

## IMPORTAÇÃO DE OUTRAS PASTAS
from Fontes.Dados import usuarioF , usuarioS , password , CaminhoExecutavel , tela_home,ErrosPath
from Consultas.ultimo_pedido_303 import obter_nr_pedido
from BibliotecaUtils.login import login_correto
from  BibliotecaUtils.WindowsActive import is_window_active 
from BibliotecaUtils.AppKill import kill_process_by_name
from BibliotecaUtils.Screenshot import save_screenshot




#Faço LOGIN

login_correto()

## adiciono janela principal a funcao que verifique se está ativo.  caso esteja visivel na tela, ira printar na tela.
if is_window_active(tela_home):  ## SE A TELA ESTIVER ATIVA, IRÁ SEGUIR A AUTOMAÇÃO

    print('Está na janela principal')
    print('Vou clicar pois está na janela certa.')
    pyautogui.click(355, 16)
  

else: ## TENTO FAZER LOGIN NOVAMENTE, CASO NAO DE ELE IRA PARAR.
    
    print('Janela errada.')
    print('Não cliquei pois está na tela errada')
    save_screenshot('Menu_Tela_Nao_Verificada.png',ErrosPath)
    kill_process_by_name('automacao.exe')
    print('Tentando realizar login novamente')
    ## FAÇO LOGIN NOVAMENTE
    login_correto()
 
    if is_window_active(tela_home):
            print('Está na janela principal')
            print('Vou clicar pois está na janela certa.')
            pyautogui.click(355, 16)
        
    else:
            print('Janela errada.')
            print('Não cliquei pois está na tela errada')
            kill_process_by_name('automacao.exe')
     
      


    
