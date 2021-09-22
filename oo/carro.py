"""Você deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:
1) Motor
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguntes atributos:
1) Atributo de dado velocidade, que informa a vel do carro
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverá decrementar a velocidade em duas unidades
2) Direção
A Direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis:
      Norte, Sul, Leste e Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

Exemplo:
>>> # Testando Motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

>>> # Testando Direcao
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar
>>> carro.calcular_velocidade()
1
>>> carro.frear
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""


class Carro:
    def __init__(self, motor, direcao):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.motor.direcao.direcao

    def girar_a_direita(self):
        return self.motor.girar_a_direita()

    def girar_a_esquerda(self):
        return self.motor.girar_a_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        # vel será o valor max entre o 1º elemento(0) e o 2º(vel atual)
        self.velocidade = max(0, self.velocidade)


class Direcao:
    posicao = ['Norte', 'Leste', 'Sul', 'Oeste']

    def __init__(self):
        self.valor = 0
        self.direcao = posicao[self.valor]

    def valor(self):
        print(self.direcao)

    def girar_a_direita(self):
        if self.valor == 3:
            self.valor = -1
        self.valor += 1

    def girar_a_esquerda(self):
        if self.valor == 0:
            self.valor = 3
        self.valor -= 1
