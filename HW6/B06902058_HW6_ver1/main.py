"""
Computer Vision HW6
Count the Yokoi connectivity number on a downsampled lena using 4-connected.
Result of this assignment is a 64x64 matrix.
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

def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    arr = binary(arr)
    arr = Downsampling(arr)
    number = count(arr)
    f = open("img.txt", 'w')
    for i in range(64):
        for j in range(64):
            if (number[i][j] == -1):
                f.write('  ')
            else:
                f.write(str(int(number[i][j])) + " ")
        f.write("\n")


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    kernel = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) + abs(j) != 4):
                kernel.append((i,j))
    length = 512
    main()
