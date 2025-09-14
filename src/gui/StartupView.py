import os
import json
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QFileDialog,
    QMessageBox,
)

CONFIG_FILE = "../config.json"


class StartupView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        self.label = QLabel("Select Backend Directory")
        layout.addWidget(self.label)

        self.current_path_label = QLabel("")
        layout.addWidget(self.current_path_label)

        self.btn_select = QPushButton("Change Directory")
        self.btn_select.clicked.connect(self.select_dir)
        layout.addWidget(self.btn_select)

        self.btn_next = QPushButton("Next")
        self.btn_next.clicked.connect(self.go_next)
        layout.addWidget(self.btn_next)

        self.setLayout(layout)
        self.load_config()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                self.backend_path = config.get("backend_dir", "")
        else:
            self.backend_path = ""
        self.update_label()

    def update_label(self):
        if self.backend_path:
            self.current_path_label.setText(f"Current: {self.backend_path}")
        else:
            self.current_path_label.setText("No directory selected")

    def select_dir(self):
        path = QFileDialog.getExistingDirectory(self, "Select Backend Directory")
        if path:
            self.backend_path = path
            with open(CONFIG_FILE, "w") as f:
                json.dump({"backend_path": path}, f)
            self.update_label()

    def go_next(self):
        if not self.backend_path:
            QMessageBox.warning(self, "Error", "Please select a backend directory.")
            return
        self.parent.stack.setCurrentIndex(1)
