import re;

def funcTitulos(TITULOS):

    titulos_nome_id = []
    cap_mes = []

    arq_titulo = open("prog/dados/titulos_tabela_modelo.txt")
    titulostxt = arq_titulo.read()
    lista_titulos = titulostxt.split("\n")

    for titulo in TITULOS:
        if titulo.value in lista_titulos:
            indice = TITULOS.index(titulo)
            coluna = str(titulo.value)
            titulos_nome_id.append((coluna, indice))

        cap_mes.extend(re.findall("^M?m?E?e?S?s? ([a-zA-Z]+)", titulo.value))
        if len(cap_mes)>0:
            mes=cap_mes[0].upper()
            indice = TITULOS.index(titulo)
            titulos_nome_id.append((mes, indice))

    return titulos_nome_id;

