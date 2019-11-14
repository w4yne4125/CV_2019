"""
Computer Vision HW4
Write programs which do binary morphology on a binary image:
(a) Dilation
(b) Erosion
(c) Opening
(d) Closing
(e) Hit-and-miss transform

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
            if (arr[i][j] == 255):
                for dx, dy in kernel:
                    nx = i + dx
                    ny = j + dy
                    if (In(nx, ny)):
                        new_graph[nx][ny] = 255
    return new_graph

def Erosion(arr, kernel):
    new_graph = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            flag = 1
            for dx, dy in kernel:
                nx = i + dx
                ny = j + dy
                if (In(nx, ny) and arr[nx][ny] == 0):
                    flag = 0
                    break
            if (flag):
                new_graph[i][j] = 255
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

def inv(arr):
    for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] == 255 else 255
    return arr

def intersec(arr, arr2):
    for i in range(length):
        for j in range(length):
            arr[i][j] = 255 if arr[i][j] == 255 and arr2[i][j] == 255 else 0
    return arr

def hit_and_miss(arr, J, K):
    arr1 = Erosion(arr, J)
    arr2 = Erosion(inv(arr), K)
    res = intersec(arr1, arr2)
    return res


def Prob_E(arr):
    """Hit and miss"""
    J = [(0, 0), (1, 0), (0, -1)]
    K = [(0, 1), (-1, 1), (-1, 0)]
    new_graph = hit_and_miss(arr, J, K)
    output = Image.fromarray(new_graph)
    output = output.convert("L")
    output.save("prob_E.bmp")


def Binary(arr):
    """binarize lena.bmp at 128 to get a binary image"""
    for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] < 128 else 255
    return arr

def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    arr = Binary(arr)
    Prob_A(np.copy(arr))
    Prob_B(np.copy(arr))
    Prob_C(np.copy(arr))
    Prob_D(np.copy(arr))
    Prob_E(np.copy(arr))


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    kernel = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) + abs(j) != 4):
                kernel.append((i,j))
    length = 512
    main()
