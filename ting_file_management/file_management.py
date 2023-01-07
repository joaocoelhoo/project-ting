import os.path
import sys


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')

    f = open(path_file, "r")
    lines = f.read().splitlines()
    f.close()
    return lines
