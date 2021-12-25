import math
import pprint
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
sampFreq, sound = wavfile.read('Trash/17.wav')


length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
signal = sound[:]


# plt.plot(time, signal )
# plt.xlabel("time, s [right channel]")
# plt.ylabel("signal, relative units")
# plt.tight_layout()
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
print((freq))
# print(fft_spectrum_abs)
#
# plt.plot(freq, fft_spectrum_abs,'r')
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")
#
# #
# for i in range(len(freq)):
#     if  i < 5000  :# (1)
#         fft_spectrum[i] =0
#
#
# #
# #
# #
# #
# fig1=plt.figure()
# fft_spectrum_abs = np.abs(fft_spectrum)
# plt.plot(freq, fft_spectrum_abs,'b')
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")
# plt.show()
#

# newSound = np.fft.irfft(fft_spectrum)

# wavfile.write("new.wav", sampFreq, newSound.astype(np.int16))






