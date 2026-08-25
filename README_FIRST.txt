BB-LINK HUZZAH32 PATCH — FIRST FLASH

This adapts Island Magic's open-source B.B. Link firmware to the Adafruit
HUZZAH32 while using Arduino IDE's ESP32 Dev Module board target.

1. Download the official source:
   https://github.com/islandmagic/bb-link
   Code -> Download ZIP

2. Unzip it.

3. Copy apply_huzzah32_patch.py into the TOP LEVEL of the extracted folder.

4. In Terminal:
   cd <drag the extracted bb-link-master folder here>
   python3 apply_huzzah32_patch.py

5. Arduino IDE 2.x:
   Install "esp32 by Espressif Systems" VERSION 2.0.15.

6. Library Manager:
   ArduinoLog 1.1.1
   ArduinoQueue 1.2.5
   TinyPICO Helper Library 1.4.0 if Arduino asks for it
   FreeRTOS 11.0.1-5 if Arduino asks for it

7. Open:
   src/bb-link/bb-link.ino

8. Board:
   ESP32 Dev Module

Recommended:
   Flash Size: 4MB
   Flash Mode: QIO
   Flash Frequency: 80MHz
   Partition Scheme: Default 4MB with SPIFFS
   Upload Speed: 115200

9. Click Verify first. If it compiles, click Upload.

10. Open Serial Monitor at 115200 baud.
    The boot line should say HUZZAH32.

Initial-port behavior:
- Keeps upstream BLE KISS bridge.
- Keeps upstream Bluetooth Classic / TH-D75 code.
- Keeps upstream RadioMail hardware-command / QSY logic.
- TinyPICO RGB/touch/battery watchdog are disabled on HUZZAH32.
- Auto-sleep is not enabled yet on HUZZAH32.

Important:
The current upstream source has bb-link.ino declaring Adapter as a pointer while
Bridge.cpp declares it as an object. This patch aligns them as a global object,
which is required for the bridge callback to reference the same Adapter safely.
