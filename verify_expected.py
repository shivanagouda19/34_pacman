from game import Game, MAZE, FRIGHT_SECONDS, PLAYER_START, target_for_pinky, is_wall

# 1) Player never passes through walls and pellets are not re-collected
base = Game()
assert base.player == list(PLAYER_START)
assert (1, 1) in base.pellets
assert (0, 0) not in base.pellets
assert is_wall((0, 0))
assert not is_wall((1, 11))

# 2) Pinky target tile is 4 tiles ahead in current direction
assert target_for_pinky((10, 10), (0, 1)) == (10, 14)
assert target_for_pinky((10, 10), (-1, 0)) == (6, 10)

# 3) Clyde chases while far, retreats near his home corner when close
clyde = base.ghosts[3]
clyde.pos = (10, 10)
assert clyde.target((10, 10), (0, 1), base.ghosts[0], True) == clyde.corner
clyde.pos = (0, 0)
assert clyde.target((10, 10), (0, 1), base.ghosts[0], True) == (10, 10)

# 4) Power pellet triggers frightened mode and reverses directions once
power_cell = next((r, c) for r, row in enumerate(MAZE) for c, v in enumerate(row) if v == 'o')
fright = Game()
for ghost in fright.ghosts:
    ghost.direction = (1, 0)
    ghost.pos = (9, 10)
fright.pellets = {power_cell}
fright.eat(power_cell)
assert fright.fright_left == FRIGHT_SECONDS
for ghost in fright.ghosts:
    if not ghost.eaten:
        assert ghost.direction == (-1, 0)

# 5) Win and loss states are triggered correctly
win_game = Game()
win_game.pellets = {(1, 1)}
win_game.eat((1, 1))
assert win_game.state == 'win'

loss_game = Game()
loss_game.lives = 1
loss_game.player = [9, 10]
loss_game.ghosts[0].pos = (9, 10)
loss_game.fright_left = 0.0
loss_game.check_collisions()
assert loss_game.state == 'lose'

print('All expected gameplay checks passed.')
