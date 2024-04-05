import numpy as np
import matplotlib.pyplot as plt

# Adjusted values of r(i), p(i), and k(i)
r_values = [0.06029142-0.14682007j , 0.06029142+0.14682007j, -0.06029459+0.02518904j,
 -0.06029459-0.02518904j]

p_values = [0.88475217+0.0445749j,  0.88475217-0.0445749j , 0.94427798+0.11485352j,
 0.94427798-0.11485352j]

k_values = [2.19006287e-05, 0, 0, 0]

# Time indices
n_values = np.arange(31)  # n values up to 30

# Compute h(n)
hn_values = np.zeros_like(n_values, dtype=np.complex128)
for n in n_values:
    for i in range(len(r_values)):
        hn_values[n] += r_values[i] * (p_values[i] ** n)
    for j in range(len(k_values)):
        if n - j >= 0:
            hn_values[n] += k_values[j]

# Compute the frequency response using FFT
N = len(hn_values)
Hk_values = np.fft.fft(hn_values)

# Frequency values
freq = np.fft.fftfreq(N)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(freq, np.abs(Hk_values))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Filter Frequency Response')
plt.grid(True)
plt.show()

