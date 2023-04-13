import gzip, pickle, pickletools
from PIL import Image, ImageEnhance
import numpy as np
from PyQt5.QtGui import QPixmap, QImage                                
from PyQt5.QtCore import Qt  
import tifffile




# reads pickled data
def read_pickle(path):
    with gzip.open(path, 'rb') as f:
        p = pickle.Unpickler(f)
        data = p.load()
    return data
# pixelsizes = read_pickle(r"D:\Datasets\ABEM\WSOD\Covid\Crops/pixelsizes.pkl")[0]


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

def compute_capside_size(pixelsize_in_m, capside_size_in_nm = 97):
    pixelsize_in_nm = pixelsize_in_m * 10**9
    capside_size_in_px = capside_size_in_nm/pixelsize_in_nm
    return round(capside_size_in_px)

def open_tif_with_properties(path):
    with tifffile.TiffFile(path) as tif:
        properties = {}
        for tag in tif.pages[0].tags.values():
            name, value = tag.name, tag.value
            properties[name] = value
        image = tif.pages[0].asarray()
    try:
        magnification = properties['OlympusSIS']['magnification']
        pixelsize = properties['OlympusSIS']['pixelsizex']
        properties = {'magnification': magnification, 'pixelsize': pixelsize, 'path': path}
    except:
        print("ERROR:: properties of file: "+str(path))
    return image, properties

def load_data(path, idx, pixmap_size):
    # load from .tif file without labels
    try: 
        img, properties = open_tif_with_properties(path)
        try:
            pixelsize = properties['pixelsize']
        except: 
            print("WARNING::Could not load pixelsize")
            pixelsize = 0
        labels = []


    except: 
        img, mask, label, xmins, xmaxs, ymins, ymaxs, magnification, pixelsize, path = read_pickle(path)
        img = np.array(img)
        img_enhanced = img.copy()
        labels = []
        for xmin,ymin,xmax,ymax in zip(xmins,ymins,xmaxs,ymaxs):
            labels.append([xmin,ymin,xmax,ymax])


    capside_size = compute_capside_size(pixelsize)
    img = np.array(img)
    if(img.shape[-1]==4):
        img = img[:,:,:3]
    img_enhanced = img.copy()
    w = img_enhanced.shape[0]+40
    h = img_enhanced.shape[1]+40
    print(img_enhanced.shape)
    zeros = np.zeros((w, h))
    minimum = img_enhanced.min()
    maximum = img_enhanced.max()
    # img_enhanced = ((img_enhanced - minimum)/(maximum - minimum))
    zeros[(w//2)-(capside_size//2): (w//2)+(capside_size//2), 3:7] = 255
    zeros[20:img_enhanced.shape[0]+20, 20:img_enhanced.shape[1]+20] = img_enhanced

    
    img_enhanced = zeros
        
        
    
    # image to save
    minimum = img.min()
    maximum = img.max()
    img = ((img - minimum)/(maximum - minimum))
    
    # image to display
    minimum = img_enhanced.min()
    maximum = img_enhanced.max()
    img_enhanced = ((img_enhanced - minimum)/(maximum - minimum))
    img_enhanced = (img_enhanced*255).astype(np.uint8)
    print(img_enhanced.shape)
    if(img_enhanced.shape[-1]!=3):
        img_enhanced = np.tile(img_enhanced[:,:,None],(1,1,3))    
    print(img_enhanced.shape)
    qimage = QImage(img_enhanced, img_enhanced.shape[0], img_enhanced.shape[1], QImage.Format_RGB888)
    pixmap = QPixmap(qimage) 
    pixmap = pixmap.scaled(pixmap_size[0],pixmap_size[1]) #, Qt.KeepAspectRatio) 

    return img, pixmap, labels, pixelsize