import sys
import datetime
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel


class DateValidationView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        self.info_label = QLabel("Checking timeframe...")
        layout.addWidget(self.info_label)

        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(sys.exit)
        layout.addWidget(self.btn_exit)

        self.btn_next = QPushButton("Proceed")
        self.btn_next.clicked.connect(self.go_next)
        layout.addWidget(self.btn_next)

        self.setLayout(layout)
        self.check_date()

    def check_date(self):
        today = datetime.date.today()
        year = today.year
        start = datetime.date(year, 3, 1)
        end = datetime.date(year, 4, 1)

        if today < start or today > end:
            self.info_label.setText(
                f"⚠ Outside allowed timeframe (March 1 – April 1)\nToday: {today}"
            )
            self.btn_next.setDisabled(True)
        else:
            self.info_label.setText(f"Date OK: {today}")
            self.btn_next.setDisabled(False)

    def go_next(self):
        self.parent.stack.setCurrentIndex(2)
