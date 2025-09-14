import sys
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)


class CompletionView(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("✅ Task Completed!\nResults have been transferred.")
        layout.addWidget(self.label)

        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(sys.exit)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)
