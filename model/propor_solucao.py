from typing import List
from repositories import CatalogoAlimentos

import random
def propor_solucao(catalogo: CatalogoAlimentos, num_porcoes: int = 3) -> List[str]:
    nomes = list(catalogo.keys())
    k = min(num_porcoes, len(nomes))
    return random.sample(nomes, k)

