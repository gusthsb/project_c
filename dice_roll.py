#!/usr/bin/env python3

from casino_base import CasinoGame
import random


class DiceGame(CasinoGame):
    def __init__(self, name: str) -> None:
        super().__init__("Classic 6 Dice")

    def without_choice_play(self, bet_amount: float) -> float:
        nbr = random.randint(1, 6)

        if nbr == 6:
             return bet_amount * 5.0
        else:
            return 0.0

    def with_choice_play(self, bet_amount: float, bet_choice: str) -> float:
        raise ValueError("O Simple Dice não aceita escolhas para apostas!")


class OverUnder7(CasinoGame):
    def __init__(self, name: str) -> None:
        super().__init__("Over/Under 7")

    def without_choice_play(self, bet_amount: float) -> float:
        raise ValueError("O Over/Under7 exige uma escolha (over, under or seven).")

    def with_choice_play(self, bet_amount: float, bet_choice: str) -> float:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        total = first_dice + second_dice
        choice = bet_choice.strip().upper()

        print(f"[{self.name}] Os dados rolaram, resultado:\n{first_dice} "
              f"e {second_dice}\nSoma: {total}")

        if choice == "OVER" and total > 7:
            return bet_amount * 2.0

        elif choice == "UNDER" and total < 7:
            return bet_amount * 2.0

        elif choice == "SEVEN" and total == 7:
            return bet_amount * 4.0

        else:
            return 0.0         


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
