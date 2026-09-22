from model.gerar_solucao_inicial import gerar_solucao_inicial
from repositories.catalogo import catalogo

# REMOVIDO: import main01

def gerar_problema(num_porcoes: int):
    # Passa o número de porções recebido como argumento
    lista_porcoes = gerar_solucao_inicial(catalogo, num_porcoes=num_porcoes)
    return lista_porcoes

def gerar_problema_binario(lista_porcoes):
    # Forma concisa de gerar a lista de zeros com o mesmo tamanho
    return [0] * len(lista_porcoes)