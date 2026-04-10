# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if indice >= len(lista) or indice < -len(lista):
        return None
    else:
        return lista[indice]

#lista = [10, 20, 30]
#print(get_element(lista, -5))
