# Begin19. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). 
# Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного прямоугольника.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
wid = (x2 - x1)
hei = (y2 - y1)
per = 2 * (wid + hei)
area = wid * hei
print(per)
print(area)