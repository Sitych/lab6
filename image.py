from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import array, arange

def median(j, mas):
	mas = mas[j - 2: j + 3]
	mas.sort()
	return mas[2]

def printf(mas, filename):
	y = array(mas)
	x = arange(len(mas))
	fig = plt.figure()
	ax = fig.add_subplot(111)
	# fig, ax = plt.subplots()
	ax.plot(x, y, color = 'r', linewidth = 1)
	#  Устанавливаем интервал основных и
	#  вспомогательных делений:
	ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(25))
	# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
	# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
	#  Добавляем линии основной сетки:
	ax.grid(which='major',color = 'k')
	#  Включаем видимость вспомогательных делений:
	ax.minorticks_on()
	#  Теперь можем отдельно задавать внешний вид
	#  вспомогательной сетки:
	ax.grid(which='minor', color = 'gray', linestyle = ':')
	ax.set_xlabel('X, пиксель')
	ax.set_ylabel('R')
	plt.savefig(filename + ".jpeg", format='jpeg', dpi = 400)
	plt.close(fig)
	plt.clf()

image = Image.open("1.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

color = [[pix[j, i][0] for j in range(width)] for i in range(height)]

y = 132 # заданное сечение
printf(color[y], "orig")

k = 1

for j in range(2, width - 2):
	color[y][j] = median(j, color[y])
printf(color[y][2:len(color[y]) - 2], "median")

w = 10
for j in range(width):
	sum1 = 0
	if (j + w > width):
		break
	for h in range(j, j + w):
		sum1 += color[y][h]
	color[y][j] = sum1 / w

printf(color[y][130:len(color[y]) - w], "sred")
# for h in range(k):
# 	for i in range(height):
# 		for j in range(2, width - 2):
# 			color[i][j] = median(j, color[i])
# printf(color[y], "median")
# # w = 5
# # for i in range(2):
# # 	for i in range(height):
# # 		for j in range(width):
# # 			if (color[i][j] > maximum):
# # 				maximum = color[i][j]

# # 	for i in range(height):
# # 		for j in range(width):
# # 			sum1 = 0
# # 			if (j + w > width):
# # 				break
# # 			for h in range(j, j + w):
# # 				sum1 += color[i][h]
# 			# color[i][j] = sum1 / w
# w = 10

# for i in range(100, 200, 2):
# 	y = array(color[i][0:len(color[i]) - w])
# 	x = arange(len(color[i]) - w)
# 	fig = plt.figure()
# 	ax = fig.add_subplot(111)
# 	# fig, ax = plt.subplots()
# 	ax.plot(x, y, color = 'r', linewidth = 1)
# 	#  Устанавливаем интервал основных и
# 	#  вспомогательных делений:
# 	ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
# 	ax.xaxis.set_minor_locator(ticker.MultipleLocator(25))
# 	# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# 	# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# 	#  Добавляем линии основной сетки:
# 	ax.grid(which='major',color = 'k')
# 	#  Включаем видимость вспомогательных делений:
# 	ax.minorticks_on()
# 	#  Теперь можем отдельно задавать внешний вид
# 	#  вспомогательной сетки:
# 	ax.grid(which='minor', color = 'gray', linestyle = ':')
# 	plt.savefig("median" + str(i) + ".jpeg", format='jpeg', dpi = 400)
# 	plt.close(fig)
# 	plt.clf()
