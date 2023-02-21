import gzip, pickle, pickletools
from PIL import Image, ImageEnhance
import numpy as np
from PyQt5.QtGui import QPixmap, QImage                                
from PyQt5.QtCore import Qt  



# reads pickled data
def read_pickle(path):
    with gzip.open(path, 'rb') as f:
        p = pickle.Unpickler(f)
        data = p.load()
    return data

#saves list of values into pkl file
def save_as_pickle(lst, path):
    with gzip.open(str(path+".pkl"), 'wb') as f:
        pickled = pickle.dumps(lst)
        optimized_pickle = pickletools.optimize(pickled)
        f.write(optimized_pickle)
        #pickle.dump(lst, f)
    if(type(lst) is list):
        lst.clear()
    return True


def load_data(path, pixmap_size):
    # load from .tif file without labels
    try: 
        contrast = 10
        img = Image.open(path)
        img = np.array(img)
        if(img.shape[-1]==4):
            img = img[:,:,:3]
        img_enhanced = img.copy()
        """enhancer = ImageEnhance.Contrast(img)
        factor = (contrast/100) +1
        img_enhanced = enhancer.enhance(factor)
        img = np.array(img)
        img_enhanced = np.array(img_enhanced)"""
        labels = []
    except: 
        img, mask, label, xmins, xmaxs, ymins, ymaxs, magnification, pixelsize, path = read_pickle(path)
        img = np.array(img)
        img_enhanced = img.copy()
        labels = []
        for xmin,ymin,xmax,ymax in zip(xmins,ymins,xmaxs,ymaxs):
            labels.append([xmin,ymin,xmax,ymax])
    
    # image to save
    minimum = img.min()
    maximum = img.max()
    img = ((img - minimum)/(maximum - minimum))
    
    # image to display
    minimum = img_enhanced.min()
    maximum = img_enhanced.max()
    img_enhanced = ((img_enhanced - minimum)/(maximum - minimum))
    img_enhanced = (img_enhanced*255).astype(np.uint8)
    if(img_enhanced.shape[-1]!=3):
        img_enhanced = np.tile(img_enhanced[:,:,None],(1,1,3))    
    qimage = QImage(img_enhanced, img_enhanced.shape[0], img_enhanced.shape[1], QImage.Format_RGB888)
    pixmap = QPixmap(qimage) 
    pixmap = pixmap.scaled(pixmap_size[0],pixmap_size[1], Qt.KeepAspectRatio) 

    return img, pixmap, labels
 