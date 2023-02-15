import pygame, sys
from pygame.locals import * 
pygame.init()

from Text import score, decoration

from Enemy import enemy

from Background import pellets

from Game_Controllers import music

point_displayer = pygame.sprite.Group()

#update

def init(all_sprites1, background_sprites1, pellets_sprites1, enemy_sprites1, fruit_sprites1):
    global all_sprites, background_sprites, pellets_sprites, enemy_sprites, fruit_sprites
    
    all_sprites = all_sprites1
    background_sprites = background_sprites1
    pellets_sprites = pellets_sprites1
    enemy_sprites = enemy_sprites1
    fruit_sprites = fruit_sprites1


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
                    
                self.sprite_object.animation_x = False
                    
            if self.axis == "y":
                
                if self.sprite_object.speed_y > 0:
                    self.sprite_object.rect.bottom = wall.rect.top
                    
                if self.sprite_object.speed_y < 0:
                    self.sprite_object.rect.top = wall.rect.bottom 

                self.sprite_object.animation_y = False


    def update(self, delta_time):
        self.Movement()
        self.Collide_Wall()


class lateral_hit_box(pygame.sprite.Sprite):
    def __init__(self, sprite_object, width, height, direction):
        super().__init__()
    
        self.sprite_object = sprite_object
        self.width = width
        self.height = height
        self.direction = direction

        self.image = pygame.Surface([width, height])
        self.image.fill((0, 100, 0)) #(255, 0, 0)
        
        self.image.set_colorkey((0, 100, 0))
        
        self.rect = self.image.get_rect()


    def redirection_n_restriction(self):
        if self.direction == "up":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.up = False
                
            else:
                self.sprite_object.up = True
                if self.sprite_object.save_direction == "up":
                    if self.sprite_object.save_direction != self.sprite_object.direction:
                    
                        self.sprite_object.direction = self.sprite_object.save_direction
    
    
        if self.direction == "left":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.left = False
                
            else:
                self.sprite_object.left = True
                if self.sprite_object.save_direction == "left":
                    if self.sprite_object.save_direction != self.sprite_object.direction:
                        self.sprite_object.direction = self.sprite_object.save_direction


        if self.direction == "down":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.down = False
                
            else:
                self.sprite_object.down = True
                if self.sprite_object.save_direction == "down":
                    if self.sprite_object.save_direction != self.sprite_object.direction:
                    
                        self.sprite_object.direction = self.sprite_object.save_direction

          
        if self.direction == "right":
            if pygame.sprite.spritecollide(self, background_sprites, False):
                self.sprite_object.right = False
                
            else:
                self.sprite_object.right = True
                if self.sprite_object.save_direction == "right":
                    if self.sprite_object.save_direction != self.sprite_object.direction:
                    
                        self.sprite_object.direction = self.sprite_object.save_direction


    def update(self, delta_time):
        if self.direction == "up":
            self.rect.x = self.sprite_object.rect.x
            self.rect.y = self.sprite_object.rect.y  +self.height*-1
        
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

 
class eat_hit_box(pygame.sprite.Sprite):
    def __init__(self, sprite_object):
        super().__init__()
        self.sprite_object = sprite_object
        
        self.image = pygame.Surface((2, 2))
        self.image.fill((0, 150, 0))
        
        self.image.set_colorkey((0, 150, 0))
 
        self.rect = self.image.get_rect()
        self.rect.center = self.sprite_object.rect.center
        
        self.eat_points = [200, 400, 800, 1600]
        self.eat_pos = 0
        
        self.stop_time = False
        
        self.pause_time = decoration.Chronometer(1)
        self.time = decoration.Chronometer(1)
        self.eat_a_fruit = False
        
        self.pellet_sound = 1
        
        self.eat_pellet_sound_1 = music.Sound("Eat_Sound_1", .6)
        self.eat_pellet_sound_2 = music.Sound("Eat_Sound_2", .6)
        self.eat_ghost_sound = music.Sound("Eat_Sound_ghost", 6)
        self.eat_a_fruit_sound = music.Sound("Eat_A_Fruit_Sound", 1)


    def Eat_Pellets(self):
        if self.sprite_object.speed != 0:
            pellet_list = pygame.sprite.spritecollide(self, pellets_sprites, True)
            for pellet in pellet_list:
                if self.pellet_sound == 1:
                    self.eat_pellet_sound_1.play()
                    self.eat_pellet_sound_2.stop()
                   
                if self.pellet_sound == -1:
                    self.eat_pellet_sound_2.play()
                    self.eat_pellet_sound_1.stop()
            
                score.update_score(pellet.score)

                if isinstance(pellet, pellets.Super_Pellet):
                    for enemy in enemy_sprites:
                        self.eat_pos = 0
                        if enemy.mode == "Frightened_1" or enemy.mode == "Frightened_2":
                            enemy.frightened_time = decoration.Chronometer(enemy.start_val[9])
                            enemy.mode = "Frightened_1"

                        if enemy.mode == "Normal":
                            enemy.mode = "Frightened_1"

                        if enemy.stade == "Out":
                            enemy.Change_180_degrees()

                self.pellet_sound *= -1


    def Eat_Enemy(self):
        Eaten_Enemy = pygame.sprite.spritecollide(self, enemy_sprites, False)
        for enemy_eaten in Eaten_Enemy:
            if enemy_eaten.mode == "Frightened_1" or enemy_eaten.mode == "Frightened_2":
            
                self.eat_ghost_sound.play() # Reproducir el sonido ------------------------------------------------
                
                enemy_eaten.mode = "Eaten" 
                
                self.point_display = decoration.Points(str(self.eat_points[self.eat_pos]), enemy_eaten.rect.center, 2)
                all_sprites.add(self.point_display)
                point_displayer.add(self.point_display)
                
                score.update_score(self.eat_points[self.eat_pos]) # Mostrando los puntos ganados ------------------
                self.eat_pos += 1
                
                self.sprite_object.Stop() # Parando a los sprites y rellenando de negro al jugador ----------------
                self.sprite_object.image.fill((0, 0, 0))

                for enemy in enemy_sprites:
                    enemy.Stop()
                    
                self.stop_time = True


        if self.stop_time == True:
            if self.pause_time.time_over(): # Quitando las pausa
                self.pause_time.kill()
                self.pause_time = decoration.Chronometer(1)
                self.sprite_object.Play()
                
                for point in point_displayer:
                    if point.symbol < 5:
                        point.kill()
                
                for enemy in enemy_sprites:
                    enemy.Play()
                
                self.stop_time = False


    def Eat_Bonus_Fruit(self):
        eaten_bonus = pygame.sprite.spritecollide(self, fruit_sprites, False)
        for eat in eaten_bonus:
            self.eat_a_fruit_sound.play()
            score.update_score(eat.score)
            
            self.fruit_point_display = decoration.Points(str(eat.score), (225, 350))
            all_sprites.add(self.fruit_point_display)
            
            eat.kill()
            self.eat_a_fruit = True
            
        if self.eat_a_fruit:
            if self.time.time_over():
                self.time = decoration.Chronometer(2)
                self.fruit_point_display.kill()
                self.eat_a_fruit = False


    def Control_Eat(self):
        self.Eat_Enemy()
        self.Eat_Pellets()
        self.Eat_Bonus_Fruit()
   
   
    def update(self, delta_time):
        self.Control_Eat()
        
        self.rect.center = self.sprite_object.rect.center


