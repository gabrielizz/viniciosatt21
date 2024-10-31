# Gabriel Gonçalves
# Fase Refactor

def calcular_media_nota(notas):
    """
    Calcula a média de uma lista de notas.
    
    Parâmetros:
    notas (list): Uma lista de números (int ou float) representando as notas.
    
    Retorna:
    float: A média das notas na lista. Retorna None se a lista estiver vazia.
    
    Lança:
    ValueError: Se a entrada não for uma lista de números válidos.
    """
    # Verificação se 'notas' é uma lista
    if not isinstance(notas, list):
        raise ValueError("A entrada deve ser uma lista de números.")
    
    # Verificação se todos os elementos são números
    if not all(isinstance(nota, (int, float)) for nota in notas):
        raise ValueError("Todos os itens na lista devem ser números (int ou float).")
    
    # Tratamento para lista vazia
    if len(notas) == 0:
        return None  # ou você pode optar por retornar 0 ou outro valor
    
    # Cálculo da média
    return sum(notas) / len(notas)
