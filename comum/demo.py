"""Rotina comum de demonstracao dos algoritmos de ordenacao."""


def demonstrar_ordenacao(nome, ordenar, valores):
    """Ordena uma copia de `valores` com `ordenar`, imprimindo antes e depois."""
    dados = list(valores)
    print(nome)
    print('Antes: ', dados)
    ordenar(dados)
    print('Depois:', dados)
    return dados
