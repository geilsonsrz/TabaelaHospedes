import re;
import openpyxl as op;

#Recebe um dicionátio.
def novaPlanilha(dict_hospedes, nome_arquivo="Nova Planilha"):

    #Inicialização da tabela modelo.
    MODELO = op.load_workbook("prog\dados\Planilha_Modelo.xlsx")
    tabela_ativa = MODELO.active
    TABELA = list(tabela_ativa.rows)
    TITULOS = TABELA[1] #Linha 2 - Localização dos títulos no arquivo modelo.
    #Índice da linha onde deve receber o primeiro nome na planilha modelo.
    i = 2   #Linha 3
    
    #Listagem que vai conter todos os hóspedes com o título no formato modelo.
    lista_hospedes = list()
    for dado in dict_hospedes:
        hospede = {}
        for (key, valor) in dado.items():
            key = re.sub("([_])", " ", key).upper()
            hospede[key] = valor
        
        lista_hospedes.append(hospede)
    
    #Agregando hóspede na linha.
    for hospede in lista_hospedes:

        for titulo in TITULOS:
            if titulo.value in hospede:
                nome_titulo = titulo.value
                id_titulo = TITULOS.index(titulo)

                TABELA[i][id_titulo].value = hospede[nome_titulo]
        
        #Incremento do índice da linha hóspede.
        i+=1
    
    #Gerando nova planiha.
    MODELO.save(f"./EDITADA_{nome_arquivo}.xlsx")
