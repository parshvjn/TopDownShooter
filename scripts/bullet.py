import pygame
from scripts.extras import *

bulletTypes = {'single': [1, 1, 550, 'straight', "bullet1"]} # amount, speed, damage, type, img

class Bullet:
    def __init__(self, surf, type, assets, pos, angle):
        self.surf = surf
        self.type = bulletTypes[type]
        self.pos = pos
        self.assets = assets
        self.dir = angle
        if self.dir < 0:
            self.dir = 180 + (180 - (self.dir*(-1)))
    
    def get_coordinates(self, speed, angle_degrees, start_x, start_y):
        angle_radians = math.radians(angle_degrees)
        delta_x = speed * math.cos(angle_radians)
        delta_y = speed * math.sin(angle_radians)
        new_x = start_x + delta_x
        new_y = start_y + (delta_y*(-1))
        
        return [new_x, new_y]
    
    def render(self):
        self.surf.blit(self.assets[self.type[-1]], self.pos)
        
    def update(self):
        print(self.pos)
        self.pos = self.get_coordinates(self.type[1], self.dir,  self.pos[0], self.pos[1])
        # print(self.pos, self.dir, self.type[1])


class BulletManager:
    def __init__(self, shotType, cooldown, reloadTime, surf, assets):
        self.type = shotType
        self.cooldown = cooldown
        self.reload = reloadTime
        self.cooltimer = None
        self.surf = surf
        self.bullets = []
        self.assets = assets
    
    def shoot(self, pos, angle):
        if self.cooltimer == None:
            self.bullets.append(Bullet(self.surf, self.type, self.assets, pos, angle))
        else:
            if self.cooltimer.count():
                self.cooltimer = None
    
    def render(self):
        for bullet in self.bullets:
            bullet.render()

    def update(self):
        for bullet in self.bullets:
            bullet.update()
            
