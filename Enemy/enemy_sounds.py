import pygame, sys
from pygame.locals import *
pygame.init()

from Game_Controllers import music

from Text import decoration

#update

def init(enemy_sprites1):
    global enemy_sprites
    
    enemy_sprites = enemy_sprites1


class Enemy_Sound_Controller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
        self.sound = "Normal"
        self.play_sound_normal = True
        self.play_sound_frihgtened = True
        self.play_sound_eaten = True
        
        # Listas de los modos de los enemigos --------------------------
        
        self.all_enemy_mode = ["?", "?", "?", "?"]
        
        self.all_enemy_stop = ["?", "?", "?", "?"]
        
        # Listas de los modos de los enemigos --------------------------
        
        # Sonidos ------------------------------------------------------
        
        self.Walking_Ghost_Normal = music.Sound("Walking_Ghost", .6)
        
        self.Walking_Ghost_Eaten = music.Sound("Walking_Ghost_Eaten", .6)
        
        self.Walking_Ghost_Frightened = music.Sound("Walking_Ghost_Frightened", .6)
        
        self.time = decoration.Chronometer(60)
        
        # Sonidos ------------------------------------------------------


    def Update_Mode(self):
        for enemy in enemy_sprites:
            if enemy.target_level == 1:
                self.all_enemy_mode[0] = enemy.mode
                
            if enemy.target_level == 2:
                self.all_enemy_mode[1] = enemy.mode
                
            if enemy.target_level == 3:
                self.all_enemy_mode[2] = enemy.mode
                
            if enemy.target_level == 4:
                self.all_enemy_mode[3] = enemy.mode


    def Update_Stop(self):
        for enemy in enemy_sprites:
            if enemy.target_level == 1:
                self.all_enemy_stop[0] = enemy.stop
                
            if enemy.target_level == 2:
                self.all_enemy_stop[1] = enemy.stop
                
            if enemy.target_level == 3:
                self.all_enemy_stop[2] = enemy.stop
                
            if enemy.target_level == 4:
                self.all_enemy_stop[3] = enemy.stop

    
    def Update_List(self):
        self.Update_Mode()
        self.Update_Stop()


    def Control_Sound(self):
        if not "Frightened_1" in self.all_enemy_mode and not "Frightened_2" in self.all_enemy_mode:
            if not "Eaten" in self.all_enemy_mode:
                self.play_sound_frihgtened = True
                self.play_sound_eaten = True
                self.sound = "Normal"
            
            
            else:
                self.play_sound_normal = True
                self.play_sound_frihgtened = True
                self.sound = "Eaten"
                
        else:
            if not "Eaten" in self.all_enemy_mode:
                self.play_sound_normal = True
                self.play_sound_eaten = True
                self.sound = "Frightened"
            
            
            else:
                self.play_sound_normal = True
                self.play_sound_frihgtened = True
                self.sound = "Eaten"


    def Stop_Sound(self):
        if not True in self.all_enemy_stop:
            self.stop = False

        else:
            self.stop = True


    def Play_Sound(self):
        if self.sound == "Normal":
            if self.play_sound_normal:
                self.Walking_Ghost_Frightened.stop()
                self.Walking_Ghost_Eaten.stop()
                
                self.Walking_Ghost_Normal = music.Sound("Walking_Ghost", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Normal.play()
                    self.play_sound_normal = False
                
            if self.stop:
                self.Walking_Ghost_Normal.stop()
                self.play_sound_normal = True

                
        if self.sound == "Frightened":
            if self.play_sound_frihgtened:
                self.Walking_Ghost_Normal.stop()
                self.Walking_Ghost_Eaten.stop()
                
                self.Walking_Ghost_Frightened = music.Sound("Walking_Ghost_Frightened", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Frightened.play()
                    self.play_sound_frihgtened = False
                
            if self.stop:
                self.Walking_Ghost_Frightened.stop()
                self.play_sound_frihgtened = True

                
        if self.sound == "Eaten":
            if self.play_sound_eaten:
                self.Walking_Ghost_Frightened.stop()
                self.Walking_Ghost_Normal.stop()
                
                self.Walking_Ghost_Eaten = music.Sound("Walking_Ghost_Eaten", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Eaten.play()
                    self.play_sound_eaten = False
                
            if self.stop:
                self.Walking_Ghost_Eaten.stop()
                self.play_sound_eaten = True


    def Reset_Normal_Sound(self):
        if self.sound == "Normal":
            if not self.stop:
                if self.time.time_over():
                    self.time = decoration.Chronometer(60)
                    
                    self.Walking_Ghost_Normal.play()
                    
            if self.stop:
                self.time = decoration.Chronometer(60)
                
        else:
            self.time = decoration.Chronometer(60)


    def update(self, delta_time):
        self.Update_List()
        self.Stop_Sound()
        self.Control_Sound()
        self.Play_Sound()
        self.Reset_Normal_Sound()

