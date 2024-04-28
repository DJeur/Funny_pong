from pygame import *


class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



back = (255, 255, 0)
win_wight = 600
win_height = 500 
window = display.set_mode((win_height, win_wight))
window.fill(back)

ball = GameSprite(Friend.jpg, 150, 150, 10, 30, 30)

game = True
finish = False
clock = time.Clock()
FPS = 60

while True:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))

    clock.tick(FPS)
    display.update()
