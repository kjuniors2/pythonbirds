class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa(nome='Joao')
    julio = Pessoa(joao, nome='Julio')
    print(julio.nome)
    print(joao.nome)
    print(julio.filhos)
    for filho in julio.filhos:
        print(filho.nome)