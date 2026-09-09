#!/usr/bin/env python3

import random
from casino_base import CasinoGame


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
        raise ValueError(
            "O Over/Under7 exige uma escolha (over, under or seven)."
        )

    def with_choice_play(self, bet_amount: float, bet_choice: str) -> float:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        total = first_dice + second_dice
        choice = bet_choice.strip().upper()

        print(
            f"[{self.name}] Os dados rolaram, resultado:\n{first_dice} "
            f"e {second_dice}\nSoma: {total}"
        )

        if choice == "OVER" and total > 7:
            return bet_amount * 2.0

        elif choice == "UNDER" and total < 7:
            return bet_amount * 2.0

        elif choice == "SEVEN" and total == 7:
            return bet_amount * 4.0

        else:
            return 0.0
