#!/usr/bin/env python3

from casino_base import CasinoGame
from wallet import PlayerWallet
from dice_game import DiceGame, OverUnder7


if __name__ == "__main__":
    print("=== Simulador de Probabilidades: Casino ===")
    print("--- Abrindo a mesa de Classic Dice ---")

    meu_jogo = DiceGame("Dado")
    valor_aposta = 10.0
    print(f"\nRolando os dados... Apostando R$ {valor_aposta} na esperança de tirar um 6!")
    resultado = meu_jogo.without_choice_play(valor_aposta)

    if resultado > 0.0:
        print(f"Você tirou o número 6 e ganhou R$ {resultado:.2f}!\n")
    else:
        print(f"Que azar! Você não tirou o 6 e a banca ficou com o seu dinheiro.")

    print("--- Fechando mesa de Classic Dice ---\n")
    print("--- Abrindo a mesa de Over/Under 7 ---")
    print("Opções de escolhas:\nOver (Acima do número 7)\nUnder (Abaixo do número 7)\nSeven (O número 7)\n")
    player_bet_choice = input("Digite sua escolha: ")

    seven_game = OverUnder7("Dado")
    valor_aposta = 20.0
    print(f"Rolando os dados... Apostando R$ {valor_aposta} na esperança de acertar no {player_bet_choice}")
    resultado = seven_game.with_choice_play(valor_aposta, player_bet_choice)

    if resultado == valor_aposta * 2.0:
        print(f"Você escolheu {player_bet_choice} e ganhou R${resultado:.2f}!\n")
    elif resultado == valor_aposta * 4.0:
        print(f"Que sorte! Você escolheu {player_bet_choice} e ganhou R${resultado:.2f}!!\n")
    else:
        print(f"Que azar! Você escolheu {player_bet_choice} e perdeu")
    
