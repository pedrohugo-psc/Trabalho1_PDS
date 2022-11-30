import numpy as np
import matplotlib.pyplot as plt

fs = 40 # frequência de amostragem
ps = 1/fs # período de amostragem
n = np.arange(0,20,ps) # tempo
print(n)


x1 = np.cos(0.2*np.pi*n)
x2 = np.cos(0.4*np.pi*n + np.pi/2)
x3 = np.cos(0.8*np.pi*n + np.pi/5)

x = x1 + x2 + x3

plt.figure(1)
plt.title("Sinal Original")
plt.plot(n,x)

fft_transformada = np.fft.fft(x)
print(np.abs(fft_transformada))
freq = np.fft.fftfreq(len(fft_transformada),ps)
print(freq)

plt.figure(2)
plt.title("Sinal da Transfomada de Fourier de x[n]")
plt.plot(freq[freq > 0],np.abs(fft_transformada[freq > 0]))

plt.figure(3)
plt.title("Normalizando o Sinal da Transfomada de Fourier de x[n]")
plt.plot(freq[freq > 0],np.abs(fft_transformada[freq > 0])*1/len(x))

plt.figure(4)
plt.title("Fase do Sinal da Transfomada de Fourier de x[n]")
plt.plot(freq,np.angle(fft_transformada))

plt.show()



