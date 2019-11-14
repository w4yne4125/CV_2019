"""
Computer Vision HW1
Part 1.
(a) upside-down lena.bmp
(b) right-side-left lena.bmp
(c) diagonally mirrored lena.bmp

Part 2. Write a program or use software to do the following requirement.
(d) rotate lena.bmp 45 degrees clockwise
(e) shrink lena.bmp in half
(f) binarize lena.bmp at 128 to get a binary image
"""

from PIL import Image
import numpy as np

def Prob_A(arr):
    """upside-down lena.bmp"""
    for i in range(int(length / 2)):
        for j in range(length):
            arr[i][j], arr[length-1-i][j] = arr[length-1-i][j], arr[i][j]
    output = Image.fromarray(arr)
    output.save("prob_A.bmp")


def Prob_B(arr):
    """right-side-left lena.bmp"""
    for i in range(int(length / 2)):
        for j in range(length):
            arr[j][i], arr[j][length-1-i] = arr[j][length-1-i], arr[j][i]
    output = Image.fromarray(arr)
    output.save("prob_B.bmp")


def Prob_C(arr):
    """diagonally mirrored lena.bmp"""
    new_arr = np.zeros((512, 512))
    for i in range(512):
        for j in range(512):
            new_arr[511-j][i] = arr[i][j]
    output = Image.fromarray(new_arr)
    output = output.convert("L")
    output.save("prob_C.bmp")

    new_arr = np.zeros((512, 512))
    for i in range(512):
        for j in range(512):
            new_arr[j][i] = arr[i][j]
    output = Image.fromarray(new_arr)
    output = output.convert("L")
    output.save("prob_C2.bmp")

def Prob_D(arr):
    """rotate lena.bmp 45 degrees clockwise"""
    rotate_arr = np.zeros((1023, 1023))
    for i in range(1023):
        for j in range(1023):
            rotate_arr[i][j] = 255
    # from (0, 511) to (511, 0)
    for i in range(512):
        nx = i
        ny = 511-i
        for j in range(512):
            rotate_arr[nx+j][ny+j] = arr[i][j]
    """Do normalize"""
    # from (1, 511) to (511, 1)
    for i in range(511):
        nx = i+1
        ny = 511-i
        for j in range(511):
            cx = nx+j
            cy = ny+j
            rotate_arr[cx][cy] = (
                    rotate_arr[cx+1][cy] +
                    rotate_arr[cx][cy+1] +
                    rotate_arr[cx-1][cy] + 
                    rotate_arr[cx][cy-1] ) / 4

    output = Image.fromarray(rotate_arr)
    output = output.convert("L")
    output.save("prob_D.bmp")

def Prob_E(arr):
    """shrink lena.bmp in half"""
    new_arr = np.zeros((512, 512))
    for i in range(512):
        for j in range(512):
            new_arr[i][j] = 255
    for i in range(128, 128+255):
        for j in range(128, 128+255):
            new_arr[i][j] = arr[i*2-256][j*2-256]
    output = Image.fromarray(new_arr)
    output = output.convert("L")
    output.save("prob_E.bmp")


def Prob_F(arr):
    """binarize lena.bmp at 128 to get a binary image"""
    for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] < 128 else 255
    output = Image.fromarray(arr)
    output.save("prob_F.bmp")


def main():
    img = Image.open(FILE_PATH)
    arr = np.array(img)
    Prob_A(np.copy(arr))
    Prob_B(np.copy(arr))
    Prob_C(np.copy(arr))
    Prob_D(np.copy(arr))
    Prob_E(np.copy(arr))
    Prob_F(np.copy(arr))


if __name__ == "__main__":
    FILE_PATH = 'lena.bmp'
    length = 512
    main()
