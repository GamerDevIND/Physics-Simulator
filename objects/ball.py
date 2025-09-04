import pygame
from math import pi

class Ball:
    def __init__(self, x:int, y, color:tuple[int, int, int] | str, mass=None, density=None, volume=None, smoothness=0.8, attraction = 1, radius = 3):
        self.type = "ball"
        self.position:pygame.Vector2 = pygame.Vector2(x, y)
        self.size = pygame.Vector2(radius * 2, radius * 2)

        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.smoothness = smoothness

        self.volume = volume if volume is not None else  pi * (radius ** 2)

        if mass is not None:
            self.mass = mass
            self.density = self.mass / self.volume
        elif density is not None:
            self.density = density
            self.mass = self.density * self.volume
        else:
            self.mass = 1
            self.density = self.mass / self.volume

        self.color = color

        self.hitbox = pygame.Rect(0,0, radius * 2, radius * 2)
        self.hitbox.center = (self.position.x, self.position.y)
        self.attraction = attraction
        self.radius = radius
    
    def move(self, damping):
        self.velocity += self.acceleration
        self.velocity *= damping
        self.position -= self.velocity
        self.hitbox = pygame.Rect(0,0, *self.size)
        self.hitbox.center = (self.position.x, self.position.y)

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)
