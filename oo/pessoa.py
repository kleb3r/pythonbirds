class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'


p = Pessoa('Jupira', 29)
if __name__ == '__main__':
    renzo = Pessoa(nome="Renzo", idade=8)
    safira = Pessoa(nome='Safira', idade=2)
    luciano = Pessoa(renzo, safira, nome="Luciano")
    print(p.idade)
    print(p.nome)
    print(luciano.filhos)
    for filho in luciano.filhos:
        print(f'sao filhos de luciano: {filho.nome}')
    print(f'{renzo.nome} tem {renzo.idade} anos')
    print(f'{safira.nome} tem {safira.idade} anos')