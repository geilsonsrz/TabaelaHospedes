AUTOMATIZAÇÃO DE PROCESSOS

Contextualizando a situação:
O funcionário de um hotel no setor de grupo recebe várias planilhas com os dados dos hospedes, números de habitações, datas de entrada e saída, entro outros dados. Nessa planilha, os dados eram transferidos para outra planilha cumprindo alguns formatos como capitalização dos caracteres, substituição dos caracteres especiais e inserção de todos os dados relevantes, tudo feito de forma manual.

Planejamento do projeto:
1 – Substituir todos os caracteres especiais;
2 – Capitalização dos caracteres;
3 – Ajuste de nomes;
4 – Captura dos dados;
5 – Criação de uma planilha padronizada.

Como o programa funciona:
Ao ser identificado o arquivo no formato “xlsx”, o script captura todos os dados conforme indicado pelos títulos das colunas. Em cada linha, os dados capturados das respectivas colunas são feitos os seguintes ajustes: substituição dos caracteres especiais e capitalização dos textos, exceto o tipo de cama. Os dados de cada linha são incrementados em um arquivo “json”, o arquivo é iniciado assim que o script é executado.
Ao ter todos os dados devidamente formatados no arquivo “json”, é criado um novo arquivo “xlsx” no formato padronizado que o sistema do hotel recebe.

Como utilizar:
1 – Abrir a planilhar que contém os dados e indicar os dados a serem selecionados nomeado/renomeando os títulos das colunas conforme indicado no arquivo “titulos_tabela_modelo.txt” localizado em “./prog/dados”.
1.1 – Caso o nome e sobrenome estejam juntos na mesma célula, utilizar os títulos que iniciam com “CAMBIO”. Caso contra, utilizar “NOMBRE” na coluna de nome e “APELLIDO” na coluna de sobrenomes.
1.2 – Caso estejam nome e sobrenome juntos, a separação dos nomes compostos é feita através dos nomes utilizados como parâmetros no arquivo “nomes_iniciais.txt” localizado em “./prog/dados”.
2 – É necessário a remoção das células mescladas do arquivo.
3 – Executar o script “index.py” localizado no diretório principal do projeto.
3.1 – Inserir o nome do arquivo, sem a extensão “xlsx”, somente o nome.
3.2 – Informar o número da linha que contém os títulos.
3.3 – Informar o número da linha que inicia os dados a serem capturados.

Resultado:
1 – É gerado uma nova planilha padronizada “xlsx” com os dados devidamente formatados.
2 – É gerado um arquivo “hospedes.json”.
O arquivo “json” é gerado para caso seja útil para os funcionários do setor de sistema do hotel. 
