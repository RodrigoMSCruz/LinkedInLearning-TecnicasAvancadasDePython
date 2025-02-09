# Usando a classe Counter
from collections import Counter


def main():
    # Uma lista de estudantes na turma A
    turma_a = ["Bárbara", "João", "Carlos", "Dário", "Priscila", "Ana"
               "Kevin", "João", "Marina", "Bianca", "Gustavo",
               "Fernanda"]

    # Uma lista de estudantes na turma B
    turma_b = ["Hiro", "Bruno", "Claudia", "Débora", "Fernanda",
               "Gabriela", "Leticia", "João", "Jairo", "Samuel",
               "Taciana", "Gabriel"]

    # TODO: Crie um Counter para as turmas A e B
    a = Counter(turma_a)
    b = Counter(turma_b)

    # TODO: Quantos estudantes na turma B se chamam João?
    print(b["João"])

    # TODO: Quantos estudantes estão na turma B?
    print(sum((b.values())))
    
    # TODO: Quais os 3 nomes mais comuns nas duas turmas?
    print(a.most_common(3))
    print(b.most_common(3))

    # TODO: Separe as duas turmas e mostre o nome mais comum da turma a

    # TODO: Qual a intersecção de nomes entre as duas turmas?

    # TODO: Quantos estudantes na turma A se chamam João?

    # TODO: Quantos estudantes estão na turma A?
    print(sum((b.values())))

    # TODO: Combine as duas turmas
    a.update(turma_b)
    print(sum(a.values()))

    # TODO: Quais os 3 nomes mais comuns nas duas turmas?
    print(a.most_common(3))
    print(b.most_common(3))

    # TODO: Separe as duas turmas e mostre o nome mais comum da turma a
    a.subtract(turma_b)
    print(a.most_common(3))

    # TODO: Qual a intersecção de nomes entre as duas turmas?
    print(a & b)


if __name__ == "__main__":
    main()
