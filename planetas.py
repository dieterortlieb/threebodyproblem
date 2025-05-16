from parametros import BLACK, WHITE, YELLOW, BLUE, RED, DARK_GREY, WIDTH, HEIGHT
from frame import com
import pygame
import math


class Body:
    G = 1
    SCALE = 1
    TIMESTEP = 1

    def __init__(
        self,
        pos_x: float,
        pos_y: float,
        vx: float,
        vy: float,
        radius: float,
        color: set,
        mass: float,
        *args,
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.x_vel = vx
        self.y_vel = vy
        self.radius = radius
        self.color = color
        self.mass = mass
        self.positions = []  # experimental

    def draw(self, screen, com_x, com_y):
        """
        Using relative coordinate system
        """
        x = self.pos_x
        y = self.pos_y

        pygame.draw.circle(
            screen,
            self.color,
            (x - com_x + WIDTH / 2, y - com_y + HEIGHT / 2),
            self.radius,
        )

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

        adjust_factor_x, adjust_factor_y = com(bodies)

        self.positions.append(
            (adjust_factor_x + self.pos_x, adjust_factor_y + self.pos_y)
        )

    def attraction(self, other_body):
        other_x, other_y = other_body.pos_x, other_body.pos_y

        dist_x = other_x - self.pos_x
        dist_y = other_y - self.pos_y

        dist = math.sqrt(dist_x**2 + dist_y**2) + 1e-5  # non-zero division

        dist = max(1, dist)
        force = self.G * self.mass * other_body.mass / (dist**2)
        angle = math.atan2(dist_y, dist_x)
        force_x = math.cos(angle) * force
        force_y = math.sin(angle) * force

        return (force_x, force_y)
