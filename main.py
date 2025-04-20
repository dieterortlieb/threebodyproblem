from planetas import Body
from parametros import (
                        BLACK,
                        WHITE,
                        YELLOW,
                        BLUE,
                        RED,
                        DARK_GREY,
                        WIDTH,
                        HEIGHT
                        )
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('THREE BODY PROBLEM')

FONT = pygame.font.SysFont('comicsans', 14)


def main():
    run = True 
    clock = pygame.time.Clock()

    body1 = Body(200, 200, 10, RED, 20)
    body2 = Body(400, 200, 10, WHITE, 20)
    body3 = Body(300, 300, 10, BLUE, 20)
    
    bodies = [body1, body2, body3]

    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break

        for body in bodies:
            body.update_position(bodies)
            body.draw(screen)
            body.bounce()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
