from wallet import PlayerWallet


def test_correct_initial_balance():
    wallet = PlayerWallet(100.0)

    assert wallet.balance == 100.0


def test_bet_with_enough_balance():
    wallet = PlayerWallet(50.0)
    sucess = wallet.try_place_bet(20.0)

    assert sucess is True
    assert wallet.balance == 30.0


def test_bet_blocked_insufficient_funds():
    wallet = PlayerWallet(10.0)
    sucess = wallet.try_place_bet(50.0)

    assert sucess is False
    assert wallet.balance == 10.0
