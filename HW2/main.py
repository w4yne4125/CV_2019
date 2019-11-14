"""
Computer Vision HW2
(a) a binary image (threshold at 128)
(b) a histogram
(c) connected components(regions with + at centroid, bounding box)

"""
from PIL import Image, ImageDraw
import queue
import matplotlib.pyplot as plt
import numpy as np

def Prob_A(arr):
    """binarize lena.bmp at 128 to get a binary image"""
    for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] < 128 else 255
    output = Image.fromarray(arr)
    output.save("prob_A.bmp")


def Prob_B(arr):
    """Draw hist"""
    cnt = []
    for i in range(length):
        for j in range(length):
            cnt.append(arr[i][j])
    plt.hist(np.array(cnt), bins=range(256))
    plt.xlabel("Gray scale intensity")
    plt.ylabel("counts")
    plt.savefig("hist.png")

def Prob_C(arr, arr2):
    """Connected component : 4-connected"""
    for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] < 128 else 255
    output = Image.fromarray(arr)
    real_out = Image.fromarray(arr2)
    draw = ImageDraw.Draw(real_out)
    visited = np.zeros((512, 512))
    que = queue.Queue()
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for i in range(length):
        for j in range(length):
            if arr[i][j] == 255 and visited[i][j] == 0:
                mxx = i 
                mnx = i
                mxy = j
                mny = j
                avg_x = i
                avg_y = j
                que.put((i, j))
                visited[i][j] = 1
                loop_cnt = 0
                while not que.empty():
                    loop_cnt += 1
                    x, y = que.get()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx > 511 or ny > 511:
                            continue
                        if arr[nx][ny] == 255 and visited[nx][ny] == 0:
                            mxx = max(mxx, nx)
                            mnx = min(mnx, nx)
                            mxy = max(mxy, ny)
                            mny = min(mny, ny)
                            avg_x += nx
                            avg_y += ny
                            que.put((nx, ny))
                            visited[nx][ny] = 1
                if loop_cnt >= 500:
                    draw.rectangle([mny, mnx, mxy, mxx], outline = 'red', width=3)
                    avg_x /= loop_cnt
                    avg_y /= loop_cnt
                    draw.ellipse([int(avg_y)-3, int(avg_x)-3, int(avg_y)+3, int(avg_x)+3], outline='red', fill='blue')
    real_out.save("prob_C_white.bmp")

def main():
    img = Image.open(FILE_PATH)
    arr , arr2= np.array(img), np.array(img.convert('RGB'))
    Prob_A(np.copy(arr))
    Prob_B(np.copy(arr))
    Prob_C(np.copy(arr), np.copy(arr2))


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    length = 512
    main()
