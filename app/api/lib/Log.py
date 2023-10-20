"""Conjunto de funções para criar um sistema de logging.
"""
from api.lib.Unbuffered import Unbuffered
import sys
import datetime
from os import environ, system
sys.stdout = Unbuffered(sys.stdout)

try:
    logname = environ['LOG_FILE_NAME']
except Exception:
    logname = "log.log"

log_div = ' -- '

def __date():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")

def __to_file(objects: str, end: str):
    """Função privada.
    concatena a string objects a um arquivo de log

    Args:
        objects (str): String a ser concatenada
        end (str): string a ser concatenada ao fim da string objects
    """
    try:
        f = open(logname, 'a')
        f.write("%s%s" % (objects, end))
        f.close()
    except Exception as e:
        print("Erro na função log. A função start_log já foi chamada?")
        print("Detalhes do erro:\n %s" % (e))


def start_log(new_logname=None):
    """Função que inicia o sistema de log, cria um arquivo de log caso
    ele não exista, ou trunca o arquivo já existente
    """
    if new_logname is not None:
        global logname
        logname = new_logname

    f = open(logname, 'w')
    f.close()


def log(objects: str, end: str='\n'):
    """exibe uma string na tela via print, e adiciona essa
    mesma string para um arquivo de log

    Args:
        objects (str): string a ser 'loggada'
        end (str, optional): string a ser concatenada
                             ao final da string objects,
                             padrão = '\n'
    """
    msg = "%s%s%s" % (__date(),log_div, objects)
    print(msg, end=end)
    __to_file(msg, end)

def read_log():
    f = open(logname, 'r')
    log = f.read()
    f.close()
    return log

def log_as_json():
    json = {}
    f = open(logname, 'r')
    for line in f:
        split_line = line.split(log_div)
        key = split_line[0]
        value = log_div.join(split_line[1:])
        json[key] = value.replace('\n','',99)
    
    f.close()
    return json