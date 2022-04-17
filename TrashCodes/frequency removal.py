# import math
# import pprint
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.io import wavfile
# sampFreq, sound = wavfile.read('Trash/17.wav')
#
#
# length_in_s = sound.shape[0] / sampFreq
# time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
# signal = sound[:]
#
#
# # plt.plot(time, signal )
# # plt.xlabel("time, s [right channel]")
# # plt.ylabel("signal, relative units")
# # plt.tight_layout()
# fft_spectrum = np.fft.rfft(signal)
# freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
# print((freq))
# # print(fft_spectrum_abs)
# #
# # plt.plot(freq, fft_spectrum_abs,'r')
# # plt.xlabel("frequency, Hz")
# # plt.ylabel("Amplitude, units")
# #
# # #
# # for i in range(len(freq)):
# #     if  i < 5000  :# (1)
# #         fft_spectrum[i] =0
# #
# #
# # #
# # #
# # #
# # #
# # fig1=plt.figure()
# # fft_spectrum_abs = np.abs(fft_spectrum)
# # plt.plot(freq, fft_spectrum_abs,'b')
# # plt.xlabel("frequency, Hz")
# # plt.ylabel("Amplitude, units")
# # plt.show()
# #
#
# # newSound = np.fft.irfft(fft_spectrum)
#
# # wavfile.write("new.wav", sampFreq, newSound.astype(np.int16))
#
#
#
#
#
#

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
