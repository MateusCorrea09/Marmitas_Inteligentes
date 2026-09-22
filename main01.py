from repositories.catalogo import catalogo
from model.gerar_solucao_inicial import gerar_solucao_inicial
from model.gerar_problema import gerar_problema, gerar_problema_binario
from model.gerar_marmita_inicial import gerar_marmita_inicial
from model.gerar_sucessor import gerar_sucessor

tamanho_lista_porcoes = 10
numero_porcoes_MAX = 3

if __name__ == "__main__":
    # 1. Gera a lista de porções sorteadas passando o tamanho desejado
    problema_mapeado = gerar_problema(tamanho_lista_porcoes)
    print("Porções selecionadas:")
    print(problema_mapeado)

    # 2. Gera a lista binária (zeros) baseada no tamanho do problema gerado
    vetor_binario = gerar_problema_binario(problema_mapeado)
    print("___________________________________________________________________________________")
    print("\nVetor binário inicial:")
    print(vetor_binario)
    print(vetor_binario)

    print("___________________________________________________________________________________")
    print(f"Lista problema tem tamanho = [{len(problema_mapeado)}]")
    print(f"Lista problema tem tamanho = [{len(vetor_binario)}]")
    print("___________________________________________________________________________________")
    vetor_binario_modificado = gerar_marmita_inicial(numero_porcoes_MAX=numero_porcoes_MAX,lista_porcoes_binaria=vetor_binario)
    print(vetor_binario)
    #print(vetor_binario_modificado)
    print("___________________________________________________________________________________")
    for i in range(len(vetor_binario)):
        if vetor_binario[i] == 1:
            print(f"Item da marmita: {problema_mapeado[i]}")
    print("___________________________________________________________________________________")
    print(f"Lista inicial:\n {vetor_binario}")
    print("___________________________________________________________________________________")
    vetores_sucessores = gerar_sucessor(vetor_binario)
    for idx, sucessor in enumerate(vetores_sucessores, 1):
        print(f"Sucessor {idx}: {sucessor}")
        print("Itens desta marmita:")
        
        # Percorre as posições do SUCESSOR ATUAL para saber os alimentos selecionados nele
        for j in range(len(sucessor)):
            if sucessor[j] == 1:
                print(f"  - [{j}] {problema_mapeado[j]}")
                
        print("___________________________________________________________________________________")