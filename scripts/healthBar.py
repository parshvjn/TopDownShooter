import pygame

class healthBar:
    def __init__(self, max_health, surf, game):
        self.max_health = max_health
        self.surf = surf
        self.health = self.max_health - 2500
        self.barw = 35
        self.barh = 12
        self.game = game
    
    def damage(self, value):
        if self.health - value >= 0:
            self.health -= value
        else:
            self.health = 0
        self.game.player.damaged = True

    def heal(self, value):
        if self.health + value <= self.max_health:
            self.health += value
        else:
            self.health = self.max_health
    
    def render(self, playerPos, playerW, offset = (0,0)):
        barx = playerPos[0] - ((self.barw - playerW) / 2)
        bary = playerPos[1] - self.barh - 2
        pygame.draw.rect(self.surf, (0,0,0), pygame.Rect(barx - offset[0], bary - offset[1], self.barw, self.barh), border_radius=3)
        healthbarw = self.health*((self.barw - 4)/self.max_health)
        pygame.draw.rect(self.surf, (102, 255, 51), pygame.Rect(barx - offset[0] + 2, bary - offset[1] + 1, healthbarw, self.barh - 2), border_radius=3)
        self.game.renderText(str(self.health), (255,255,255), (barx + (self.barw/2) - ((len(str(self.health))/2)*4) - offset[0], bary + 1 - offset[1]), 14)
