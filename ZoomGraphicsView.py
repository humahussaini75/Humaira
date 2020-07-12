from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import pyqtSignal

# from View.StyleSheet import StyleSheet


# ==============================================================================
# ZoomGraphicsView
# ==============================================================================

class ZoomGraphicsView(QGraphicsView):
    '''Statement.

    Description Line1
    .
    .
    .
    Description LineN
    '''
# |----------------------------------------------------------------------------|
# class Variables
# |----------------------------------------------------------------------------|
    reScaled = pyqtSignal(float, float, int, int)

    adjustScale = pyqtSignal(float, int, int)

# |----------------------------------------------------------------------------|
# Constructor
# |----------------------------------------------------------------------------|
    def __init__(self, *args, **kwargs):
        QGraphicsView.__init__(self, *args, **kwargs)
        self._absVal = 1
        self._relZoom = 1
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.setStyleSheet(StyleSheet.scrollBar+StyleSheet.defaultButton)
        self._scrollZoomEnabled = True

# |--------------------------End of Constructor-------------------------------|

# |----------------------------------------------------------------------------|
# wheelEvent
# |----------------------------------------------------------------------------|
    def wheelEvent(self, event):
        if self._scrollZoomEnabled:
            if self._absVal < 20 and event.angleDelta().y() > 0:
                self._relZoom = 1.25
                self._absVal *= self._relZoom
                self.scale(self._relZoom, self._relZoom)
                self.reScaled.emit(self._relZoom, self._relZoom,
                                   self.horizontalScrollBar().value(),
                                   self.verticalScrollBar().value())
            elif event.angleDelta().y() < 0 and self._absVal > 0.1:
                self._relZoom = 0.8
                self._absVal *= self._relZoom
                self.scale(self._relZoom, self._relZoom)
                self.reScaled.emit(self._relZoom, self._relZoom,
                                   self.horizontalScrollBar().value(),
                                   self.verticalScrollBar().value())

# |-----------------------End of wheelEvent-----------------------------------|

# |----------------------------------------------------------------------------|
# reScale
# |----------------------------------------------------------------------------|
    def reScale(self, xZ, yZ, x, y):
        self.scale(xZ, yZ)
        self._absVal *= xZ
        self.horizontalScrollBar().setValue(x)
        self.verticalScrollBar().setValue(y)

# |-----------------------End of reScale--------------------------------------|

# |----------------------------------------------------------------------------|
# setScale
# |----------------------------------------------------------------------------|
    def setScale(self):
        self.adjustScale.emit(self._absVal,
                              self.horizontalScrollBar().value(),
                              self.verticalScrollBar().value())

# |-----------------------End of setScale-------------------------------------|

# |----------------------------------------------------------------------------|
# onAdjustScale
# |----------------------------------------------------------------------------|
    def onAdjustScale(self, scaleValue, x, y):
        # Scale to original size.
        self.scale(1/self._absVal, 1/self._absVal)

        self._absVal = scaleValue
        # Scale to new level.
        self.scale(self._absVal, self._absVal)
        self.horizontalScrollBar().setValue(x)
        self.verticalScrollBar().setValue(y)

# |---------------------------End of onAdjustScale----------------------------|
