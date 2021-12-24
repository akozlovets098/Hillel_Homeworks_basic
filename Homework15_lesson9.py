# Вычисление расстояния
def distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

point1 = (7, 3)
point2 = (4, -3)
print(distance(point1, point2))