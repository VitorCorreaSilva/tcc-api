from api.arquivo.conf import *
from traceback import format_exc as e_msg
from pypdf import PdfReader, PdfWriter
from api.lib.Log import log, read_log, start_log, log_as_json
import re

words = ["pagamento",
"fatura",
"juros",
"saldo",
"financiamento",
"iof"]

def search_words(text):
    regex = "|".join(words)

    retorno = re.search(regex, text.lower())

    if retorno:
        return False
    else:
        return True

def main(file):
    reader = PdfReader(file)

    if reader.is_encrypted:
        reader.decrypt("02346")

    text = ''
    for page in reader.pages:
        text += page.extract_text()

    regex = r"((\d{2}\W)(\d{2}\s|[a-zA-Z]{3}\s|\d{2})([a-zA-Z\s*-]*(\d{1,2}/\d{1,2}\W)?)(\d{1,}[,]\d{2}))"

    text = text.replace('\n','')

    dates = re.finditer(regex, text)

    result = []
    for i in dates:
        dif = i.end() - i.start()
        if(dif > 15 and dif < 50 and search_words(i.group())):
            data = {
                "day": i.group(2)[:-1],
                "month": i.group(3).strip(),
                "title": i.group(4).strip(),
                "value": i.group(6),
            }
            result.append(data)

    return result

def upload(file):
    # Inicia o sistema de log
    start_log(new_logname=logfile_name)
    sucesso = False
    try:
        sucesso = main(file)
    except Exception as e:
        log("ERRO: Um erro desconhecido aconteceu.")
        log(e)
        log(e_msg())
    return {
        "payload": sucesso,
        "log": log_as_json()
    }, 200 if sucesso else 500