from PIL import Image, ImageEnhance

import numpy as np

from PyQt5.QtGui import QPixmap, QImage                                
from PyQt5.QtCore import Qt    

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

class GUILogic():
    def __init__(self,mainwindow, paths):
        self.mw = mainwindow
        self.paths = paths
        self.curr_idx = 0
        self.set_image(self.curr_idx)
        print(self.paths)
        self.mw.label_currnum.setText(str(self.curr_idx+1)+"/"+str(len(self.paths)))
        self.descision_made = False
        self.labels = []
        self.curr_label = 0

    
    
    def set_image(self, idx):
        if(idx > len(self.paths)):
            img = np.ones((100,100,3))
            self.mw.img.setText("Done")
        else:
            contrast = 10
            img = Image.open(self.paths[idx])
            enhancer = ImageEnhance.Contrast(img)
            factor = (contrast/100) +1
            img = enhancer.enhance(factor)
            img = np.array(img)
            minimum = img.min()
            maximum = img.max()
            img = (((img - minimum)/(maximum - minimum))*255).astype(np.uint8)
            img = np.tile(img[:,:,None],(1,1,3))
        qimage = QImage(img, img.shape[0], img.shape[1], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)                                                                                                                                                                               
        pixmap = pixmap.scaled(421,431, Qt.KeepAspectRatio) 
        self.mw.img.setPixmap(pixmap)                                                                                                                                                                         

    def connect_handlers(self):
        self.mw.btn_yes.clicked.connect(self.yes)
        self.mw.btn_no.clicked.connect(self.no)
        self.mw.btn_next.clicked.connect(self.next)

    def yes(self):
        self.mw.frame.setStyleSheet("background-color: green;")
        self.descision_made = True
        self.curr_label = 1

    def no(self):
        self.mw.frame.setStyleSheet("background-color: red;")
        self.descision_made = True
        self.curr_label = 0

    def next(self):
        if(self.descision_made):
            self.labels.append(self.curr_label)
            self.curr_idx += 1
            self.set_image(self.curr_idx)
            self.mw.label_currnum.setText(str(self.curr_idx+1)+"/"+str(len(self.paths)))
            self.descision_made = False
            self.mw.frame.setStyleSheet("background-color: yellow;")
        else:
            # TODO warning dialog
            pass

    
