# Iteradores do módulo itertools
import itertools


def condicao(x):
    return x < 40


def main():
    # TODO: Iterador cycle pode ser usado como o iter para iterar sobre
    # uma lista
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))

    # TODO: Use count para criar um contador
    contador = itertools.count(100, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))

    # TODO: A função groupby cria um iterador que agrupa elementos de uma
    # sequência

    # TODO: A função starmap cria um iterador que aplica uma função
    # aos elementos de duas sequências

    # TODO: A função product cria um iterador que produz todos os
    # possíveis produtos de duas ou mais sequências

    # TODO: A função permutations cria um iterador que produz todas as
    # possíveis permutações de uma sequência

    # TODO: A função combinations cria um iterador que produz todas as
    # possíveis combinações de um determinado número de elementos de uma
    # sequência

    # TODO: A função accumulate cria um iterdor que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores)
    print(list(acumulado))

    acumulado = itertools.accumulate(valores, max)
    print(list(acumulado))

    # TODO: Use a função chain para conectar listas
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # TODO: As funções dropwhile e takewhile vai retornar valores até
    # que uma condição seja atingida

    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))

if __name__ == "__main__":
    main()
