import pygame

class Box:
    def __init__(self, x:int, y, width:int, height:int, color:tuple[int, int, int] | str, mass=None, density=None, volume=None, smoothness=0.8, attraction = 1):
        self.type = "box"
        self.position:pygame.Vector2 = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.size = pygame.Vector2(width, height)

        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.smoothness = smoothness

        self.volume = volume if volume is not None else width * height

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

        self.hitbox = pygame.Rect(0,0, self.width, self.height)
        self.hitbox.center = (self.position.x, self.position.y)
        self.attraction = attraction

    def move(self, damping):
        self.velocity += self.acceleration
        self.velocity *= damping
        self.position -= self.velocity
        self.hitbox = pygame.Rect(0,0, self.width, self.height)
        self.hitbox.center = (self.position.x, self.position.y)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.hitbox)