# Voice-Controlled LED Bulb and More with Arduino and Python

This project demonstrates how to control an LED bulb and other devices using voice commands through Python and Arduino. It utilizes Python's speech recognition module and Arduino Uno's PWM capabilities for controlling the LED bulb's intensity. Additionally, it incorporates a screen display to show the current state of the LED.

## Demo

https://github.com/praveensg0/Voice-Control-Arduino/assets/144553645/ba5d9dd0-ea4c-46d2-aec8-cbddfa68f24f

## Features

- Voice-controlled LED bulb intensity adjustment.
- Screen display for visual feedback on LED state.
- Support for extending functionality to control other devices such as motors.

## Requirements

- Arduino Uno.
- LED bulb or other device.
- Screen display (e.g., OLED or LCD).
- Microphone(I used laptop microphone, you can use).
- Python.
- Arduino IDE.

## Installation and Setup

1. Connect the LED bulb to pin 11 of the Arduino Uno.
2. Connect the screen display according to the manufacturer's instructions.
3. Upload the provided Arduino sketch (`light_control.ino`) to the Arduino Uno using the Arduino IDE.
4. Install the required Python packages by running
   
   ```bash
   pip install pyserial
   pip install SpeechRecognition

5. Connect the microphone to your computer. You can use a laptop microphone, Bluetooth earphones, headphones, etc.
6. Connect the Arduino Uno to your computer via USB.
7. Run the provided Python script (`voice_recognition.py`).

## Usage

1. Run the Python script.
2. Speak one of the supported voice commands to control the LED bulb:
   - "Turn on the lights"
   - "Turn off the lights"
   - "Set ambient mode"
3. The Arduino Uno will receive the command via serial communication and adjust the intensity of the LED bulb accordingly. The screen display will show the current state of the LED.

## License

This project is licensed under the [MIT License](LICENSE).
