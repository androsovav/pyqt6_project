import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

#path0 = "C:\\Users\\Val\\Downloads\\3210.txt"
path0 = "channel-1.txt"

#file_data = pd.read_csv(path0, delimiter='\t', header=None, dtype=np.float64, decimal=',')
file_data = pd.read_csv(path0, delimiter=' ', header=None, dtype=np.float64, decimal='.')

#print(file_data)
#print(file_data.values.T)

x = -file_data.values.T[1]
#print(np.shape(x))

b, a = signal.butter(3, 0.1) #0.01
y = signal.filtfilt(b, a, x)

peaks2, _ = signal.find_peaks(x, prominence=0.9)      # BEST!
peaks2b, _ = signal.find_peaks(-x, prominence=0.9)
peaks3, _ = signal.find_peaks(y, prominence=0.9)
peaks3b, _ = signal.find_peaks(-y, prominence=0.9)

peaks2 = np.sort(np.append(peaks2, peaks2b))
peaks3 = np.sort(np.append(peaks3, peaks3b))

print(peaks2)
print(peaks3)

plt.subplot(1, 2, 1)
plt.plot(peaks2, x[peaks2], "ob"); plt.plot(x); plt.legend(['prominence'])
plt.subplot(1, 2, 2)
plt.plot(peaks3, y[peaks3], "vg"); plt.plot(y); plt.legend(['prominence'])

np.savetxt('fltflt.txt', np.c_[file_data.values.T[0], y])

plt.show()



