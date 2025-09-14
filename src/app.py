import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout
from gui.StartupView import StartupView
from gui.CompletionView import CompletionView
from gui.DateValidationView import DateValidationView
from gui.PipelineView import PipelineView


# -------------------------------
# Main Application
# -------------------------------
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Land Cover Pipeline")

        self.stack = QStackedWidget()
        self.view1 = StartupView(self)
        self.view2 = DateValidationView(self)
        self.view3 = PipelineView(self)
        self.view4 = CompletionView(self)

        self.stack.addWidget(self.view1)
        self.stack.addWidget(self.view2)
        self.stack.addWidget(self.view3)
        self.stack.addWidget(self.view4)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.resize(600, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
