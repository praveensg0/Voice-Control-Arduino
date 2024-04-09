"""
MIT License:
- Copyright © Praveen S G
- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software...
- For more details, please refer to the LICENSE file.
"""

import serial
import speech_recognition as sr

# Establish serial connection with Arduino
ser = serial.Serial("COM5", 9600)

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Timeout for listening for voice commands
listen_timeout = 10

# Intensity level for ambient mode
ambient_intensity = 35

while True:
    # Listening for voice commands
    with sr.Microphone() as source:
        print(f"Listening for commands (timeout: {listen_timeout} seconds)...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Listen to audio for a specific timeout
            audio = recognizer.listen(source, timeout=listen_timeout)
        except sr.WaitTimeoutError:
            print("Timeout reached. No command detected.")
            continue

    try:
        # Attempt to recognize voice command
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)

        # List of phrases to end the session
        end_phrases = [
            "stop",
            "end",
            "clear",
            "finish",
            "terminate",
            "exit",
            "conclude",
            "close",
            "halt",
        ]
        if any(phrase in command for phrase in end_phrases):
            print("Ending session...")
            break

        # List of phrases to activate ambient mode
        ambient_phrases = [
            "ambient mode",
            "mode",
            "dim",
            "decrease",
            "set ambient mode",
            "adjust lighting",
            "change to ambient mode",
            "set the mood",
            "set the ambiance",
            "set the lighting",
        ]
        if any(phrase in command for phrase in ambient_phrases):
            print("Setting ambient mode...")
            ser.write(b"2")

        # List of phrases to turn on the lights
        on_phrases = [
            "turn on the lights",
            "turn on the light",
            "switch on the lights",
            "light on",
            "lights on",
            "activate the lights",
            "illuminate the room",
            "brighten up the space",
            "enable the lighting",
            "power on the lights",
            "turn on",
            "light on",
            "lights on",
            "power on",
            "switch on",
            "turn up",
            "turn the lights on",
            "flip the lights on",
            "switch the lights on",
            "activate lighting",
            "activate illumination",
            "fire up",
            "engage the lights",
            "fire up the lights",
            "increase",
        ]
        if any(phrase in command for phrase in on_phrases):
            print("Turning on the lights...")
            ser.write(b"1")

        # List of phrases to turn off the lights
        off_phrases = [
            "turn off the lights",
            "switch off the lights",
            "light off",
            "lights off",
            "deactivate the lights",
            "darken the room",
            "dim the lights",
            "disable the lighting",
            "power off the lights",
            "light off",
            "lights off",
            "power off",
            "turn off the light",
            "turn off",
            "turn of",
            "turn the lights off",
            "flip the lights off",
            "switch the lights off",
            "deactivate lighting",
            "extinguish the lights",
            "disengage the lights",
            "kill the lights",
        ]
        if any(phrase in command for phrase in off_phrases):
            print("Turning off the lights...")
            ser.write(b"0")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Close the serial connection
ser.close()
print("Session ended.")
