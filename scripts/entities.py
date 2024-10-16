import pygame

class PhysicsEntity:
    def __init__(self, game, entity, pos, size):
        self.game = game
        self.type = entity
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, tilemap, movement = (0,0)):
        move = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += move[0] if movement.count(0) >= 1 else move[0]/2
        entity_rect = self.rect()
        
        for rect in tilemap.physics_rects_around(self.pos):
            if rect.y >= entity_rect.y and (0, -1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.y += tilemap.tile_size/2
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
                rect.y += tilemap.tile_size/2
            if rect.y <= entity_rect.y and (0, 1) not in [block for block in tilemap.tiles_around((rect.x, rect.y), locCheck = True)]:
                rect.h -= tilemap.tile_size/2
            if entity_rect.colliderect(rect): # if collision occurs vertically
                if move[1] > 0: #moving down
                    entity_rect.bottom = rect.top
                if move[1] < 0: #moving up
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y
    
    def render(self, surf, offset = (0,0)):
        surf.blit(self.game.assets['player'][0], (self.pos[0] - offset[0], self.pos[1] - offset[1]))