import pygame
from .object import Object

class Box(Object):
    def __init__(self, x:int, y, width:int, height:int, color:tuple[int, int, int] | str, mass=None, density=None,):
        self.hitbox = pygame.Rect(0,0, width, height)
        super().__init__("box", x, y, width * height, color, self.hitbox, mass, density)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.hitbox)