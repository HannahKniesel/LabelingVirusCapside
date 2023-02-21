import sys
from PyQt5 import QtWidgets, uic
from glob import glob
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
from timeit import default_timer as timer
import numpy as np
import os 
import json
import sys

from PyQt5.QtGui import QPixmap, QImage                                
from PyQt5.QtCore import Qt  
from PyQt5 import QtCore, QtGui, QtWidgets

from pathlib import Path 
from Form import Ui_BinaryLabeling
from Utils import *

IMG_SIZE = 600

class MainWindow(QtWidgets.QMainWindow, Ui_BinaryLabeling):
    def __init__(self, paths, save_to, start_idx, training_period, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.paths = paths
        self.save_to = save_to
        self.curr_idx = start_idx 
        self.started = False
        self.elapsed = 0
        self.label = -1
        self.training_period = training_period
        self.training_imgs = ["../Probanden_TestData/Bin1.png", "../Probanden_TestData/Bin2.png", "../Probanden_TestData/End2.png"]


        self.start_timer = 0


        # self.labels = np.zeros((len(self.paths),)) -1
        # self.timings = np.zeros((len(self.paths),))
        """if(self.curr_idx > 0):
            self.timings[:self.curr_idx] = read_pickle(self.save_to + "/Timings.pkl")[:self.curr_idx]
            self.labels[:self.curr_idx] = read_pickle(self.save_to + "/Labels.pkl")[:self.curr_idx]    """    
        
        self.crop = []

        self.labeled_data_dir = self.save_to
        os.makedirs(self.labeled_data_dir,exist_ok=True)

    def closeEvent(self, e):
        if((self.curr_idx < len(self.paths)) and (self.label != -1)):
            # save last label and timing
            self.end = timer()
            elapsed = self.end - self.start_timer
            # self.timings[self.curr_idx] += elapsed
            self.loading.setText("saving data...")
            print("Save idx: "+str(self.curr_idx))
            self.loading.repaint()
            save_as_pickle([self.crop, self.label, self.bb_labels, self.elapsed + elapsed], self.labeled_data_dir+"/"+str(self.curr_idx))
            self.curr_idx +=1
            # self.curr_idx = np.argwhere(self.labels != -1).max() +1

        print("Finished "+str(self.curr_idx)+"/"+str(len(self.paths))+" images.")
        # print("Timings: "+str(self.timings[:self.curr_idx]))
        # print("Labels: "+str(self.labels[:self.curr_idx]))

        # save_as_pickle(self.timings[:self.curr_idx], self.save_to + "/Timings")
        # save_as_pickle(self.labels[:self.curr_idx], self.save_to + "/Labels")
        save_as_pickle(self.paths[:self.curr_idx], self.save_to + "/Paths")

    def keyPressEvent(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            if e.key() == Qt.Key_F5:
                self.close()
            if(((e.key() == Qt.Key_Up) and self.started) and (self.curr_idx < len(self.paths)) and (self.curr_idx >= 0)):
                self.yes()
                self.next()
            if(((e.key() == Qt.Key_Down) and self.started) and (self.curr_idx < len(self.paths)) and (self.curr_idx >= 0)):
                self.no()
                self.next()
            if(((e.key() == Qt.Key_Return) or (e.key() == Qt.Key_Right)) and (self.curr_idx < len(self.paths))):
                """if(self.started):
                    self.next()"""
                if(e.key() == Qt.Key_Return):
                    self.start()
            if(((e.key() == Qt.Key_Backspace) or (e.key() == Qt.Key_Left)) and self.curr_idx>0):
                # self.prev()
                pass
       
    def set_image(self, idx):
        if(self.training_period):
            if(idx < len(self.training_imgs)):
                print(idx)
                self.crop, pixmap, self.bb_labels = load_data(self.training_imgs[idx], pixmap_size = (IMG_SIZE,IMG_SIZE))
                self.img.setPixmap(pixmap)
                return
            else: 
                self.training_period = False
                idx = 0
                self.curr_idx = 0
        if(idx >= len(self.paths)):
            self.close()
            return
        else:
            self.crop, pixmap, self.bb_labels = load_data(self.paths[idx], pixmap_size = (IMG_SIZE,IMG_SIZE))
        self.img.setPixmap(pixmap)     


    def connect_handlers(self):
        # self.btn_yes.clicked.connect(self.yes)
        # self.btn_no.clicked.connect(self.no)
        # self.btn_next.clicked.connect(self.next)
        # self.btn_prev.clicked.connect(self.prev)
        self.btn_start.clicked.connect(self.start)


    def start(self):
        self.set_image(self.curr_idx)
        self.label_currnum.setText(str(self.curr_idx+1)+"/"+str(len(self.paths)))
        self.frame.setStyleSheet("background-color: yellow;")
        # self.btn_next.setEnabled(True)
        # if(self.curr_idx > 0):
            # self.btn_prev.setEnabled(True)
        self.btn_start.setEnabled(False)
        self.started = True
        self.start_timer = timer()

    def yes(self):
        self.frame.setStyleSheet("background-color: green;")
        self.label = 1          

    def no(self):
        self.frame.setStyleSheet("background-color: red;")
        self.label = 0   

    def next(self):
        if((self.label != -1)):
            self.end = timer()
            elapsed = self.end - self.start_timer
            if(elapsed < 0.2):
                return
            self.loading.setText("saving data...")
            print("Save idx: "+str(self.curr_idx))
            self.loading.repaint()
            if(not self.training_period):
                save_as_pickle([self.crop, self.label, self.bb_labels, self.elapsed + elapsed], self.labeled_data_dir+"/"+str(self.curr_idx))
            self.curr_idx += 1 
            # self.btn_prev.setEnabled(True)
            self.set_image(self.curr_idx)
            self.label_currnum.setText(str(self.curr_idx+1)+"/"+str(len(self.paths)))
            try:
                _, self.label, self.bb_labels, self.elapsed = read_pickle(self.labeled_data_dir+"/"+str(self.curr_idx)+".pkl")
            except: 
                self.label = -1
                self.elapsed = 0

            if(self.label == 0):
                self.frame.setStyleSheet("background-color: red;")
            elif(self.label == 1):
                self.frame.setStyleSheet("background-color: green;")
            else:
                self.frame.setStyleSheet("background-color: yellow;")

            self.loading.setText("")
            self.loading.repaint()
            self.start_timer = timer()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You first need to make a descision. Therefore you can use the provided buttons below or the key 'y' or 'n' on your keyboard.")
            msg.setWindowTitle("Error")
            msg.exec_()
            

    def prev(self):
        if((self.label != -1)):
            self.end = timer()
            elapsed = self.end - self.start_timer
            self.loading.setText("saving data...")
            self.loading.repaint()
            # self.timings[self.curr_idx] += elapsed
            print("Save idx: "+str(self.curr_idx))
            save_as_pickle([self.crop, self.label, self.bb_labels, self.elapsed + elapsed], self.labeled_data_dir+"/"+str(self.curr_idx))
            self.loading.setText("")
            self.loading.repaint()
            
        self.curr_idx -= 1
        # if(self.curr_idx == 0):
            # self.btn_prev.setEnabled(False)
        self.set_image(self.curr_idx)
        self.label_currnum.setText(str(self.curr_idx+1)+"/"+str(len(self.paths)))

        try:
            _, self.label, self.bb_labels, self.elapsed = read_pickle(self.labeled_data_dir+"/"+str(self.curr_idx)+".pkl")
        except: 
            self.label = -1
            self.elapsed = 0

        if(self.label == 0):
            self.frame.setStyleSheet("background-color: red;")
        elif(self.label == 1):
            self.frame.setStyleSheet("background-color: green;")
        
        self.start_timer = timer()


app = QtWidgets.QApplication(sys.argv)

config_path = "../config.json"
with open(config_path, 'r') as f:
  data = json.load(f)

path = data['path']
training_period = False
if(Path(path).stem == "Train"):
    training_period = True
file_format = data['format']
save_to = data['save_to']+"/"+Path(path).stem+"/BinaryLabels/"
start_idx = data['start_idx']

paths = glob(path+"*"+file_format)
if(data['randomize'] == "True"): 
    paths = np.random.permutation(paths)

if(len(paths) == 0):
    print("ERROR::Could not find files in specified directory '"+path+"*"+file_format)
    exit()

if(start_idx != 0):
    if(os.path.isdir(save_to)):
        print("WARNING::Labeling is being continued in folder: "+str(save_to))
        existing_files = glob(save_to+"/*.pkl")
        if(len(existing_files)<start_idx):
            print("WARNING::start_idx is greater than number of existing files. Continue with start_idx="+str(len(existing_files)-1))
            start_idx = len(existing_files)
        elif(len(existing_files)>start_idx):
            print("WARNING::start_idx is smaller than number of existing files. Continue with start_idx="+str(len(existing_files)-1))
            start_idx = len(existing_files)

    else:
        print("ERROR::Could not find labeling folder, but start_idx > 0")
        exit()
    os.makedirs(save_to, exist_ok = True)
else:
    try:
        os.makedirs(save_to, exist_ok = False)
    except: 
        print("ERROR::Save directory already exists. Use different save_to directory in config.json file.")
        existing_files = glob(save_to+"/*.pkl")
        if(len(existing_files)<len(paths)):
            print("If you wish to continue labeling in this folder please set the start_idx to: "+str(len(existing_files)-1))
        exit()


window = MainWindow(paths, save_to, start_idx, training_period)
window.connect_handlers()
window.show()
app.exec()

