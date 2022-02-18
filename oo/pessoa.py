class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'olá {id(self)}'


p = Pessoa('Jupira', 29)
if __name__ == '__main__':
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)
    p.nome = 'Renzo'
    print(p.idade)
    print(p.nome)
