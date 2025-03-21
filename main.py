import sys
import requests
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
