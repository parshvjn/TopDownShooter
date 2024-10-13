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
            print(f"Entity rect: {entity_rect}")
            print(f"Tile rect: {rect}")
            if entity_rect.colliderect(rect):
                print("Collision detected!")
            if entity_rect.colliderect(rect): # if collision occurs horizontally
                if move[0] > 0: #moving right
                    entity_rect.right = rect.left
                if move[0] < 0: #moving left
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x

        self.pos[1] += move[1] if movement.count(0) >= 1 else move[1]/2
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect): # if collision occurs horizontally
                if move[1] > 0: #moving down
                    entity_rect.bottom = rect.top
                if move[1] < 0: #moving up
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y
    
        pygame.draw.rect(self.game.display, (255,255,255), self.rect(), 3)
    def render(self, surf):
        surf.blit(self.game.assets['player'][0], self.pos)