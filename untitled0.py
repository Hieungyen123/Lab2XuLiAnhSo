# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KblbWq8Zjq4Ojt_LOlU194yeHWePu7xp
"""

#1.5. Thay đổi ảnh với Contrast Stretching
from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/baby.jpeg').convert('L')
iml= np.asarray (img)

b = iml.max()
a = iml.min()
print (a, b)

c = iml.astype (float)

im2 = 255 * (c - a) / (b - a)

im3 = Image.fromarray(im2)

img.show()
im3.show()
plt.imshow(im3)
plt.show()

# 1.6.1. Biến đổi ảnh với Fast Fourier
from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/baby.jpeg').convert('L')
im1= np.asarray (img)

c = abs(scipy.fftpack.fft2(im1))

d = scipy.fftpack.fftshift(c)
d = d.astype(float)

im3 = Image.fromarray(d)

img.show()
im3.show()
plt.imshow(im3)
plt.show()

#1.6.2. Lọc ảnh trong miền tần suất\
#Butterworth Lowpass Filter

from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/baby.jpeg').convert('L')
im1= np.asarray (img)

c = abs(scipy.fftpack.fft2(im1))

d = scipy.fftpack.fftshift(c)

M = d.shape[0]
N = d.shape[1]

H = np.ones((M, N))

center1 = M/2
center2 = N/2
d_0 = 30.0
t1 = 1
t2 = 2 * t1

for i in range(1, M):
  for j in range(1, N):
    r1 = (i - center1)**2 + (j - center2)**2
    r = math.sqrt(r1)

    if r > d_0:
      H[i, j] = 1/(1 + (r/d_0)**t1)

H = H.astype(float)
H = Image.fromarray(H)

con = d * H
e = abs(scipy.fftpack.ifft2(con))

e = e.astype(float)
im3 = Image.fromarray(e)

img.show()
im3.show()
plt.imshow(im3)
plt.show()

#1.6.2. Lọc ảnh trong miền tần suất\
#Butterworth highpass Filter
from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/balloons_noisy.png').convert('L')
im1= np.asarray (img)

c = abs(scipy.fftpack.fft2(im1))

d = scipy.fftpack.fftshift(c)

M = d.shape[0]
N = d.shape[1]

H = np.ones((M, N))

center1 = M/2
center2 = N/2
d_0 = 30.0
t1 = 1
t2 = 2 * t1

for i in range(1, M):
  for j in range(1, N):
    r1 = (i - center1)**2 + (j - center2)**2
    r = math.sqrt(r1)

    if r > d_0:
      H[i, j] = 1/(1 + (r/d_0)**t2)

H = H.astype(float)
H = Image.fromarray(H)

con = d * H
e = abs(scipy.fftpack.ifft2(con))

e = e.astype(float)
im3 = Image.fromarray(e)

img.show()
im3.show()
plt.imshow(im3)
plt.show()

#1.1. Biến đổi cường độ ảnh (Image inverse transformation)
import math
from PIL import Image
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

#open a grayscale image
lmg = Image.open('drive/MyDrive/exercise/pagoda.jpg').convert('L')

#convert image 1l into an ndarray
im_1 = np.asarray (lmg)

#inversion operation
im_2 = 255 - im_1

#convert image 2 from ndarray to image
new_img = Image.fromarray(im_2)

plt.show ()
plt.imshow(new_img)
plt.show()

# 1.2. Thay đổi chất lượng ảnh với Power law (Gamma-Correction)
import math
from PIL import Image
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

#open a grayscale image
img = Image.open('drive/MyDrive/exercise/quang_ninh.jpg').convert('L')

#convezt image 1 into an ngazzay
im_1 = np.asarray(img)

#init gamna
gamma = 0.5

#convert ndarray from int to float
b1 = im_1.astype(np.uint8)

#find maximum value in bl
b2 = np.max (b1)

#b3 is normalized
b3 = b1/b2

#b2 gamma correction exponent is computed
b2 = np.log(b3) * 5

#gamma correction is computed
c = np.exp(b2)*255.0

#c1 is converted to type int
c1 = c.astype(np.uint8)
d = Image.fromarray(c1)

img.show()
d.show()
plt.imshow(d)
plt.show()

# 1.3. Thay đổi cường độ điểm ảnh với Log Transformation
import math
from PIL import Image
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/flower.jpeg').convert('L')

im_1 = np.asarray(img)

b1 = im_1.astype(float)

b2 = np.max(b1)

c = (128.0 * np.log(1 + b1)) / np.log(1 + b2)

c1 = c.astype(np.uint8)

d = Image.fromarray(c1)

img.show()
d.show()
plt.imshow(d)
plt.show()

# 1.4. Histogram equalization
import math
from PIL import Image
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('drive/MyDrive/exercise/quang_ninh.jpg').convert('L')

im_1 = np.asarray(img)

b1 = im_1.flatten()

hist, bins = np.histogram(im_1, 256, [0, 255])
cdf = hist.cumsum()

cdf_m = np.ma.masked_equal(cdf,0)

num_cdf_m = (cdf_m - cdf_m.min()) * 255
den_cdf_m = (cdf.max() - cdf_m.min())

cdf_m = num_cdf_m / den_cdf_m
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

im_2 = cdf[b1]
im_3 = np.reshape(im_2, im_1.shape)

im_4 = Image.fromarray(im_3)

img.show()
im_4.show()
plt.imshow(im_4)
plt.show()