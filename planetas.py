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
import math

class Body:
    AU = 149.6e6 * 1000
    G = 6.67e-11
    SCALE = 250 / AU 
    TIMESTEP = 3600 * 24

    def __init__(
                self,
                pos_x: float, 
                pos_y: float,
                radius: float, 
                color: set, 
                mass: float
                ) -> None:

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.trace = []

        self.x_vel = 0
        self.y_vel = 0
        
    def draw(self, screen):
        x = self.pos_x
        y = self.pos_y

        self.trace.append((x, y))
        if len(self.trace) > 100:
            self.trace.pop(0)
        
        pygame.draw.circle(screen, self.color, (x,y), self.radius)
        
        for pair in self.trace:
            pygame.draw.circle(screen, self.color, pair, self.radius / 5)

    def update_position(self, bodies: list):
        net_force_x = 0
        net_force_y = 0

        for body in bodies:
            if self == body:
                continue

            force_x, force_y = self.attraction(body)
            net_force_x += force_x * self.TIMESTEP
            net_force_y += force_y * self.TIMESTEP

        self.x_vel += net_force_x / self.mass * self.TIMESTEP
        self.y_vel += net_force_y / self.mass * self.TIMESTEP

        self.pos_x += self.x_vel
        self.pos_y += self.y_vel

    def bounce(self):
        if self.pos_x + self.radius == WIDTH:
            self.x_vel = -self.x_vel

        if self.pos_x - self.radius == 0:
            self.x_vel = -self.x_vel


        if self.pos_y - self.radius == 0:
            self.y_vel = -self.y_vel
    
        if self.pos_y + self.radius == 0:
            self.y_vel = -self.y_vel


    def attraction(self, other_body):
        other_x, other_y = other_body.pos_x, other_body.pos_y

        dist_x = other_x - self.pos_x 
        dist_y = other_y - self.pos_y

        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
        dist = max(1, dist)

        force = self.G * self.mass * other_body.mass / (dist ** 2)
        angle = math.atan2(dist_y, dist_x)
        force_x = math.cos(angle) * force 
        force_y = math.sin(angle) * force 

        return (force_x, force_y)





