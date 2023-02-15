import pygame, sys
from pygame.locals import *
pygame.init()

from Text import decoration

#update

def init(background_sprites1, player_sprites1, enemy_sprites1):
    global background_sprites, player_sprites, enemy_sprites
    
    background_sprites, player_sprites, enemy_sprites = background_sprites1, player_sprites1, enemy_sprites1


class central_hit_box(pygame.sprite.Sprite):
    def __init__(self, sprite_object, width, height, axis):
        super().__init__()
        self.sprite_object = sprite_object
        
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 0, 0))
        
        self.image.set_colorkey((100, 0, 0))
 
        self.rect = self.image.get_rect()
        
        self.rect.center = self.sprite_object.rect.center
        
        self.axis = axis
        

    def Movement(self):
        self.rect.center = self.sprite_object.rect.center

  
    def Collide_Wall(self):
        wall_impact = pygame.sprite.spritecollide(self, background_sprites, False)
        for wall in wall_impact:
            if self.axis == "x":
                if self.sprite_object.speed_x > 0:
                    self.sprite_object.rect.right = wall.rect.left
                    
                if self.sprite_object.speed_x < 0:
                    self.sprite_object.rect.left = wall.rect.right
                    
            if self.axis == "y":
                
                if self.sprite_object.speed_y > 0:
                    self.sprite_object.rect.bottom = wall.rect.top
                    
                if self.sprite_object.speed_y < 0:
                    self.sprite_object.rect.top = wall.rect.bottom 
                    
    def Teleport(self):
        if self.sprite_object.rect.x < -55:
            self.sprite_object.rect.x = 435

        if self.sprite_object.rect.x > 445:
            self.sprite_object.rect.x = -45


    def update(self, delta_time):
        self.Teleport()
        self.Movement()
        self.Collide_Wall()


class lateral_hit_box(pygame.sprite.Sprite):
    def __init__(self, sprite_object, width, height, direction):
        self.direction = direction
        super().__init__()
        
        self.sprite_object = sprite_object
        self.width = width
        self.height = height
        self.direction = direction
 
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 100, 0)) #(255, 0, 0)
        
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey((0, 100, 0))

    def redirection_n_restriction(self):
        if self.direction == "up":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.up = False
                
            else:
                self.sprite_object.up = True
    
    
        if self.direction == "left":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.left = False
                
            else:
                self.sprite_object.left = True


        if self.direction == "down":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.down = False
                
            else:
                self.sprite_object.down = True

          
        if self.direction == "right":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.right = False
                
            else:
                self.sprite_object.right = True


    def update(self, delta_time):
        if self.direction == "up":
            self.rect.x = self.sprite_object.rect.x
            self.rect.y = self.sprite_object.rect.y +self.height*-1
        
        if self.direction == "left":
            self.rect.x = self.sprite_object.rect.x +self.width*-1
            self.rect.y = self.sprite_object.rect.y 
            
        if self.direction == "down":
            self.rect.x = self.sprite_object.rect.x
            self.rect.y = self.sprite_object.rect.y +self.width

        if self.direction == "right":
            self.rect.x = self.sprite_object.rect.x +self.height
            self.rect.y = self.sprite_object.rect.y
            
        self.redirection_n_restriction() 


# class kill_hit_box(pygame.sprite.Sprite):
    # def __init__(self, sprite_object):
        # super().__init__()
        
        # self.sprite_object = sprite_object
        
        # self.image = pygame.Surface((1, 1))
        # self.image.fill((100, 0, 0))
        
        # self.image.set_colorkey((100, 0, 0))
 
        # self.rect = self.image.get_rect()

        # self.stress_time = decoration.Chronometer(2)
        # self.stop = False
       


    # def Kill_Player(self):
        # if self.sprite_object.stade == "Out":
            # if self.sprite_object.mode == "Normal":
                # killed_player = pygame.sprite.spritecollide(self, player_sprites, False)
                # for player in killed_player:
                    # player.Stop()
                    
                    # for enemy in enemy_sprites:
                        # enemy.Stop()
                        
                    # self.stop = True
                            
        # if self.stop:
            # if self.stress_time.time_over():
                # self.stress_time = decoration.Chronometer(2)
                
                # for player in player_sprites:
                    # player.mode = "Dead"
                    # player.live -= 1
                
                # for enemy in enemy_sprites:
                    # enemy.rect.x, enemy.rect.y = 210, 595 
                    
                # self.stop = False


    # def Position(self):
        # if self.sprite_object.direction == "up":
            # self.rect.x = self.sprite_object.rect.x+15
            # self.rect.y = self.sprite_object.rect.y+20
            
        # if self.sprite_object.direction == "left":
            # self.rect.x = self.sprite_object.rect.x+20
            # self.rect.y = self.sprite_object.rect.y+15
            
        # if self.sprite_object.direction == "down":
            # self.rect.x = self.sprite_object.rect.x+15
            # self.rect.y = self.sprite_object.rect.y+8
            
        # if self.sprite_object.direction == "right":
            # self.rect.x = self.sprite_object.rect.x+8
            # self.rect.y = self.sprite_object.rect.y+15



    # def update(self):
        # self.Position()
        # self.Kill_Player() 


class kill_hit_box(pygame.sprite.Sprite):
    def __init__(self, sprite_object, w, h, axis):
        super().__init__()
        
        self.sprite_object = sprite_object
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((100, 0, 0))
        
        self.image.set_colorkey((100, 0, 0))
 
        self.rect = self.image.get_rect()
        
        self.axis = axis

        self.stress_time = decoration.Chronometer(2)
        self.stop = False


    def Kill_Player(self):
        if self.sprite_object.stade == "Out":
            if self.sprite_object.mode == "Normal":
                killed_player = pygame.sprite.spritecollide(self, player_sprites, False)
                for player in killed_player:
                    if self.axis == "x":
                        if self.sprite_object.direction == "up" or self.sprite_object.direction == "down":
                            player.Stop()
                            
                            for enemy in enemy_sprites:
                                enemy.Stop()
                                
                            self.stop = True


                    if self.axis == "y":
                        if self.sprite_object.direction == "left" or self.sprite_object.direction == "right":
                            player.Stop()
                            
                            for enemy in enemy_sprites:
                                enemy.Stop()
                                
                            self.stop = True
                            
        if self.stop:
            if self.stress_time.time_over():
                self.stress_time = decoration.Chronometer(2)
                
                for player in player_sprites:
                    player.mode = "Dead"
                    player.live -= 1
                
                for enemy in enemy_sprites:
                    enemy.rect.x, enemy.rect.y = 210, 595 
                    
                self.stop = False


    def Position(self):
        self.rect.center = self.sprite_object.rect.center

    def update(self, delta_time):
        self.Position()
        self.Kill_Player() 

