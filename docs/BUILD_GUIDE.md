# HUZZAH32 B.B. Link Build Guide

## 1. Install Arduino IDE

Install Arduino IDE 2.x.

## 2. Install ESP32 board support

Open Boards Manager and install:

`esp32 by Espressif Systems`

Use version:

**2.0.15**

This version is the known-working baseline for the HUZZAH32 B.B. Link port.

## 3. Install libraries

Using Arduino Library Manager, install:

- ArduinoLog 1.1.1
- ArduinoQueue 1.2.5

The upstream project may also require:

- TinyPICO Helper Library 1.4.0
- FreeRTOS 11.0.1-5

If the compiler reports a missing header, verify the corresponding library before changing source code.

## 4. Open the sketch

Open:

`src/bb-link/bb-link.ino`

## 5. Select the board

Select:

**Tools -> Board -> ESP32 Arduino -> ESP32 Dev Module**

The HUZZAH32 is built using this target in the current port.

## 6. Compile first

Click **Verify**.

A successful compile confirms the source and dependencies are correct before attempting an upload.

### ArduinoLog error

If you see:

`ArduinoLog.h: No such file or directory`

install ArduinoLog.

### ArduinoQueue error

If you see:

`ArduinoQueue.h: No such file or directory`

install ArduinoQueue.

### ESP32 3.x errors

Errors such as:

`conversion from 'String' to non-scalar type 'std::string'`

or a complaint that:

`BluetoothSerial::setPin()`

requires two arguments generally indicate Arduino is compiling with ESP32 core 3.x.

Return to Boards Manager and install/select ESP32 core **2.0.15**.

## 7. Connect the HUZZAH32

Connect the board to the Mac with a USB data cable.

Select:

**Tools -> Port**

Choose the serial port that appears when the board is connected.

On macOS this may resemble:

- `/dev/cu.SLAB_USBtoUART`
- `/dev/cu.usbserial-...`

If no port appears, first verify the USB cable supports data.

## 8. Upload

Click **Upload**.

A message such as:

`Failed uploading: no upload port provided`

does not indicate a compile problem. Select the correct port and upload again.

## 9. Serial monitor

Open Serial Monitor and use:

**115200 baud**

Confirm the firmware starts normally and identifies the HUZZAH32 build.

## 10. Preserve known-good builds

Once a firmware revision passes end-to-end testing, record:

- Git commit SHA
- ESP32 core version
- Arduino library versions
- RadioMail version
- TH-D75 firmware version

This makes future troubleshooting reproducible.
