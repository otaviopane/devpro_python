class Pessoa:  # CamelCase
    def __init__(self, nome=None, idade=25):
        self.nome = nome  # o atributo de objeto, o campo existe mas não tem valor atribuido a ele
        # atributo nome // parametro nome
        # atr é o "nome" do objeto definido pelo self

    def cumprimentar(self):
        return 'Olá'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3  # sobrescrita de atributo


if __name__ == "__main__":
    jorge = Mutante(nome='Jorge')
    jurandy = Homem(jorge, nome='Jurandy')
    print(p.cumprimentar())  # ou print(Pessoa.cumprimentar(p)) // dá no mesmo
    # Ex que não cabe a esse arquivo que só recebe 1(self), mas para ilustrar:
    # passando 2 argumentos: print(p.cumprimentar(7)) ou print(Pessoa.cumprimentar(p,7)) // dá no mesmo
    print(p.nome)
