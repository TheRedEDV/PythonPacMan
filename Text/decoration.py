import pygame, sys
from pygame.locals import *
pygame.init()

Texture_pack = "Recursos/Texture_pack.png"

#update

def init(all_sprites1, decoration_sprites1):
    global all_sprites
    global decoration_sprites
    
    all_sprites = all_sprites1
    decoration_sprites =  decoration_sprites1


class Decoration_part(pygame.sprite.Sprite):
    def __init__(self, symbol, x, y, color, identifier, s_color):
        super().__init__()
        self.identifier = identifier
        self.symbol =  symbol
        self.wh = (7, 7)
        self.conv = (18, 18)
        
        if self.symbol == 27:
            self.wh = (8, 7)
            self.conv = (20, 18)
            
        if self.symbol == 28:
            self.wh = (8, 8)
            self.conv = (20, 20)
            
        if self.symbol == 29:
            self.wh = (1, 1)
            self.conv = (18, 18)
            
        if self.symbol == 44:
            self.wh = (7, 8)
            self.conv = (18, 20)

        if self.symbol == 45:
            self.wh = (182, 46)
            self.conv = (455, 115)
            
        if self.symbol == 46:
            self.wh = (70, 10)
            self.conv = (175, 25)
            
        if self.symbol == 47:
            self.wh = (14, 13)
            self.conv = (30, 30)
            
        if self.symbol == 50:
            self.wh = (12, 13)
            self.conv = (27, 29)

                              # a        b          c         d         e        f          g         h
        self.sprite_sheet = [(9, 61), (17, 61), (25, 61), (33, 61), (41, 61), (49, 61), (57, 61), (65, 61),
        
                              # i         j          k         l         m          n          o         p
                             (73, 61), (81, 61), (89, 61), (97, 61), (105, 61), (113, 61), (121, 61), (1, 69),
                             
                             #  q         r         s         t         u         v         w         x
                             (9, 69), (17, 69), (25, 69), (33, 69), (41, 69), (49, 69), (57, 69), (65, 69),
                             
                             #  y          z         .         >        (c)       space         "       0
                             (73, 69), (81, 69), (89, 69), (96, 69), (105, 69), (113, 69), (121, 69), (1, 53), 
                             
                             #  1          2        3        4         5          6         7         8     
                             (9, 53), (17, 53), (25, 53), (33, 53), (41, 53), (49, 53), (57, 53), (65, 53),
                             
                             #  9          -         /         !         ,      PAC MAN    NANCO    ghost
                             (73, 53), (81, 53), (89, 53), (97, 53), (105, 52), (2, 4), (20, 78), (3, 125), 
                             
                             #pellet  s-pellet  pac-man
                             (1, 79), (8, 79), (46, 91)]
                             #
                             #(4, 91), (1, 79), (8, 79), (3, 125), (71, 125), (54, 125)]
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[self.symbol] + self.wh))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        
        if s_color == False:
            self.image.set_colorkey((0, 0, 1, 1))
            self.image_pixel_array = pygame.PixelArray(self.image)
            self.image_pixel_array.replace((255, 255, 255), color)
            
        else:
            self.image.set_colorkey((0, 0, 0))
            self.image_pixel_array = pygame.PixelArray(self.image)
            self.image_pixel_array.replace(s_color, color)

        self.image = pygame.transform.scale(self.image, self.conv) #14 = 12, 13 = 11
        
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y


def Generate_Decoration(message, x, y, color, identifier, s_color=False):
    banned_characters = ['"', "\\", "¿", "¡", "¬", "´", "¨", "~", "[", "^", "]", "`"]
    space = 20
    
    for banned in banned_characters:
        message = message.replace(banned, "")
        
    message = message.lower()
    letters = list()
    for n in message:
        if n == "a":
            n = 0
        if n == "b":
            n = 1
        if n == "c":
            n = 2
        if n == "d":
            n = 3
        if n == "e":
            n = 4
        if n == "f":    
            n = 5
        if n == "g":
            n = 6
        if n == "h":
            n = 7
        if n == "i":
            n = 8
        if n == "j":
            n = 9
        if n == "k":
            n = 10
        if n == "l":
            n = 11
        if n == "m":
            n = 12
        if n == "n":
            n = 13
        if n == "o":
            n = 14
        if n == "p":
            n = 15
        if n == "q":
            n = 16
        if n == "r":
            n = 17
        if n == "s":
            n = 18
        if n == "t":
            n = 19
        if n == "u":
            n = 20
        if n == "v":
            n = 21
        if n == "w":
            n = 22
        if n == "x":
            n = 23
        if n == "y":
            n = 24
        if n == "z":
            n = 25
        if n == ".":
            n = 26
        if n == ">":
            n = 27
        if n == "+":
            n  = 28
        if n == " ":
            n = 29
        if n == "'":
            n = 30
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
        if n == "-":
            n = 41
        if n == "/":
            n = 42
        if n == "!":
            n = 43
        if n == ",":
            n = 44
        if n == "*":
            n = 45
        if n == "|":
            n = 46    
        if n == "{":
            n = 47
        if n == "(":
            n = 48
        if n == ")":
            n = 49
        if n == "#":
            n = 50

        letters.append(n)

    message = letters
    
    for letter in message:
        Decoration_letter = Decoration_part(letter, x, y, color, identifier, s_color)
        all_sprites.add(Decoration_letter)
        decoration_sprites.add(Decoration_letter)
        x += space


