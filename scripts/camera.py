
class Camera:
    def __init__(self, game, tileMap): # [[tile, pos], [...]]; [[playerObject, pos], [...]]
        self.tilesmap = tileMap
        self.game = game
    
    def render(self, surf, walls, players):
        self.walls = walls
        self.players = players
        self.entities = self.walls + self.players
        self.order = []
        for entity in sorted(self.entities, key = lambda e: e[1][1]):
            if entity in self.walls:
                if self.game.render_scroll[0] // self.game.tilemap.tile_size - 1 < entity[0]['pos'][0] and ((self.game.render_scroll[0] + self.game.display.get_width()) // self.game.tilemap.tile_size + 1) > entity[0]['pos'][0] and self.game.render_scroll[1] // self.game.tilemap.tile_size - 1 < entity[0]['pos'][1] and ((self.game.render_scroll[1] + self.game.display.get_height()) // self.game.tilemap.tile_size + 1) > entity[0]['pos'][1]:
                    self.tilesmap.render(surf, entity[0], offset = self.game.render_scroll)
            else:
                entity[0].render(surf, offset = self.game.render_scroll)
            self.order.append(entity)