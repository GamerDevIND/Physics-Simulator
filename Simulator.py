import pygame
from objects import ball, box
from configs import G, mu

pygame.init()

pygame.display.set_caption("E")
screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 24)

acceleration_scaler = 1
acceleration_scaler_var = acceleration_scaler

box_1 = box.Box(0,0,50,50,"white", 50)
ball_1 = ball.Ball(0,0,"white", 20, radius=5)

objects:list[box.Box | ball.Ball] = [ball_1,]

mouse_mass = 40


main_loop = True
while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

    dt = clock.tick(30) / 1000

    mouse = pygame.Vector2(pygame.mouse.get_pos())

    screen.fill((25,25,25))

    for obj in objects:
        direction = mouse - obj.position
        dist_sq = direction.length_squared()
        if dist_sq > 25:
            magnitude = (G * mouse_mass * obj.mass) / dist_sq
            gravity = direction.normalize() * magnitude
            print(gravity)
            obj.apply_force(gravity)

        if obj.velocity.length() > 0.1:
            friction_dir = -obj.velocity.normalize()
            friction_mag = min(mu * obj.mass, obj.velocity.length() * obj.mass)

            fric = friction_dir * friction_mag

            obj.apply_force(fric)

        obj.update(dt)

        if pygame.mouse.get_pressed()[0]:
            obj.position = mouse
            obj.acceleration = obj.velocity = pygame.Vector2()

        obj.draw(screen)

    pygame.display.flip()

pygame.quit()