import pygame, sys
from pygame.locals import * 
pygame.init()

from Text import decoration

Texture_pack = "Recursos/Texture_pack.png"


class Display_Live():
    def __init__(self, sprite_object):
        self.sprite_object = sprite_object
        decoration.Generate_Decoration("live", 440, 455, (255, 0, 0, 1), "pac_man_live_word")
        decoration.Generate_Decoration("#", 487, 488, (255, 0, 0, 1), "pac_man_live_word")


    def Get_Live(self):
        if self.sprite_object.live >= 100:
            self.sprite_object.live = 99
    
        
        if len(str(self.sprite_object.live)) == 2:
            self.live_number_display = str(self.sprite_object.live)
    
    
        if len(str(self.sprite_object.live)) == 1:
            self.live_number_display = " " + str(self.sprite_object.live)


    def update_live(self):
        self.Get_Live()
        decoration.Kill_Identifier("pac_man_live")
        decoration.Generate_Decoration(self.live_number_display, 440, 494, (255, 255, 255), "pac_man_live")


class Dead_Explosion(pygame.sprite.Sprite):
    def __init__(self, sprite_object):
        super().__init__()
        self.sprite_object = sprite_object
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect((4, 110, 15, 9)))
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image =  pygame.transform.scale(self.image, (38, 23))
        
        self.rect = self.image.get_rect()
        
        self.rect.center = self.sprite_object.rect.center
        
        self.explosition_states = ((4, 110, 15, 9), (23, 110, 15, 9), (42, 110, 15, 9), (61, 110, 15, 9), (80, 110, 15, 9), 
                                   (98, 110, 15, 9), (113, 110, 15, 9), (128, 110, 15, 9), (140, 110, 15, 9), (155, 110, 15, 9))
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200


    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            
            if self.frame == len(self.explosition_states):
                self.kill()


            else:
                self.sheet.set_clip(pygame.Rect(self.explosition_states[self.frame]))
 
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                
                self.image =  pygame.transform.scale(self.image, (38, 23))
                

    def update(self, delta_time):
        self.Animation()