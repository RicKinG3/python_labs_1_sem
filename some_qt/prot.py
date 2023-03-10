# Выбрать три различные точки из заданного множества точек на плоскости
# так, чтобы площадь построенного по ним треугольника была максимальна.

from math import sqrt
from tkinter import Tk, Canvas, Label, Button, Entry, messagebox


def triangle_check(triangle):
    x1 = triangle[0]
    y1 = triangle[1]
    x2 = triangle[2]
    y2 = triangle[3]
    x3 = triangle[4]
    y3 = triangle[5]

    AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    AC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    if AC < AB + BC and BC < AB + AC and AB < BC + AC:
        P = (AB + BC + AC) / 2
        S = (P * (P - AB) * (P - BC) * (P - AC)) ** 0.5
        triangle_sq.append(S)

    else:
        triangle_sq.append(0)


def delete():
    return 0


def clear_canvas():
    point_coordinates.clear()
    coordinates_of_triangles.clear()
    triangle.clear()
    triangle_sq.clear()
    index_max_sq.clear()
    canvas.delete("all")


def clear_fields():
    a = point_txt.get()
    len_a = len(a)

    while len_a >= 1:
        point_txt.delete(0)
        len_a -= 1


def build_point():
    a = point_txt.get()
    array = a.split()

    for i in range(len(array)):
        try:
            array[i] = int(array[i])
        except:
            messagebox.showwarning('Ошибка',
                                   'Неверно введены координаты точки!')
            return

    if len(array) != 2:
        messagebox.showerror('Ошибка',
                             'У точки должно быть две координаты!')
        return

    if point_coordinates.count(array) == 0:
        point_coordinates.append(array)
        r = 3.5
        canvas.create_oval(array[0] - r, array[1] - r,
                           array[0] + r, array[1] + r,
                           width=1, outline='red', fill='red')


def build_a_triangle():
    array_point = []
    index_max_sq = []
    for i in range(len(point_coordinates)):
        for j in point_coordinates[i]:
            array_point.append(j)

    index_max_sq.clear()
    for i in range(0, len(array_point) - 1, 2):
        triangle.clear()
        triangle.append(array_point[i])
        triangle.append(array_point[i + 1])
        for j in range(0, len(array_point) - 1, 2):
            triangle.append(array_point[j])
            triangle.append(array_point[j + 1])
            for k in range(0, len(array_point) - 1, 2):
                triangle.append(array_point[k])
                triangle.append(array_point[k + 1])
                triangle_check(triangle)
                triangle.pop(5)
                triangle.pop(4)

                index_max_sq.append(i)
                index_max_sq.append(j)
                index_max_sq.append(k)
            triangle.pop(3)
            triangle.pop(2)
    max_sq = max(triangle_sq)
    if max_sq != 0:

        index_max = triangle_sq.index(max_sq)
        ind = (index_max * 3)
        array = [ array_point [index_max_sq[ind]], array_point [index_max_sq[ind] + 1], array_point [index_max_sq[ind+1]], array_point [index_max_sq[ind+1]+1], array_point [index_max_sq[ind+2]], array_point [index_max_sq[ind+2] + 1]  ]

        r = 3.5

        for i in range(0, 6, 2):
            ec = canvas.create_oval(array[i] - r, array[i + 1] - r,
                               array[i] + r, array[i + 1] + r,
                               width=1, outline='green', fill='green')



        if coordinates_of_triangles.count(array) == 0:

            for i in range(0, 6, 2):
                canvas.create_oval(array[i] - r, array[i + 1] - r,
                                    array[i] + r, array[i + 1] + r,
                                    width=1, outline='green', fill='green')

                coordinates_of_triangles.append(array[:])
                array.append(array[0])
                array.append(array[1])
                canvas.create_line(array, width=3, fill='green')

            coordinates_of_triangles.clear()
            triangle.clear()
            triangle_sq.clear()
            index_max_sq.clear()


def click1(event):
    x = event.x
    y = event.y

    if point_coordinates.count([x, y]) == 0:
        point_coordinates.append([x, y])
        r = 3.5
        canvas.create_oval(x - r, y - r, x + r, y + r,
                           width=1, outline='red', fill='red')





window = Tk()
window.title('Решение планиметрических задач')
window.geometry("800x600")
window.resizable(False, False)

canvas = Canvas(window, width=800, height=500, bg="lightgray")
canvas.place(x=0, y=175)

point_coordinates = []
coordinates_of_triangles = []
triangle = []
triangle_sq = []
index_max_sq = []

canvas.bind('<1>', click1)


Label(window, text='Координаты точки',
      font=('Courier New', 18)).place(x=10, y=10)

point_txt = Entry(window, font=('Courier New', 18))
point_txt.place(width=490, x=290, y=10)

point_txt.insert(0, '50 40')

Button(text='Отчистить полотно', font=('Courier New', 18),
       command=clear_canvas). \
    place(width=250, height=40, x=510, y=50)

Button(text='Очистить ввод', font=('Courier New', 18),
       command=clear_fields). \
    place(width=200, height=40, x=310, y=50)

Button(text='Построить\nточку', font=('Courier New', 18),
       command=build_point). \
    place(width=140, height=60, x=10, y=50)

Button(text='Построить\nтреугольник', font=('Courier New', 18),
       command=build_a_triangle). \
    place(width=160, height=60, x=150, y=50)

window.mainloop()
# 1 точка и много окр и ищем ближ к облости окр