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
    LAGRANGE_TRIANGLE,
)

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

# LOAD POSITIONS
for i in range(3600):
    for body in bodies:
        body.update_position(bodies)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THREE BODY PROBLEM")

FONT = pygame.font.SysFont("comicsans", 14)


def main():
    run = True
    clock = pygame.time.Clock()

    frame = 0
    try:
        sys.argv[1]
    except IndexError:
        print("Invalid solution.")
        run = False

    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for body in bodies:
            pygame.draw.circle(
                screen,
                body.color,
                (
                    body.positions[frame][0] + WIDTH / 2,
                    body.positions[frame][1] + HEIGHT / 2,
                ),
                body.radius,
            )

        frame += 1

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
