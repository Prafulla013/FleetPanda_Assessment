class BowlingGame:
    def __init__(self) -> None:
        self.rolls: list[int] = []

    def roll(self, pins: int) -> None:

        # Records a single roll. Validates input.

        if not (0 <= pins <= 10):
            raise ValueError(f"Invalid pin count: {pins}. Must be between 0 and 10.")
        self.rolls.append(pins)

    def score(self) -> int:
       
        # Calculates the total score based on standard bowling rules.
        
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if roll_index >= len(self.rolls):
                raise IndexError("Not enough rolls to complete 10 frames.")

            if self._is_strike(roll_index):
                total_score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total_score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self._frame_points(roll_index)
                roll_index += 2

        return total_score

    def display_rolls_by_frame(self) -> None:
       
        # Prints rolls frame by frame, using standard bowling notation.
        
        print("\n📋 Rolls by Frame:")
        roll_index = 0
        for frame in range(1, 11):
            if roll_index >= len(self.rolls):
                break

            if frame < 10:
                if self._is_strike(roll_index):
                    print(f"Frame {frame}: [X]")
                    roll_index += 1
                elif self._is_spare(roll_index):
                    print(f"Frame {frame}: [{self.rolls[roll_index]}, /]")
                    roll_index += 2
                else:
                    print(f"Frame {frame}: [{self.rolls[roll_index]}, {self.rolls[roll_index + 1]}]")
                    roll_index += 2
            else:
                # Frame 10 logic: up to 3 rolls
                rolls = self.rolls[roll_index:]
                display = []
                for i in range(min(3, len(rolls))):
                    r = rolls[i]
                    if r == 10:
                        display.append("X")
                    elif i > 0 and rolls[i - 1] + r == 10 and rolls[i - 1] != 10:
                        display.append("/")
                    else:
                        display.append(str(r))
                print(f"Frame {frame}: [{', '.join(display)}]")

    def _is_strike(self, index: int) -> bool:
        return self.rolls[index] == 10

    def _is_spare(self, index: int) -> bool:
        return self.rolls[index] + self.rolls[index + 1] == 10

    def _strike_bonus(self, index: int) -> int:
        return self.rolls[index + 1] + self.rolls[index + 2]

    def _spare_bonus(self, index: int) -> int:
        return self.rolls[index + 2]

    def _frame_points(self, index: int) -> int:
        return self.rolls[index] + self.rolls[index + 1]


def main():
    print("🎳 Bowling Game Score Calculator")
    game = BowlingGame()

    # Example rolls based on the challenge
    example_rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10,
                     0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
    for pins in example_rolls:
        game.roll(pins)

    game.display_rolls_by_frame()
    print("\n✅ Total Score:", game.score())


if __name__ == "__main__":
    main()
