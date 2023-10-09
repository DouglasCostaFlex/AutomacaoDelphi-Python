

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
from Fontes.Dados import usuarioF , usuarioS , password , CaminhoExecutavel
from Consultas.ultimo_pedido_303 import obter_nr_pedido
from Fontes.Dados import tela_home

##TIME QUE O CODIGO IRA RODAR .  O.5 SEGUNDOS.
pyautogui.PAUSE = 0.5



   
def criar_pedido():
 
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
        janela_principal.wait('ready')

        # Encontre o controle pela classe 
        controle = janela_principal.window(class_name='TdxRibbonQuickAccessToolbarBarControl')
        # Clique no controle
        controle.click_input() 

        ######Pesquiso por 303
        pyautogui.write('303')
        pyautogui.press('Enter')
        time.sleep(5) #-- Espero abrir a ação 303

        ######Dados do pedido

        print('Definindo dados...')

        pyautogui.write('11089') #-- Defino comprador
        pyautogui.press('Enter')

        pyautogui.press('Enter') #-- Numero do pedido

        pyautogui.write('19068') #-- Defino fornecedor
        pyautogui.press('Enter')

        for _ in range(6): # -- Aperto a tecla "Enter" 6
            pyautogui.press('Enter')

        pyautogui.write('19068') #-- Defino Transportadora.
        pyautogui.press('Enter')

        pyautogui.write('50') #-- Defino frete da Transportadora.
        pyautogui.press('Enter')

        pyautogui.write('07558') #-- Defino produto.

        for _ in range(5): # -- Aperto a tecla "Enter" 5
            pyautogui.press('Enter')

        pyautogui.write('50') #-- Defino QNT
        pyautogui.press('Enter')

        pyautogui.write('150') #-- Defino VALOR
        pyautogui.press('Enter')


        for _ in range(9): # -- Aperto a tecla "Enter" 9
            pyautogui.press('Enter')



        #######CAMPO FORMA DE PAGAMENTO

        pyautogui.write('1') #-- Forma de pgt
        pyautogui.press('Enter')

        pyautogui.write('1') #-- Condição de pagamento
        pyautogui.press('Enter')

        pyautogui.write('teste observação pedido criado') #-- Obeservação
        pyautogui.press('Enter')

        ############ pegar numero do pedido

        print('Quase finalizando...')

        ########## Finalizar
        pyautogui.press('Enter')
        pyautogui.press('Tab')
        pyautogui.press('Enter')

        #Fecho o flextotal
        app.kill()

        ## Avisa o usuario que o pedido foi criado.
        nr_pedido = obter_nr_pedido() # Chame a função para obter o número do pedido
        mensagem = f"Número do Pedido criado: {nr_pedido}"
        print(mensagem)
        pass


    ############ EDITAR PEDIDO ############

def editar_pedido():

        print('#############################')
        print('Iniciando edição de pedido...')
        print('#############################')

        # Vou para area de trabalho
        pyautogui.hotkey('winleft','d') 

        # Inicie o aplicativo
        CaminhoTrunk = (CaminhoExecutavel)
        app = Application().start(CaminhoTrunk)

        #Logando ERP
        time.sleep(4)  # espero abrir o ERP
        pyautogui.write('30352311')
        pyautogui.press('Enter')
        time.sleep(5)
        pyautogui.press('Enter') # clico no aviso de certificado digital

        print('Logando no ERP...')


        # Aguarde até que a janela principal esteja pronta
        janela_principal = app.window(title=tela_home)
        janela_principal.wait('ready')

        # Encontre o controle pela classe 
        controle = janela_principal.window(class_name='TdxRibbonQuickAccessToolbarBarControl')
        # Clique no controle
        controle.click_input()

        ######Pesquiso por 303

        pyautogui.write('303')
        pyautogui.press('Enter')
        time.sleep(5) #-- Espero abrir a ação 303


        ######Dados do pedido

        print('Editando dados...')

        pyautogui.press('Enter') # Vou até numero de pedido

        nr_pedido = obter_nr_pedido() ## pego o ultimo pedido feito 

        pyautogui.write(nr_pedido) # defino o numero de pedido anterior
        pyautogui.press('Enter')  #vou até fornecedor

        pyautogui.write('11933') # defino o novo fornecedor
        pyautogui.press('Enter') # Vou até produto


        pyautogui.write('16057') #-- Defino produto.

        for _ in range(5): # -- Aperto a tecla "Enter" 5
            pyautogui.press('Enter')

        pyautogui.write('30') #-- Defino QNT
        pyautogui.press('Enter')

        pyautogui.write('200') #-- Defino VALOR
        pyautogui.press('Enter')


        for _ in range(9): # -- Aperto a tecla "Enter" 9
            pyautogui.press('Enter')



        #######CAMPO FORMA DE PAGAMENTO

        pyautogui.write('106') #-- Forma de pgt
        pyautogui.press('Enter')
        pyautogui.press('Enter')

        pyautogui.write('teste observação pedido criado EDITADO') #-- Obeservação
        pyautogui.press('Enter')

        ############ pegar numero do pedido

        print('Quase finalizando a edição...')

        ########## Finalizar
        pyautogui.press('Enter')
        time.sleep(2)
        pyautogui.press('Tab')
        time.sleep(2)
        pyautogui.press('Enter')

        #### Mensagem de finalização
        print('Pedido Editado com sucesso!!!')

        #Fecho o flextotal
        app.kill()
        pass


criar_pedido()











