"""
Você deve criar uma classe carro que vai possuir dois atributos
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


class Motor:
    def __init__(self, velocidade):
        self.velocidade = 0
		return velocidade

    def mostrar_velocidade(velocidade):
        Motor.vel_agora = velocidade
        return print(velocidade)

    def acelerar(velocidade):
        velocidade += 1
        return velocidade

    def frear(velocidade):
        velocidade -= 2
        return velocidade


posicao = ['Norte', 'Leste', 'Sul', 'Oeste']


class Direcao:
	def __init__(self, numero):
		self.numero = 0
		return numero

    def valor(numero):
        direcao = posicao[numero]
        return print(direcao)

    def girar_a_direita(numero):
        if numero == 3:
			numero = -1
		numero += 1
        return numero

    def girar_a_esquerda(numero):
		if numero == 0:
			numero = 3	
        numero -= 1
        return numero
