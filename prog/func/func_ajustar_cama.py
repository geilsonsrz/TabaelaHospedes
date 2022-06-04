import re;

def ajustarCama(tipo_cama):

    cama = list()

    cama.extend(re.findall(r'(KING)', tipo_cama.upper()))
    cama.extend(re.findall(r'0?([1-9])', tipo_cama.upper()))
    cama.extend(re.findall(r'(ONE)', tipo_cama.upper()))
    cama.extend(re.findall(r'(UNA?O?)', tipo_cama.upper()))
    cama.extend(re.findall(r'(SGL)', tipo_cama.upper()))
    cama.extend(re.findall(r'(DOS)', tipo_cama.upper()))
    cama.extend(re.findall(r'(DBL)', tipo_cama.upper()))

    king = ["KING", "SGL", "UNO", "UNA", "ONE", "1"]
    
    if cama[0] in king: tipo_cama = "KING"
    else: tipo_cama = "DOS CAMAS"

    return tipo_cama
    