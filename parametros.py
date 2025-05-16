import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

WIDTH, HEIGHT =  800, 800

# KNOW SOLUTIONS
mult = 1.8 # apparently stable (not sure)

FIGURE_8 = [[0.97000436 * 300, -0.24308753 * 300, 0.466203685 * mult, 0.43236573 * mult, 8, RED, 1000],
            [-0.97000436 * 300, 0.24308753 * 300, 0.466203685 * mult, 0.43236573 * mult, 8, WHITE, 1000],
            [0, 0, -0.93240737 * mult, -0.86473146 * mult, 8 , BLUE, 1000]]

SUN_PLANET_SATELLITE = [[0, 0, 0, 0, 12, RED, 5000],
                        [200, 0, 0, 2.5, 8, YELLOW, 8],
                        [230, 0, 0, 3.5, 5, WHITE, 5]]

m = 1000
r = 200  # triangle radius
v = 1.7 # tweak this value for stability

LAGRANGE_TRIANGLE = [
    [r * math.cos(2 * math.pi / 3), r * math.sin(2 * math.pi / 3), -v*math.sin(2 * math.pi / 3), v*math.cos(2 * math.pi / 3), 8, RED, m],
    [r * math.cos(4 * math.pi / 3), r * math.sin(4 * math.pi / 3), -v*math.sin(4 * math.pi / 3), v*math.cos(4 * math.pi / 3), 8, WHITE, m],
    [r * math.cos(6 * math.pi / 3), r * math.sin(6 * math.pi / 3), -v*math.sin(6 * math.pi / 3), v*math.cos(6 * math.pi / 3), 8, BLUE, m]]

