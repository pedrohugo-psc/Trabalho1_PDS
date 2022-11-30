import numpy as np
import matplotlib.pyplot as plt

freq_amos = 1000 # frequência de amostragem
period_amos = 1/freq_amos # período de amostragem
t = np.arange(0,200,period_amos)
print(t)