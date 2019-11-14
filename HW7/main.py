"""
Computer Vision HW7
Write a program which does thinning on a downsampled image (lena.bmp).
"""
from PIL import Image, ImageDraw
import queue
import matplotlib.pyplot as plt
import numpy as np



def get(x, y, arr):
    if (x < 0 or x >= 64 or y < 0 or y >= 64 or arr[x][y] == 0):
        return 0
    return 1

def binary(arr):
    new = arr
    for i in range(length):
        for j in range(length):
            new[i][j] = 0 if new[i][j] < 128 else 255
    return new

def Downsampling(arr):
    new = np.zeros((64,64))
    for i in range(64):
        for j in range(64):
            new[i][j] = arr[i*8][j*8]
    output = Image.fromarray(new)
    output = output.convert("L")
    output.save("downsample.bmp")
    return new

def process(res):
    tot = res[1] + res[3] + res[5] + res[7]
    for k in range(4):
        if (res[k*2] and res[k*2 + 1] and res[k*2-1]):
            tot -= 1
    return tot 

def count(arr):
    seq = [(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1)]
    ret = np.zeros((64,64))
    for i in range(64):
        for j in range(64):
            if (arr[i][j] == 0):
                ret[i][j] = -1
                continue
            res = []
            for k in range(8):
                res.append(get(i + seq[k][0], j + seq[k][1], arr))
            if (all(res)):
                ret[i][j] = 5
                continue
            ret[i][j] = process(res)
    return ret

def get_num(x, y, number):
    if (x < 0 or x >= 64 or y < 0 or y >= 64):
        return 0
    return number[x][y]

def check(x, y):
    if (x < 0 or x >= 64 or y < 0 or y >= 64):
        return 0
    return 1

def h(b, c, d, e, arr):
    B = arr[b[0]][b[1]] if check(b[0], b[1]) else 0
    C = arr[c[0]][c[1]] if check(c[0], c[1]) else 0
    D = arr[d[0]][d[1]] if check(d[0], d[1]) else 0
    E = arr[e[0]][e[1]] if check(e[0], e[1]) else 0
    if (B == C and (D != B or E != B)):
        return 1
    return 0

def thinning(arr):
    number = count(arr)
    deletable = np.zeros((64, 64))
    dx = [0, -1, 0 , 1]
    dy = [-1, 0 , 1, 0]
    for i in range(64):
        for j in range(64):
            if (get_num(i, j, number) != 1):
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if (get_num(nx, ny, number) == 1):
                    deletable[i][j] = 1

    for i in range(64):
        for j in range(64):
            if deletable[i][j]:
                x0 = (i, j)
                x1 = (i, j+1)
                x2 = (i-1, j)
                x3 = (i, j-1)
                x4 = (i+1, j)
                x5 = (i+1, j+1)
                x6 = (i-1, j+1)
                x7 = (i-1, j-1)
                x8 = (i+1, j-1)
                a1 = h(x0, x1, x6, x2, arr)
                a2 = h(x0, x2, x7, x3, arr)
                a3 = h(x0, x3, x8, x4, arr)
                a4 = h(x0, x4, x5, x1, arr)
                if (a1 + a2 + a3 + a4 == 1):
                    arr[i][j] = 0
    return arr

def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    arr = binary(arr)
    arr = Downsampling(arr)
    number = count(arr)
    for _ in range(7):
        arr = thinning(np.copy(arr))
    output = Image.fromarray(arr)
    output = output.convert("L")
    output.save("thinning.bmp")


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    kernel = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) + abs(j) != 4):
                kernel.append((i,j))
    length = 512
    main()

