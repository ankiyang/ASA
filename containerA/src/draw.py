import datetime
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


def draw_frequency(data):
    df0 = pd.read_csv(data)
    df_avg = df.dropna().mean()
    date = df_avg.index.to_datetime()
    temp = (df_avg['TMAX'] + df_avg['TMIN']) / 20.
    N = len(temp)
    fig, ax = plt.subplots(1, 1, figsize=(6, 3))
    plt.plot(ax=ax, lw=.5)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.plot(t, s)
    plt.show()


    #Applying Fourier Transform
    fft = fftpack.fft(s)

    #Time taken by one complete cycle of wave (seconds)
    T = t[1] - t[0] 

    #Calculating sampling frequency
    F = 1/T

    N = s.size

    #Avoid aliasing by multiplying sampling frequency by 1/2 
    f = np.linspace(0, 0.5*F, N)

    #Convert frequency to mHz
    f = f * 1000

    #Plotting frequency domain against amplitude
    sns.set_style("darkgrid")
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [mHz]")
    plt.plot(f[:N // 2], np.abs(fft)[:N // 2])  
    plt.show()  