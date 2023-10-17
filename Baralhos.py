import random
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self, values = [], suits = []):
        self.cartas = [Carta(valor, naipe) for valor in values for naipe in suits]

    def create_deck(self, values, suits):
        self.cartas = [Carta(valor, naipe) for valor in values for naipe in suits]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def criaCarta(self, valor, naipe):
        self.cartas.append(Carta(valor, naipe))

    def card_value_as_number(self, carta):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
        return values.index(carta.valor)

    def menorValor(self):
        if not self.cartas:
            return None
        return (min(self.cartas, key=self.card_value_as_number)).valor

    def maiorValor(self):
        if not self.cartas:
            return None
        return (max(self.cartas, key=self.card_value_as_number)).valor

    def primeiroNaipe(self):
        if not self.cartas:
            return None
        return self.cartas[-1].naipe

    def ultimoNaipe(self):
        if not self.cartas:
            return None
        return self.cartas[0].naipe

    def pegaCarta(self):
        if len(self.cartas) > 0:
            self.iterator = max(0, self.iterator - 1)
            return self.cartas.pop()
        else:
            return None
    
    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < len(self.cartas):
            carta = self.cartas[self.iterator]
            self.iterator += 1
            return carta
        raise StopIteration

class BaralhoPoker(Baralho):
    def __init__(self):
        super().__init__()
        self.create_deck()

    def create_deck(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
        suits = ['Copas', 'Ouros', 'Paus', 'Espadas']
        super().create_deck(values, suits)

class BaralhoTruco(Baralho):
    def __init__(self):
        super().__init__()
        self.create_deck()
    
    def create_deck(self):
        values = ['Ás', '2', '3', '4', '5', '6', '7', 'Valete', 'Cavalo', 'Rei']
        suits = ['Ouros', 'Bastos', 'Copas', 'Espadas']
        super().create_deck(values, suits)

    def card_value_as_number(self, carta):
        values = ['Ás', '2', '3', '4', '5', '6', '7', 'Valete', 'Cavalo', 'Rei']
        return values.index(carta.valor)

# values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
# suits = ['Copas', 'Ouros', 'Paus', 'Espadas']

deck_poker = BaralhoPoker()
deck_poker.embaralhar()

deck_truco = BaralhoTruco()
deck_truco.embaralhar()

print('\nBaralho de Poker:')
print('Maior valor do baralho: ' + str(deck_poker.maiorValor()))
print('Menor valor do baralho: ' + str(deck_poker.menorValor()))
print('Naipe da primeira carta: ' + str(deck_poker.primeiroNaipe()))
print('Naipe da ultima carta: ' + str(deck_poker.ultimoNaipe()))
# Se quiser a hierarquia entre os naipes teria que modificar o metodo; ordenando os naipes e fazendo que nem nos metods maiorValor() e menorValor()
print('Carta no topo: ' + str(deck_poker.pegaCarta()))

print('\n\nBaralho de Truco:')
print('Maior valor do baralho: ' + str(deck_truco.maiorValor()))
print('Menor valor do baralho: ' + str(deck_truco.menorValor()))
print('Naipe da primeira carta: ' + str(deck_truco.primeiroNaipe()))
print('Naipe da ultima carta: ' + str(deck_truco.ultimoNaipe()))
print('Carta no topo: ' + str(deck_truco.pegaCarta()))
print()

# for card in deck_poker:
#     print('Carta do baralho de Poker: ' + str(card))

# for card in deck_truco:
#     print('Carta do baralho de Truco: ' + str(card))