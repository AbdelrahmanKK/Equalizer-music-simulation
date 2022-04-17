#this version is fine but the spectro is outside the tab and the sliders are vertical
import sys
from PyQt5.QtWidgets import *
import time
import threading
import sys
import copy
import wave
import contextlib

from PyQt5.QtWidgets import (QWidget,
                             QPushButton, QApplication, QGridLayout)
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound
from PyQt5.QtMultimedia import QSound
import keyboard
import time
import numpy as np
import sounddevice
import sys
from PyQt5.QtWidgets import (QWidget,
                             QPushButton, QApplication, QGridLayout)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.io import wavfile
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import sys
import matplotlib
import math

matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5 import QtCore, QtWidgets
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
import sys
import shutil
import os
import csv
import datetime
import numpy as np
import pandas as pd
import pyqtgraph.exporters
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore, QtGui, QtWidgets
import logging

from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
from scipy import signal
import matplotlib.pyplot as plt
import pyqtgraph.exporters
from matplotlib.animation import FuncAnimation


# logger = logging.getLogger('equalizer')
# logger.setLevel(logging.DEBUG)


# formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(levelno)s:%(name)s:%(lineno)d:%(filename)s:%(funcName)s:%(message)s:')

# file_handler = logging.FileHandler('Equalizer.log')
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)


###############################################################

