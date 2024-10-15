
class Camera:
    def __init__(self, tileMap): # [[tile, pos], [...]]; [[playerObject, pos], [...]]
        self.tilesmap = tileMap
    
    def render(self, surf, walls, players):
        self.walls = walls
        self.players = players
        self.entities = self.walls + self.players
        self.order = []
        for entity in sorted(self.entities, key = lambda e: e[1][1]):
            if entity in self.walls:
                self.tilesmap.render(surf, entity[0])
            else:
                entity[0].render(surf)
            self.order.append(entity)
        print([type(order[0]) for order in self.order])