## RGB直方图和灰色图的直方图
```
import cv2 as cv
import matplotlib.pyplot as plt
import  numpy as np
img = cv.imread(r'F:\flower.bmp')
color = ['b', 'g', 'r']
plt.figure("RGB直方图")
for i, color_ in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color_)
cv.imshow('flwoer1', img)
img_gray = cv.imread(r'F:\flower.bmp', 0)
cv.imshow('flwoer2', img_gray)
plt.figure('灰色直方图')
hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

```
![image](/image/flower.bmp)
![image](/image/RGB直方图.png)
![image](/image/灰色直方图.png)
