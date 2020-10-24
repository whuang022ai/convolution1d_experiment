import numpy as np
from scipy import signal as tool
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(5, sharex=True, sharey=True, figsize=(6, 12))


signal = np.array(
    [
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0],
    ]
)
hpf = np.array([[0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0]])
lpf = np.array([[0, 0, 2, 2, 2, 0, 0], [0, 0, 2, 2, 2, 0, 0], [0, 0, 2, 2, 2, 0, 0]])


out1 = tool.convolve2d(signal, hpf, boundary="symm", mode="same")
print(out1)
out2 = tool.convolve2d(signal, lpf, boundary="symm", mode="same")
print(out2)

x = range(0, len(signal))
values = signal
img= ax[0].imshow(values, cmap="gray", interpolation="nearest")
ax[0].set_title("Original Signal")
plt.colorbar(img, ax=ax[0])
x = range(0, len(hpf))
values = hpf
img1=ax[1].imshow(values, cmap="gray", interpolation="nearest")
ax[1].set_title("High Pass Filter Kernel (1Hz)")
plt.colorbar(img1, ax=ax[1])
x = range(0, len(out1))
values = out1
img2=ax[2].imshow(values, cmap="gray", interpolation="nearest")
ax[2].set_title("Filtered Output")
plt.colorbar(img2, ax=ax[2])
x = range(0, len(lpf))
values = lpf
img3=ax[3].imshow(values, cmap="gray", interpolation="nearest")
ax[3].set_title("Low Pass Filter Kernel (0.333Hz)")
plt.colorbar(img3, ax=ax[3])
x = range(0, len(out2))
values = out2
img4=ax[4].imshow(values, cmap="gray", interpolation="nearest")
ax[4].set_title("Filtered Output")
plt.colorbar(img4, ax=ax[4])

plt.tight_layout()
plt.savefig("2d.png")

