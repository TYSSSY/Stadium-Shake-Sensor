import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from get_data import shake_input
from itertools import count
import time
rcParams['animation.convert_path'] = r'/usr/bin/convert'
rcParams['animation.ffmpeg_path'] = r'/usr/bin/ffmpeg'
	
def clear_data():
	global x, y, start_time
	x = []
	y = []
	start_time = time.time()


def plot_input(i):
	current_time = time.time() - start_time
	x.append(current_time)
	y.append(shake_input())
	
	plt.cla()
	current_plot = plt.plot(x,y)
	
	plt.xlabel('Time(seconds)')
	plt.ylabel('Amplitude')
	plt.title('Shake Over 20 seconds')
	
	#print(current_time)
	if current_time >= 20:
		clear_data()
	return current_plot,


def visualize(save=False):
	global x, y, start_time,fig
	x = []
	y = []
	start_time = time.time()
	fig = plt.gcf()

	if save:
		ani = FuncAnimation(fig,
						plot_input,
						interval=100,
						frames=200)
		ani.save('/home/pi/Desktop/Shake_Sensor_Prototype/shake.mp4', writer='ffmpeg', fps=10)
	else:
		ani = FuncAnimation(fig,
						plot_input,
						interval=100)
		plt.show()


def test():
	visualize()

if __name__ == '__main__':
	test()