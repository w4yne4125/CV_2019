"""
Computer Vision HW5
Write programs which do gray-scale morphology on a gray-scale image(lena.bmp):
(a) Dilation
(b) Erosion
(c) Opening
(d) Closing

"""
from PIL import Image, ImageDraw
import queue
import matplotlib.pyplot as plt
import numpy as np


def In(x, y):
    if ( x >= 0 and x <= 511 and y >= 0 and y <= 511):
        return 1
    else:
        return 0

def Dilation(arr, kernel):
    new_graph = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            mx = 0
            for dx, dy in kernel:
                nx = i - dx
                ny = j - dy
                if (In(nx, ny)):
                    mx = max(mx, arr[nx][ny])
            new_graph[i][j] = mx
    return new_graph

def Erosion(arr, kernel):
    new_graph = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            mn = 255
            for dx, dy in kernel:
                nx = i + dx
                ny = j + dy
                if (In(nx, ny)):
                    mn = min(mn, arr[nx][ny])
            new_graph[i][j] = mn
    return new_graph

def Prob_A(arr):
    """Dilation"""
    new_graph = Dilation(arr, kernel)
    output = Image.fromarray(new_graph)
    output = output.convert("L")
    output.save("prob_A.bmp")

def Prob_B(arr):
    """Erosion"""
    new_graph = Erosion(arr, kernel)
    output = Image.fromarray(new_graph)
    output = output.convert("L")
    output.save("prob_B.bmp")

def Prob_C(arr):
    """Opening"""
    new_graph = Dilation(Erosion(arr, kernel), kernel)
    output = Image.fromarray(new_graph)
    output = output.convert("L")
    output.save("prob_C.bmp")

def Prob_D(arr):
    """Closing"""
    new_graph = Erosion(Dilation(arr, kernel), kernel)
    output = Image.fromarray(new_graph)
    output = output.convert("L")
    output.save("prob_D.bmp")

def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    Prob_A(np.copy(arr))
    Prob_B(np.copy(arr))
    Prob_C(np.copy(arr))
    Prob_D(np.copy(arr))


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    kernel = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) + abs(j) != 4):
                kernel.append((i,j))
    length = 512
    main()
