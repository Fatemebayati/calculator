import pygame
import sys
from math import radians,sin,cos
import datetime

class clock():
    def __init__(self):
        self.width,self.height=800,800
        self.white=(255,255,255)
        self.blue=(34,79,228)
        self.PPS=60
        self.center=(self.width//2,self.height//2)
        self.clock_radius=self.width//2
        pygame.init()
        self.screen=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Analog Clock")
        self.clock=pygame.time.Clock()

        def numbers(self,number,size,position):
            font=pygame.font.SysFont("Calibri",size,True,False)
            text=font.render(str(number),True,self.white)
            text_rect=text.get_rect(center=position)

