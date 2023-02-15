import pygame, sys
from pygame.locals import * 
pygame.init()

from Game_Controllers import music

from Enemy import enemy

from Text import decoration, animation

from Background import background, pellets

from Fruit import fruit

fruit_counter_sprites = pygame.sprite.Group()

#update

def init(all_sprites1, player_sprites1, enemy_sprites1, pellets_sprites1, fruit_sprites1):
    global all_sprites, player_sprites, enemy_sprites, pellets_sprites, fruit_sprites
    
    all_sprites, player_sprites, enemy_sprites, pellets_sprites, fruit_sprites = all_sprites1, player_sprites1, enemy_sprites1, pellets_sprites1, fruit_sprites1


class Pause(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
        self.pause = False
        
        self.key_down = False
        
    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if self.pause:
                
        
                if event.key == pygame.K_p:
                    decoration.Kill_Identifier("volume")
                    if music.Get_Volume():
                        decoration.Generate_Decoration("off", 580, 286, (255, 0, 0), "volume")
                        music.Set_Volume(False)
                        
                    elif not music.Get_Volume():
                        decoration.Generate_Decoration("on", 580, 286, (1, 255, 255, 1), "volume")
                        music.Set_Volume(True)
        
            if event.key == pygame.K_RETURN:
                if not self.key_down:
                    if not self.pause:
                        for player in player_sprites:
                            if player.speed != 0:
                                for enemy_to in enemy_sprites:
                                    enemy_to.Stop()
                                    
                                enemy.Stop_Frame()
                                
                                for player in player_sprites:
                                    player.Stop()
                                    
                                decoration.Kill_Identifier("pause")
                                decoration.Generate_Decoration("press p !", 440, 244, (255, 0, 0), "pause")
                                decoration.Generate_Decoration("volume", 440, 286, (255, 255, 255), "pause")
                                
                                if music.Get_Volume():
                                    decoration.Generate_Decoration("on", 580, 286, (1, 255, 255, 1), "volume")
                                
                                if not music.Get_Volume():
                                    decoration.Generate_Decoration("off", 580, 286, (255, 0, 0), "volume")

                                decoration.Generate_Decoration("pause", 460, 330, (1, 255, 255, 1), "pause")
                                
                                self.pause_sound = music.Sound("Pause_Sound", .6, True)
                                self.pause_sound.play()
                                
                                self.pause = True
                        
                    elif self.pause:
                        for enemy_to in enemy_sprites:
                            enemy_to.Play()
                            
                        enemy.Play_Frame()
                        
                        for player in player_sprites:
                            player.Play()
                        
                        decoration.Kill_Identifier("pause")
                        decoration.Kill_Identifier("volume")
                        self.pause = False
                        
                self.key_down = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.key_down = False


class Fruit_Per_Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
        self.level = 1
        self.rev_level = False
        self.fruit_table = ["", 
                            "cherry", "strawberry",
                            "peach", "peach", 
                            "apple", "apple", 
                            "melon", "melon", 
                            "flagship", "flagship", 
                            "bell", "bell",
                            "key", "key",
                            "key", "key",
                            "key", "key",
                            "key", "key",           ]

        self.x = 440
        self.y = 360
        
        self.Controll_Display()
        
        self.appear_reazon = 134
        self.time = decoration.Chronometer(10)
        self.is_fruit = False


    def Display(self, n):
        self.fruit = fruit.Level_Fruit(self.fruit_table[n], self.x, self.y)
        all_sprites.add(self.fruit)
        fruit_counter_sprites.add(self.fruit)
        
        if self.x >= 560:
            self.x = 400
        
        if self.level < 9:
            if n >= 4:
                self.y = 400
                
        if self.level > 8 and self.level < 20:
            if n >= self.level-4:
                self.y = 400
                
        if self.level > 19:
            if n >= 16:
                self.y = 400
        
        self.x += 40


    def Controll_Display(self):
        if self.level > 19:
            for n in range(13, 21):
                self.Display(n)
                
        if self.level > 8  and self.level < 20:
            for n in range(self.level-7, self.level+1):
                self.Display(n)
                
        if self.level < 9:
            for n in range(1, self.level+1):
                self.Display(n)


    def Update_Level(self):
        if not self.rev_level:
            if len(pellets_sprites) <= 0:
                self.level += 1
                self.rev_level = True
        
        if self.rev_level:
            if len(pellets_sprites) > 10:
                self.x = 440
                self.y = 360
                self.appear_reazon = 134
                for sprite in fruit_counter_sprites:
                    sprite.kill()
                
                for sprite in fruit_sprites:
                    sprite.kill()
                self.Controll_Display()
                self.rev_level = False


    def Generate_Bonus_Fruit(self):
        if len(pellets_sprites) <= self.appear_reazon:
            if self.level < 5 or self.level > 10:
                if self.level < 20:
                    self.bonus = fruit.Bonus_Fruit(self.fruit_table[self.level], 210, 332)
                    
                else:
                    self.bonus = fruit.Bonus_Fruit(self.fruit_table[20], 210, 332)
                
            else:
                self.bonus = fruit.Bonus_Fruit(self.fruit_table[self.level], 210, 330)
            
            fruit_sprites.add(self.bonus)
            self.appear_reazon -= 82
            self.is_fruit = True


    def Kill_Bonus_Fruit(self):
        if self.is_fruit:
            for player in player_sprites:
                if player.speed != 0:
                    if self.time.time_over():
                        self.time = decoration.Chronometer(10)
                        self.bonus.kill()
                        self.is_fruit = False
                
                if player.mode == "Dead":
                    self.time = decoration.Chronometer(10)
                    self.bonus.kill()
                    self.is_fruit = False
    

    def update(self, delta_time):
        self.Generate_Bonus_Fruit()
        self.Kill_Bonus_Fruit()
        self.Update_Level()


class Intro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.theme_Game = music.Sound("Theme_Game", .6)
        self.theme_Game.play()

        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.time = decoration.Chronometer(2)
        
        self.mode = "Gen_player/ready"


    def Mode_Control(self):
        if self.mode == "Gen_player/ready":
            decoration.Generate_Decoration("player", 165, 242, (1, 255, 255, 1), "player")
            decoration.Generate_Decoration("ready!", 165, 342, (255, 247, 0, 1), "ready!")
            self.mode = "player"
            
            for enemy_to in enemy_sprites: # Enemigos en la casa secreta --------------------------
                enemy_to.Stop()
                enemy_to.rect.x, enemy_to.rect.y = 210, 595
                    
            for player in player_sprites:
                player.Stop()
                player.rect.x, player.rect.y = 250, 595 # Jugador en la casa secreta --------------


        if self.mode == "player":
            if self.time.time_over():
                self.time = decoration.Chronometer(2)
                decoration.Kill_Identifier("player")
                self.mode = "ready!"
                
                for enemy_to in enemy_sprites: # Enemigos en el escenario --------------------------
                    enemy_to.Reset()
                    
                for player in player_sprites:
                    player.Reset()             # Jugador en el escenario ---------------------------
                    
                enemy.Stop_Frame()
                
        if self.mode == "ready!":
            if self.time.time_over():
                enemy.Play_Frame()
                decoration.Kill_Identifier("ready!")

                decoration.Generate_Decoration("press", 440, 244, (255, 0, 0), "pause")
                #decoration.Generate_Decoration("      key", 440, 286, (255, 0, 0), "pause")
                decoration.Generate_Decoration("enter!", 440, 286, (255, 255, 255), "pause")
            
                for enemy_to in enemy_sprites: # Todo se mueve -------------------------------------
                    enemy_to.Play()
                    
                for player in player_sprites: 
                    player.Play()              # Todo se mueve -------------------------------------
                    
                    
                enemy.Play_Frame()
                    
                self.kill()


    def update(self, delta_time):
        self.Mode_Control()


class Dead_Reset(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.mode = "pac_man_death"
        self.state = False
        
        for player in player_sprites:
            self.player = player

        self.time = decoration.Chronometer(2)


    def Stade_Controll(self):
        if self.player.mode == "Dead":
            if self.player.live > 0:
                self.state = True


    def Mode_Control(self):
        if self.state:
            if self.mode == "pac_man_death":
                if self.time.time_over():
                    self.time = decoration.Chronometer(2)
                    self.mode = "Generate_text"
                    
            if self.mode == "Generate_text":
                enemy.Stop_Frame()
                
                for enemy_to in enemy_sprites:
                    enemy_to.Reset()
                    
                for player in player_sprites:
                    player.Reset()
                    player.live_count.update_live()
            
                decoration.Generate_Decoration("ready!", 165, 342, (255, 247, 0, 1), "dead_reset")
                self.mode = "ready!"
                
            if self.mode == "ready!":
                if self.time.time_over():
                    self.time = decoration.Chronometer(2)
                    enemy.Play_Frame()
                    decoration.Kill_Identifier("dead_reset")
                
                    for enemy_to in enemy_sprites:
                        enemy_to.Play()
                        
                    for player in player_sprites:
                        player.Play()
                    
                    self.mode = "pac_man_death"
                    self.state = False


    def update(self, delta_time):
        self.Stade_Controll()
        self.Mode_Control()


class Pellet_Reset(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.mode = "stop_player"
        self.state = False
        
        self.level = 1
        
        self.coffe_break = 9
        
        self.color_list = [(255, 0, 0, 1), (250, 180, 250, 1), (1, 255, 255, 1), (250, 190, 90, 1)]
        self.color_pos = 2
        
        for player in player_sprites:
            self.player = player

        self.time = decoration.Chronometer(2)


    def Stade_Controll(self):
        if len(pellets_sprites) <= 0:
            self.state = True

 
    def Mode_Control(self):
        if self.state:
            if self.mode == "stop_player":
                self.player.Stop()
                
                for enemy_to in enemy_sprites:
                    enemy_to.Stop()
                    
                enemy.Stop_Frame()
                
                self.mode = "wait"


            if self.mode == "wait":
                if self.time.time_over():
                    self.time = decoration.Chronometer(2)
                    
                    for enemy_to in enemy_sprites:
                        enemy_to.Stop()
                        enemy_to.rect.x, enemy_to.rect.y = 210, 595
                        
                    self.mode = "fliker"
                    
                    self.fliker_walls = background.Flicker_Bacground(20, 45)
                    all_sprites.add(self.fliker_walls)

 
            if self.mode == "fliker":
                if self.time.time_over():
                    self.fliker_walls.kill()
                    
                    if self.level == 2:
                        self.time = decoration.Chronometer(10)
                        self.coffe_break_1 = Coffe_Break_1()
                        all_sprites.add(self.coffe_break_1)
                        self.coffe_break_1.Generate_Animation()

                    if self.level == 5:
                        self.time = decoration.Chronometer(10)
                        self.coffe_break_1 = Coffe_Break_3(self.color_list[1])
                        all_sprites.add(self.coffe_break_1)
                        self.coffe_break_1.Generate_Animation()
                        
                    if self.level == self.coffe_break:
                        if self.color_pos > 3:
                            self.color_pos = 0
                    
                        self.time = decoration.Chronometer(10)
                        self.coffe_break_1 = Coffe_Break_3(self.color_list[self.color_pos])
                        all_sprites.add(self.coffe_break_1)
                        self.coffe_break_1.Generate_Animation()
                        
                        self.coffe_break += 4
                        self.color_pos += 1
                    
                    self.mode = "coffe_break"


            if self.mode == "coffe_break":
                if self.time.time_over():
                    self.time = decoration.Chronometer(2)
                    self.mode = "Generate_text"


            if self.mode == "Generate_text":
                for player in player_sprites:
                    player.Reset()
                    player.live += 1
                    
                    player.live_count.update_live()
            
                for enemy_to in enemy_sprites:
                    enemy_to.Reset() # Reseto de los enemigos 
                    
                    if enemy_to.pellet_limit >= 30:
                        enemy_to.pellet_limit = enemy_to.pellet_limit -30 # Forzando la salida mas pronta de la casa 
                        
                    enemy_to.pellet_to_go = 192 - enemy_to.pellet_limit
                    enemy_to.start_val[9] -= .375  # Disminullendo los tiempos para comer a los fantasmas
                    enemy_to.start_val[10] -= .125  # Disminullendo los tiempos para comer a los fantasmas


                self.level += 1 
                decoration.Kill_Identifier("level")
                decoration.Generate_Decoration(str(self.level), 550, 198, (255, 255, 255), "level")
                decoration.Generate_Decoration("ready!", 165, 342, (255, 247, 0, 1), "dead_reset")
                self.mode = "ready!"
                
                pellets.Generate_pellets(20, 45)


            if self.mode == "ready!":
                if self.time.time_over():
                    self.time = decoration.Chronometer(2)
                    enemy.Play_Frame()
                    decoration.Kill_Identifier("dead_reset")
                
                    for enemy_to in enemy_sprites:
                        enemy_to.Play()
                        
                    for player in player_sprites:
                        player.Play()
                    
                    self.mode = "stop_player"
                    self.state = False


    def update(self, delta_time):
        self.Stade_Controll()
        self.Mode_Control()


class Coffe_Break_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((640, 620))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.time = decoration.Chronometer(10)
        
        self.coffe_break_sound = music.Sound("Coffe_Break_Theme", .4)
        self.coffe_break_sound.play()


    def Generate_Animation(self):
        self.pac_man = animation.Pac_man_eater(640, 320, -180)
        self.pac_man.speed_x = -3
        all_sprites.add(self.pac_man)
        
        self.ghost = animation.Chasing_n_Chased(888, 320, (255, 0, 0), self.pac_man)
        self.ghost.speed_x = -4
        all_sprites.add(self.ghost)
        
        self.wall_l = background.Wall(0, 0, 20, 640, False)
        all_sprites.add(self.wall_l)
        
        self.wall_r = background.Wall(620, 0, 20, 640, False)
        all_sprites.add(self.wall_r)
        
        self.rev = False


    def Control_Animation(self):
        if not self.rev:
            if self.ghost.direction == "right": #3, 218, 30, 29
                self.ghost.speed_x = 3
                self.pac_man.kill()
                self.pac_man = animation.MEGA_pac_man(-300, 297)
                all_sprites.add(self.pac_man)
                self.ghost.rect.x = 0
                self.rev = True
    
                self.wall_r.kill()
                self.wall_r = background.Wall(620, 0, 20, 640, False)
                all_sprites.add(self.wall_r)


    def Kill_Animation(self):
        if self.time.time_over():
            self.pac_man.kill()
            self.ghost.kill()
            self.wall_l.kill()
            self.wall_r.kill()
            self.kill()


    def update(self, delta_time):
        self.Control_Animation()
        self.Kill_Animation()


class Coffe_Break_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((640, 620))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.time = decoration.Chronometer(5)
        
        self.coffe_break_sound = music.Sound("Coffe_Break_Theme", .4)
        self.coffe_break_sound.play()


    def Generate_Animation(self):
        self.pac_man = animation.Pac_man_eater(640, 320, -180)
        self.pac_man.speed_x = -3
        all_sprites.add(self.pac_man)
        
        self.ghost = animation.True_Ghost(920, 320, (250, 180, 250, 1), 320)
        all_sprites.add(self.ghost)
        
        self.wall_l = background.Wall(0, 0, 20, 640, False)
        all_sprites.add(self.wall_l)
        
        self.wall_r = background.Wall(620, 0, 20, 640, False)
        all_sprites.add(self.wall_r)
        
        self.rev = False


    def Kill_Animation(self):
        if self.time.time_over():
            self.coffe_break_sound.stop()
            self.pac_man.kill()
            self.ghost.kill()
            self.wall_l.kill()
            self.wall_r.kill()
            self.kill()


    def update(self, delta_time):
        self.Kill_Animation()


class Coffe_Break_3(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((640, 620))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.time = decoration.Chronometer(10)
        
        self.coffe_break_sound = music.Sound("Coffe_Break_Theme", .4)
        self.coffe_break_sound.play()

        self.color = color


    def Generate_Animation(self):
        self.pac_man = animation.Pac_man_eater(640, 320, -90)
        self.pac_man.speed_x = -3
        all_sprites.add(self.pac_man)
        
        self.ghost = animation.True_Ghost(704, 320, self.color, -60)
        all_sprites.add(self.ghost)
        
        self.wall_l = background.Wall(0, 0, 20, 640, False)
        all_sprites.add(self.wall_l)
        
        self.wall_r = background.Wall(620, 0, 20, 640, False)
        all_sprites.add(self.wall_r)
        
        self.rev = False


    def Control_Animation(self):
        if not self.rev:
            if self.ghost.direction == "right": #3, 218, 30, 29
                self.pac_man.kill()
                self.rev = True


    def Kill_Animation(self):
        if self.time.time_over():
            self.pac_man.kill()
            self.ghost.kill()
            self.wall_l.kill()
            self.wall_r.kill()
            self.kill()


    def update(self, delta_time):
        self.Control_Animation()
        self.Kill_Animation()


class Game_Over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.mode = "pac_man_death" 
        self.state = False
        
        self.game_over = False
        
        for player in player_sprites:
            self.player = player

        self.time = decoration.Chronometer(2)
      
    def Stade_Controll(self):
        if self.player.mode == "Dead":
            if self.player.live <= 0:
                self.state = True


    def Mode_Control(self):
        if self.state:
            if self.mode == "pac_man_death":
                if self.time.time_over():
                    self.time = decoration.Chronometer(4)
                    self.mode = "Generate_text"
                    
            if self.mode == "Generate_text":
                decoration.Generate_Decoration("game over", 135, 342, (250, 0, 0, 1), "game_over")
                
                for player in player_sprites:
                    player.live_count.update_live()
                
                self.mode = "main"
                
            if self.mode == "main":
                if self.time.time_over():
                    music.Set_Volume(True)
                    self.game_over = True
                
    def get_game_over(self):
        if self.game_over == True:
            return True

    def update(self, delta_time):
        self.Stade_Controll()
        self.Mode_Control()
