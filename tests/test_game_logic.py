from logic_utils import check_guess, reset_game

def test_guess_of_one_is_told_to_go_higher():
    # Bug 1: guessing 1 against a secret like 100 said "Go LOWER" because
    # the secret was compared as a string ("1" > "100" is False).
    outcome, message = check_guess(1, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_new_game_after_loss_resets_status():
    # Bug 2: New Game reset attempts/secret but left status as "lost",
    # so the app hit st.stop() and never started a new game.
    state = {"status": "lost", "attempts": 8, "secret": 42, "history": [1, 2, 3]}
    reset_game(state, 1, 20)
    assert state["status"] == "playing"
    assert state["attempts"] == 0
    assert state["history"] == []
    assert 1 <= state["secret"] <= 20
