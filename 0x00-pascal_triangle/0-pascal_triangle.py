def pascal_triangle(n):
    """ pascal_triangle """
    if (n <= 0):
        return []

    triangleP = []

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangleP[-1]
            for j in range(i - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangleP.append(row)

    return triangleP
