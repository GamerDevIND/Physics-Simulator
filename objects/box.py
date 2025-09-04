import pygame
from object import Object

class Box(Object):
    def __init__(self, x:int, y, width:int, height:int, color:tuple[int, int, int] | str, mass=None, density=None, volume=None, smoothness=0.8, attraction = 1):
        self.hitbox = pygame.Rect(0,0, width, height)
        super().__init__("box", x, y, width * height, color, self.hitbox, mass, density)


    # def move(self, damping):
    #     self.velocity += self.acceleration
    #     self.velocity *= damping
    #     self.position -= self.velocity
    #     self.hitbox = pygame.Rect(0,0, self.width, self.height)
    #     self.hitbox.center = (self.position.x, self.position.y)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.hitbox)