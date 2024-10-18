import pygame
from scripts.extras import *
from scripts.constants import *

class Weapon:
    def __init__(self, game):
        self.game = game
        self.img = self.game.assets['weapons'][0]
        self.angle = 0

    def render(self, surf, pos, offset = (0,0)):
        # self.img = self.game.assets['weapons'][0]
        fixed = (pos[0] - offset[0], pos[1] - offset[1])
        self.angle = get_angle((pos[0], pos[1]), (pos[0] - 7 + ((pygame.mouse.get_pos()[0]/2.5) - (self.game.display.get_size()[0]/2)), pos[1] - 10 + ((pygame.mouse.get_pos()[1]/2.5) - (self.game.display.get_size()[1]/2))))
        self.rimg = self.img
        if self.angle >= 95 or self.angle <= -90:
            self.rimg = pygame.transform.flip(self.img, False, True)
            # angle*=-1
        self.rimg = pygame.transform.rotate(self.rimg, self.angle)
        # print(self.angle)
        # print(get_angle((pos[0] - offset[0], pos[1] - offset[1]), (pygame.mouse.get_pos()[0]/2.5 - offset[0], pygame.mouse.get_pos()[1]/2.5 - offset[1])))
        rotRect = self.rimg.get_rect()
        rotRect.topleft = (fixed[0] -rotRect.width/2, fixed[1] - rotRect.height/2)
        # self.img = pygame.transform.rotate(self.img, 2)
        # print(get_angle(pos[0] - offset[0], pos[1] - offset[1], pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        surf.blit(self.rimg, rotRect)