class GuitarString:
    def __init__(self, pitch, starting_sample, sampling_freq, stretch_factor):
        """Inits the guitar string."""
        self.pitch = pitch
        self.starting_sample = starting_sample
        self.sampling_freq = sampling_freq
        self.stretch_factor = stretch_factor
        self.init_wavetable()
        self.current_sample = 0
        self.previous_value = 0

    def init_wavetable(self):
        """Generates a new wavetable for the string."""
        wavetable_size = self.sampling_freq // int(self.pitch)
        self.wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(float)

    def get_sample(self):
        """Returns next sample from string."""
        if self.current_sample >= self.starting_sample:
            current_sample_mod = self.current_sample % self.wavetable.size
            randomVariable = np.random.binomial(1, 1 - 1 / self.stretch_factor)
            if randomVariable == 0:
                self.wavetable[current_sample_mod] = 0.5 * (self.wavetable[current_sample_mod] + self.previous_value)
            sample = self.wavetable[current_sample_mod]
            self.previous_value = sample
            self.current_sample += 1
        else:
            self.current_sample += 1
            sample = 0
        return sample


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1162, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setHandleWidth(10)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_signal = PlotWidget(self.layoutWidget)
        self.graphicsView_signal.setMinimumSize(QtCore.QSize(600, 0))
        self.graphicsView_signal.setObjectName("graphicsView_signal")
        self.verticalLayout.addWidget(self.graphicsView_signal)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.play_pause = QtWidgets.QPushButton(self.layoutWidget)
        self.play_pause.setText("play/pause")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/play1.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ICONS/pause2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.play_pause.setIcon(icon)
        self.play_pause.setIconSize(QtCore.QSize(30, 30))
        self.play_pause.setObjectName("play_pause")
        self.horizontalLayout.addWidget(self.play_pause)
        self.reset = QtWidgets.QPushButton(self.layoutWidget)
        self.reset.setText("Reset")
        icon = QtGui.QIcon()
        self.reset.setIcon(icon)
        self.reset.setIconSize(QtCore.QSize(30, 30))
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.labelVolume = QtWidgets.QLabel(self.layoutWidget)
        Volumefont = QtGui.QFont()
        Volumefont.setPointSize(9)
        Volumefont.setBold(True)
        Volumefont.setWeight(75)
        self.labelVolume.setFont(Volumefont)
        self.labelVolume.setObjectName("labelVolume")
        self.gridLayout.addWidget(self.labelVolume, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalSlider_volume = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_volume.setProperty("value", 50)
        self.horizontalSlider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_volume.setObjectName("horizontalSlider_volume")
        self.gridLayout.addWidget(self.horizontalSlider_volume, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        stretches = [1, 1, 1, 2, 1]
        for i in range(5):
            self.horizontalLayout.setStretch(i, stretches[i])

        # self.horizontalLayout.setStretch(0, 1)
        # self.horizontalLayout.setStretch(1, 1)
        # self.horizontalLayout.setStretch(2, 1)
        # self.horizontalLayout.setStretch(3, 2)
        # self.horizontalLayout.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.figure_Spectrogram = Figure(figsize=(3, 3), dpi=100)
        self.axes_Spectrogram = self.figure_Spectrogram.add_subplot()
        self.canvas_Spectrogram = FigureCanvas(self.figure_Spectrogram)
        self.canvas_Spectrogram.figure.set_facecolor("#e5e5e6")  # applying the GUI's color on matplotlib to look nice

        self.splitter.setMinimumSize(QtCore.QSize(60, 200))
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget1)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.equalizerTab = QtWidgets.QWidget()
        self.equalizerTab.setObjectName("equalizerTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.equalizerTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSlider_1 = QtWidgets.QSlider(self.equalizerTab)
        self.verticalSlider_1.setProperty("value", 50)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.verticalLayout_2.addWidget(self.verticalSlider_1, 0, QtCore.Qt.AlignHCenter)
        self.label_piano = QtWidgets.QLabel(self.equalizerTab)
        self.label_piano.setObjectName("label_piano")
        self.verticalLayout_2.addWidget(self.label_piano)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalSlider_2 = QtWidgets.QSlider(self.equalizerTab)
        self.verticalSlider_2.setProperty("value", 50)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalLayout_3.addWidget(self.verticalSlider_2, 0, QtCore.Qt.AlignHCenter)
        self.label_flute = QtWidgets.QLabel(self.equalizerTab)
        self.label_flute.setObjectName("label_flute")
        self.verticalLayout_3.addWidget(self.label_flute, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalSlider_3 = QtWidgets.QSlider(self.equalizerTab)
        self.verticalSlider_3.setProperty("value", 50)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_4.addWidget(self.verticalSlider_3, 0, QtCore.Qt.AlignHCenter)
        self.label_guitar = QtWidgets.QLabel(self.equalizerTab)
        self.label_guitar.setObjectName("label_guitar")
        self.verticalLayout_4.addWidget(self.label_guitar, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.equalizerTab, "")
        self.pianoTab = QtWidgets.QWidget()
        self.pianoTab.setObjectName("pianoTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.pianoTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_keyboardControls1 = QtWidgets.QLabel(self.pianoTab)
        self.label_keyboardControls1.setObjectName("label_keyboardControls1")
        self.verticalLayout_8.addWidget(self.label_keyboardControls1, 0, QtCore.Qt.AlignHCenter)
        self.label_pianoKeys = QtWidgets.QLabel(self.pianoTab)
        self.label_pianoKeys.setObjectName("label_pianoKeys")
        self.verticalLayout_8.addWidget(self.label_pianoKeys)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.label_pianoImage = QtWidgets.QLabel(self.pianoTab)
        self.label_pianoImage.setText("")
        self.label_pianoImage.setPixmap(QtGui.QPixmap("piano.jpeg"))
        self.label_pianoImage.setScaledContents(True)
        self.label_pianoImage.setObjectName("label_pianoImage")
        self.horizontalLayout_5.addWidget(self.label_pianoImage)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.pianoTab, "")
        self.guitarTab = QtWidgets.QWidget()
        self.guitarTab.setObjectName("guitarTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.guitarTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_keyboardControls2 = QtWidgets.QLabel(self.guitarTab)
        self.label_keyboardControls2.setObjectName("label_keyboardControls2")
        self.verticalLayout_10.addWidget(self.label_keyboardControls2, 0, QtCore.Qt.AlignHCenter)
        self.label_guitarKeys = QtWidgets.QLabel(self.guitarTab)
        self.label_guitarKeys.setObjectName("label_guitarKeys")
        self.verticalLayout_10.addWidget(self.label_guitarKeys, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.label_guitarImage = QtWidgets.QLabel(self.guitarTab)
        self.label_guitarImage.setText("")
        self.label_guitarImage.setPixmap(QtGui.QPixmap("guitar.jpeg"))
        self.label_guitarImage.setScaledContents(True)
        self.label_guitarImage.setObjectName("label_guitarImage")
        self.horizontalLayout_6.addWidget(self.label_guitarImage)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.guitarTab, "")
        self.drumsTab = QtWidgets.QWidget()
        self.drumsTab.setObjectName("drumsTab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.drumsTab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_keyboardControls3 = QtWidgets.QLabel(self.drumsTab)
        self.label_keyboardControls3.setObjectName("label_keyboardControls3")
        self.verticalLayout_11.addWidget(self.label_keyboardControls3, 0, QtCore.Qt.AlignHCenter)
        self.label_drumsKeys = QtWidgets.QLabel(self.drumsTab)
        self.label_drumsKeys.setObjectName("label_drumsKeys")
        self.verticalLayout_11.addWidget(self.label_drumsKeys, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.label_drumImage = QtWidgets.QLabel(self.drumsTab)
        self.label_drumImage.setText("")
        self.label_drumImage.setPixmap(QtGui.QPixmap("drums.jpeg"))
        self.label_drumImage.setScaledContents(True)
        self.label_drumImage.setObjectName("label_drumImage")
        self.horizontalLayout_7.addWidget(self.label_drumImage)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.drumsTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.addWidget(self.canvas_Spectrogram)  ##########
        # spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 4)
        # self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(1, 3)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.setNativeMenuBar(False)

        ############################################################
        self.player = QMediaPlayer()

        self.sliders = [self.verticalSlider_1, self.verticalSlider_2, self.verticalSlider_3]

        # self.verticalSlider_4, self.verticalSlider_5, self.verticalSlider_6]
        for n in range(3):  # sliders congifuration
            self.sliders[n].setSingleStep(1)
            self.sliders[n].setMinimum(0)
            self.sliders[n].setMaximum(10)
            self.sliders[n].setValue(5)

        self.horizontalSlider_volume.setMinimum(0)
        self.horizontalSlider_volume.setMaximum(100)
        self.horizontalSlider_volume.setSingleStep(5)
        self.horizontalSlider_volume.setValue(50)  # set the volume to be in the middle
        self.player.setVolume(self.horizontalSlider_volume.value())

        self.verticalSlider_1.sliderReleased.connect(lambda: self.equalizer(0, 1, 2000))
        self.verticalSlider_2.sliderReleased.connect(lambda: self.equalizer(1, 2100, 5000))
        # this is commented self.verticalSlider_4.sliderReleased.connect(lambda: self.equalizer(3, 5001,  7000))
        # self.verticalSlider_5.sliderReleased.connect(lambda: self.equalizer(4, 7001,  10000))
        # self.verticalSlider_6.sliderReleased.connect(lambda: self.equalizer(5, 10001, 12000))
        self.horizontalSlider_volume.valueChanged[int].connect(lambda: self.volumeControl())

        self.verticalSlider_3.sliderReleased.connect(lambda: self.equalizer(2, 6001, 9000))

        self.data = []
        self.samplingFrequency = 0
        self.sound = []
        self.length_in_seconds = 0
        self.time = 0
        self.signal = 0
        self.fft_spectrumCurrent = 0
        self.fft_spectrumOriginal = 0
        self.frequencyBins = []
        self.fileCount = 0
        self.originalPath = ""
        self.duration = 0
        self.updatePlotIndex = 0
        # self.data_line=[]

        self.play_pause_flag = True

        self.pens = [pg.mkPen('r'), pg.mkPen('g'), pg.mkPen('b'), pg.mkPen('y')]
        self.palette = ['viridis', 'plasma', 'Blues', 'Greys', 'pink']  # spectrogram palettes

        self.timer_updatePlot = QtCore.QTimer()  ##timers configurarion
        self.timer_fileDuration = QtCore.QTimer()  ##timers configurarion
        self.timer_fileDuration.timeout.connect(lambda: self.timer_updatePlot.stop())
        self.timer_updatePlot.setInterval(5)
        self.timer_updatePlot.timeout.connect(self.update_plot_data)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)  ##set default tap to be equalizer
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionOpen.triggered.connect(lambda: self.open())
        self.play_pause.clicked.connect(lambda: self.play_pauseFunction())
        self.reset.clicked.connect(lambda: self.resetFunction())
        self.virtual_Instruments_thread_Function()  ##start virtual instruments
        ########################################
        self.guitar_sounds = []  # storing guitar notes
        self.guitar()  ##calculating guitar notes
        ##############################

        self.pianoSounds = []  # storing piano notes
        self.piano()  ##calculating piano notes
        #######################
        self.drumSounds = []  # storing drums notes
        self.drum()  ##calculating drums notes

    def drum(self):
        notes = [.9, .1, .2, .3, .4, .5, .6, .7, .8, .9]
        for note in notes:
            freq_sample = 3000
            stretch_factor = 2
            wavetable_size = freq_sample // 80
            wavetable = np.ones(wavetable_size)
            samples = []
            current_sample = 0
            previous_value = 0
            while len(samples) < freq_sample:
                randomVariable = np.random.binomial(1, note)
                sign = float(randomVariable == 1) * 2 - 1
                stretch = np.random.binomial(1, 1 - 1 / stretch_factor)
                if stretch == 0:
                    wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)
                samples.append(wavetable[current_sample])
                previous_value = samples[-1]
                current_sample += 1
                current_sample = current_sample % wavetable.size
            song = np.array(samples)
            self.drumSounds.append(song)

    def piano(self, duration=1):
        sample_rate = 44100

        list = [294, 329, 349, 370, 392, 416, 440, 467, 494]
        for freq in list:
            amplitude = 4096
            t = np.linspace(0, duration, int(sample_rate * duration))
            wave = 0.5 * amplitude * np.sin(np.pi * freq * t) * np.exp(-0.0004 * 2 * np.pi * freq * t)
            divided = 2
            for iterator in range(4, 15, 2):
                wave += 10 * amplitude * np.sin(iterator * np.pi * freq * t) * np.exp(
                    -0.0001 * 2 * np.pi * freq * t) / divided
                divided *= 2
            wave += wave * wave * wave
            wave *= 1 + (16 * t * np.exp(-6 * t))

            audio = wave * (2 ** 15 - 1) / np.max(np.abs(wave))
            audio = audio.astype(np.int16)
            self.pianoSounds.append(audio)

    def guitar(self):
        frequenciesOfString = [[98], [123], [147], [196], [294], [392], [294], [196], [100],
                               [400]]  ## specify any notes we need
        for frequency in frequenciesOfString:
            samplingFrequency = 7000
            unit_delay = 0  # samplingFrequency//3## return int not float
            delays = [unit_delay * _ for _ in range(len(frequency))]
            stretch_factors = [2 * f / 98 for f in frequency]
            strings = []
            for freq, delay, stretch_factor in zip(frequency, delays, stretch_factors):
                string = GuitarString(freq, delay, samplingFrequency, stretch_factor)
                strings.append(string)
            guitar_sound = [sum(string.get_sample() for string in strings) for _ in range(samplingFrequency * 6)]
            self.guitar_sounds.append(guitar_sound)

    def virtual_Instruments_thread_Function(self):
        virtual_Instruments_thread = threading.Thread(target=self.virtualInstruments)
        virtual_Instruments_thread.start()

    def virtualInstruments(self):
        while (True):
            notes = keyboard.read_key()
            if notes == 'q':
                sounddevice.play(self.pianoSounds[0])

            elif notes == 'w':
                sounddevice.play(self.pianoSounds[1])

            elif notes == 'e':
                sounddevice.play(self.pianoSounds[2])

            elif notes == 'r':
                sounddevice.play(self.pianoSounds[3])
            elif notes == 't':
                sounddevice.play(self.pianoSounds[4])

            elif notes == 'a':
                sounddevice.play(self.guitar_sounds[0], samplerate=7000)

            elif notes == 's':
                sounddevice.play(self.guitar_sounds[1], samplerate=7000)

            elif notes == 'd':
                sounddevice.play(self.guitar_sounds[2], samplerate=7000)

            elif notes == 'f':
                sounddevice.play(self.guitar_sounds[3], samplerate=7000)

            elif notes == 'g':
                sounddevice.play(self.guitar_sounds[4], samplerate=7000)

            elif notes == 'z':
                sounddevice.play(self.drumSounds[0], samplerate=3000)

            elif notes == 'x':
                sounddevice.play(self.drumSounds[1], samplerate=3000)


            elif notes == 'c':
                sounddevice.play(self.drumSounds[2], samplerate=3000)


            elif notes == 'v':
                sounddevice.play(self.drumSounds[3], samplerate=3000)


            elif notes == 'b':
                sounddevice.play(self.drumSounds[4], samplerate=3000)

            time.sleep(.5)

    def open(self):
        self.player.setVolume(50)  # reset
        self.horizontalSlider_volume.setValue(50)  # reset
        for n in range(3):
            self.sliders[n].setValue(5)  # reset

        path = QFileDialog.getOpenFileName()[0]  # get file path
        self.originalPath = path  # store original path
        filename = path
        with contextlib.closing(wave.open(filename, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            self.duration = frames / float(rate)
            # logger.info(self.duration)

        self.samplingFrequency, self.soundOriginaal = wavfile.read(path)
        self.length_in_seconds = self.soundOriginaal.shape[0] / self.samplingFrequency
        self.time = np.arange(self.soundOriginaal.shape[0]) / self.soundOriginaal.shape[0] * self.length_in_seconds

        if len(self.soundOriginaal.shape) == 2:  ##if the file is stereo ,, make it mono
            self.signalOriginaal = self.soundOriginaal[:, 1]
        else:
            self.signalOriginaal = self.soundOriginaal[:]

        self.fft_spectrumOriginal = np.fft.rfft(self.signalOriginaal)
        self.frequencyBins = np.fft.rfftfreq(self.signalOriginaal.size, d=1. / self.samplingFrequency)

        self.timer_fileDuration.setInterval(int(self.duration * (10 ** 3)))  ##initializing timer
        self.timer_fileDuration.start()
        self.playfile(path)
        self.plotting()
        self.play()

    def equalizer(self, sliderIndex, minFreqency, maxFreqency):
        self.timer_fileDuration.setInterval(int(self.duration * (10 ** 3)))  # timer reset
        self.timer_fileDuration.start()
        self.timer_updatePlot.start()

        # self.fft_spectrumCurrent[(self.frequencyBins >= minFreqency) & (self.frequencyBins <= maxFreqency)] =\
        #     self.fft_spectrumOriginal[(self.frequencyBins >= minFreqency) & (self.frequencyBins <= maxFreqency)] * (self.sliders[sliderIndex].value()/5)

        for i, frequency in enumerate(self.frequencyBins):
            if frequency > minFreqency and frequency < maxFreqency:
                self.fft_spectrumCurrent[i] = self.fft_spectrumOriginal[i] * (
                        self.sliders[sliderIndex].value() / 5)  ##amplitude * gain from slider

        newSound = np.fft.irfft(self.fft_spectrumCurrent)  ##back to time domain
        directory = "/Users/mn3n3/Documents/GitHub/github-equalizer/Trash/trash" + str(self.fileCount) + ".wav"
        wavfile.write(directory, self.samplingFrequency, newSound.astype(np.int16))
        path = os.path.abspath(directory)
        self.playfile(path)
        self.fileCount += 1

    def playfile(self, path):
        samplingFrequency, self.sound = wavfile.read(path)
        if len(self.sound.shape) == 2:  # if stereo ,,, make it mono
            self.signal = self.sound[:, 1]
        else:
            self.signal = self.sound[:]

        self.fft_spectrumCurrent = np.fft.rfft(self.signal)

        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.play()
        self.plotSpectrogram()

    def play_pauseFunction(self):
        if (self.play_pause_flag == 0):
            self.pause()
        else:
            self.play()

    def pause(self):
        self.player.setMuted(True)
        self.timer_updatePlot.stop()
        self.timer_fileDuration.stop()
        self.play_pause_flag = 1

    def play(self):
        self.player.setMuted(False)
        self.timer_updatePlot.start()
        self.timer_fileDuration.start()
        self.play_pause_flag = 0

    def volumeControl(self):
        self.player.setVolume(self.horizontalSlider_volume.value())

    def resetFunction(self):
        self.player.setVolume(50)
        self.horizontalSlider_volume.setValue(50)
        for n in range(3):
            self.sliders[n].setValue(5)

        self.updatePlotIndex = 0
        self.timer_fileDuration.setInterval(int(self.duration * (10 ** 3)))
        self.timer_fileDuration.start()
        self.timer_updatePlot.start()
        self.playfile(self.originalPath)

    def plotting(self):
        self.data = self.signal[:] / max(self.signal)  ##normlization
        self.data_line = self.graphicsView_signal.plot(self.time, self.data, pen=self.pens[3])
        self.updatePlotIndex = 0
        self.timer_updatePlot.start()  ##signal moves

    def update_plot_data(self):
        self.timeUpdate = self.time[:self.updatePlotIndex]
        self.signalUpdate = self.data[:self.updatePlotIndex]
        self.updatePlotIndex += 50
        self.graphicsView_signal.plotItem.setXRange(max(self.timeUpdate, default=0) - 1,
                                                    max(self.timeUpdate, default=0))
        self.data_line.setData(self.timeUpdate, self.signalUpdate)

    def plotSpectrogram(self):
        self.axes_Spectrogram.clear()
        self.axes_Spectrogram.specgram(self.signal)
        self.axes_Spectrogram.set_xticks([])
        self.axes_Spectrogram.set_yticks([])
        self.canvas_Spectrogram.draw()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelVolume.setText(_translate("MainWindow", "Voulme"))
        self.label_piano.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">1 Hz -2 kHz<br/>piano</span></p></body></html>"))
        self.label_flute.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2.1 kHz -5 kHz<br/>flute</span></p></body></html>"))
        self.label_guitar.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">6 kHz -10 kHz<br/>guitar</span></p></body></html>"))
        # self.label_violin.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">200 Hz -3.5 kHz<br/>Violin</span></p></body></html>"))
        # self.label_piano.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">1 kHz -4.1 kHz<br/>Piano</span></p></body></html>"))
        # self.label_harmonica.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">300 Hz -10 kHz<br/>Harmonica</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.equalizerTab), _translate("MainWindow", "Equalizer"))
        self.label_keyboardControls1.setText(_translate("MainWindow",
                                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Keyboard Controls</span></p></body></html>"))
        self.label_pianoKeys.setText(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Q W E R T</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pianoTab), _translate("MainWindow", "Piano"))
        self.label_keyboardControls2.setText(_translate("MainWindow",
                                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Keyboard Controls</span></p></body></html>"))
        self.label_guitarKeys.setText(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">A S D F G</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.guitarTab), _translate("MainWindow", "Guitar"))
        self.label_keyboardControls3.setText(_translate("MainWindow",
                                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Keyboard Controls</span></p></body></html>"))
        self.label_drumsKeys.setText(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Z X C V B</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drumsTab), _translate("MainWindow", "Drums"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
