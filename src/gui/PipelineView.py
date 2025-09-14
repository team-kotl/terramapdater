import sys
import subprocess
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal


class ScriptRunner(QThread):
    output = pyqtSignal(str)  # send script stdout
    finished = pyqtSignal(bool)  # notify when done

    def __init__(self, script):
        super().__init__()
        self.script = script

    def run(self):
        try:
            process = subprocess.Popen(
                [sys.executable, self.script],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            for line in process.stdout:
                self.output.emit(line.strip())
            process.wait()
            self.finished.emit(process.returncode == 0)
        except Exception as e:
            self.output.emit(f"[ERROR] {e}")
            self.finished.emit(False)


class PipelineView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        self.header = QLabel("Starting...")
        layout.addWidget(self.header)

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        layout.addWidget(self.console)

        self.setLayout(layout)

        # List of scripts to run in sequence
        self.scripts = [
            ("Downloading Satellite Imagery", "scripts/get-imagery.py"),
            ("Combining and Clipping Tiles", "scripts/combine-tiles.py"),
            ("Generating Land Cover Map", "scripts/use.py"),
            ("Fine Tuning Model", "scripts/train.py"),
            ("Generating Areas", "scripts/extract-areas.py"),
            ("Transferring to Backend", "scripts/transfer-file.py"),
        ]
        self.current_index = -1
        self.run_next_script()

    def run_next_script(self):
        self.current_index += 1
        if self.current_index >= len(self.scripts):
            self.parent.stack.setCurrentIndex(3)
            return

        title, script = self.scripts[self.current_index]
        self.header.setText(title)
        self.console.append(f"\n--- {title} ({script}) ---")

        self.runner = ScriptRunner(script)
        self.runner.output.connect(self.console.append)
        self.runner.finished.connect(self.script_finished)
        self.runner.start()

    def script_finished(self, success):
        if success:
            self.console.append("[DONE]")
            self.run_next_script()
        else:
            self.console.append("[FAILED]")
            QMessageBox.critical(
                self, "Error", f"Script failed: {self.scripts[self.current_index][1]}"
            )
