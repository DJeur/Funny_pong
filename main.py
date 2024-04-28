from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect. y -= self.speed
    if keys[K_DOWN] and self.rect.y < win_deight - 80:
      self.rect. y += self.speed
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
      self.rect. y -= self.speed
    if keys[K_s] and self.rect.y < win_deight - 80:
      self.rect. y += self.speed

speed_x = 3
speed_y = 3
back = (255, 255, 0)
win_wight = 600
win_height = 500 
window = display.set_mode((win_height, win_wight))
window.fill(back)

player_1 = Player('racket.png', 130, 130, 10, 40, 60)
player_2 = Player('racket.png', 530, 130, 10, 40, 60)
ball = GameSprite('Friend.jpg', 150, 150, 30, 30, 30)


font = font.Font(None, 50)
lose1 = font.render('Player 1 Lose', True, (100, 100, 100))
lose2 = font.render('Player 2 Lose', True, (100, 100, 100))
game = True
finish = False
clock = time.Clock()
FPS = 60

while True:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(back)
        player_1.update_l()
        player_2.update_r()
        ball.rect.y += speed_y
        ball.rect.x += speed_x

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1 
            speed_y *= 1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        window.blit(background, (0,0))
        player_2.reset()
        player_1.reset()
        ball.reset()
    clock.tick(FPS)
    display.update()
