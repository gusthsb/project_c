#!/usr/bin/env python3

from casino_base import CasinoGame
from wallet import PlayerWallet
from dice_game import DiceGame, OverUnder7


def main() -> None:
    print("=== Bem-vindo ao Casino Python ===")

    carteira = PlayerWallet(100.0)
    jogo_classico = DiceGame("Dado")
    jogo_over_under = OverUnder7("Dado")

    while True:
        print("\n" + "="*40)
        carteira.show_balance()
        
        if carteira.balance <= 0:
            print(" Você faliu! O cassino agradece o seu dinheiro. Fim de jogo.")
            break
            
        print("\nEscolha o seu jogo:")
        print("[1] Classic 6 Dice (Aposte na sorte para tirar o número 6!)")
        print("[2] Over/Under 7 (Aposte na soma de dois dados)")
        print("[3] Sair do Cassino")
        
        opcao = input("\nDigite a sua opção: ").strip()
        
        if opcao == '3':
            print(f"Você saiu do cassino com R$ {carteira.balance:.2f}. Volte sempre!")
            break
            
        if opcao not in ['1', '2']:
            print(" Opção inválida. Escolha um número do menu.")
            continue

        try:
            valor_aposta = float(input("Quanto quer apostar? R$ "))
        except ValueError:
            print(" Por favor, digite um valor numérico válido!")
            continue

        if carteira.try_place_bet(valor_aposta):
            resultado = 0.0
            
            if opcao == '1':
                print(f"\n Rolando os dados no {jogo_classico.name}...")
                resultado = jogo_classico.without_choice_play(valor_aposta)
                
            elif opcao == '2':
                escolha = input("Sua escolha [over] [under] [seven]: ").strip().lower()
                print(f"\n Rolando os dados no {jogo_over_under.name} para {escolha.upper()}...")
                
                try:
                    resultado = jogo_over_under.with_choice_play(valor_aposta, escolha)
                except Exception as e:
                    print(f"Erro na aposta: {e}")
                    carteira.add_winnings(valor_aposta) 
                    continue

            if resultado > 0.0:
                print(f"BINGO! Você ganhou R$ {resultado:.2f}!")
                carteira.add_winnings(resultado)
            else:
                print("Que azar! A banca levou a sua aposta.")


if __name__ == "__main__":
    main()
