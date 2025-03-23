# Weather API Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)


## Introduction
The Weather API Project is designed to provide weather data for various locations. It fetches real-time weather information using OpenWeatherMap API and displays it in a user-friendly format. 

### Note: 
OpenWeatherAPIs to fetch historical weather data is behind a paywall (see: https://openweathermap.org/api), so all requests to any of those APIs result in 401 response. 
    
    API used: https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}
    
    {'cod': 401, 'message': 'Please note that using One Call 3.0 requires a separate subscription to the One Call by Call plan. Learn more here https://openweathermap.org/price. If you have a valid subscription to the One Call by Call plan, but still receive this error, then please see https://openweathermap.org/faq#error401 for more info.'}
    

Currently in this implementation only the city search functionality is working. 



## Features
- Fetch current weather data.
- Display temperature, humidity, and weather conditions.
- Support for multiple locations.

## Technologies Used
- Programming Language: Python
- API: OpenWeatherMap API

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/animesh698/WeatherAPIProject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd WeatherAPIProject
    ```
3. Install dependencies:
    ```bash
    pip install PySide6, requests
    ```
4. Set up API keys:
    - Set up your key here: https://home.openweathermap.org/api_keys, and replace api_key string with your key

## Usage
Run the application:
    - On VS code, click run from top right OR in ~/WeatherAPIProject/ run command:
    ```
    python main.py
    ```


   
