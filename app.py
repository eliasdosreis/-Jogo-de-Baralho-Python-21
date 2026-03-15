import random 

naipes = ["Ouros","Copas","Paus","Espadas"]

valores = ["A","2","3","4","5","6","7","8","9","10","Q","K","J"]

pontos_carta = {
    "A" : 1, "2" : 2,"3" : 3,"4" : 4,"5" : 5,"6" : 6,"7" : 7,"8" : 8,"9" : 9, "10" : 10, "Q" : 10, "J" : 10, "K" : 10
}

# Função que CRIA o baralho completo — ela combina cada naipe com cada valor
def criar_baralho():
   
    baralho = [(naipe,valor) for naipe in naipes for valor in valores]

    random.shuffle(baralho)

    return baralho




# Função que retira UMA carta do topo do baralho e entrega para uma mão
def distribuir_carta(baralho, mao):
   
    carta = baralho.pop()

    mao.append(carta)

# Função que soma os pontos de todas as cartas na mão e trata o Ás (1 ou 11)
def calcular_pontos(mao):
    total = sum(pontos_carta[valor]  for naipe, valor in mao  )

    if total > 21 and any(v == "A" for _, v in mao):
        total -= 10

    return total



# Função que mostra as cartas de uma mão formatadas — ex: "[Copas - K] [Ouros - 5]"
def exibir_mao(mao, dono):
    #
    cartas = " ".join(f"[{n} - {v}]" for n, v in mao)
    
    print(f"{dono}: {cartas} → {calcular_pontos(mao)} pontos")


baralho = criar_baralho()
mao_jogador = []  
mao_banca   = []  

# Distribui 2 cartas para cada um — como num jogo real de blackjack
for _ in range(2): distribuir_carta(baralho, mao_jogador); distribuir_carta(baralho, mao_banca)

exibir_mao(mao_jogador, "Você")
exibir_mao(mao_banca, "Banca")