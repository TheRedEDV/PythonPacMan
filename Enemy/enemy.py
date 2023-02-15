import pygame, random, sys
from pygame.locals import *
pygame.init()

from Enemy import target_tile, hit_box_enemy

from Text import decoration

Texture_pack = "Recursos/Texture_pack.png"

en_width = 29
en_height = 29

val = 2
frame = 0
frame_rate = 120

#update 

def init(all_sprites1, enemy_sprites1, target_tile_sprites1, hit_box_sprites1, pellets_sprites1):
    global all_sprites, enemy_sprites, target_tile_sprites, hit_box_sprites, pellets_sprites
    
    all_sprites, enemy_sprites, target_tile_sprites = all_sprites1, enemy_sprites1, target_tile_sprites1
  
    hit_box_sprites, pellets_sprites = hit_box_sprites1, pellets_sprites1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color, target_level, pellet_limit):
        super().__init__()
        
        # Variables que controlan al enemigo --------------------------------------------------------
        self.start_val =  ["Inside", "Normal", x, y, True, False, False, False, "up", 6, 2]
        
        self.stade = self.start_val[0] # Estado
        self.mode = self.start_val[1] # Modo
        
        self.color = color # Color
        
        self.target_level = target_level # Nivel de el target
        
        self.pellet_limit = pellet_limit # limit de los pellets
        self.pellet_to_go = 192 - self.pellet_limit
        
        self.randnumber_x = 0 # Para las coordenas aleatorias
        self.randnumber_y = 0 # Para las coordenas aleatorias
        
        self.frightened_time = decoration.Chronometer(self.start_val[9])
        
        self.stop = False
        
        self.box = False       
        
        # Variables que controlan al enemigo --------------------------------------------------------
        
        
        # Sprite inicial ---------------------------------------------------------------------------
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(3, 125, 1, 1))
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((255, 0, 0, 1), self.color)
        self.image = pygame.transform.scale(self.image, (en_width, en_width)) #14 = 12, 13 = 11
        
        # Sprite inicial ---------------------------------------------------------------------------
        
        
        # Obteniendo coordenadas -------------------------------------------------------------------
        
        self.rect = self.image.get_rect()
        
        self.in_house_rect =  [200, 290]
        
        
        self.rect.x = self.start_val[2]
        self.rect.y = self.start_val[3]
        
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.speed = 2
        
        # Obteniendo coordenadas -------------------------------------------------------------------
        
        
        # States -----------------------------------------------------------------------------------
        
        self.up_dir = self.start_val[4]
        self.up =    True 
        self.up_states =    ((71, 125), (88, 125))
        
        self.left_dir =  self.start_val[5]
        self.left =  True
        self.left_states =  ((37, 125), (54, 125))
        
        self.down_dir =  self.start_val[6]
        self.down =  True
        self.down_states =  ((105, 125), (122, 125))
        
        self.right_dir = self.start_val[7]
        self.right = True
        self.right_states = ((3, 125), (20, 125))
        
        self.frightened_sates_1 = ((3, 197), (20, 197))
        #self.frightened_sates_2 = ((37, 197), (54, 197), (3, 197), (20, 197))
        self.frightened_sates_2 = ((37, 197), (20, 197))
        
        self.eaten_sates = ((69, 197), (88, 197), (103, 197), (120, 197))
        
        self.direction = self.start_val[8]
        
        # States -----------------------------------------------------------------------------------
        
        
        # Generando hit_box ------------------------------------------------------------------------
        
        self.Generate_hit_box()
        self.Generate_Target()
        
        self.house_target = target_tile.Target_House(210, 235, (30, 90))
        all_sprites.add(self.house_target)
        target_tile_sprites.add(self.house_target)
        
        self.target = self.target_to_follow

        # Generando hit_box ------------------------------------------------------------------------


    def Generate_hit_box(self):
        self.central_box_x = hit_box_enemy.central_hit_box(self, en_width, en_width/2, "x")
        all_sprites.add(self.central_box_x)
        hit_box_sprites.add(self.central_box_x)
        
        self.central_box_y = hit_box_enemy.central_hit_box(self, en_width/2, en_width, "y")
        all_sprites.add(self.central_box_y)
        hit_box_sprites.add(self.central_box_y)
        
        self.lateral_box_up = hit_box_enemy.lateral_hit_box(self, en_width, val, "up")
        all_sprites.add(self.lateral_box_up)
        hit_box_sprites.add(self.lateral_box_up)
        
        self.lateral_box_dowm = hit_box_enemy.lateral_hit_box(self, en_width, val, "down")
        all_sprites.add(self.lateral_box_dowm)
        hit_box_sprites.add(self.lateral_box_dowm)
        
        self.lateral_box_left = hit_box_enemy.lateral_hit_box(self, val, en_width, "left")
        all_sprites.add(self.lateral_box_left)
        hit_box_sprites.add(self.lateral_box_left)
        
        self.lateral_box_right = hit_box_enemy.lateral_hit_box(self, val, en_width, "right")
        all_sprites.add(self.lateral_box_right)
        hit_box_sprites.add(self.lateral_box_right)
        
        self.kill_box_x = hit_box_enemy.kill_hit_box(self, en_width/8, en_width/20, "x")
        all_sprites.add(self.kill_box_x)
        hit_box_sprites.add(self.kill_box_x)
        
        self.kill_box_y = hit_box_enemy.kill_hit_box(self, en_width/20, en_width/8, "y")
        all_sprites.add(self.kill_box_y)
        hit_box_sprites.add(self.kill_box_y)
        
        self.box = True


    def Generate_Target(self):
        if self.target_level == 1:
            self.target_to_follow = target_tile.Target_tile_simple(self, (350, 95))
            
        if self.target_level == 2:
            self.target_to_follow = target_tile.Target_tile_subsimple(self, (70, 95))
            
        if self.target_level == 3:
            self.target_to_follow = target_tile.Target_tile_impredecible(self, (315, 510))
            
        if self.target_level == 4:
            self.target_to_follow = target_tile.Target_tile_triangle(self, (125, 510))


        all_sprites.add(self.target_to_follow)
        target_tile_sprites.add(self.target_to_follow)


    def Destroy_hit_box(self):
        self.central_box_x.kill()
        self.central_box_y.kill()
      
        self.lateral_box_up.kill()
        self.lateral_box_left.kill()
        self.lateral_box_right.kill()
        self.lateral_box_dowm.kill()
        
        self.kill_box_x.kill()
        self.kill_box_y.kill()
        
        self.box = False


    def Animation(self):
        global frame, frame_rate
        
        if self.mode == "Normal":

            if self.direction == "up":
                self.sheet.set_clip(pygame.Rect(self.up_states[frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
                
            if self.direction == "left":
                self.sheet.set_clip(pygame.Rect(self.left_states[frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
               
                
            if self.direction == "down":
                self.sheet.set_clip(pygame.Rect(self.down_states[frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())


            if self.direction == "right":
                self.sheet.set_clip(pygame.Rect(self.right_states[frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
                
            self.image.set_colorkey((0, 0, 0))
            self.image_pixel_array = pygame.PixelArray(self.image)
            self.image_pixel_array.replace((255, 0, 0, 1), self.color)
            self.image = pygame.transform.scale(self.image, (en_width, en_height))


        if self.mode == "Frightened_1":
            if frame >= 1:
                self.randnumber_x = random.randint(0, 700)
                self.randnumber_y = random.randint(0, 700)

            self.sheet.set_clip(pygame.Rect(self.frightened_sates_1[frame]+(14, 13)))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (en_width, en_height))


        if self.mode == "Frightened_2":
            if frame >= 1:
                self.randnumber_x = random.randint(0, 700)
                self.randnumber_y = random.randint(0, 700)
        
            self.sheet.set_clip(pygame.Rect(self.frightened_sates_2[frame]+(14, 13)))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (en_width, en_height))


        if self.mode == "Eaten":
        
            if self.direction == "up":
                self.sheet.set_clip(pygame.Rect(self.eaten_sates[2]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
            if self.direction == "left":
                self.sheet.set_clip(pygame.Rect(self.eaten_sates[1]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
            if self.direction == "down":
                self.sheet.set_clip(pygame.Rect(self.eaten_sates[3]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
            if self.direction == "right":
                self.sheet.set_clip(pygame.Rect(self.eaten_sates[0]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())

            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (en_width, en_height))
    
    
    def Change_180_degrees(self):
        if self.direction == "up":
            if self.up:
                if self.up_dir:
                    self.up_dir = False
                    self.down_dir = True
                    self.direction = "down"

        elif self.direction == "down":
            if self.down:
                if self.down_dir:
                    self.down_dir = False
                    self.up_dir = True
                    self.direction = "up"
                    
        elif self.direction == "left":
            if self.left:
                if self.left_dir:
                    self.left_dir = False
                    self.right_dir = True
                    self.direction = "right"
                    
        elif self.direction == "right":
            if self.right:
                if self.right_dir:
                    self.right_dir = False
                    self.left_dir = True
                    self.direction = "left"


    def Random_Movement(self):
        if self.randnumber_x < self.rect.x: # Movimiento en eje x ------------------
            if self.left_dir:
                if self.left:
                    self.direction = "left"

        if self.randnumber_x > self.rect.x:
            if self.right_dir:
                if self.right:
                    self.direction = "right"

        if self.randnumber_y < self.rect.y: # Movimiento en eje y ------------------
            if self.up_dir:
                if self.up:
                    self.direction = "up"

        if self.randnumber_y > self.rect.y:
            if self.down_dir:
                if self.down:
                    self.direction = "down"

        self.Correct_Movement()


    def Follow_Target(self):
        if self.target.rect.x > self.rect.x: # Movimiento en eje x ------------------
            if self.right_dir:
                if self.right:
                    self.direction = "right"
                    
        if self.target.rect.y > self.rect.y: # Movimiento en eje y ------------------
            if self.down_dir:
                if self.down:
                    self.direction = "down"
                    
        if self.target.rect.x < self.rect.x: # Movimiento en eje x ------------------
            if self.left_dir:
                if self.left:
                    self.direction = "left"
                    
        if self.target.rect.y < self.rect.y: # Movimiento en eje y ------------------
            if self.up_dir:
                if self.up:
                    self.direction = "up"
        
        self.Correct_Movement()
 
 
    def Correct_Movement(self):
        if not self.right:
            if self.direction == "right":
                if not self.up:
                    self.direction = "down"
                    
                elif not self.down:
                    self.direction = "up" 
                    
                else:
                    self.direction = "up" 


        if not self.down:
            if self.direction == "down":
                if not self.left:
                    self.direction = "right"
                    
                elif not self.right:
                    self.direction = "left" 
                    
                else:
                    self.direction = "left"          


        if not self.left:
            if self.direction == "left":
                if not self.up:
                    self.direction = "down"
                    
                elif not self.down:
                    self.direction = "up"
                    
                else:
                    self.direction = "down"

 
        if not self.up:
            if self.direction == "up":
                if not self.left:
                    self.direction = "right"
                    
                elif not self.right:
                    self.direction = "left"
                    
                else:
                    self.direction = "right"


    def Change_direction(self):
        if self.direction == "up":
            self.Block_speed_x()
            self.speed_y = self.speed*-1
            self.down_dir = False
            
            if self.left == False and self.right == False:
                self.left_dir = True
                self.right_dir = True
                
                
        if self.direction == "down":
            self.Block_speed_x()
            self.speed_y = self.speed
            self.up_dir = False
            
            if self.left == False and self.right == False:
                self.left_dir = True
                self.right_dir = True
            
            
        if self.direction == "left":
            self.Block_speed_y()
            self.speed_x = self.speed*-1
            self.right_dir = False
            
            if self.down == False and self.up == False:
                self.up_dir = True
                self.down_dir = True
                
                
        if self.direction == "right":
            self.Block_speed_y()
            self.speed_x = self.speed
            self.left_dir = False
            
            if self.down == False and self.up == False:
                self.up_dir = True
                self.down_dir = True
                
            
        if self.direction == "?":
            self.Block_speed_x()
            self.Block_speed_y()


    def Block_speed_x(self):
        if self.speed_x < 0:
            self.speed_x += self.speed
                
        if self.speed_x > 0:
            self.speed_x += self.speed*-1


    def Block_speed_y(self):
        if self.speed_y < 0:
            self.speed_y += self.speed
                
        if self.speed_y > 0:
            self.speed_y += self.speed*-1


    def Count_Pellets(self):
        if self.pellet_limit <= 15:
            return True
            
        else:
            if len(pellets_sprites) <= self.pellet_to_go:
                return True


    def Inside(self):        
        self.left_dir = False
        self.right_dir = False
        
        if self.mode == "Eaten":
            self.target = self.target_to_follow
            self.mode = "Normal"
        
        if self.Count_Pellets(): 
            if pygame.sprite.collide_rect(self, self.house_target):
                
                self.left_dir = False
                self.right_dir = False
                self.up_dir = True
                self.down_dir = False
                
                self.direction = "up"
                
                self.stade = "Go_OUT"
                
        else: 
            if self.rect.y <= 277: # Rebote ----------------------------
                self.Change_180_degrees()


            if self.rect.y >= 293: # Rebote ----------------------------
                self.Change_180_degrees()


    def Go_OUT(self):
        if self.rect.left >= self.house_target.rect.left and self.rect.right <= self.house_target.rect.right:
            if self.direction == "up": # Salir de la casa solo si el enemigo esta en la puerta
            

                self.up_dir = True
                self.down_dir = False
                self.right_dir = False
                self.left_dir = False
                
                self.Destroy_hit_box()
                
                self.direction = "up"


            if self.direction == "left":
                if self.rect.left <= self.house_target.rect.left:
                    self.direction = "up"
                    
            if self.direction == "right":
                if self.rect.right >= self.house_target.rect.right:
                    self.direction = "up"
                    
        if self.rect.y <= 236:
            self.Generate_hit_box()

            self.up_dir = False
            self.down_dir = False
            self.right_dir = False
            self.left_dir = True
            self.direction = "left"
            
            self.stade = "Out"


    def Out(self):
        if self.mode == "Eaten":
            self.stade = "Go_INSIDE"


    def Go_INSIDE(self):
        self.target = self.house_target
        if pygame.sprite.collide_rect(self, self.house_target):
            if self.direction == "left":
                if self.rect.left <= self.house_target.rect.left:
                    self.rect.x = self.in_house_rect[0]
                    self.rect.y = self.in_house_rect[1]
                    
                    self.left_dir =  False
                    self.right_dir = False
                    self.up_dir =    True
                    self.down_dir =  False
                    
                    self.direction =  "up"
                    
                    self.stade =  "Inside"
                    
            if self.direction == "right":
                if self.rect.right >= self.house_target.rect.right:
                    self.rect.x = self.in_house_rect[0]
                    self.rect.y = self.in_house_rect[1]
                    
                    self.left_dir =  False
                    self.right_dir = False
                    self.up_dir =    True
                    self.down_dir =  False
                    
                    self.direction =  "up"
                    
                    self.stade =  "Inside"


    def Stade_Control(self):
        if self.stade == "Inside":
            self.Inside()
            
        if self.stade == "Go_OUT":
            self.Go_OUT()
            
        if self.stade == "Out":
            self.Out()
            
        if self.stade == "Go_INSIDE":
            self.Go_INSIDE()


    def Mode_Control(self):
        if self.mode == "Normal":
            self.Follow_Target()
            self.frightened_time = decoration.Chronometer(self.start_val[9])
            
        if self.mode == "Frightened_1":
            self.Random_Movement()
            if not self.stop:
                if self.frightened_time.time_over():
                    self.frightened_time.kill()
                    self.frightened_time = decoration.Chronometer(self.start_val[10])
                    self.mode = "Frightened_2"
                
        if self.mode == "Frightened_2":
            self.Random_Movement()
            if not self.stop:
                if self.frightened_time.time_over():
                    self.frightened_time.kill()
                    self.frightened_time = decoration.Chronometer(self.start_val[9])
                    self.mode = "Normal"
            
        if self.mode == "Eaten":
            self.Follow_Target()


    def Control_Speed(self):
        if not self.stop:
    
            if self.stade == "Inside" or self.stade == "Go_OUT":
                self.speed = 60


            if self.stade == "Out":
                if self.mode == "Normal":
                    self.speed = 120


                if self.mode == "Frightened_1" or self.mode == "Frightened_2":
                    self.speed = 60


            if self.stade == "Go_INSIDE":
                self.speed = 240


        if self.stop:
            self.speed = 0
            self.speed_x = 0
            self.speed_y = 0


    def Stop(self):
        self.stop = True


    def Play(self):
        self.stop = False

    
    def Reset(self):
        #["Inside", "Normal", x, y, True, False, False, False, "up", 6?, 2?]
        if not self.box:
            self.Generate_hit_box() # Evitar errores de generacion
        
        self.pellet_to_go = len(pellets_sprites) - self.pellet_limit
        
        
        self.stade = self.start_val[0] # Resetear todos los valores a los iniciales ----------------------------
        
        self.mode = self.start_val[1]
        
        self.rect.x, self.rect.y = self.start_val[2], self.start_val[3]
        
        self.up_dir = self.start_val[4]
        self.left_dir = self.start_val[5]
        self.down_dir = self.start_val[6]
        self.right_dir = self.start_val[7]
        self.direction = self.start_val[8]
        
        self.frightened_time = decoration.Chronometer(self.start_val[9]) # Resetear todos los valores a los iniciales -----------
        
        self.target = self.target_to_follow

        target_tile.RESET() # Resetear a el target_tile


    def update(self, delta_time):
        self.Stade_Control()
        self.Mode_Control()
            
        self.Change_direction()
        
        self.Control_Speed()
        self.rect.x += round(self.speed_x*delta_time, 0)
        self.rect.y += round(self.speed_y*delta_time, 0)
        
        self.Animation()


class Frame_control(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

        self.last_update = pygame.time.get_ticks()
        
    def Animation(self):
        global frame
        global frame_rate
    
        now = pygame.time.get_ticks()
        if now - self.last_update > frame_rate:    
            self.last_update = now
            frame += 1
            
            if frame >= 2:
                frame = 0
            
            
    def update(self, delta_time):
        self.Animation()


def Play_Frame():
    global frame_rate
    
    frame_rate = 120


def Stop_Frame():
    global frame_rate, frame
    
    frame, frame_rate = 0, 60000
    

