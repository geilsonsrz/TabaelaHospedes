
def funcMes(titulo_nome_id):

    arq_dados = open("prog/dados/meses.txt")
    lista_dados = arq_dados.read().split("\n")

    mes_num = {}
    lista_mes = []
    for dados in lista_dados:
        l_mes_num = dados.split()
        lista_mes.append(l_mes_num[0])
        mes_num[l_mes_num[0]] = l_mes_num[1]

    mes = None

    for item in titulo_nome_id:
        if item[0] in lista_mes:
            mes = mes_num[item[0]]
    
    return mes
