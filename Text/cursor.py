import pygame, sys
from pygame.locals import *
pygame.init()

Texture_pack = "Recursos/Texture_pack.png"

def init(all_sprites1):
    global all_sprites
    
    all_sprites = all_sprites1

class Black_rect(pygame.sprite.Sprite):
    def __init__(self, sprite_object):
        super().__init__()
        self.image = pygame.Surface((20, 18))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        
        self.sprite_object = sprite_object
        
        self.rect.x = self.sprite_object.rect.x-20
        self.rect.y = self.sprite_object.rect.y
        self.speed_x = 20
        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 300


    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.rect.x += self.speed_x
            
            self.speed_x *= -1


    def update(self, delta_time):
        self.Animation()
        self.rect.y = self.sprite_object.rect.y


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(96, 69, 8, 7))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 1, 1))
        self.image = pygame.transform.scale(self.image, (20, 18)) #14 = 12, 13 = 11

        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 0
        
        self.speed_y = 0
        self.speed = 44


    def limit(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        
        if self.rect.y >= 616:
            self.rect.y = 616


    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.speed_y += self.speed*-1
            
        
            if event.key == pygame.K_s:
                self.speed_y += self.speed

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.speed_y = 0
            
        
            if event.key == pygame.K_s:
                self.speed_y = 0


    def update(self, delta_time):
        
        self.rect.y += self.speed_y
        
        if self.speed_y <= -44:
            self.speed_y = 0
        
        if self.speed_y >= 44:
            self.speed_y = 0
            
        self.limit()


class Main_Cursor(Cursor):
    def __init__(self):
        Cursor.__init__(self)
        
        self.rect.x = 200
        self.rect.y = 286
    
    def limit(self):
        if self.rect.y <= 286:
            self.rect.y = 286
        
        if self.rect.y >= 374:
            self.rect.y = 374