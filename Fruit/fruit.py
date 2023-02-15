import pygame, sys
from pygame.locals import * 
pygame.init() 

Texture_pack = "Recursos/Texture_pack.png"

class Level_Fruit(pygame.sprite.Sprite):
    def __init__(self, fruit, x, y):
        super().__init__()
        
        self.fruit_sheet = {"cherry":     (207,), 
                            "strawberry": (223,), 
                            "peach":      (239,), 
                            "apple":      (255,), 
                            "melon":      (271,), 
                            "flagship":   (287,), 
                            "bell":       (304,), 
                            "key":        (319,) }
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.fruit_sheet[fruit] + (223, 12, 14) ))
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (30, 35))
        
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = x, y


class Bonus_Fruit(pygame.sprite.Sprite):
    def __init__(self, fruit, x, y): # 58, 138
        super().__init__()
        
                            # key           x_pos  score     
        self.fruit_sheet = {"cherry":     ((207,),  100), 
                            "strawberry": ((223,),  300), 
                            "peach":      ((239,),  500), 
                            "apple":      ((255,),  700), 
                            "melon":      ((271,), 1000), 
                            "flagship":   ((287,), 2000),
                            "bell":       ((304,), 3000),
                            "key":        ((319,), 5000), }
                            
        self.score = self.fruit_sheet[fruit][1]
                            
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.fruit_sheet[fruit][0] + (223, 12, 14) ))
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (30, 35))
        
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = x, y