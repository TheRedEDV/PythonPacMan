import pygame, sys
from pygame.locals import * 
pygame.init()

from Player import hit_box_player, live_count

from Text import decoration

from Game_Controllers import game_controll, music

from Enemy import target_tile

Texture_pack = "Recursos/Texture_pack.png"

pl_widt = 27
pl_height = 29

long = 10 

#update

def init(all_sprites1, hit_box_sprites1, enemy_sprites1):
    global all_sprites, hit_box_sprites, enemy_sprites
    
    all_sprites = all_sprites1
    hit_box_sprites = hit_box_sprites1
    enemy_sprites = enemy_sprites1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Varianles que controlan al jugador ------------------------------------------------------------
        
        self.start_val = ["Live", 210, 435, (4, 91, 12, 13), "left", 0, False]
        
        self.mode = self.start_val[0]
        
        self.live = 3

        self.live_count = live_count.Display_Live(self)
        self.live_count.update_live()
        
        self.death_rev = self.start_val[6]
        
        self.death_sound = music.Sound("Death_Sound_pm", .6)

        # Varianles que controlan al jugador ------------------------------------------------------------
        
        
        # Sprite inicial ---------------------------------------------------------------------------
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.start_val[3]))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (pl_height, pl_height)) #14 = 12, 13 = 11
        
        # Sprite inicial ---------------------------------------------------------------------------
        
        
        # Obteniendo coordenadas -------------------------------------------------------------------
        
        self.rect = self.image.get_rect()
        self.rect.x = self.start_val[1] # -35
        self.rect.y = self.start_val[2] # -36
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.speed = 2
        
        # Obteniendo coordenadas -------------------------------------------------------------------
        
        
        # States -----------------------------------------------------------------------------------
        
        self.animation_x = True
        self.animation_y = True
        
        self.up =    True 
        self.up_states =    ((76, 92, 13, 12), (143, 92, 13, 12), (76, 92, 13, 12), (93, 92, 13, 12))
        
        self.left =  True
        self.left_states =  ((46, 91, 12, 13), (4, 91, 12, 13), (46, 91, 12, 13), (60, 91, 12, 13))
        
        self.down =  True
        self.down_states =  ((110, 92, 13, 12), (143, 92, 13, 12), (110, 92, 13, 12), (127, 95, 13, 12))
        
        self.right = True
        self.right_states = ((18, 91, 12, 13), (4, 91, 12, 13), (18, 91, 12, 13), (32, 91, 12, 13))
        
        self.direction = self.save_direction = self.start_val[4]
        
        # States -----------------------------------------------------------------------------------
        
        
        # Generando hit_box ------------------------------------------------------------------------
        
        self.Generate_hit_box()
        
        # Generando hit_box ------------------------------------------------------------------------

        
        # Animation --------------------------------------------------------------------------------

        self.frame = self.start_val[5]       
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        
        # Animation --------------------------------------------------------------------------------


    def Generate_hit_box(self):
        central_box = hit_box_player.central_hit_box(self, pl_height, pl_height/2, "x")
        all_sprites.add(central_box)
        hit_box_sprites.add(central_box)
        
        central_box = hit_box_player.central_hit_box(self, pl_height/2, pl_height, "y")
        all_sprites.add(central_box)
        hit_box_sprites.add(central_box)
        
        lateral_box = hit_box_player.lateral_hit_box(self, pl_height, long, "up")
        all_sprites.add(lateral_box)
        hit_box_sprites.add(lateral_box)
        
        lateral_box = hit_box_player.lateral_hit_box(self, pl_height, long, "down")
        all_sprites.add(lateral_box)
        hit_box_sprites.add(lateral_box)
        
        lateral_box = hit_box_player.lateral_hit_box(self, long, pl_height, "left")
        all_sprites.add(lateral_box)
        hit_box_sprites.add(lateral_box)
        
        lateral_box = hit_box_player.lateral_hit_box(self, long, pl_height, "right")
        all_sprites.add(lateral_box)
        hit_box_sprites.add(lateral_box)
        
        eat_box = hit_box_player.eat_hit_box(self)
        all_sprites.add(eat_box)
        hit_box_sprites.add(eat_box)


    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.frame += 1
            
            
            if self.frame >= 4:
                 self.frame = 0     


            if self.animation_x == True:
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))

                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))


            if self.animation_x == False:
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))

                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))


            if self.animation_y == True:
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.up_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.down_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))


            if self.animation_y == False:
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.up_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.down_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                    
            if self.direction == "?":
                self.sheet = pygame.image.load(Texture_pack).convert()
                self.sheet.set_clip(pygame.Rect(4, 91, 12, 13)) 
                
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                
                self.image = pygame.transform.scale(self.image, (pl_height, pl_height))


    def Repair_Animation(self):
        if self.speed_x != 0:
            self.animation_x = True
            
        if self.speed_y != 0:
            self.animation_y = True
  

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.up == True:
                    self.direction = "up"
                    self.save_direction = "up"

                if self.up == False:
                    self.save_direction = "up"
                
                
            elif event.key == pygame.K_a:
                if self.left == True:
                    self.direction = "left"
                    self.save_direction = "left"
                    
                if self.left == False:
                    self.save_direction = "left"
                    
                
            elif event.key == pygame.K_s:
                if self.down == True:
                    self.direction = "down"
                    self.save_direction = "down"
   
                if self.down == False:
                    self.save_direction = "down"
                
                
            elif event.key == pygame.K_d:
                if self.right == True:
                    self.direction = "right"
                    self.save_direction = "right"

                if self.right == False:
                    self.save_direction = "right"
                    
            # elif event.key == 93:
                # self.live += 1
                # self.live_count.update_live()
                
            # elif event.key == 47:
                # self.live -= 1
                # self.live_count.update_live()
                
            # elif event.key == pygame.K_p:
                        # print("x: ", self.rect.x, "Y: ", self.rect.y)
                        # print("top: ", self.rect.top, 
                              # "left: ", self.rect.left,
                              # "bottom: ", self.rect.bottom,
                              # "right: ", self.rect.right)



    def Change_direction(self):
        if self.direction == "up":
            self.Block_speed_x()
            self.speed_y = (self.speed*-1)
            
            
        if self.direction == "left":
            self.Block_speed_y()
            self.speed_x = (self.speed*-1)
            
            
        if self.direction == "down":
            self.Block_speed_x()
            self.speed_y = self.speed
            
            
        if self.direction == "right":
            self.Block_speed_y()
            self.speed_x = self.speed
            
        if self.direction == "?":
            self.Block_speed_x()
            self.Block_speed_y()
            
        #print(self.speed_x, "x", self.speed_y, "y", self.speed, "speed")


    def Block_speed_x(self):
        if self.speed_x < 0:
            self.speed_x += self.speed
                
        if self.speed_x > 0:
            self.speed_x += (self.speed*-1)


    def Block_speed_y(self):
        if self.speed_y < 0:
            self.speed_y += self.speed
                
        if self.speed_y > 0:
            self.speed_y += (self.speed*-1)


    def Teleport(self):
        if self.rect.x < -55:
            self.rect.x = 435

        if self.rect.x > 445:
            self.rect.x = -45

    
    def Play(self):
        self.speed = 100
        self.frame_rate = 50

 
    def Stop(self):
        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.frame_rate = 60000


    def Live(self, delta_time):
        self.Change_direction()
    
        self.rect.x += round(self.speed_x*delta_time, 0)
        self.rect.y += round(self.speed_y*delta_time, 0)

        self.Animation()
        
        self.Teleport()
        
        self.Repair_Animation()

    def Dead(self):
        if not self.death_rev:
            all_sprites.add(live_count.Dead_Explosion(self))
            self.death_sound.play()
            self.death_rev = True
            
        self.rect.x, self.rect.y = 250, 595


    def Reset(self):
        #["Live", 210, 435, (4, 91, 12, 13), "left", 0]
        
        self.mode = self.start_val[0]
        
        self.rect.x, self.rect.y = self.start_val[1], self.start_val[2]
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.start_val[3]))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (pl_height, pl_height))
        
        self.direction = self.save_direction = self.start_val[4]
        
        self.frame = self.start_val[5]
        
        self.death_rev = self.start_val[6]


    def Control_mode(self, delta_time):
        if self.mode == "Live":
            self.Live(delta_time)
            
        if self.mode == "Dead":
            self.Dead()


    def update(self, delta_time):
        self.Control_mode(delta_time)
