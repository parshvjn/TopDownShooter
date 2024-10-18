import pygame
from scripts.extras import Timer
from scripts.constants import *
from scripts.weapon import Weapon

class PhysicsEntity:
    def __init__(self, game, entity, pos, size):
        self.game = game
        self.type = entity
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        self.action = ''
        self.set_action('idle/right')
        self.last_movement = [0,0]
        self.speed = 2
        self.max_heatlh = 20000
        self.health = self.max_heatlh - 19000
        self.timer = None
        self.damaged = False
        self.damageTimer = None
        self.weapon = Weapon(self.game)
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def set_action(self, action):
        if action != self.action: #only doing the rest if the action changed
            self.action = action
            # i accessed a class property from another file by saying self.fileName (in this case game)
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    
    def update(self, tilemap, movement = (0,0)):
        movement = (movement[0] * self.speed,  movement[1] * self.speed)

        move = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += move[0] if movement.count(0) >= 1 else move[0]/1.5
        entity_rect = self.rect()
        
        for rect in tilemap.physics_rects_around(self.pos):
            if rect.y >= entity_rect.y and (0, -1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.y += tilemap.tile_size/4
            if rect.y <= entity_rect.y and (0, 1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.h -= tilemap.tile_size/2
            if entity_rect.colliderect(rect): # if collision occurs horizontally
                if move[0] > 0: #moving right
                    entity_rect.right = rect.left
                if move[0] < 0: #moving left
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x

        self.pos[1] += move[1] if movement.count(0) >= 1 else move[1]/2
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if rect.y >= entity_rect.y and (0, -1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.y += tilemap.tile_size/4
            if rect.y <= entity_rect.y and (0, 1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.h -= tilemap.tile_size/2
            if entity_rect.colliderect(rect): # if collision occurs vertically
                if move[1] > 0: #moving down
                    entity_rect.bottom = rect.top
                if move[1] < 0: #moving up
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y
        
        if movement[0] > 0:
            self.set_action("walk/right")
        elif movement[0] < 0:
            self.set_action('walk/left')
        elif movement[1] > 0:
            self.set_action("walk/down")
        elif movement[1] < 0:
            self.set_action('walk/up')
        else:
            if self.last_movement[0] > 0:
                self.set_action('idle/right')
            elif self.last_movement[0] < 0:
                self.set_action('idle/left')
            elif self.last_movement[1] > 0:
                self.set_action('idle/down')
            elif self.last_movement[1] < 0:
                self.set_action('idle/up')

        self.last_movement = movement

        self.animation.update()

        # health bar timers
        if self.damaged == True and self.damageTimer == None:
            self.damageTimer = Timer(HEALAFTERDAMAGERATE)

        if self.damageTimer != None and self.damageTimer.count():
            del self.damageTimer
            self.damageTimer = None
            self.damaged = False

        if self.timer != None and self.timer.count():
            self.timer = None
        
        if self.health < self.max_heatlh:
            if self.timer == None and self.damageTimer == None:
                self.game.pHealth.heal(int(round(self.max_heatlh/7, 0)))
                del self.timer
                self.timer = Timer(PASSIVEHEALRATE)
                
            

    
    def render(self, surf, offset = (0,0)):
        if self.weapon.angle < 95 and self.weapon.angle > -90:
            surf.blit(self.animation.img(), (self.pos[0] - offset[0], self.pos[1] - offset[1]))
            self.weapon.render(surf, (self.rect().centerx + 7, self.rect().centery+ 10), offset)
        else:
            self.weapon.render(surf, (self.rect().centerx - 5, self.rect().centery+ 10), offset)
            surf.blit(self.animation.img(), (self.pos[0] - offset[0], self.pos[1] - offset[1]))
