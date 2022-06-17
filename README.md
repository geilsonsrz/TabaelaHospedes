<h2>AUTOMATIZAÇÃO DE PROCESSOS</h2>

<h3>Contextualizando a situação:</h3>
<p>
  O funcionário de um hotel no setor de grupo recebe várias planilhas com os dados dos hospedes, números de habitações, datas de entrada e saída, entro outros dados. Nessa planilha, os dados eram transferidos para outra planilha cumprindo alguns formatos como capitalização dos caracteres, substituição dos caracteres especiais e inserção de todos os dados relevantes, tudo feito de forma manual.
</p>
<h3>Planejamento do projeto:</h3>
<ol>
  <li>
    Substituir todos os caracteres especiais;
  </li>
  <li>
    Capitalização dos caracteres;
  </li>
  <li>
    Ajuste de nomes;
  </li>
  <li>
    Captura dos dados;
  </li>
  <li>
    Criação de uma planilha padronizada.
  </li>
</ol>
<h3>Como o programa funciona:</h3>
<p>
  Ao ser identificado o arquivo no formato “xlsx”, o script captura todos os dados conforme indicado pelos títulos das colunas. Em cada linha, os dados capturados das respectivas colunas são feitos os seguintes ajustes: substituição dos caracteres especiais e capitalização dos textos, exceto o tipo de cama. Os dados de cada linha são incrementados em um arquivo “json”, o arquivo é iniciado assim que o script é executado.
  Ao ter todos os dados devidamente formatados no arquivo “json”, é criado um novo arquivo “xlsx” no formato padronizado que o sistema do hotel recebe.
</p>
<h3>Como utilizar:</h3>
<ol>
  <li>
    Abrir a planilhar que contém os dados e indicar os dados a serem selecionados nomeado/renomeando os títulos das colunas conforme indicado no arquivo “titulos_tabela_modelo.txt” localizado em “./prog/dados”.
    <ul>
      <li>
        Caso o nome e sobrenome estejam juntos na mesma célula, utilizar os títulos que iniciam com “CAMBIO”. Caso contra, utilizar “NOMBRE” na coluna de nome e “APELLIDO” na coluna de sobrenomes.
      </li>
      <li>
        Caso estejam nome e sobrenome juntos, a separação dos nomes compostos é feita através dos nomes utilizados como parâmetros no arquivo “nomes_iniciais.txt” localizado em “./prog/dados”.
      </li>
    </ul>
  <li>
    É necessário a remoção das células mescladas do arquivo.
  </li>
  <li>
    Executar o script “index.py” localizado no diretório principal do projeto.
    <ol>
      <li>
        Inserir o nome do arquivo, sem a extensão “xlsx”, somente o nome.
      </li>
      <li>
        Informar o número da linha que contém os títulos.
      </li>
      <li>
        Informar o número da linha que inicia os dados a serem capturados.
      </li>
    </ol>
</ol>

<h3>Resultado:</h3>
<ol>
  <li>É gerado uma nova planilha padronizada “xlsx” com os dados devidamente formatados.</li>
  <li>É gerado um arquivo “hospedes.json”.</li>
  <p>
    O arquivo “json” é gerado para caso seja útil para os funcionários do setor de sistema do hotel.
  </p>
</ol>
