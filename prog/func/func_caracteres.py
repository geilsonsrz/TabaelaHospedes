###   É necessário importar a regex.
import re

###   Função para cada palavra
def converterLetra(objpalavra):
    #palavra vem como um objeto, devemos acessar o valor com a propriedade 'value'
    palavra = str(objpalavra.value)

    #Remover vírgulas;
    rem_virgula = ''
    palavra = re.sub("([,])", rem_virgula, palavra)
    palavra = re.sub("([\u00b4`'])", " ", palavra)

    for letra in palavra:

        if letra in "áàâãäå":
            letra = "a"
            palavra = re.sub("([áàâãäå])", letra, palavra)

        elif letra in "ÁÀÂÃÄÅ":
            letra = "A"
            palavra = re.sub("([ÁÀÂÃÄÅ])", letra, palavra)

        elif letra in "éèêë":
            letra = "e"
            palavra = re.sub("([éèêë])", letra, palavra)

        elif letra in "ÉÈÊË":
            letra = "E"
            palavra = re.sub("([ÉÈÊË])", letra, palavra)

        elif letra in "íïìî":
            letra = "i"
            palavra = re.sub("([íïìî])", letra, palavra)

        elif letra in "ÍÏÌÎ":
            letra = "I"
            palavra = re.sub("([ÍÏÌÎ])", letra, palavra)

        elif letra in "óôõöò":
            letra = "o"
            palavra = re.sub("([óôõöò])", letra, palavra)

        elif letra in "ÓÔÕÖÒ":
            letra = "O"
            palavra = re.sub("([ÓÔÕÖÒ])", letra, palavra)

        elif letra in "úùüû":
            letra = "u"
            palavra = re.sub("([úùüû])", letra, palavra)

        elif letra in "ÜÚÙÛ":
            letra = "U"
            palavra = re.sub("([ÜÚÙÛ])", letra, palavra)

        elif letra == "ç":
            letra = "c"
            palavra = re.sub("([ç])", letra, palavra)

        elif letra == "Ç":
            letra = "C"
            palavra = re.sub("([Ç])", letra, palavra)

        elif letra == "ñ":
            letra = "n"
            palavra = re.sub("([ñ])", letra, palavra)

        elif letra == "Ñ":
            letra = "N"
            palavra = re.sub("([Ñ])", letra, palavra)

        elif letra == "ý":
            letra = "y"
            palavra = re.sub("([ý])", letra, palavra)

        elif letra == "Ý":
            letra = "Y"
            palavra = re.sub("([Ý])", letra, palavra)

        elif letra == "æ":
            letra = "ae"
            palavra = re.sub("([æ])", letra, palavra)

        elif letra == "Æ":
            letra = "AE"
            palavra = re.sub("([Æ])", letra, palavra)

        elif letra == "ß":
            letra = "SS"
            palavra = re.sub("([ß])", letra, palavra)

    return palavra


def removerEspecial(tabela, inicio_dos_dados_indice):

    #i - índice inicial
    i = inicio_dos_dados_indice
    # r = range
    r = range(i, len(tabela))

    for i in r:
        for celula in tabela[i]:
            valor = str(celula.value)
            if celula.value == None: celula.value = ""
            elif valor[0] == "=": continue
            else: celula.value = converterLetra(celula)

