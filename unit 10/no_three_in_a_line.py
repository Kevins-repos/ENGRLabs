# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   10.14 LAB: No three in a line
# Date:         24 10 2024
#comment
def no_three_in_line(n):
    points = []
    x, y = 0, 0
    for i in range(n):
        points.append([x, y])
        x = (x + 2) % n
        y = (y + 3) % n

    # Ensure to have n points and no collinear points
    additional_points = []
    for x in range(n):
        for y in range(n):
            if [x, y] not in points:
                if not any(are_collinear(points[i], points[j], [x, y])
                           for i in range(len(points)) for j in range(i + 1, len(points))):
                    additional_points.append([x, y])
                if len(points) + len(additional_points) >= n:
                    break
        if len(points) + len(additional_points) >= n:
            break

    points.extend(additional_points)
    return points

def are_collinear(p1, p2, p3):
    return (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) == 0