import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")

ball_radius = 25
ball_speed = 20
x, y = 400, 300


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                y = max(y - ball_speed, ball_radius)
            elif i.key == pygame.K_DOWN:
                y = min(y + ball_speed, 600 - ball_radius)
            elif i.key == pygame.K_LEFT:
                x = max(x - ball_speed, ball_radius)
            elif i.key == pygame.K_RIGHT:
                x = min(x + ball_speed, 800 - ball_radius)

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x, y), ball_radius)
    pygame.display.flip()

pygame.quit()