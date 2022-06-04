import json;
import re;
import prog.func.func_ajustar_nome as fan;
import prog.func.func_ajustar_cama as fac;
import prog.func.func_ajustar_data as fad;
import prog.func.func_mes as fm;


def capturarDados(TABELA, linha_inicio_nomes, titulos_nome_id):

    num_mes = fm.funcMes(titulos_nome_id)

    lista_hospedes = list()

    range_tabela = range(linha_inicio_nomes, len(TABELA))

    i = linha_inicio_nomes
    for i in range_tabela:

        dados_hospede = TABELA[i]
        hospede = {}

        for item in titulos_nome_id:

            titulo = item[0].lower()
            titulo = re.sub("([\s])", "_", titulo)
            id_titulo = item[1]

            if len(dados_hospede[id_titulo].value) <1: pass

            elif titulo == "cambio_titular":
                nome_completo = fan.ajustarNome(dados_hospede[id_titulo].value)
                hospede["apellido_titular"] = nome_completo[1]
                hospede["nombre_titular"] = nome_completo[0]

            elif titulo == "cambio_acompanante_1":
                nome_completo = fan.ajustarNome(dados_hospede[id_titulo].value)
                hospede["apellido_acompanante_1"] = nome_completo[1]
                hospede["nombre_acompanante_1"] = nome_completo[0]
                
            elif titulo == "cambio_acompanante_2":
                nome_completo = fan.ajustarNome(dados_hospede[id_titulo].value)
                hospede["apellido_acompanante_2"] = nome_completo[1]
                hospede["nombre_acompanante_2"] = nome_completo[0]

            elif titulo == "cambio_acompanante_3":
                nome_completo = fan.ajustarNome(dados_hospede[id_titulo].value)
                hospede["apellido_acompanante_3"] = nome_completo[1]
                hospede["nombre_acompanante_3"] = nome_completo[0]

            elif titulo == "apellido_titular":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "nombre_titular":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "apellido_acompanante_1":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "nombre_acompanante_1":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "apellido_acompanante_2":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "nombre_acompanante_2":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "apellido_acompanante_3":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "nombre_acompanante_3":
                hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

            elif titulo == "tipo_de_cama":
                if len(dados_hospede[id_titulo].value)>1:
                    hospede[titulo] = fac.ajustarCama(dados_hospede[id_titulo].value)

            elif titulo=="in" or titulo=="out":
                hospede[titulo] = fad.ajustarData(dados_hospede[id_titulo].value, num_mes)

            else: hospede[titulo] = fan.capitalizar(dados_hospede[id_titulo].value)

        #Confição de existência de hóspede.
        if len(hospede) >= 4:
            lista_hospedes.append(hospede)

    '''
    #Criação do arquivo JSON
    with open("dados_hospedes.json", "w") as f:
        json.dump(lista_hospedes, f, indent=2)
    '''
    
    #Retorno do Dicionário
    return lista_hospedes
