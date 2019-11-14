"""
Computer Vision HW3
(a) original image and its histogram
(b) image with intensity divided by 3 and its histogram
(c) image after applying histogram equalization to (b) and its histogram


"""
from PIL import Image, ImageDraw
import queue
import matplotlib.pyplot as plt
import numpy as np

def Prob_A(arr):
    """Draw hist"""
    cnt = []
    for i in range(length):
        for j in range(length):
            cnt.append(arr[i][j])
    plt.hist(np.array(cnt), bins=range(256))
    plt.xlabel("Gray scale intensity")
    plt.ylabel("counts")
    plt.savefig("histA.png")
    plt.close()
    output = Image.fromarray(arr)
    output.save("prob_A.bmp")

def Prob_B(arr):
    """Draw hist with division 3"""
    cnt = []
    for i in range(length):
        for j in range(length):
            arr[i][j] = arr[i][j] // 3
            cnt.append(arr[i][j])
    plt.hist(np.array(cnt), bins=range(256))
    plt.xlabel("Gray scale intensity")
    plt.ylabel("counts")
    plt.savefig("histB.png")
    plt.close()
    output = Image.fromarray(arr)
    output.save("prob_B.bmp")

def Prob_C(arr):
    """Draw hist with equalization"""
    for i in range(length):
        for j in range(length):
            arr[i][j] = arr[i][j] // 3

    cnt = np.zeros(256)
    tot = 0
    for i in range(length):
        for j in range(length):
            cnt[arr[i][j]] += 1
            tot += 1
    mp = np.zeros(256)
    acc = 0
    for i in range(256):
        acc += cnt[i]
        mp[i] = int(255 * (acc / tot))
    cnt = []
    for i in range(length):
        for j in range(length):
            arr[i][j] = mp[arr[i][j]]
            cnt.append(arr[i][j])

    plt.hist(np.array(cnt), bins=range(256))
    plt.xlabel("Gray scale intensity")
    plt.ylabel("counts")
    plt.savefig("histC.png")
    plt.close()
    output = Image.fromarray(arr)
    output.save("prob_C.bmp")

def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    Prob_A(np.copy(arr))
    Prob_B(np.copy(arr))
    Prob_C(np.copy(arr))


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    length = 512
    main()
