from planetas import Body
import time
import sys
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
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('THREE BODY PROBLEM')

FONT = pygame.font.SysFont('comicsans', 14)


def main():
    run = True 
    clock = pygame.time.Clock()

    # LOAD DIFFERENT SOLUTIONS
    
    #bodies = [Body(*FIGURE_8[0]), Body(*FIGURE_8[1]), Body(*FIGURE_8[2])]
    #bodies = [Body(*SUN_PLANET_SATELLITE[0]), Body(*SUN_PLANET_SATELLITE[1]), Body(*SUN_PLANET_SATELLITE[2])]
    #bodies = [Body(*LAGRANGE_TRIANGLE[0]), Body(*LAGRANGE_TRIANGLE[1]), Body(*LAGRANGE_TRIANGLE[2])]
    if sys.argv[1] == "SUN":
        body1 = Body(*SUN_PLANET_SATELLITE[0])
        body2 = Body(*SUN_PLANET_SATELLITE[1])
        body3 = Body(*SUN_PLANET_SATELLITE[2])
    elif sys.argv[1] == "LAGRANGE":
        body1 = Body(*LAGRANGE_TRIANGLE[0])
        body2 = Body(*LAGRANGE_TRIANGLE[1])
        body3 = Body(*LAGRANGE_TRIANGLE[2])
    elif sys.argv[1] == "EIGHT":
        body1 = Body(*FIGURE_8[0])
        body2 = Body(*FIGURE_8[1])
        body3 = Body(*FIGURE_8[2])

    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        start = time.time()
        #for body in bodies:
            #com_x, com_y = com(bodies)
            #body.update_position(bodies)
            #body.draw(screen, com_x, com_y)
        body1.update_position([body2, body3])
        body2.update_position([body1, body3])
        body3.update_position([body1, body2])

        com_x, com_y = com([body1, body2, body3])

        body1.draw(screen, com_x, com_y)
        body2.draw(screen, com_x, com_y)
        body3.draw(screen, com_x, com_y)

        pygame.display.update()
        end = time.time()
        print(f'Loop time {end - start}')

    pygame.quit()

if __name__ == '__main__':
    main()
