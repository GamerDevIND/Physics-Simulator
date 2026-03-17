import pygame
from math import pi
from .object import Object

class Ball(Object):
    def __init__(self, x:int, y, color:tuple[int, int, int] | str, mass=None, density=None, radius = 3):
        self.radius = radius
        self.hitbox = pygame.Rect(0,0, self.radius * 2, radius * 2)

        super().__init__("ball", x, y, pi * (radius ** 2), color, self.hitbox, mass, density)

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)