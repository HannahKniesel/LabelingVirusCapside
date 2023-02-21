
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QPen, QBrush, QIcon
import sys
# from PySide2.QtWidgets import QApplication

stroke_size = 10
w = stroke_size
class Widget_Location(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        # self.setGeometry(30,30,600,400)
        self.drawing_enabled = False
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.start_rel_pos = QtCore.QPoint()
        self.rel_pos = QtCore.QPoint()
        self.point_to_move = None

        self.draw_point = False
        self.move_point = False
        self.points = []
        self.show()

    def paintEvent(self, event):
        super().paintEvent(event)
        if(self.drawing_enabled):
            qp = QPainter(self)
            qp.setPen(QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))
            qp.setBrush(QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))

            for point in self.points:
                qp.drawEllipse(point.x()-(stroke_size//2), point.y()-(stroke_size//2), stroke_size, stroke_size)

            qp_green = QPainter(self)
            qp_green.setPen(QPen(QtCore.Qt.green, 1, QtCore.Qt.SolidLine))
            qp_green.setBrush(QBrush(QtCore.Qt.green, QtCore.Qt.SolidPattern))

            if not self.begin.isNull() and not self.end.isNull():
                qp_green.drawEllipse(self.end.x()-(stroke_size//2), self.end.y()-(stroke_size//2), stroke_size, stroke_size)
                # qp.drawRect(QtCore.QRect(self.begin, self.end).normalized())

            if not self.start_rel_pos.isNull():
                pos = self.end-self.rel_pos
                qp.drawEllipse(pos.x()-(stroke_size//2), pos.y()-(stroke_size//2), stroke_size, stroke_size)

                # qp.drawRect(QtCore.QRect(self.begin-self.rel_pos, self.end-self.rel_pos).normalized())


    def mousePressEvent(self, event):
        if(self.drawing_enabled):
            if event.button() == QtCore.Qt.LeftButton:
                pos = event.pos()
                # move point
                for point in self.points:
                    
                    if((pos.x()>(point.x()-w)) and (pos.x()<(point.x()+w)) and (pos.y()>(point.y()-w)) and (pos.y()<(point.y()+w))):
                        self.start_rel_pos = event.pos()
                        self.move_point = True
                        self.point_to_move = point
                        self.begin = point #QtCore.QPoint(int(point), int(point))
                        self.end = point #QtCore.QPoint(int(point), int(point))
                        
                # draw point        
                if(not self.move_point):
                    self.begin = self.end = event.pos()
                    self.draw_point = True

                self.update()
            else: 
                pos = event.pos()
                # remove point
                for point in self.points:
                    if((pos.x()>(point.x()-w)) and (pos.x()<(point.x()+w)) and (pos.y()>(point.y()-w)) and (pos.y()<(point.y()+w))):
                        self.points.remove(point)
                        self.update()
                """for rectangle in self.rectangles:
                    xmin,ymin, xmax,ymax = rectangle.getCoords()
                    # if((pos.x()==xmin or pos.x()==xmax) and (pos.y()==ymin or pos.y()==ymax)):
                    if((pos.x()>xmin) and (pos.x()<xmax) and (pos.y()>ymin) and (pos.y()<ymax)):
                        self.rectangles.remove(rectangle)
                        self.update()"""
                self.draw_point = False
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if(self.drawing_enabled):
            pos = event.pos()
            # change cursor on hover for move
            for point in self.points:
                if((pos.x()>(point.x()-w)) and (pos.x()<(point.x()+w)) and (pos.y()>(point.y()-w)) and (pos.y()<(point.y()+w))):
                    self.setCursor(QtCore.Qt.PointingHandCursor)
                else:
                    self.setCursor(QtCore.Qt.ArrowCursor)

            if(self.move_point):
                self.rel_pos = self.start_rel_pos - event.pos()
            else:
                self.end = event.pos()
            self.update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if(self.drawing_enabled):
            if(self.draw_point):
                p = event.pos()
                # r = QtCore.QRect(self.begin, self.end).normalized()
                self.points.append(p)
                self.begin = self.end = QtCore.QPoint()
                self.draw_point = False
            if(self.move_point):
                self.points.remove(self.point_to_move)
                p = event.pos()

                # r = QtCore.QRect(self.begin-self.rel_pos, self.end-self.rel_pos).normalized()
                self.points.append(p)
                self.point_to_move = None
                self.rel_pos = self.start_rel_pos = QtCore.QPoint()
                self.begin = self.end = QtCore.QPoint()
                self.move_point = False
            self.update()
        super().mouseReleaseEvent(event)
        

"""if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget_BB()
    widget.show()
    sys.exit(app.exec_())"""