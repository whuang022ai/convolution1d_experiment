import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(5, sharex=True, sharey=True, figsize=(6, 12))

signal = [0, 0, 0, 2, 2, 4, 2, 2, 0, 0, 0]
hpf = [0, 2, 0, 2, 0, 2, 0]
lpf = [0, 0, 2, 2, 2, 0, 0]


out1 = np.convolve(signal, hpf)
print(out1)
out2 = np.convolve(signal, lpf)
print(out2)

x = range(1, len(signal) + 1)
values = signal
ax[0].stem(x, values, use_line_collection=True, linefmt="grey")
ax[0].set_title("Original Signal")

for x, y in zip(x, values):
    ax[0].annotate(
        "{:.0f}".format(y),
        xy=(x, y),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
    )

x = range(1, len(hpf) + 1)
values = hpf
ax[1].stem(x, values, use_line_collection=True, linefmt="grey")
ax[1].set_title("High Pass Filter Kernel (1Hz)")

for x, y in zip(x, values):
    ax[1].annotate(
        "{:.0f}".format(y),
        xy=(x, y),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
    )

x = range(1, len(out1) + 1)
values = out1
ax[2].stem(x, values, use_line_collection=True, linefmt="grey")
ax[2].set_title(" Filtered of Signal")

for x, y in zip(x, values):
    ax[2].annotate(
        "{:.0f}".format(y),
        xy=(x, y),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
    )

x = range(1, len(lpf) + 1)
values = lpf
ax[3].stem(x, values, use_line_collection=True, linefmt="grey")
ax[3].set_title("Low Pass Filter Kernel (0.333Hz)")

for x, y in zip(x, values):
    ax[3].annotate(
        "{:.0f}".format(y),
        xy=(x, y),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
    )

x = range(1, len(out2) + 1)
values = out2
ax[4].stem(x, values, use_line_collection=True, linefmt="grey")
ax[4].set_title(" Filtered of Signal")

for x, y in zip(x, values):
    ax[4].annotate(
        "{:.0f}".format(y),
        xy=(x, y),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
    )
    
plt.tight_layout()
plt.savefig("1d.png")