def Kill_Identifier(identifier):
    for decoration in decoration_sprites:
        try:
            if decoration.identifier == identifier:
                decoration.kill()
                
        except:
            pass


class Points(pygame.sprite.Sprite):
    def __init__(self, symbol, center, y_P=False):
        super().__init__()
        
        self.symbol_list = {0 : ["200", (15, 7), (38, 18)], 
                            1 : ["400", (15, 7), (38, 18)], 
                            2 : ["800", (15, 7), (38, 18)], 
                            3 : ["1600",(20, 7), (50, 18)],
                            4 : ["100", (15, 7), (38, 18)], 
                            5 : ["300", (15, 7), (38, 18)], 
                            6 : ["500", (15, 7), (38, 18)], 
                            7 : ["700", (15, 7), (38, 18)],
                            8 : ["1000",(20, 7), (50, 18)], 
                            9 : ["2000",(20, 7), (50, 18)], 
                           10 : ["3000",(20, 7), (50, 18)], 
                           11 : ["5000",(20, 7), (50, 18)]}
        
        for n in self.symbol_list:
            if symbol == self.symbol_list[n][0]:
                self.symbol = n
                self.wh =   self.symbol_list[n][1]
                self.conv = self.symbol_list[n][2]

                             #  200         400         800         1600
        self.symbol_sheet = [(157, 169), (157, 178), (157, 187), (152, 196),
        
                             #   100         300         500         700         1000       2000        3000        5000
                             (180, 133), (180, 142), (180, 151), (180, 160), (175, 169), (175, 178), (175, 187), (175, 196)]
                             
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.symbol_sheet[self.symbol] + self.wh))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
     
        self.image = pygame.transform.scale(self.image, self.conv) #14 = 12, 13 = 11

        self.rect = self.image.get_rect()

        self.rect.center = center
        if not y_P:
            pass
            
        else:
            self.rect.y += y_P
 

class Black_Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, large, speed_X, speed_Y, frame_rate, identifier):
        super().__init__()
        self.identifier = identifier
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(113, 69, 1, 1))  # x, y, ancho+1, alto
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.image = pygame.transform.scale(self.image, large)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed_X = speed_X
        self.speed_Y = speed_Y

        
          
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
        
            self.rect.x += self.speed_X #El movimiemto va acorde la animación 
            self.rect.y += self.speed_Y
            self.last_update = now
            
            
        
    def update(self, delta_time): 
        self.Animation()


class Black_Rect_flicker(pygame.sprite.Sprite):
    def __init__(self, x, y, large, frame_rate, identifier):
        self.identifier = identifier
        self.large = large
    
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(113, 69, 1, 1))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.image = pygame.transform.scale(self.image, self.large)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
       
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
        self.rev = 0
        
        
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.rev += 1
            
            if self.rev >= 2:
                self.rev = 0
            
            
            if self.rev == 0:
            
                self.sheet.set_clip(pygame.Rect(113, 69, 1, 1))  # x, y, ancho+1, alto+1
         
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
                self.image = pygame.transform.scale(self.image, self.large)
                self.image.set_colorkey((0, 0, 1, 1))

            
            
            if self.rev == 1:
            
                self.sheet.set_clip(pygame.Rect(113, 69, 1, 1))  # x, y, ancho+1, alto+1
         
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
                self.image = pygame.transform.scale(self.image, self.large)
                
            

    def update(self, delta_time):
        self.Animation()


def Write_Message(message, x, y, speed_X, speed_Y, frame_rate, color,  identifier, s_color=False):
    reazon = 20
    high = 18

    if "|" in message:
        reazon = 175
        high = 25
        
    if "{" in message:
        reazon = 30
        high = 30


    Generate_Decoration(message, x, y, color,  identifier, s_color)
    black = Black_Rect(x, y, (len(message)*reazon, high), speed_X, speed_Y,frame_rate, identifier)
    all_sprites.add(black)
    decoration_sprites.add(black)
   
   
def Flicker_Message(message, x, y, frame_rate, color, identifier):
    Generate_Decoration(message, x, y, color, identifier)
    black = Black_Rect_flicker(x, y, (len(message)*20, 18), frame_rate, identifier)
    all_sprites.add(black)
    decoration_sprites.add(black)

  
class Chronometer(pygame.sprite.Sprite):
    def __init__(self, time):
        super().__init__()
        self.time = time
        self.decreasing_reazon = -0.6
        
        
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 185, 176)) #(0, 0, 255)
 
        self.rect = self.image.get_rect()
        
        self.rect.x = -5
        self.rect.y = -5
            
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 600
        
    
    def time_over(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            
            self.time += self.decreasing_reazon
            
        if self.time <= 0:
            self.kill()
            return True

    def play(self):
        self.decreasing_reazon = -6


    def stop(self):
        self.decreasing_reazon = 0


def fibbonaci(total):
    place = 1
    fibo = [0, 1]
    for n in range(total):
        number = fibo[place] + fibo[place-1]
        fibo.append(number)
        place +=1   
    return fibo

