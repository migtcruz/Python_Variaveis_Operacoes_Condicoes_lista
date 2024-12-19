import random

def gerar_jogo():
    """Gera 15 números aleatórios e não repetidos entre 1 e 25."""
    numeros = random.sample(range(1, 26), 15)
    return sorted(numeros)

def gerar_jogos(quantidade):
    """Gera uma quantidade específica de jogos da Lotofácil."""
    jogos = []
    for _ in range(quantidade):
        jogos.append(gerar_jogo())
    return jogos

def mostrar_jogos(jogos):
    """Exibe os jogos gerados de forma formatada."""
    for jogo in jogos:
        print('-', *jogo, '-')

if __name__ == "__main__":
    quantidade = int(input("Quantos jogos você deseja gerar? "))
    jogos = gerar_jogos(quantidade)
    mostrar_jogos(jogos)

