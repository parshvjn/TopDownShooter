import pygame
OFFSETS = [(-1,0), (-1,-1), (0, -1), (1,-1), (1,0), (0,0), (-1, 1), (0,1), (1,1), (-1, 2), (0, 2), (1, 2)]
PHYSICS_TILES = {'walls'}

class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid = []
        self.game = game

        for i in range(10):
            self.tilemap[str(3+i) + ';10'] = {'type': 'walls', 'variant' : 0, 'pos': (3+i, 10)}
            self.tilemap['10;' +  str(5+i)] = {'type': 'walls', 'variant' : 3, 'pos': (10, 5+i)}
    
    def tiles_around(self, pos): #just checking neighboring tiles for collisions with player because why would we need to check every tile
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)) # convert pixel position to grid position
        for offset in OFFSETS:
            check_loc = str(tile_loc[0]+offset[0]) + ';' + str(tile_loc[1]+offset[1])
            print(check_loc)
            if check_loc in self.tilemap: # checking if there is a surface collision and not just air around player
                tiles.append(self.tilemap[check_loc])
        print('-')
        return tiles #return all tiles around player (not air)
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def render(self, surf):
        for tile in self.offgrid:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
            
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
        