#!/usr/bin/env python3

from abc import ABC, abstractmethod


class CasinoGame(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    @abstractmethod
    def without_choice_play(self, bet_amount: float) -> float:
        """
        Recebe o valor da aposta e retorna o prêmio.
        Se perder, retorna 0.0
        """
        pass

    @abstractmethod
    def with_choice_play(self, bet_amount: float, bet_choice: str) -> float:
        """
        Recebe o valor da aposta e retorna o prêmio.
        Se perder, retorna 0.0
        """
        pass
