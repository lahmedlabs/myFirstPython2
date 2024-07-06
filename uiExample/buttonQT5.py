from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

def on_button_click():
    label.setText("Hello, PyQt5!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 Example")

layout = QVBoxLayout()

label = QLabel("Click the button")
layout.addWidget(label)

button = QPushButton("Click Me")
button.clicked.connect(on_button_click)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
