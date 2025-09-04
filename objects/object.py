import pygame

class Object:
    def __init__(self, type_, x:int, y:int, area:int|float, color:tuple[int, int, int] | str, hitbox:pygame.Rect,  mass=None, density=None, ) -> None:
        self.type = type_
        self.position:pygame.Vector2 = pygame.Vector2(x, y)
        self.area = area

        if mass is not None:
            self.mass = mass
            self.density = self.mass / self.area
        elif density is not None:
            self.density = density
            self.mass = self.density * self.area
        else:
            self.mass = 1
            self.density = self.mass / self.area

        self.color = color

        self.hitbox = hitbox
        self.hitbox.center = (self.position.x, self.position.y)
