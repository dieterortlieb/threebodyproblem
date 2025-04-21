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
                        SUN_PLANET_SATELLITE
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
    bodies = [Body(*SUN_PLANET_SATELLITE[0]), Body(*SUN_PLANET_SATELLITE[1]), Body(*SUN_PLANET_SATELLITE[2])]

    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        for body in bodies:
            body.update_position(bodies)

        com_x, com_y = com(bodies)
        for body in bodies:
            body.draw(screen, com_x, com_y)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
