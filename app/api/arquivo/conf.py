from os import environ as env

try:
    logfile_name = env['LOG_FILE_NAME']
except KeyError:
    logfile_name = ''