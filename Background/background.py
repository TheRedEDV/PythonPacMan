import pygame, sys
from pygame.locals import *
pygame.init()

Texture_pack = "Recursos/Texture_pack.png"

background__ = pygame.sprite.Group()

#update

def init(all_sprites1, background_sprites1):
    global all_sprites, background_sprites
    
    all_sprites = all_sprites1
    background_sprites = background_sprites1

def kill():
    for sprite in background_sprites:
        sprite.kill()
        
    for sprite in background__:
        sprite.kill()


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(371, 4, 164, 212))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (410, 530))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x#60
        self.rect.y = y#100


class Flicker_Bacground(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(202, 4, 164, 212))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (410, 530))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed_x = -610
        
        self.frame_rate = 150
        self.last_update = pygame.time.get_ticks()
        
    def Movement(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:    
            self.last_update = now
            
            self.rect.x += self.speed_x
            
            self.speed_x *=-1
            
    def update(self, delta_time):
        self.Movement()

   
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, weidth, height, color_key=True):
        super().__init__()
 
        self.image = pygame.Surface([weidth, height])
        self.image.fill((0, 0, 0)) #(0, 0, 255)
        
        if color_key == True: self.image.set_colorkey((0, 0, 0))
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


def Generate_Wall(x, y, weidth, height, Transpareance=False, color_key=True):
    wall = Wall(x, y, weidth, height, color_key)
    
    all_sprites.add(wall)
    
    if Transpareance == False:
        background_sprites.add(wall)

  
def Generate_Stage(x, y):
    # ----Barras horizontales-------
    
    Generate_Wall(x,     y,     410, 10)
    Generate_Wall(x,     y+520, 410, 10)
    
    Generate_Wall(x+40,  y+480, 130, 10)
    Generate_Wall(x+240, y+480, 130, 10)
    
    Generate_Wall(x+40,  y+380, 50, 10)
    Generate_Wall(x+120, y+380, 50, 10)
    Generate_Wall(x+240, y+380, 50, 10)
    Generate_Wall(x+320, y+380, 50, 10)
    
    Generate_Wall(x+120, y+180, 50, 10)
    Generate_Wall(x+240, y+180, 50, 10)
    
    # Generate_Wall(x+170, y+220, 70, 1)
    Generate_Wall(x+170, y+220, 20, 10)
    Generate_Wall(x+220, y+220, 20, 10)
    Generate_Wall(x+190, y+220, 30, 1)
    
    Generate_Wall(x+170, y+280, 70, 10)
    
    Generate_Wall(x+180, y+540, 80, 10) #casa-secreta
    Generate_Wall(x+180, y+580, 80, 10) #casa-secreta
   
    
    # ----Barras horizontales-------
    
    
    # ------Barras verticales--------

    Generate_Wall(x,     y    , 10, 190)
    Generate_Wall(x+400, y    , 10, 190)
    
    Generate_Wall(x,     y+340, 10, 190)
    Generate_Wall(x+400, y+340, 10, 190)
    
    Generate_Wall(x+200, y+10  , 10, 80)
    
    Generate_Wall(x+120, y+120, 10, 130)
    Generate_Wall(x+280, y+120, 10, 130)
    
    Generate_Wall(x+120, y+280, 10, 70)
    Generate_Wall(x+280, y+280, 10, 70)
    
    Generate_Wall(x+80,  y+380, 10, 70)
    Generate_Wall(x+320, y+380, 10, 70)
    
    Generate_Wall(x+120, y+420, 10, 70)
    Generate_Wall(x+280, y+420, 10, 70)
    
    Generate_Wall(x+200, y+150, 10, 40)
    Generate_Wall(x+200, y+350, 10, 40)
    Generate_Wall(x+200, y+450, 10, 40)
    
    Generate_Wall(x+160, y+220, 10, 70)
    Generate_Wall(x+240, y+220, 10, 70)
    
    Generate_Wall(x+180, y+540, 10, 50) #casa-secreta
    Generate_Wall(x+220, y+540, 10, 50) #casa-secreta
    Generate_Wall(x+260, y+540, 10, 50)
   
    
    # ------Barras verticales--------
    
    
    # -----Cuadrados ----------------
    
    Generate_Wall(x+40   ,y+40  , 50, 50)
    Generate_Wall(x+120  ,y+40  , 50, 50)
    
    Generate_Wall(x+240  ,y+40  , 50, 50)
    Generate_Wall(x+320  ,y+40  , 50, 50)
    
    Generate_Wall(x+40   ,y+120 , 50, 30)
    Generate_Wall(x+160  ,y+120 , 90, 30)
    Generate_Wall(x+320  ,y+120 , 50, 30)
    
    Generate_Wall(x+160  ,y+320 , 90, 30)
    Generate_Wall(x+160  ,y+420 , 90, 30)
    
    Generate_Wall(x      ,y+420 , 50, 30)
    Generate_Wall(x+360  ,y+420 , 50, 30)
    
    Generate_Wall(x+320  ,y+180 , 150, 70)
    Generate_Wall(x+320  ,y+280 , 150, 70)
    
    Generate_Wall(x-60   ,y+180 , 150, 70)
    Generate_Wall(x-60   ,y+280 , 150, 70)
    
    Generate_Wall(x+180, y+540, 100, 50, True, False) # Casa secreta
    
    # -----Cuadrados ----------------
    
    #Fondo --------------------------
    
    # background = Background(x, y)
    # all_sprites.add(background)
    # background__.add(background)
    
    #Fondo --------------------------
    
    # ---- Cuadrados ----------------
    Generate_Wall(x-60, y+180, 60, 170, True, False)
    Generate_Wall(x+410, y+180, 60, 170, True, False)
    
    # ---- Cuadrados ---------------- 
