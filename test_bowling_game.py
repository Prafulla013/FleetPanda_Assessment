import pytest
from bowling_game import BowlingGame

def roll_many(game: BowlingGame, rolls: list[int]) -> None:
    for pins in rolls:
        game.roll(pins)

@pytest.mark.parametrize("rolls, expected", [
    ([0] * 20, 0),
    ([1] * 20, 20),
    ([10] * 12, 300),
    ([5, 5] * 10 + [5], 150),
    ([1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1,
      7, 3, 6, 4, 10, 2, 8, 6], 133)
])
def test_valid_scores(rolls, expected):
    game = BowlingGame()
    roll_many(game, rolls)
    assert game.score() == expected

def test_invalid_negative_pin():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(-1)

def test_invalid_pin_over_ten():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(11)

def test_incomplete_game_raises_error():
    game = BowlingGame()
    rolls = [10] * 5  # only 5 strikes, not enough for full game
    roll_many(game, rolls)
    with pytest.raises(IndexError):
        game.score()

# Purposely broken tests to simulate catching bugs (for demo)
def test_broken_spare_should_fail():
    game = BowlingGame()
    rolls = [5, 5, 3] + [0] * 17  # should be 16, but we assert wrong value
    roll_many(game, rolls)
    assert game.score() == 15  # this is correct
    # let's break it
    # assert game.score() == 13

def test_broken_strike_should_fail():
    game = BowlingGame()
    rolls = [10, 3, 4] + [0] * 17  # 10 + 3 + 4 = 17
    roll_many(game, rolls)
    assert game.score() == 24  # intentionally wrong
