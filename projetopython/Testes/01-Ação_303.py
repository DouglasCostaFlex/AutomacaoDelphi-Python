import sys
import openpyxl
sys.path.append('c:/Users/flexmobile/Documents/projetopython')
import pandas as pd

from Fontes.Acao303 import criar_pedido,editar_pedido

try:
    
    criar_pedido()
    editar_pedido()

    with open("C:/Users/flexmobile/Documents/projetopython/Relatorios/RelatorioDeTeste.txt","a")  as arquivo:
     relatorio = arquivo.write('01-Acao 303 - Pedido de compra - com sucesso.\n')

        
    # Caminho do arquivo de texto (txt)
    txt_path = "C:/Users/flexmobile/Documents/projetopython/Relatorios/RelatorioDeTeste.txt"

    # Leitura do arquivo de texto para um DataFrame
    df = pd.read_csv(txt_path, delimiter='\t')  # Pode ser necessário ajustar o delimitador

    # Caminho para salvar o arquivo Excel
    excel_path = "C:/Users/flexmobile/Documents/projetopython/Relatorios/RelatorioDeTeste.xlsx"

    # Salva o DataFrame no arquivo Excel
    df.to_excel(excel_path, index=False)

    print(f"Arquivo Excel '{excel_path}' criado com sucesso!")

except Exception as e:

    print('Erro ao criar pedido de compra')









