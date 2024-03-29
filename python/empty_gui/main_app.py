# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:21:08 2019

@author: danaukes
"""

import os
import sys
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import PyQt5.QtWidgets as qw
from empty_gui.matplotlib_widget import GraphView
import empty_gui
import empty_gui.empty_main_widget as de
import  numpy

app = qw.QApplication(sys.argv)
app.setWindowIcon(qg.QIcon('python/empty_gui/files/logo_4_1_icon.ico'))

main_window = de.MainWindow()
#    widget = Widget()
#tw= de.TextWidget()
widget = GraphView()
t = numpy.r_[0:100]
y = numpy.sin(t)
widget.plot(t,y)
main_window.setCentralWidget(widget)
main_window.show()
app.exec_()
sys.exit()    