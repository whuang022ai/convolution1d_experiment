import numpy as np
from scipy import signal
from PIL import Image
from matplotlib import pyplot as plt

img = Image.open("lenna.jpg").convert("L")
plt.imshow(img, cmap="gray")
plt.show()
g = np.asarray([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
img_filtered = signal.convolve2d(img, g)
plt.imshow(img_filtered, cmap="gray", vmin=0, vmax=255)
plt.show()
