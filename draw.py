from display import *
from matrix import *
import math


def add_circle(points, cx, cy, cz, r, step):
    for i in range(step):
        t0 = i / step
        t1 = (i + 1) / step
        x0 = r * math.cos(2 * math.pi * t0) + cx
        y0 = r * math.sin(2 * math.pi * t0) + cy
        x1 = r * math.cos(2 * math.pi * t1) + cx
        y1 = r * math.sin(2 * math.pi * t1) + cy
        add_edge(points, x0, y0, cz, x1, y1, cz)


def add_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    for i in range(step):
        t0 = i / step
        t1 = (i + 1) / step
        x0 = xcoefs[0][0] * (t0 ** 3) + xcoefs[0][1] * (t0 * t0) + xcoefs[0][2] * t0 + xcoefs[0][3]
        y0 = ycoefs[0][0] * (t0 ** 3) + ycoefs[0][1] * (t0 * t0) + ycoefs[0][2] * t0 + ycoefs[0][3]
        x1 = xcoefs[0][0] * (t1 ** 3) + xcoefs[0][1] * (t1 * t1) + xcoefs[0][2] * t1 + xcoefs[0][3]
        y1 = ycoefs[0][0] * (t1 ** 3) + ycoefs[0][1] * (t1 * t1) + ycoefs[0][2] * t1 + ycoefs[0][3]
        add_edge(points, x0, y0, 0, x1, y1, 0)


def draw_lines(matrix, screen, color):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line(int(matrix[point][0]),
                  int(matrix[point][1]),
                  int(matrix[point + 1][0]),
                  int(matrix[point + 1][1]),
                  screen, color)
        point += 2


def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)


def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])


def draw_line(x0, y0, x1, y1, screen, color):
    # swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    # octants 1 and 8
    if (abs(x1 - x0) >= abs(y1 - y0)):

        # octant 1
        if A > 0:
            d = A + B / 2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += B
                x += 1
                d += A
            # end octant 1 while
            plot(screen, color, x1, y1)
        # end octant 1

        # octant 8
        else:
            d = A - B / 2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= B
                x += 1
                d += A
            # end octant 8 while
            plot(screen, color, x1, y1)
        # end octant 8
    # end octants 1 and 8

    # octants 2 and 7
    else:
        # octant 2
        if A > 0:
            d = A / 2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += A
                y += 1
                d += B
            # end octant 2 while
            plot(screen, color, x1, y1)
        # end octant 2

        # octant 7
        else:
            d = A / 2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += A
                y -= 1
                d -= B
            # end octant 7 while
            plot(screen, color, x1, y1)
        # end octant 7
    # end octants 2 and 7
# end draw_line
