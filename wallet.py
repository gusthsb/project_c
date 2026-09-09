#!/usr/bin/env python3


class PlayerWallet:
    def __init__(self, initial_balance: float = 100.0) -> None:
        self.balance: float = initial_balance

    def try_place_bet(self, amount: float) -> bool:
        """Tenta fazer uma aposta. Retorna True se tiver saldo"""
        if amount > self.balance:
            print(
                f"Saldo insuficiente! Você tem"
                f" no momento R${self.balance:.2f}."
            )
            return False
        else:
            self.balance -= amount
            return True

    def add_winnings(self, amount: float) -> None:
        """Adiciona na conta o dinheiro recebido pelas apostas"""
        self.balance += amount

    def show_balance(self) -> None:
        """Mostra a carteira atual"""
        print(f"Saldo atual: R${self.balance:.2f}")
