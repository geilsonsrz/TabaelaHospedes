import re

#Atenção, 'hospede' é a linha da tabela.
def ajustarNome(nome_junto):

    if len(nome_junto) > 1:

        arq_nomes = open("prog/dados/nomes_iniciais.txt")
        nomestxt = arq_nomes.read()
        nomestxt = re.sub("[;]", "", nomestxt)
        lista_nomes_iniciais = nomestxt.split()
        for nome in lista_nomes_iniciais:
            p = lista_nomes_iniciais.index(nome)
            lista_nomes_iniciais[p] = nome.capitalize()

        nome_listado = str(nome_junto).split()
        for nome in nome_listado:
            q = nome_listado.index(nome)
            nome_listado[q] = nome.capitalize().strip()

        nombre = None
        apellido = None

        for nome in nome_listado:
            if nome in lista_nomes_iniciais:
                k = nome_listado.index(nome)
                nombre = " ".join(nome_listado[k:])
                apellido = " ".join(nome_listado[:k])

        if nombre==None and apellido==None:
            k = len(nome_listado)-1
            nombre = nome_listado[k]
            apellido = " ".join(nome_listado[:k])

        return( [nombre, apellido] )
    
    else: return( ["", ""] )

def capitalizar(nome):

    fragmentos_nome = nome.split()
    for n in fragmentos_nome:
        i = fragmentos_nome.index(n)
        fragmentos_nome[i] = n.capitalize()

    nome = " ".join(fragmentos_nome)
    
    return nome