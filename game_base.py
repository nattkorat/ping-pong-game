from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if (keys[K_UP]):
            self.rect.y -= self.speed
        if (keys[K_DOWN]):
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if (keys[K_w]):
            self.rect.y -= self.speed
        if (keys[K_s]):
            self.rect.y += self.speed
