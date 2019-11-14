# Computer Vision Hw #7

> B06902058 吳崇維  																											     

### Homework Description

- Write a program which does thinning on a downsampled image (lena.bmp).

--------------



- **Thinning**

Implementing the method in ptt.

```python
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

```

![prob_A](/Users/loyolaaa/2019_fall/CV/HW7/thinning.bmp)







