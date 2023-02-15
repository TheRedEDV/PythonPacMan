import pygame, random, sys
from pygame.locals import *
pygame.init()

from Enemy import target_tile

from Text import decoration

Texture_pack =  "Recursos/Texture_pack.png"

en_width = 28
en_height = 28

#update

def init(all_sprites1):
    global all_sprites
    
    all_sprites = all_sprites1
    

class Pac_man_eater(pygame.sprite.Sprite):
    def __init__(self, x, y, coor):
        super().__init__()
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(4, 91, 12, 13))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (10, 10)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = -2

        self.left_states =  ((46, 91, 12, 13), (4, 91, 12, 13), (46, 91, 12, 13), (60, 91, 12, 13))
        self.right_states = ((18, 91, 12, 13), (4, 91, 12, 13), (18, 91, 12, 13), (32, 91, 12, 13))
        
        self.direction = "left"
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        
        self.coor = coor
        
    def Change_Direction(self):
        if self.rect.x <= self.coor:
            self.direction = "right"
            self.speed_x = 2
        
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.frame += 1
            
            
            if self.frame >= 4:
                 self.frame = 0    
                 
            
            if self.direction == "left":
                self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (27, 29))


            if self.direction == "right":
                self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (27, 29))
                
    def Play(self):
        self.speed_x = 2
        self.frame_rate = 50


    def Stop(self):
        self.speed_x = 0
        self.frame_rate = 6000

  
    def update(self, delta_time):
        self.Change_Direction()
        
        self.rect.x += round(self.speed_x*60*delta_time, 0)
    
        self.Animation()


class MEGA_pac_man(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(3, 218, 30, 29))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (10, 10)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.right_states = ((36, 218, 30, 29), (3, 218, 30, 29), (36, 218, 30, 29), (66, 218, 30, 29))
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30


    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.frame += 1
            
            
            if self.frame >= 4:
                 self.frame = 0    
                 
            self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (75, 75))


    def update(self, delta_time):
        self.Animation()
        self.rect.x += round(4*60*delta_time, 0)


class Chasing_n_Chased(pygame.sprite.Sprite):
    def __init__(self, x, y, color, sprite_object):
        super().__init__()
        self.mode = 1
        
        self.color = color
        
        self.sprite_object = sprite_object
    
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(3, 125, 1, 1))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        
        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((255, 0, 0, 1), self.color)
        
        self.image = pygame.transform.scale(self.image, (30, 30)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed_x = -2
        
        self.left_states =  ((37, 125), (54, 125))
        self.right_states = ((3, 125), (20, 125))
        self.frightened_sates_1 = ((3, 197), (20, 197))
        
        self.direction = "left"

        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 120

        self.rev = True

    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:          
            self.last_update = now
            self.frame += 1
            
            if self.frame >= 2:
                self.frame = 0
    
            if self.mode == 1:
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())


                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                    
                self.image.set_colorkey((0, 0, 0))
                self.image_pixel_array = pygame.PixelArray(self.image)
                self.image_pixel_array.replace((255, 0, 0, 1), self.color)
                self.image = pygame.transform.scale(self.image, (30, 30))
                
                
            if self.mode == 2:

                self.sheet.set_clip(pygame.Rect(self.frightened_sates_1[self.frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (30, 30))

    
    def Change_Direction(self):
        if self.rev:
            if self.sprite_object.direction == "right":
                self.rev = False
                self.mode = 2
                self.speed_x = 1
                self.direction = "right"
            
    def Play(self):
        self.speed_x = 1


    def Stop(self):
        self.speed_x = 0

    
    def update(self, delta_time):
        self.Change_Direction()
    
        self.rect.x += round(self.speed_x*60*delta_time, 0)
        
        self.Animation()


class True_Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, color, coor):
        super().__init__()
        self.color = color
        
        self.coor = coor
    
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(3, 125, 1, 1))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        
        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((255, 0, 0, 1), self.color)
        
        self.image = pygame.transform.scale(self.image, (30, 30)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed_x = -3
        
        self.left_states =  ((105, 235), (122, 235))
        self.right_states = ((140, 238), (165, 238))
        
        self.direction = "left"

        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 120

        self.rev = True

    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:          
            self.last_update = now
            self.frame += 1
            
            if self.frame >= 2:
                self.frame = 0
    

            if self.direction == "left":
                self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image_pixel_array = pygame.PixelArray(self.image)
                self.image_pixel_array.replace((255, 0, 0, 1), self.color)
                self.image = pygame.transform.scale(self.image, (30, 30))


            if self.direction == "right":
                self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]+(22, 11)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image_pixel_array = pygame.PixelArray(self.image)
                self.image_pixel_array.replace((255, 0, 0, 1), self.color)
                self.image = pygame.transform.scale(self.image, (50, 28))


    def Change_Direction(self):
        if self.rev:
            if self.rect.x <= self.coor:
                self.rev = False
                self.speed_x = 3
                self.direction = "right"
  

    def update(self, delta_time):
        self.Change_Direction()
    
        self.rect.x += round(self.speed_x*60*delta_time, 0)
        
        self.Animation()


class Black(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.Surface([50, 30])
        self.image.fill((0, 0, 0)) #(0, 0, 255)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Point_Animation(pygame.sprite.Sprite):
    def __init__(self, symbol, x, y):
        super().__init__()   
        
        self.symbol = symbol
        
                             #  200         400         800         1600
        self.symbol_sheet = [(152, 169), (152, 178), (152, 187), (152, 196),
        
                             #   100         300         500         700         1000       2000        3000        5000
                             (175, 133), (175, 142), (175, 151), (175, 160), (175, 169), (175, 178), (175, 187), (175, 196)]
                             
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.symbol_sheet[self.symbol] + (20, 7)))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0, 1))
        
        self.image = pygame.transform.scale(self.image, (50, 18)) #14 = 12, 13 = 11
        
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y+6


class Generate_Point():
    def __init__(self, symbol, x, y):
        self.black = Black(x, y)
        all_sprites.add(self.black)
        
        self.point = Point_Animation(symbol, x, y)
        all_sprites.add(self.point)
        
    def kill(self):
        self.black.kill()
        self.point.kill()
        