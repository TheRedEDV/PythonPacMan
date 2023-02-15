import pygame
from pygame .locals import *
pygame.init()

from Text import decoration

hi_score = 0
score = 0

#update

def init(all_sprites1):
    global all_sprites
    all_sprites =  all_sprites1


def update_score(score_plus):
    global score, hi_score
    
    score += score_plus

    if score >= hi_score:
        hi_score = score

  
def Reset_score():
    global score
    
    score = 0


class Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x, pos_y):
        decoration.Decoration_part.__init__(self, 0, 440, 166, (255, 255, 255), "s", False)
        self.pos = pos
        self.pos_x = pos_x
        self.pos_y = pos_y
            
            
    def display(self):
        local_score = str(score)
        if len(local_score) >= 8:
            local_score = "error"

        if len(local_score) == 1:
            local_score = "     00"+local_score
            
        if len(local_score) == 2:
            local_score = "     "+local_score
            
        if len(local_score) == 3:
            local_score = "    "+local_score
            
        if len(local_score) == 4:
            local_score = "   "+local_score
            
        if len(local_score) == 5:
            local_score = "  "+local_score
            
        if len(local_score) == 6:
            local_score = " "+local_score
            
        if len(local_score) == 7:
            local_score = local_score

        
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 31
            if n == "1":
                n = 32
            if n == "2":
                n = 33
            if n == "3":
                n = 34
            if n == "4":
                n = 35
            if n == "5":
                n = 36
            if n == "6":
                n = 37
            if n == "7":
                n = 38
            if n == "8":
                n = 39
            if n == "9":
                n = 40
            if n == " ":
                n = 29
            if n == "e":
                n = 4
            if n == "o":
                n = 14  
            if n == "r":
                n = 17
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[local_score[self.pos]]+(7, 7)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((0, 0, 0, 1), (0, 0, 1, 1))
        
        self.image.set_colorkey((0, 0, 1, 1))
        
        self.image = pygame.transform.scale(self.image, (18, 18))
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
    def update(self, delta_time):
        self.display()


def Score():
    x = 440
    y = 166
    for n in range(7):
        score_a = Score_Part(n, x, y)
        all_sprites.add(score_a)
        x += 20


class Hi_Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x, pos_y):
        decoration.Decoration_part.__init__(self, 0, 440, 166, (255, 255, 255), "s", False)
        self.pos = pos
        self.pos_x = pos_x
        self.pos_y = pos_y
            
            
    def display(self):
        local_score = str(hi_score)
        if len(local_score) >= 8:
            local_score = "error"

        if len(local_score) == 1:
            local_score = "     00"+local_score
            
        if len(local_score) == 2:
            local_score = "     "+local_score
            
        if len(local_score) == 3:
            local_score = "    "+local_score
            
        if len(local_score) == 4:
            local_score = "   "+local_score
            
        if len(local_score) == 5:
            local_score = "  "+local_score
            
        if len(local_score) == 6:
            local_score = " "+local_score
            
        if len(local_score) == 7:
            local_score = local_score

        
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 31
            if n == "1":
                n = 32
            if n == "2":
                n = 33
            if n == "3":
                n = 34
            if n == "4":
                n = 35
            if n == "5":
                n = 36
            if n == "6":
                n = 37
            if n == "7":
                n = 38
            if n == "8":
                n = 39
            if n == "9":
                n = 40
            if n == " ":
                n = 29
            if n == "e":
                n = 4
            if n == "o":
                n = 14  
            if n == "r":
                n = 17
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[local_score[self.pos]]+(7, 7)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((0, 0, 0, 1), (0, 0, 1, 1))
        
        self.image.set_colorkey((0, 0, 1, 1))
        
        self.image = pygame.transform.scale(self.image, (18, 18))
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

  
    def update(self, delta_time):
        self.display()


def Hi_Score():
    x = 440
    y = 100
    for n in range(7):
        score_a = Hi_Score_Part(n, x, y)
        all_sprites.add(score_a)
        x += 20


def return_hi_score():
    local_score = str(hi_score)

    if len(local_score) >= 8:
            local_score = "error"

    if len(local_score) == 1:
        local_score = "     0"+local_score
        
    if len(local_score) == 2:
        local_score = "     "+local_score
        
    if len(local_score) == 3:
        local_score = "    "+local_score
        
    if len(local_score) == 4:
        local_score = "   "+local_score
        
    if len(local_score) == 5:
        local_score = "  "+local_score
        
    if len(local_score) == 6:
        local_score = " "+local_score
        
    if len(local_score) == 7:
        local_score = local_score

    return local_score