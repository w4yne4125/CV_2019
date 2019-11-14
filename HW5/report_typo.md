# Computer Vision Hw #5

> B06902058 吳崇維  																											     

### Homework Description

- Write programs which do gray-scale morphology on a **gray-scale** image(lena.bmp):

- - (a) Dilation
  - (b) Erosion
  - (c) Opening
  - (d) Closing

--------------



- **Dilation**

```python
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
```

![prob_A](/Users/loyolaaa/2019_fall/CV/HW5/prob_A.bmp)

---------------------



- **Erosion** 

```python
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
```

![prob_B](/Users/loyolaaa/2019_fall/CV/HW5/prob_B.bmp)



-----------------------



- **Opening**

Just call the function : Erosion & Dilation

```python
new_graph = Dilation(Erosion(arr, kernel), kernel)
```

![prob_C](/Users/loyolaaa/2019_fall/CV/HW5/prob_C.bmp)

--------------

- **Closing**

Just call the function : Erosion & Dilation

```python
new_graph = Erosion(Dilation(arr, kernel), kernel)
```

![prob_C](/Users/loyolaaa/2019_fall/CV/HW5/prob_D.bmp)


