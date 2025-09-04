import pygame
from objects import ball, box

pygame.init()

pygame.display.set_caption("E")
screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 24)

acceleration_scaler = 1
acceleration_scaler_var = acceleration_scaler
damping  = 0.9

box_1 = box.Box(0,0,50,50,"white", 20)
ball_1 = ball.Ball(0,0,"white", 20)

main_loop = True
while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

    dt = clock.tick(60) / 1000

    dt *= 10

    mouse = pygame.Vector2(pygame.mouse.get_pos())

    screen.fill((25,25,25))

    direction_1 = box_1.position - mouse

    # screen.blit(font.render(f"Distance: {direction_1.length():.2f}\nSpeed: {box_1.velocity.length():.2f}\nMouse: {mouse.x} / {mouse.y}\nFPS: {int(clock.get_fps())}", True, "white"), (50, 50))

    # if direction_1.length() > 5:
    #     box_1.acceleration = direction_1.normalize()  * acceleration_scaler_var
    #     acceleration_scaler_var += 0.01
    # else: 
    #     box_1.acceleration = pygame.Vector2(0,0)
    #     acceleration_scaler_var = acceleration_scaler


    # box_1.move(damping)

    # if point0.x > screen.get_width() or point0.x < 0:
    #     velocity.x *= -1
    # if point0.y > screen.get_height() or point0.y < 0:
    #     velocity.y *= -1

    # if not (0 < box_1.hitbox.centerx < screen.get_width()):
    #     box_1.velocity.x *= -1
    
    # if not (0 < box_1.hitbox.centery < screen.get_height()):
    #     box_1.velocity.y *= -1

    # if pygame.mouse.get_pressed()[0]:
    #     box_1.position = mouse.copy()
    #     box_1.velocity = pygame.Vector2(0, 0)
    #     box_1.acceleration = pygame.Vector2(0, 0)

    box_1.draw(screen)

    # pygame.draw.line(screen, "green", point0, mouse, 3)

    pygame.display.flip()

pygame.quit()