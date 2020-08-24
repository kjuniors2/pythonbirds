class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    @staticmethod
    def metodoestatico():
        return 42

    @classmethod
    def classemetodo(cls):
        return f'{cls} - olhos {cls.olhos}'


    def cumprimentar(self):
        return f'Olá {id(self)}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    joao = Homem(nome='Joao')
    julio = Pessoa(joao, nome='Julio')
    print(julio.nome)
    print(joao.nome)
    print(julio.filhos)
    for filho in julio.filhos:
        print(filho.nome)
    julio.sobrenome = 'Kimichi'
    print(julio.sobrenome)
    del joao.filhos
    julio.olhos = 3
    print(joao.__dict__)
    print(julio.__dict__)
    print(julio.olhos)
    print(joao.olhos)
    print(id(Pessoa.olhos), id(julio.olhos), id(joao.olhos))
    print(Pessoa.metodoestatico(), julio.metodoestatico())
    print(Pessoa.classemetodo(), julio.classemetodo())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Homem))
    print(isinstance(pessoa, Pessoa))
    print(isinstance(joao, Homem))
    print(isinstance(joao, Pessoa))

