import time
import sys
import random
import pygame
from planetas import Body
from frame import com
from parametros import (
                        BLACK,
                        WHITE,
                        YELLOW,
                        BLUE,
                        RED,
                        DARK_GREY,
                        WIDTH,
                        HEIGHT,
                        FIGURE_8,
                        SUN_PLANET_SATELLITE,
                        LAGRANGE_TRIANGLE
                        )

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('THREE BODY PROBLEM')

FONT = pygame.font.SysFont('comicsans', 14)


def main():
    run = True 
    clock = pygame.time.Clock()

    try:
        sys.argv[1]
    except IndexError:
        print ("Invalid solution.")
        run = False
    else:
        if sys.argv[1] == "SUN":
            body1 = Body(*SUN_PLANET_SATELLITE[0])
            body2 = Body(*SUN_PLANET_SATELLITE[1])
            body3 = Body(*SUN_PLANET_SATELLITE[2])
            bodies = [body1, body2, body3]
        elif sys.argv[1] == "LAGRANGE":
            body1 = Body(*LAGRANGE_TRIANGLE[0])
            body2 = Body(*LAGRANGE_TRIANGLE[1])
            body3 = Body(*LAGRANGE_TRIANGLE[2])
            bodies = [body1, body2, body3]
        elif sys.argv[1] == "EIGHT":
            body1 = Body(*FIGURE_8[0])
            body2 = Body(*FIGURE_8[1])
            body3 = Body(*FIGURE_8[2])
            bodies = [body1, body2, body3]
        else:
            run = False
            print("Invalid solution.")


    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        random.shuffle(bodies)
        start = time.time()
        for body in bodies:
            body.update_position(bodies)

        com_x, com_y = com([body1, body2, body3])

        for body in bodies:
            body.draw(screen, com_x, com_y)


        pygame.display.update()
        end = time.time()
        print(f'Loop time {end - start}')

    pygame.quit()

if __name__ == '__main__':
    main()
