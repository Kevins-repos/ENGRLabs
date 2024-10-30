def no_three_in_line(n):
    points = []
    try:
        for x in range(n):
            y = (x * x) % n
            points.append((x, y))
        try:
            assert points == list
        except AssertionError:
            return 'Doesnt return list of lists'
        return points
    except TypeError:
        return 'Not an int'
