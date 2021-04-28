"""Custom widgets for Image Viewer."""

from PySide6.QtCore import Signal
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget

class ResizedNotifyingWidget(QWidget):
    """A widget with a resize handler that can be set at runtime."""

    resized = Signal(QResizeEvent)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.resized.emit(event)
