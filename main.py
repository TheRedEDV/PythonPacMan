import pygame, sys, time
from pygame.locals import *
    
    
from Player import player, hit_box_player, live_count

from Enemy import enemy, target_tile, hit_box_enemy, enemy_sounds

from Background import background, pellets

from Text import animation, decoration, score, cursor

from Game import game

from Game_Controllers import game_controll, music

all_sprites =  pygame.sprite.Group()

player_sprites = pygame.sprite.Group()

enemy_sprites = pygame.sprite.Group()

target_tile_sprites = pygame.sprite.Group()
hit_box_sprites = pygame.sprite.Group()

background_sprites = pygame.sprite.Group()
pellets_sprites = pygame.sprite.Group()

animation_sprites = pygame.sprite.Group()
score_sprites = pygame.sprite.Group()
decoration_sprites = pygame.sprite.Group()
cursor_sprites = pygame.sprite.Group()

fruit_sprites = pygame.sprite.Group()

player.init(all_sprites, hit_box_sprites, enemy_sprites)
hit_box_player.init(all_sprites, background_sprites, pellets_sprites, enemy_sprites, fruit_sprites)

enemy.init(all_sprites, enemy_sprites, target_tile_sprites, hit_box_sprites, pellets_sprites)
target_tile.init(all_sprites, player_sprites, enemy_sprites, target_tile_sprites)
hit_box_enemy.init(background_sprites, player_sprites, enemy_sprites)
enemy_sounds.init(enemy_sprites)

animation.init(all_sprites)
cursor.init(all_sprites)
decoration.init(all_sprites, decoration_sprites)
score.init(all_sprites)

background.init(all_sprites, background_sprites)
pellets.init(all_sprites, pellets_sprites, background_sprites)

game_controll.init(all_sprites, player_sprites, enemy_sprites, pellets_sprites, fruit_sprites)

game.init(all_sprites, player_sprites, enemy_sprites, decoration_sprites, pellets_sprites)

re = False

screen_shoot_val = 0

canvas = pygame.Surface((640, 600))
fullscreen = False   

class Game(object):
    def __init__(self): # hay que cambiarlo
        for sprite in all_sprites:
            sprite.kill()
        for sprite in pellets_sprites:
            sprite.kill()
    
        self.main_menu = game.Main_Menu()
        all_sprites.add(self.main_menu)
        
        self.presentation = game.Presentation()
        all_sprites.add(self.presentation)
        
        self.main_menu.execobj = self.presentation
        
        self.credit =    game.Credits()
        
        self.game_play = game.Game_Play()
        
        all_sprites.add(game.Intro(self.main_menu))
        
        score.Reset_score()

    def process_events(self):
        global screen_shoot_val, fullscreen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                    
            self.main_menu_returns = self.main_menu.handle(event)
            self.presentation_returns = self.presentation.handle(event)
            self.credit_returns =  self.credit.handle(event)
            self.game_play_returns = self.game_play.handle(event)


            # main_menu_returns ----------------------------
            if self.main_menu_returns == 0:
                self.game_play.execute()
                
            if self.main_menu_returns == 1:
                self.credit.execute()
                
            if self.main_menu_returns == 2:
                return True
            # main_menu_returns ----------------------------
            
            
            # credit_returns -------------------------------
            if self.credit_returns == 0:
                self.main_menu.execute()
            # credit_returns -------------------------------
            
            
            # presentation_returns -------------------------
            if self.presentation_returns == 0:
                self.main_menu.execute()
            
            # presentation_returns -------------------------
            
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

                if event.key == pygame.K_F11:
                    if fullscreen:
                        pygame.display.set_mode((canvas.get_width(), canvas.get_height()), pygame.RESIZABLE)
                    else:
                        pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)
                    fullscreen = not fullscreen

                """      
                if event.key == pygame.K_l:
                    pygame.image.save(screen, "screen_shoot_{}.png".format(screen_shoot_val))
                    screen_shoot_val += 1
                """

    def run_logic(self, delta_time):
        all_sprites.update(delta_time)
        self.mouse_pos = pygame.mouse.get_pos()
        
        # game_play_returns -------------------
        
        if self.game_play.update(delta_time) == 0:
            self.__init__()
            
        # game_play_returns -------------------

    def display_frame(self, display):
        canvas.fill((0, 0, 0))
        pellets_sprites.draw(canvas)
        fruit_sprites.draw(canvas)
        all_sprites.draw(canvas)

        pixels_per_unit = min(display.get_size()[0]/canvas.get_size()[0], display.get_size()[1]/canvas.get_size()[1])
        w = int(canvas.get_size()[0]*pixels_per_unit)
        h = int(canvas.get_size()[1]*pixels_per_unit)

        x = int(max((display.get_size()[0]-w)/2, 0))
        y = int(max((display.get_size()[1]-h)/2, 0))

        display.blit(pygame.transform.scale(canvas, (w, h)), (x, y))
        pygame.display.flip()


def main():
    pygame.init()
    
    display = pygame.display.set_mode((640, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Pac-Man")
    icon_game = pygame.image.load("LogoTiny.png")
    pygame.display.set_icon(icon_game)
    clock = pygame.time.Clock()
    game = Game()

    delta_time = 0.016666666666666666
    
    done = False
    while not done:
        clock.tick(60)/1000
        done = game.process_events()       
        game.run_logic(delta_time)
        game.display_frame(display)
        
    pygame.quit()

if __name__ == "__main__":
    main()
