class Pessoa:
    olhos = 2
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
    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    luciano.olhos = 1
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(renzo.olhos), id(luciano.olhos), id(Pessoa.olhos))
    del luciano.olhos
    print(luciano.olhos)
    print(id(renzo.olhos), id(luciano.olhos), id(Pessoa.olhos))
