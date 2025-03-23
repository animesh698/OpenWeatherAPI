import sys
import requests
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFrame
from PySide6.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # set up widgets to display
        self.city_label = QLabel("Enter City: ", self)
        self.city_input = QLineEdit(self)
        
        self.date_range_label = QLabel("(Optional) Date Range for Historical Data", self)
        self.start_date_input = QLineEdit(self)
        self.start_date_input.setPlaceholderText("Start Date (YYYY-MM-DD)")
        self.end_date_input = QLineEdit(self)
        self.end_date_input.setPlaceholderText("End Date (YYYY-MM-DD)")
        
        self.weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        
        # assign object names for CSS styling
        self.city_label.setObjectName("city_label")
        self.date_range_label.setObjectName("date_range_label")
        self.city_input.setObjectName("city_input")
        self.start_date_input.setObjectName("start_date_input")
        self.end_date_input.setObjectName("end_date_input")
        self.weather_button.setObjectName("weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.initUI()

    # initialize the layout
    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        layout.addWidget(self.date_range_label)
        
        date_layout = QHBoxLayout()
        date_layout.addWidget(self.start_date_input)
        date_layout.addWidget(self.end_date_input)
        layout.addLayout(date_layout)

        layout.addWidget(self.weather_button)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)

        self.setLayout(layout)
        self.setWindowTitle('Weather App')

        # widget horizontal alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.date_range_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # css styling for widgets
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
                font-style: bold;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLabel#date_range_label {
                font-family: calibri;
                font-size: 25px;
                font-style: italic;
                color: gray;
            }
            QLineEdit#city_input {
                font-size: 40px;
                padding: 0 8px;
            }
            QLineEdit#start_date_input, QLineEdit#end_date_input {
                font-size: 30px;
                padding: 5px;
            }
            QPushButton#weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temp_label {
                font-size: 75px;
                font-weight: bold;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        # connect get weather button to function
        self.weather_button.clicked.connect(self.get_weather)

    # fetch weather data from API
    def get_weather(self):

        api_key = "185f53c13ab6ee39bf2805e4edfb7862"
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.display_weather(data)
            # print(data)
            # print(data['main'])
            temp = int(data['main']['temp'])
            # print(data['weather'][0])
            weather_description = data['weather'][0]['description']
            icon_code = data['weather'][0]['icon']

            emoji = self.get_weather_emoji(icon_code)
            self.temp_label.setText(f"{temp}°C")
            self.emoji_label.setText(emoji)
            self.description_label.setText(weather_description.capitalize())
        else:
            self.display_message("City not found!")

    def display_message(self, message):
        pass

    def display_weather(self, data):
        print(data)

    def get_weather_emoji(self, icon_code):
        emoji_map = {
            "01d": "☀️",
            "01n": "🌙",
            "02d": "⛅",
            "02n": "🌤️",
            "03d": "🌥️",
            "03n": "☁️",
            "04d": "☁️",
            "04n": "☁️",
            "09d": "🌧️",
            "09n": "🌧️",
            "10d": "🌦️",
            "10n": "🌧️",
            "11d": "⛈️",
            "11n": "⛈️",
            "13d": "❄️",
            "13n": "❄️",
            "50d": "🌫️",
            "50n": "🌫️",
        }
        return emoji_map.get(icon_code, "❓")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
