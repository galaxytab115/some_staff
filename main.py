import pygame
import numpy as np
import copy
from pygame.draw import *

pygame.init()

FPS = 300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
shirina = 800
A = [-100, 1000, 100]
B = [100, 1000, 100]
C = [100, 1000, -100]
D = [-100, 1000, -100]
A1 = [-100, 1200, 100]
B1 = [100, 1200, 100]
C1 = [100, 1200, -100]
D1 = [-100, 1200, -100]
V = 20

dots = [A, B, C, D, A1, B1, C1, D1]


screen = pygame.display.set_mode((shirina, shirina))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


#pygame.mouse.set_visible(False)
while not finished:
    clock.tick(FPS)
    dx = 0
    dy = 0
    x_m = 400
    y_m = 400
    pygame.mouse.set_pos(400, 400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dx = -V
            elif event.key == pygame.K_s:
                dy = -V
            elif event.key == pygame.K_d:
                dx = V
            elif event.key == pygame.K_w:
                dy = V
            elif event.key == pygame.K_ESCAPE:
                finished = True
        elif event.type == pygame.MOUSEMOTION:
            x_m, y_m = pygame.mouse.get_pos()
    fi = np.pi * (400 - x_m) / 400
    teta = np.pi * (400 - y_m) / 400
    teta = 0
    for x in dots:
        x0 = x[0]
        y0 = x[1]
        z0 = x[2]
        x[0] = np.cos(fi) * (x0 - dx) + np.sin(fi) * (y0 - dy)
        x[1] = np.cos(teta) * np.cos(fi) * (y0 - dy) + z0 * np.sin(teta) - np.sin(fi) * np.cos(teta) * (x0 - dx)
        x[2] = z0 * np.cos(teta) - np.sin(teta) * np.cos(fi) * (y0 - dy) - np.sin(fi) * np.sin(teta) * (x0 - dx)
    dots2 = copy.deepcopy(dots)
    h = 0
    for y in dots2:
        x0 = y[0]
        y0 = y[1]
        h = y[1]
        z0 = y[2]
        y.remove(y[0])
        y[0] = 400 + x0 * shirina / (2 * y0 * np.sqrt(3))
        y[1] = 400 - z0 * shirina / (2 * y0 * np.sqrt(3))
    screen.fill((0, 0, 0))
    for dot in dots2:
        circle(screen, WHITE, dot, 5)
    lines(screen, WHITE, True, [dots2[0], dots2[1], dots2[2], dots2[3]], 1)
    lines(screen, RED, True, [dots2[4], dots2[5], dots2[6], dots2[7]], 1)
    lines(screen, WHITE, True, [dots2[0], dots2[4], dots2[7], dots2[3]], 1)
    lines(screen, WHITE, True, [dots2[1], dots2[5], dots2[6], dots2[2]], 1)
    pygame.display.update()

pygame.quit()
