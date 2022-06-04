import re;

def ajustarData(x_data, n_mes=None):

    l_data = re.findall(r"([0-9]{4}-[0-9][0-9]-[0-9][0-9])\s.*", x_data)
    if len(l_data)==1:
        ano_mes_dia = l_data[0].split("-")
        dia = ano_mes_dia[2]
        mes = ano_mes_dia[1]
        ano = ano_mes_dia[0]
        data = (f"{dia}/{mes}/{ano}")

        return data

    elif len(l_data)==0:

        data = (f"{x_data}/{n_mes}")

        return data
    
    else:
        x = ("Verificar DATA")
        return x


