import openpyxl as op;
import prog.func.func_caracteres as fc;
import prog.func.func_titulos as ft;
import prog.func.func_capturar_dados as fcd;
import prog.func.func_nova_planilha as np;


#Inicializando o arquivo.
def alterarArquivo(nome_arquivo, linha_titulo, linha_inicio_nomes):

    #Controle ao abrir o arquivo.
    try:
    # 1ª FASE - Captura de dados para criar JSON

    #Propriedade "data_only" é para habilitar/desabilitar a leitura de formulas.
    # data_only=True, desabilita, ler os resultados das selução com fórmulas
    # data_only=False, valor padrão, ler as fórmulas e não os resultados.
        arquivo = op.load_workbook(f"{nome_arquivo}.xlsx", data_only=True)
        tabela_ativa = arquivo.active
        TABELA = list(tabela_ativa.rows)    #Tabela completa em objeto.
        TITULOS = TABELA[linha_titulo]      #Linha dos títulos em objeto.

    #Remover acentos e vírgulas do título.
        fc.removerEspecial(TABELA, linha_titulo)

    #Tupla com os títulos e id base que contem no título.
        titulos_nome_id = ft.funcTitulos(TITULOS)

    #Criação do JSON e ajuste dos nomes.
        dict_hospedes = fcd.capturarDados(TABELA, linha_inicio_nomes, titulos_nome_id)

    # 1ª FASE --- CONCLÍDA.
    # 2ª FASE - Transferência de dados do JSON para XLSX modelo.
        np.novaPlanilha(dict_hospedes, nome_arquivo)

    except:
        print(f'''
        [ ERRO ]
Não foi possível abrir o arquivo {nome_arquivo}.
Verifique que o nome e/ou o formado 'xlsx'.
''')
