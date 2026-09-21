from model import (propor_solucao,validar_solucao,aplicar_restricoes,calcular_metricas)
from repositories import catalogo
import random

if __name__ == "__main__":
    random.seed(42)

    capacidade_max = 500       
    carboidrato_max = 200      
    proteina_max = 100          
    exigir_vegetal = True      

    invalida = 0
    lista_solucoes = []
    #lista_metricas_solucoes = []
    for i in range(10):
        solucao = propor_solucao(catalogo, num_porcoes=3)
        eh_valida = validar_solucao(solucao, catalogo, capacidade_max, proteina_max, carboidrato_max, exigir_vegetal)[0]
        #eh_valida, lista_solucoes.append(solucao) if eh_valida == True else invalida = invalida + 1
        if eh_valida == True:
            #lista_metricas_solucoes.append(calcular_metricas(solucao, catalogo))
            lista_solucoes.append(solucao)
            lista_solucoes.append(calcular_metricas(solucao, catalogo))

    print("_____________________________________________________________________________________")
    for i in lista_solucoes:
        print(i)
        print("_____________________________________________________________________________________")
    
    
    #solucao = propor_solucao(catalogo, num_porcoes=3)
    #print("_________________________")
    #solucao = aplicar_restricoes(solucao, catalogo, capacidade_max, proteina_max, carboidrato_max, exigir_vegetal)
    #print("\nApós aplicar_restricoes:", solucao)
    #print("Métricas:", calcular_metricas(solucao, catalogo))
    #print("Válida?", validar_solucao(solucao, catalogo, capacidade_max, proteina_max, carboidrato_max, exigir_vegetal)[0])