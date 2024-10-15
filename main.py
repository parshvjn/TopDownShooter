import pygame, sys, random
from scripts.constants import *
from scripts.extras import *
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.camera import Camera

class main: # ! for the layering like if the player is behidn or in front of a wall, use the blackbox or look at clear code's project
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINW, WINH))
        pygame.display.set_caption("Brawl Stars Clone")

        self.display = pygame.Surface((WINW/2.5, WINH/2.5))

        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': load_images('player'), # 17 x 30
            'walls': load_images('walls', scaleFactor = 0.3) # 30 x 30
        }

        self.movement = [False, False]
        self.movement1 = [False, False]

        self.player = PhysicsEntity(self, 'player', (168,168), (17, 30)) # ! fix the size

        self.tilemap = Tilemap(self, tile_size = 30)
        self.camera = Camera(self.tilemap)
    
    def run(self):
        while True:
            self.display.fill(COLOR)

            self.camera.render(self.display, [[value, [value['pos'][0]*self.tilemap.tile_size, value['pos'][1]*self.tilemap.tile_size]] for value in self.tilemap.tilemap.values()], [[self.player, self.player.pos]])
            print(self.player.pos)
            # self.tilemap.render(self.display)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement1[1] - self.movement1[0]))
            # self.player.render(self.display)

            # drawGrid(30, WINW, WINH, self.display, (255,255,255))
            print(random.randint(1,10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    elif event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    elif event.key == pygame.K_UP:
                        self.movement1[0] = True
                    elif event.key == pygame.K_DOWN:
                        self.movement1[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    elif event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    elif event.key == pygame.K_UP:
                        self.movement1[0] = False
                    elif event.key == pygame.K_DOWN:
                        self.movement1[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

main().run()