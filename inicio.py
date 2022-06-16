#Código Inicial.
#Código responsável pela interção.
#Deve ser garantido que os nomes das colunas estejam padronizados.
import prog.index as index;


print('''
        [ AVISOS ]
1. É necessário que os nomes das colunas estejam padronizados.
2. E que a planinha esteja no mesmo local que esse programa.
3. É necessário que não tenha células mescladas na planilha.
''')
#Garantindo que a linha seja um número inteiro.
try:
    nome_arquivo = str(input("Nome da planilha: "))
    linha_titulo = int(input("Número da linha que contem o cabeçalho: "))-1
    linha_inicio_nomes = int(input("Número da linha que inicia os nomes: "))-1
    index.alterarArquivo(nome_arquivo, linha_titulo, linha_inicio_nomes)

except: print("[ ERRO ] Em no número da linha. Digite valores numéricos válidos.")
