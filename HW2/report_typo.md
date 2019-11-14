# Computer Vision Hw #2

> B06902058 吳崇維  																											     	2019/09/19

### Homework Description

- (a) a binary image (threshold at 128)	
- (b) a histogram	
- (c) connected components(regions with + at centroid, bounding box)

--------------

- **Binary Image**

Simple if-else (The same as Hw1)

```python
for i in range(length):
        for j in range(length):
            arr[i][j] = 0 if arr[i][j] < 128 else 255
```

![prob_A](/Users/loyolaaa/2019_fall/CV/HW2/prob_A.bmp)



- **Histogram**

Use : matplotlib

```python
cnt = []
for i in range(length):
    for j in range(length):
        cnt.append(arr[i][j])
plt.hist(np.array(cnt), bins=range(256))
```

![hist](/Users/loyolaaa/2019_fall/CV/HW2/hist.png)



- **Connected components**

使用4-connect ， 並且使用**bfs來找出連通分量**，以連通分量中的最大最小x, y值來畫box，以平均座標畫原點

其中圖片連通白色pixel

因code 較長，請直接參考source code.

![prob_C_white](/Users/loyolaaa/2019_fall/CV/HW2/prob_C_white.bmp)















