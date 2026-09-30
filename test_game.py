import unittest

from game import Game, FRIGHT_SECONDS, MAZE, bonus_life_threshold, ghost_color


class PacManTests(unittest.TestCase):
    def test_power_pellet_activates_frightened_mode(self):
        game = Game()
        power_cell = next((r, c) for r, row in enumerate(MAZE) for c, value in enumerate(row) if value == "o")
        game.pellets.add(power_cell)
        game.fright_left = 0.0
        for ghost in game.ghosts:
            ghost.direction = (1, 0)
        game.eat(power_cell)
        self.assertEqual(game.fright_left, FRIGHT_SECONDS)
        self.assertGreaterEqual(game.score, 50)

    def test_ghost_color_returns_tint_for_frightened_mode(self):
        color = ghost_color("pinky", "frightened")
        self.assertIsInstance(color, tuple)
        self.assertEqual(len(color), 3)

    def test_bonus_life_threshold_is_configured(self):
        self.assertIsInstance(bonus_life_threshold(), int)
        self.assertGreater(bonus_life_threshold(), 0)


if __name__ == "__main__":
    unittest.main()
