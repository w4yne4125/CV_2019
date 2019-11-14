# Computer Vision Hw #6

> B06902058 吳崇維  																											     

### Homework Description

- Count the Yokoi connectivity number on a downsampled lena using 4-connected.
Result of this assignment is a 64x64 matrix.

--------------



- **Downsampling**

Simply run some loops

```python
def Downsampling(arr):
    new = np.zeros((64,64))
    for i in range(64):
        for j in range(64):
            new[i][j] = arr[i*8][j*8]
    output = Image.fromarray(new)
    output = output.convert("L")
    output.save("downsample.bmp")
    return new
```

![prob_A](/Users/loyolaaa/2019_fall/CV/HW6/downsample.bmp)

---------------------



- **Yokoi connectivity number**

```python
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
```



![Screen Shot 2019-10-30 at 23.35.02](/Users/loyolaaa/Downloads/螢幕截圖/Screen Shot 2019-10-30 at 23.35.02.jpg)

