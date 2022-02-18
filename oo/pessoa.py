class Pessoa:
    def cumprimentar(self):
        return f'olá {id(self)}'


p = Pessoa()
if __name__ == '__main__':
    print(p.cumprimentar())
    print(id(p))

