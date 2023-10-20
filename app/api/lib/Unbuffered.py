class Unbuffered(object):
    """
        Classe que implementa um novo wrapper para o print.
        retirado da página https://stackoverflow.com/a/10771

        Utilizado para implementar o flush stdout após cada print,
        de modo que o print aconteça durante a execução do script,
        e não após sua execução.
    """

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)
