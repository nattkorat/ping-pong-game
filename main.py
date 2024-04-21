from pygame import *
from game_base import *

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Ping Game")

clock = time.Clock()

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))


player_l = Player("images/paddle.png", 10, 200, 50, 100, 5)
player_r = Player("images/paddle.png", 750, 200, 50, 100, 5)
ball = GameSprite("images/baseball.png", 350, 200, 25, 25, 5)

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    window.fill(back_color)
    reset(player_l)
    reset(player_r)
    reset(ball)
    player_l.update()

    clock.tick(40)
    display.update()
