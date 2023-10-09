# funcoes_banco.py
import psycopg2


def obter_nr_pedido():
    # Parâmetros de conexão ao banco de dados
    conexao_parametros = {
        'dbname': 'rezzadori_automacao_trunk',
        'user': 'flextotal',
        'password': 'Fl3xt0t@L',
        'host': '192.168.1.3',
        'port': '5432'
    }

    # Construa a consulta SQL
    consulta_sql = """
        select nr_pedido from pedido_compra WHERE PEDIDO_COMPRA.CD_FILIAL = 1
        ORDER BY dt_atz desc limit 1;
    """

    try:
        # Conectar ao banco de dados
        conexao = psycopg2.connect(**conexao_parametros)

        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Executar a consulta
        cursor.execute(consulta_sql)

        # Obter os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        for resultado in resultados:
            nr_pedido = resultado[0]
            return  (str(nr_pedido))

    except psycopg2.Error as e:
        print("Erro ao conectar ou executar a consulta:", e)
        return None

    finally:
        # Certificar-se de fechar a conexão
        if conexao:
            conexao.close()