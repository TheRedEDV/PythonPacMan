import pygame, sys
from pygame.locals import * 
pygame.init()

vol = True

lib = "Recursos/"

class Sound():
    def __init__(self, sound, volume, exception=False):
        global vol
        self.sound = pygame.mixer.Sound(lib + sound + ".wav") 

        self.exception = exception

        self.volume = volume
  
    def play(self):
        global vol
        self.sound.play()
        
        if vol: 
            self.sound.set_volume(self.volume)
  
        if not vol:
            if not self.exception:
                self.sound.set_volume(0.0)
                
            if self.exception:
                self.sound.set_volume(self.volume)
        

    def stop(self):
        self.sound.stop()



def Set_Volume(boolean):
    global vol
    
    vol = boolean
    
    
def Get_Volume():
    global vol
    return vol