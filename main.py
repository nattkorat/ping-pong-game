from pygame import *
from game_base import *

font.init()

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Ping Game")

clock = time.Clock()

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))


player_l = Player("images/paddle.png", 10, 200, 50, 150, 5)
player_r = Player("images/paddle.png", 700, 200, 50, 150, 5)
ball = GameSprite("images/baseball.png", 350, 200, 50, 50, 5)

font_game = font.Font(None, 30) # create the font

player_l_lose = font_game.render(
    "Player 1 Lose!", True, (255, 0, 0)
)

player_r_lose = font_game.render(
    "Player 2 Lose!", True, (255, 0, 0)
)

ball_speed_x = ball.speed
ball_speed_y = ball.speed

running = True
finish = False

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    if not finish:
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
        
        if ball.rect.x < player_l.rect.x - 10:
            window.blit(player_l_lose, (350, 200))
            finish = True
        
        if ball.rect.x > player_r.rect.x + 10:
            window.blit(player_r_lose, (350, 200))
            finish = True


    clock.tick(40)
    display.update()
