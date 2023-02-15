import pygame, sys
from pygame.locals import *
pygame.init()

from Text import decoration

Texture_pack = "Recursos/Texture_pack.png"

#update

def init(all_sprites1, pellets_sprites1, background_sprites1):
    global all_sprites
    global pellets_sprites
    global background_sprites
    
    all_sprites = all_sprites1
    pellets_sprites = pellets_sprites1
    background_sprites = background_sprites1

def kill():
    for pellet in pellets_sprites:
        pellet.kill()


class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        super().__init__()
        self.score = score
        
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 185, 176)) #(0, 0, 255)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Super_Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        super().__init__()
        self.score = score
    
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect((8, 79, 7, 7)))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (18, 18)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.frame_rate = 300
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        
        self.states = ((8, 79, 7, 7), ((8, 79, 1, 1)))




class Kill_pellet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 185, 176)) #(0, 0, 255)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
        self.Chronometer1 = decoration.Chronometer(.1)
        
    def update(self, delta_time):
        pygame.sprite.groupcollide(pellets_sprites, background_sprites, True, False)
        if self.Chronometer1.time_over():
            self.Chronometer1.kill()
            self.kill()


def Generate_pellets(x, y):
    init_x = x
    init_y = y

    # Parte superior --------------------
    
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+23, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
    
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+43, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
    
    # super pellet -------------------------------
    
    x = init_x
    super_pellet = Super_Pellet(x+16, y+56, 50)
    #all_sprites.add(super_pellet)
    pellets_sprites.add(super_pellet)
    
    # super pellet -------------------------------
        
    x = init_x
    for n in range(17):
        pellet = Pellet(x+43, y+63, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    # super pellet -------------------------------
        
    x = init_x
    super_pellet = Super_Pellet(x+376, y+56, 50)
    #all_sprites.add(super_pellet)
    pellets_sprites.add(super_pellet)
    
    # super pellet -------------------------------
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+83, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+103, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+123, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20 
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+143, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+163, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    # Parte superior --------------------
        
    # Parte central ---------------------
    
    x = init_x
    y = init_y
    for n in range(9):
        pellet = Pellet(x+103, y+183, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        y += 20
        
    x = init_x
    y = init_y
    for n in range(9):
        pellet = Pellet(x+303, y+183, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        y += 20

    y =  init_y
    
    # Parte central ---------------------

    # Parte inferior --------------------
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+363, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20 

    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+383, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
    
    # super pellet -------------------------------
    
    x = init_x
    super_pellet = Super_Pellet(x+16, y+396, 50)
    #all_sprites.add(super_pellet)
    pellets_sprites.add(super_pellet)

    # super pellet -------------------------------

    x = init_x
    for n in range(8):
        pellet = Pellet(x+43, y+403, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(8):
        pellet = Pellet(x+223, y+403, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
     
    # super pellet -------------------------------
        
    x = init_x
    super_pellet = Super_Pellet(x+376, y+396, 50)
    #all_sprites.add(super_pellet)
    pellets_sprites.add(super_pellet)
    
    # super pellet -------------------------------
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+423, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+443, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20  

    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+463, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20

    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+483, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    x = init_x
    for n in range(19):
        pellet = Pellet(x+23, y+503, 10)
        #all_sprites.add(pellet)
        pellets_sprites.add(pellet)
        x += 20
        
    # Parte inferior --------------------
          
    
    # eliminando pelletas que estan entre las paredes
    
    kill_pellets = Kill_pellet()
    all_sprites.add(kill_pellets) 
