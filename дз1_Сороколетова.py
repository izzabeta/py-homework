#############
# задание 1 #
#############

# напишите цикл, рисующий по
# вертикали фигуры (квадраты
# или другие из ссылки выше)

from drawbot_skia.drawbot import rect, saveImage, fill, oval, newDrawing, line
y = 0
step = 100
# чтобы выполнить какую-либо инструкцию строго определенное число раз, воспользуемся функцией range()
for i in range(10):
    fill(178/255, 1, 102/255)
    rect(450, y, 100, 100)
    y = y + step
saveImage("задание 1.pdf")

#############
# задание 2 #
#############

# напишите вложенный (двойной)
# цикл, заполняющий холст фигурами
# полностью, по вертикали и
# горизонтали
newDrawing()
x = 0
y = 0
step = 100
for a in range(10):
    for b in range(10):
        fill(255/255, 102/255, 178/255)
        oval(x, y, 100, 100)
        y = y + step
    y = 0
    x = x + step

saveImage("задание 2.pdf")

##########################
# задание дополнительное #
# творческое, свободное  #
##########################

newDrawing()
fill(1, 1, 0)
oval(300, 300, 400, 400)
line((0, 500), (1000, 500))
line((500,0), (500, 1000))
line((0, 1000), (1000, 0))
line((0, 0), (1000, 1000))
line((100, 350), (900, 650))
line((100, 650), (900, 350))
line((350, 100), (650, 900))
line((350, 900), (650, 100))
saveImage("задание 3.pdf")

# хорошего Вам настроения!