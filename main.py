import pygame, sys, random
from scripts.constants import *
from scripts.extras import *
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.camera import Camera
from scripts.healthBar import healthBar

class main: # ! for the layering like if the player is behidn or in front of a wall, use the blackbox or look at clear code's project
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINW, WINH))
        pygame.display.set_caption("Brawl Stars Clone")

        self.display = pygame.Surface((WINW/2.5, WINH/2.5))

        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player/idle/right': Animation(load_images('player/idle/right',scaleFactor = 1.5), img_dur = 7),
            'player/idle/left': Animation(load_images('player/idle/left',scaleFactor = 1.5), img_dur = 7),
            'player/idle/up': Animation(load_images('player/idle/up',scaleFactor = 1.5), img_dur = 7),
            'player/idle/down': Animation(load_images('player/idle/down',scaleFactor = 1.5), img_dur = 7),
            'player/walk/right': Animation(load_images('player/walk/right',scaleFactor = 1.5), img_dur = 7),
            'player/walk/left': Animation(load_images('player/walk/left',scaleFactor = 1.5), img_dur = 7),
            'player/walk/up': Animation(load_images('player/walk/up',scaleFactor = 1.5), img_dur = 7),
            'player/walk/down': Animation(load_images('player/walk/down',scaleFactor = 1.5), img_dur = 7),
            'player/death/right': Animation(load_images('player/death/right',scaleFactor = 1.5), img_dur = 7),
            'player/death/left':Animation(load_images('player/death/left',scaleFactor = 1.5), img_dur = 7),
            'player/death/up': Animation(load_images('player/death/up',scaleFactor = 1.5), img_dur = 7),
            'player/death/down': Animation(load_images('player/death/down',scaleFactor = 1.5), img_dur = 7),
            'walls':load_images('walls', scaleFactor = 0.3) # 30 x 30
        }

        self.movement = [False, False]
        self.movement1 = [False, False]
        
        self.player = PhysicsEntity(self, 'player', (168,168), (13*1.5, 25*1.5))
        self.pHealth = healthBar(self.player.max_heatlh, self.display, self)

        self.tilemap = Tilemap(self, tile_size = 30)
        self.camera = Camera(self, self.tilemap)

        self.scroll = [0,0]
    
    def renderText(self, tex1, color, pos, font = 30):
        font = pygame.font.Font(None, font)
        text = font.render(tex1, 1, pygame.Color(color))
        self.display.blit(text, pos)

    def run(self):
        while True:
            self.display.fill(COLOR)

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            self.render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.camera.render(self.display, [[value, [value['pos'][0]*self.tilemap.tile_size, value['pos'][1]*self.tilemap.tile_size]] for value in self.tilemap.tilemap.values()], [[self.player, self.player.pos]])
            self.pHealth.render(self.player.pos, self.player.animation.img().get_size()[0], self.render_scroll)
            # self.tilemap.render(self.display)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement1[1] - self.movement1[0]))
            self.renderText(str(int(self.clock.get_fps())), (255, 255, 255), (10, 10))
            print(int(self.clock.get_fps()))
            # self.player.render(self.display)

            # drawGrid(30, WINW, WINH, self.display, (255,255,255))

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
                    elif event.key == pygame.K_b:
                        self.pHealth.damage(334)
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