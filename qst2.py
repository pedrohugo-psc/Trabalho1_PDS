import numpy as np
import matplotlib.pyplot as plt

fs = 40 # frequência de amostragem
ps = 1/fs # período de amostragem
n = np.arange(0,40,ps)
n1 = np.arange(0,1,ps) # 40 amostras
n1_1 = np.pad(n1, (0,len(n) - len(n1)),'constant')
t = n*ps # tempo
M = 60

wn =  0.54 - 0.46 * np.cos((2*np.pi*n1_1)/M)

x1 = wn * np.cos(0.2*np.pi*(n-M-1))
x2 = wn * np.cos(0.4*np.pi*(n - 2*M - 2) - np.pi/2)
x3 = wn * np.cos(0.8*np.pi*n + np.pi/5)

x = x1 + x2 + x3

plt.figure(1)
plt.title("Sinal Original I")
plt.ylabel("Amplitude")
plt.xlabel("Tempo (s)")
plt.plot(t,x)

fft_transformada = np.fft.fft(x)
freq = np.fft.fftfreq(len(fft_transformada),ps)

plt.figure(2)
plt.title("Sinal da Transfomada de Fourier de x[n] I")
plt.ylabel("Magnitude")
plt.xlabel("Frequência (Hz)")
plt.plot(freq[freq > 0],np.abs(fft_transformada)[freq > 0])

N = len(n)
fn = np.arange(0,N)
plt.figure(3)
plt.title("Normalizando o Sinal da Transfomada de Fourier de x[n] I")
plt.ylabel("Magnitude")
plt.xlabel("Frequência normalizada")
plt.plot(fn[freq > 0]*2/N,np.abs(fft_transformada)[freq > 0])

plt.figure(4)
plt.title("Fase do Sinal da Transfomada de Fourier de x[n] I")
plt.plot(freq,np.angle(fft_transformada))

#--------------------------------------------------------------------#

fs_2 = 20000 # frequência de amostragem
ps_2 = 1/fs_2 # período de amostragem
n_2 = np.arange(0,40,ps_2) # 800000 amostras
n_2_1 = np.arange(0,1/500,ps_2) # 40 amostras
n_2_1_1 = np.pad(n1, (0,len(n_2) - len(n_2_1)),'constant')
t_2 = n_2 * ps_2 # tempo

wn =  0.54 - 0.46 * np.cos((2*np.pi*n_2_1_1)/M)

x1 = wn * np.cos(0.2*np.pi*(n_2-M-1))
x2 = wn * np.cos(0.4*np.pi*(n_2 - 2*M - 2) - np.pi/2)
x3 = wn * np.cos(0.8*np.pi*n_2 + np.pi/5)

x = x1 + x2 + x3

plt.figure(5)
plt.title("Sinal Original II")
plt.ylabel("Amplitude")
plt.xlabel("Tempo (s)")
plt.plot(t_2,x)

fft_transformada = np.fft.fft(x)
freq = np.fft.fftfreq(len(fft_transformada),ps_2)

plt.figure(6)
plt.title("Sinal da Transfomada de Fourier de x[n] II")
plt.ylabel("Magnitude")
plt.xlabel("Frequência (Hz)")
plt.plot(freq[freq > 0],np.abs(fft_transformada)[freq > 0])


plt.show()
