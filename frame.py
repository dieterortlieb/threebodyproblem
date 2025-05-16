def com(bodies: list):
    """
    Calculate Center of Mass for the System
    """
    total_mass = sum(body.mass for body in bodies)
    x = sum(body.pos_x * body.mass for body in bodies) / total_mass
    y = sum(body.pos_y * body.mass for body in bodies) / total_mass
    return x, y
