import pygame
import random
import math
import colorsys
from pygame.locals import *

idx = [0, 0, 0]

def mark_pixel(surface, pos, pcol):
    col = surface.get_at(pos)
    surface.set_at(pos, (min(col[0] + pcol[0]/10, 255),
                         min(col[1] + pcol[1]/10, 255),
                         min(col[2] + pcol[2]/10, 255)))

def random_point_index(p):
    global idx
    idx[2] = idx[1]
    idx[1] = idx[0]
    dst1 = abs(idx[1] - idx[2])

    while True:
        idx[0] = random.randint(0, len(p) - 1)
        dst = abs(idx[0] - idx[1])
        if dst1 == 0 and (dst == 1 or dst == len(p) - 1):
            continue
        else:
            break

    return idx[0]

def init_polygon(width, height, n):
    delta_angle = 360/n
    r = width/2 - 10
    p = []

    for i in range(0, n):
        angle = (180 + i*delta_angle) * math.pi / 180
        color = colorsys.hsv_to_rgb((i*delta_angle)/360, 0.8, 1)
        p.append(((width/2 + r*math.sin(angle),
                   height/2 + r*math.cos(angle)),
                  (int(color[0]*255), int(color[1]*255), int(color[2]*255))))
    return p

def main(width, height, n, r):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Das Chaos Spiel')

    p = init_polygon(width, height, n)

    x, y = (400, 300)
    for i in range(0, width*height*3):
        i = random_point_index(p)
        x += (p[i][0][0] - x) * r
        y += (p[i][0][1] - y) * r

        mark_pixel(surface, (int(x), int(y)), p[i][1])
        if i % 1000 == 0:
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

    pygame.image.save(surface, 'chaosspiel.jpg')
    pygame.quit()

if __name__ == "__main__":
    main(500, 480, 8, 0.6)