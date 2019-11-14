# Computer Vision Hw #3

> B06902058 吳崇維  																											     

### Homework Description

- (a) original image and its histogram	
- (b) image with intensity divided by 3 and its histogram	
- (c) image after applying histogram equalization to (b) and its histogram

--------------



- **Histogram**

Use : matplotlib

```python
cnt = []
for i in range(length):
    for j in range(length):
        cnt.append(arr[i][j])
plt.hist(np.array(cnt), bins=range(256))
```

![prob_A](/Users/loyolaaa/2019_fall/CV/HW3/prob_A.bmp)![hist](/Users/loyolaaa/2019_fall/CV/HW2/hist.png)

---------------------



- Histogram with intensity divided by 3** 

Simply change the value of array

```python
cnt = []
for i in range(length):
	  for j in range(length):
  		  arr[i][j] = arr[i][j] // 3
        cnt.append(arr[i][j])
plt.hist(np.array(cnt), bins=range(256))
```

![prob_B](/Users/loyolaaa/2019_fall/CV/HW3/prob_B.bmp)![hist](/Users/loyolaaa/2019_fall/CV/HW3/histB.png)



-----------------------



- **Image after applying histogram equalization to (b) and its histogram**

Apply the equalization on the image from (b)

![Screen Shot 2019-09-24 at 20.07.34](/Users/loyolaaa/Downloads/螢幕截圖/Screen Shot 2019-09-24 at 20.07.34.jpg)

```python
"""get the image from (b)"""
for i in range(length):
    for j in range(length):
        arr[i][j] = arr[i][j] // 3

"""do accumulation"""
cnt = np.zeros(256)
tot = 0
for i in range(length):
    for j in range(length):
        cnt[arr[i][j]] += 1
        tot += 1
"""create mapping"""
mp = np.zeros(256)
acc = 0
for i in range(256):
    acc += cnt[i]
    mp[i] = int(255 * (acc / tot))
cnt = []
"""Finally the image"""
for i in range(length):
    for j in range(length):
        arr[i][j] = mp[arr[i][j]]
        cnt.append(arr[i][j])

plt.hist(np.array(cnt), bins=range(256))
```



![prob_C](/Users/loyolaaa/2019_fall/CV/HW3/prob_C.bmp)![histC](/Users/loyolaaa/2019_fall/CV/HW3/histC.png)

