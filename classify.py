import hy
import ast
import re

def classify_image(pixels):
	file = open("program.txt", "r")
	data = file.read()
	file.close()
	
	data = data.replace("ite", "if")
	
	args = ""
	size = len(pixels)
	for y in range(size):
		for x in range(size):
			args += "(setv b{}_{} {})".format(x, y, pixels[y][x])
	
	prog = args + data
	expr = hy.read_str(f"((fn [] {prog}))")
	return hy.eval(expr)