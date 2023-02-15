import pygame, sys, colorama
from pygame.locals import * 
pygame.init()
colorama.init()

from Text import decoration

target_mode = "Scatter"
time_to_change = decoration.Chronometer(4.2)

#update

def init(all_sprites1, player_sprites1, enemy_sprites1, target_tile_sprites1):
    global all_sprites, player_sprites, enemy_sprites, target_tile_sprites

    all_sprites, player_sprites, enemy_sprites, target_tile_sprites = all_sprites1, player_sprites1, enemy_sprites1, target_tile_sprites1


def RESET():
    global target_mode, time_to_change
    target_mode = "Scatter"
    
    time_to_change = decoration.Chronometer(4.2)
    

class Target_tile(pygame.sprite.Sprite):
    def __init__(self, sprite_object, scatter_xy, color):
        super().__init__()
        self.sprite_object = sprite_object
        
        self.color = color
        self.image = pygame.Surface((10, 10))
        self.image.fill(self.color)
        
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = 465
        self.rect.y = 60
        
        for player in player_sprites:
            self.player = player

        self.scatter_xy = scatter_xy
        
        self.all_enemy_mode = ["?", "?", "?", "?"]
        self.all_enemy_stop = ["?", "?", "?", "?"]


    def Scatter(self): 
        self.rect.x = self.scatter_xy[0]
        self.rect.y = self.scatter_xy[1]


    def Chase(self):
        pass


    def Update_enemy_mode(self):
        for enemy in enemy_sprites:
            if enemy.target_level == 1:
                self.all_enemy_mode[0] = enemy.mode
                
            if enemy.target_level == 2:
                self.all_enemy_mode[1] = enemy.mode
                
            if enemy.target_level == 3:
                self.all_enemy_mode[2] = enemy.mode
                
            if enemy.target_level == 4:
                self.all_enemy_mode[3] = enemy.mode


    def Update_enemy_stop(self):
        for enemy in enemy_sprites:
            if enemy.target_level == 1:
                self.all_enemy_stop[0] = enemy.stop
                
            if enemy.target_level == 2:
                self.all_enemy_stop[1] = enemy.stop
                
            if enemy.target_level == 3:
                self.all_enemy_stop[2] = enemy.stop
                
            if enemy.target_level == 4:
                self.all_enemy_stop[3] = enemy.stop

    
    def Control_Mode(self):
        global target_mode, time_to_change
        
        if target_mode == "Scatter":
            self.Scatter()
            
            if not True in self.all_enemy_stop:
                if not "Frightened_1" in self.all_enemy_mode:
                    if not "Frightened_2" in self.all_enemy_mode:
                        self.image.fill(self.color)
                        if time_to_change.time_over():
                            time_to_change.kill()
                            
                            for enemy in enemy_sprites:
                                if enemy.stade == "Out":
                                    if not enemy.stop:
                                        enemy.Change_180_degrees()
                                
                            time_to_change = decoration.Chronometer(12)
                            target_mode = "Chase"
                else:
                    pass
                    #self.image.fill((255, 255, 255))
            
            else:
                pass
                #self.image.fill((255, 255, 255))


        if target_mode == "Chase":
            self.Chase()
            
            if not True in self.all_enemy_stop:
                if not "Frightened_1" in self.all_enemy_mode:
                    if not "Frightened_2" in self.all_enemy_mode:
                        self.image.fill(self.color)
                        if time_to_change.time_over():
                            time_to_change.kill()
                            
                            for enemy in enemy_sprites:
                                if enemy.stade == "Out":
                                    if not enemy.stop:
                                        enemy.Change_180_degrees()
                                
                            time_to_change = decoration.Chronometer(4.2)
                            target_mode = "Scatter"
                else:
                    pass
                    #self.image.fill((255, 255, 255))
                            
            else:
                pass
                #self.image.fill((255, 255, 255))

 
    def update(self, delta_time):
        self.Update_enemy_mode()
        self.Update_enemy_stop()
        self.Control_Mode()


class Target_help(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        
        
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        
        for player in player_sprites:
            self.player = player
            
    def Follow_player(self):
        if self.player.direction == "up": 
            self.rect.x = self.player.rect.x - 28
            self.rect.y = self.player.rect.y - 28
            
        if self.player.direction == "down":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + 28
            
        if self.player.direction == "left":
            self.rect.x = self.player.rect.x - 28
            self.rect.y = self.player.rect.y 
            
        if self.player.direction == "right":
            self.rect.x = self.player.rect.x + 28
            self.rect.y = self.player.rect.y
            
    def update(self, delta_time):
        self.Follow_player()


class Target_House(pygame.sprite.Sprite):
    def __init__(self, x, y, geometry, color=(255, 255, 255), color_key=True):
        super().__init__()
        
        self.image = pygame.Surface(geometry)
        self.image.fill(color)
        
        if color_key:
            self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y


class Target_tile_simple(Target_tile):
    def __init__(self, sprite_object, scatter_xy):
        Target_tile.__init__(self, sprite_object, scatter_xy, (255, 0, 0))
        
    def Chase(self):
        self.rect.center = self.player.rect.center


class Target_tile_subsimple(Target_tile):
    def __init__(self, sprite_object, scatter_xy):
        Target_tile.__init__(self, sprite_object, scatter_xy, (250, 180, 250, 1))
        
    def Chase(self):
        if self.player.direction == "up": 
            self.rect.x = self.player.rect.x - 56
            self.rect.y = self.player.rect.y - 56
            
        if self.player.direction == "down":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + 56
            
        if self.player.direction == "left":
            self.rect.x = self.player.rect.x - 56
            self.rect.y = self.player.rect.y 
            
        if self.player.direction == "right":
            self.rect.x = self.player.rect.x + 56
            self.rect.y = self.player.rect.y 


class Target_tile_impredecible(Target_tile):
    def __init__(self, sprite_object, scatter_xy):
        Target_tile.__init__(self, sprite_object, scatter_xy, (1, 255, 255, 1))
        
        self.target_helper = Target_help()
        all_sprites.add(self.target_helper)
        target_tile_sprites.add(self.target_helper)
        
        for enemy  in enemy_sprites:
            if enemy.target_level == 1:
                self.enemy = enemy


    def Chase(self):
        self.rect.x = self.target_helper.rect.x + (self.target_helper.rect.x - self.enemy.rect.x)
        self.rect.y = self.target_helper.rect.y + (self.target_helper.rect.y - self.enemy.rect.y)


class Target_tile_triangle(Target_tile):
    def __init__(self, sprite_object, scatter_xy):
        Target_tile.__init__(self, sprite_object, scatter_xy, (250, 190, 90, 1))
        self.scatter_xy = scatter_xy

        for player in player_sprites:
            self.player = player

    def Chase(self):
        if get_distance(self.sprite_object, self.player) <= 112:
            self.rect.x, self.rect.y = self.scatter_xy[0], self.scatter_xy[1]
            
        else:
            self.rect.center = self.player.rect.center


def get_distance(sprite_object_1, sprite_object_2, rev=False):
    if not rev:
        adjecent_cathetus = sprite_object_1.rect.x - sprite_object_2.rect.x
        opposite_cathetus = sprite_object_1.rect.y - sprite_object_2.rect.y
        
    if rev:
        adjecent_cathetus = sprite_object_1[0] - sprite_object_2.rect.x
        opposite_cathetus = sprite_object_1[1] - sprite_object_2.rect.y

    hypotenuse = ((adjecent_cathetus)**2 + (opposite_cathetus)**2)**.5
    return hypotenuse