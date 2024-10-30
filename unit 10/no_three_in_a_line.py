 # By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:       Maximus Maizus
#              Miranda Yang
#              Kevin Alcantara 
#              Rebecca Eason

# Section:     578
# Assignment: Team Lab 10
# Date:        10/30/24

def are_collinear(p1, p2, p3):
    """
    Check if three points p1, p2, p3 are collinear using the area of the triangle.
    If the area is 0, the points are collinear.
    """
    return (p1[0] * (p2[1] - p3[1]) +
            p2[0] * (p3[1] - p1[1]) +
            p3[0] * (p1[1] - p2[1])) == 0

def no_three_in_line(n):
    """
    Find the largest set of points in an n x n grid such that no three points are collinear.
    """
    points = [(i, j) for i in range(n) for j in range(n)]
    selected_points = []

    for point in points:
        is_valid = True
        
        # Manually checking all pairs of selected points
        for i in range(len(selected_points)):
            for j in range(i + 1, len(selected_points)):
                p1 = selected_points[i]
                p2 = selected_points[j]
                
                if are_collinear(p1, p2, point):
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            selected_points.append(point)
    
    return selected_points