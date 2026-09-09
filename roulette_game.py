#!/usr/bin/env python3

import random
from casino_base import CasinoGame


class RouletteGame(CasinoGame):
    def __init__(self, name: str) -> None:
        super().__init__("Roleta americana")
        self.red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

    def without_choice_play(self, bet_amount: float) -> float:
        raise ValueError("A Roleta exige uma escolha (ex: 'red', 'black', 'even', 'odd' ou um número de 0 a 36).")

    def with_choice_play(self, bet_amount: float, bet_choice: str) -> float:
        spin_result = random.randint(0, 36)

        is_red = spin_result in self.red_numbers
        is_black = spin_result != 0 and not is_red

        is_even = spin_result != 0 and spin_result % 2 == 0
        is_odd = spin_result != 0 and spin_result % 2 != 0

        color = "🔴 Red" if is_red else "♠️ Black" if is_black else "🟢 Green"
        print(f"[{self.name}] A bola caiu no: {spin_result} ({color})")

        choice = bet_choice.strip().lower()

        if choice == "red" and is_red:
            return bet_amount * 2.0

        elif choice == "black" and is_black:
            return bet_amount * 2.0

        elif choice == "even" and is_even:
            return bet_amount * 2.0

        elif choice == "odd" and is_odd:
            return bet_amount * 2.0

        elif choice.isdigit() and int(choice) == spin_result:
            return bet_amount * 36.0

        else:
            return 0.0

