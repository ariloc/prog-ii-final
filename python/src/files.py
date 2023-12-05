INPUTS_PATH = "Entradas"
SENTENCES_PATH = "Frases"
OUTPUTS_PATH = "Salidas"

# File operations
def path_readlines_no_endline(path: str) -> list[str]:
    file = open(path,"r")
    lines = file.read().splitlines()
    file.close()
    return lines

def path_writelines_newline(lines: list[str], path: str):
    file = open(path,"w")
    file.writelines('\n'.join(lines) + '\n')
    file.close()

# Paths
def inputs_path(personName: str) -> str:
    return INPUTS_PATH + '/' + personName + '.txt'

def sentences_path(personName: str) -> str:
    return SENTENCES_PATH + '/' + personName + '.txt'

def outputs_path(personName: str) -> str:
    return OUTPUTS_PATH + '/' + personName + '.txt'

# Script-specific file operations
def read_input_sentences(personName: str) -> list[str]:
    return path_readlines_no_endline(inputs_path(personName))

def read_incomplete_sentences(personName: str) -> list[str]:
    return path_readlines_no_endline(sentences_path(personName))

def write_sentences(sentences: list[str], personName: str):
    path_writelines_newline(sentences, outputs_path(personName))
