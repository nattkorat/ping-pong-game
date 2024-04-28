from pygame import *
from game_base import *

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Ping Game")

clock = time.Clock()

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))


player_l = Player("images/paddle.png", 10, 200, 50, 150, 5)
player_r = Player("images/paddle.png", 700, 200, 50, 150, 5)
ball = GameSprite("images/baseball.png", 350, 200, 50, 50, 5)

ball_speed_x = ball.speed
ball_speed_y = ball.speed

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    window.fill(back_color)
    reset(player_l)
    reset(player_r)
    reset(ball)

    player_l.update_l()
    player_r.update_r()

    # make the ball move
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y

    # bouncing of the ball
    if ball.rect.y < 0 or ball.rect.y >= 450:
        ball_speed_y *= -1
    
    if sprite.collide_rect(ball, player_l) or sprite.collide_rect(ball, player_r):
        ball_speed_x *= -1



    clock.tick(40)
    display.update()
