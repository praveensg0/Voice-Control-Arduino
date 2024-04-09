/*
MIT License:
- Copyright © Praveen S G
- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software...
- For more details, please refer to the LICENSE file.
*/

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define LED_PIN 11
#define OLED_RESET -1
#define OLED_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);

  // Initialize OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    while (1);
  }

  // Clear the display and set initial text
  display.clearDisplay();
  display.setTextSize(2); 
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Automation");
  display.display();
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read command from serial input
    if (command == '1') {
      // Turn on the lights (set intensity to maximum)
      analogWrite(LED_PIN, 255);
      display.clearDisplay();
      display.setCursor(0, 0);
      display.println("Light: On");
      display.display();
      Serial.println("Lights turned on.");
    } else if (command == '0') {
      // Turn off the lights (set intensity to minimum)
      analogWrite(LED_PIN, 0);
      display.clearDisplay();
      display.setCursor(0, 0);
      display.println("Light: Off");
      display.display();
      Serial.println("Lights turned off.");
    } else if (command == '2') {
      // Set intensity to 35 for ambient mode
      analogWrite(LED_PIN, 35);
      display.clearDisplay();
      display.setCursor(0, 0);
      display.println("Ambient   Mode");
      display.display();
      Serial.println("Ambient mode activated (intensity set to 30).");
    } else {
      Serial.println("Invalid command.");
    }
  }
  delay(100);  // Delay to avoid excessive serial communication
}
