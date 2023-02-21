
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QPen, QBrush, QIcon

import numpy as np

import sys
# from PySide2.QtWidgets import QApplication

class Widget_BB(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        # self.setGeometry(30,30,600,400)
        self.drawing_enabled = False
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.start_rel_pos = QtCore.QPoint()
        self.rel_pos = QtCore.QPoint()
        self.rect_to_move = None
        self.rect_to_change = QtCore.QRect()


        self.draw_rect = False
        self.move_rect = False
        self.rectangles = []
        self.show()

    def paintEvent(self, event):
        super().paintEvent(event)
        if(self.drawing_enabled):
            qp = QPainter(self)
            qp.setPen(QPen(QtCore.Qt.red, 4, QtCore.Qt.SolidLine))

            for rectangle in self.rectangles:
                qp.drawRect(rectangle)

            qp_green = QPainter(self)
            qp_green.setPen(QPen(QtCore.Qt.green, 4, QtCore.Qt.SolidLine))

            if(not self.rect_to_change.isNull()):
                begin = QtCore.QPoint(self.xmin,self.ymin)
                end = QtCore.QPoint(self.xmax,self.ymax)
                qp_green.drawRect(QtCore.QRect(begin,end).normalized())

            if not self.begin.isNull() and not self.end.isNull():
                qp_green.drawRect(QtCore.QRect(self.begin, self.end).normalized())

            if not self.start_rel_pos.isNull():
                qp_green.drawRect(QtCore.QRect(self.begin-self.rel_pos, self.end-self.rel_pos).normalized()) 

    def mousePressEvent(self, event):
        if(self.drawing_enabled):
            if event.button() == QtCore.Qt.LeftButton:
                pos = event.pos()
                pos_np = np.array([pos.x(), pos.y()])
                eps_np = np.array([5,5])
                # change size of rectangle
                self.change_xmin = False
                self.change_xmax = False
                self.change_ymin = False
                self.change_ymax = False
                for rectangle in self.rectangles:
                    xmin,ymin, xmax,ymax = rectangle.getCoords()
                    if(np.all(np.array([xmin,ymin]) >= pos_np-eps_np) and np.all(np.array([xmin,ymin]) <= pos_np+eps_np)):
                        self.setCursor(QtCore.Qt.SizeFDiagCursor)
                        self.rect_to_change = rectangle
                        self.xmin,self.ymin,self.xmax,self.ymax = self.rect_to_change.getCoords()
                        self.change_xmin = True
                        self.change_ymin = True

                    elif(np.all(np.array([xmin,ymax]) >= pos_np-eps_np) and np.all(np.array([xmin,ymax]) <= pos_np+eps_np)):
                        self.setCursor(QtCore.Qt.SizeBDiagCursor)
                        self.rect_to_change = rectangle
                        self.xmin,self.ymin,self.xmax,self.ymax = self.rect_to_change.getCoords()
                        self.change_xmin = True
                        self.change_ymax = True

                    elif(np.all(np.array([xmax,ymin]) >= pos_np-eps_np) and np.all(np.array([xmax,ymin]) <= pos_np+eps_np)):
                        self.setCursor(QtCore.Qt.SizeBDiagCursor)
                        self.rect_to_change = rectangle
                        self.xmin,self.ymin,self.xmax,self.ymax = self.rect_to_change.getCoords()
                        self.change_ymin = True
                        self.change_xmax = True

                    elif(np.all(np.array([xmax,ymax]) >= pos_np-eps_np) and np.all(np.array([xmax,ymax]) <= pos_np+eps_np)):
                        self.setCursor(QtCore.Qt.SizeFDiagCursor)
                        self.rect_to_change = rectangle
                        self.xmin,self.ymin,self.xmax,self.ymax = self.rect_to_change.getCoords()
                        self.change_ymax = True
                        self.change_xmax = True

                # move rectangle
                for rectangle in self.rectangles:
                    xmin,ymin, xmax,ymax = rectangle.getCoords()
                    if((pos.x()>xmin) and (pos.x()<xmax) and (pos.y()>ymin) and (pos.y()<ymax)):
                        self.start_rel_pos = event.pos()
                        self.move_rect = True
                        self.rect_to_move = rectangle
                        self.begin = rectangle.topLeft()
                        self.end = rectangle.bottomRight()
                        
                # draw rectangle       
                if(not self.move_rect):
                    self.begin = self.end = event.pos()
                    self.draw_rect = True


                self.update()
            else: 
                pos = event.pos()
                for rectangle in self.rectangles:
                    xmin,ymin, xmax,ymax = rectangle.getCoords()
                    # if((pos.x()==xmin or pos.x()==xmax) and (pos.y()==ymin or pos.y()==ymax)):
                    if((pos.x()>xmin) and (pos.x()<xmax) and (pos.y()>ymin) and (pos.y()<ymax)):
                        self.rectangles.remove(rectangle)
                        self.update()
                self.draw_rect = False
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):     
        if(self.drawing_enabled):
            pos = event.pos()
            # change cursor on hover for resize and move
            pos_np = np.array([pos.x(), pos.y()])
            eps_np = np.array([5,5])
            for rectangle in self.rectangles:
                xmin,ymin, xmax,ymax = rectangle.getCoords()
                if(np.all(np.array([xmin,ymin]) >= pos_np-eps_np) and np.all(np.array([xmin,ymin]) <= pos_np+eps_np)):
                    self.setCursor(QtCore.Qt.SizeFDiagCursor)
                elif(np.all(np.array([xmin,ymax]) >= pos_np-eps_np) and np.all(np.array([xmin,ymax]) <= pos_np+eps_np)):
                    self.setCursor(QtCore.Qt.SizeBDiagCursor)
                elif(np.all(np.array([xmax,ymin]) >= pos_np-eps_np) and np.all(np.array([xmax,ymin]) <= pos_np+eps_np)):
                    self.setCursor(QtCore.Qt.SizeBDiagCursor)
                elif(np.all(np.array([xmax,ymax]) >= pos_np-eps_np) and np.all(np.array([xmax,ymax]) <= pos_np+eps_np)):
                    self.setCursor(QtCore.Qt.SizeFDiagCursor)
                elif((pos.x()>xmin) and (pos.x()<xmax) and (pos.y()>ymin) and (pos.y()<ymax)):
                    self.setCursor(QtCore.Qt.PointingHandCursor)
                else:
                    self.setCursor(QtCore.Qt.ArrowCursor)

            # change size of rectangle
            if(not self.rect_to_change.isNull()):
                self.xmin,self.ymin,self.xmax,self.ymax = self.rect_to_change.getCoords()
                if(self.change_xmin):
                    self.xmin = pos.x()
                if(self.change_xmax):
                    self.xmax = pos.x()
                if(self.change_ymin):
                    self.ymin = pos.y()
                if(self.change_ymax):
                    self.ymax = pos.y()                    
                
            elif(self.move_rect):
                self.rel_pos = self.start_rel_pos - event.pos()
            else:
                self.end = event.pos()
            self.update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if(self.drawing_enabled):
            if(self.draw_rect):
                if((self.begin.x() != self.end.x()) and (self.begin.y() != self.end.y())):
                    r = QtCore.QRect(self.begin, self.end).normalized()
                    self.rectangles.append(r)
                self.begin = self.end = QtCore.QPoint()
                self.draw_rect = False
            # move rect
            if(self.move_rect):
                self.rectangles.remove(self.rect_to_move)
                r = QtCore.QRect(self.begin-self.rel_pos, self.end-self.rel_pos).normalized()
                self.rectangles.append(r)
                self.rect_to_move = None
                self.rel_pos = self.start_rel_pos = QtCore.QPoint()
                self.begin = self.end = QtCore.QPoint()
                self.move_rect = False
            # change size of rect
            if(not self.rect_to_change.isNull()):
                self.rectangles.remove(self.rect_to_change)
                begin = QtCore.QPoint(self.xmin,self.ymin)
                end = QtCore.QPoint(self.xmax,self.ymax)
                r = QtCore.QRect(begin,end).normalized()
                self.rectangles.append(r)
                self.change_xmin = False
                self.change_xmax = False
                self.change_ymin = False
                self.change_ymax = False
                self.rect_to_change = QtCore.QRect()
            self.update()
        self.setCursor(QtCore.Qt.ArrowCursor)
        super().mouseReleaseEvent(event)
        

"""if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget_BB()
    widget.show()
    sys.exit(app.exec_())"""