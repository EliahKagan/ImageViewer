"""Custom widgets for Image Viewer."""

from PySide2.QtGui import QResizeEvent
from PySide2.QtWidgets import QWidget

class ResizeNotifyingWidget(QWidget):
    """A widget with a reisze handler that can be set at runtime."""

    __slots__ = ('resizeHandler', )

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resizeHandler = None

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

        handler = self.resizeHandler
        if handler is not None:
            handler(event)
