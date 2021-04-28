"""Custom widgets for Image Viewer."""

from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget

class ResizeNotifyingWidget(QWidget):
    """A widget with a resize handler that can be set at runtime."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.onResize = lambda _: None

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.onResize(event)
