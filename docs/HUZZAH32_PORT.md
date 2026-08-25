# Adafruit HUZZAH32 Port

## Purpose

This fork adapts B.B. Link for the Adafruit HUZZAH32 ESP32 Feather.

The project goal is a compact wireless bridge allowing RadioMail on an iPhone or iPad to communicate with a Kenwood TH-D75 for packet/Winlink operation.

## Architecture

`RadioMail -> BLE -> HUZZAH32 / B.B. Link -> Bluetooth Classic SPP -> Kenwood TH-D75`

The HUZZAH32 bridges the Bluetooth technologies required by the two devices. RadioMail communicates with B.B. Link over BLE, while the Kenwood radio uses Bluetooth Classic Serial Port Profile.

## Upstream

This project is based on the Island Magic B.B. Link project. This repository remains a fork so upstream development can be tracked separately from HUZZAH32-specific changes.

## HUZZAH32 changes

The initial port:

- Adds HUZZAH32 board support to the B.B. Link hardware abstraction.
- Uses the Arduino `ESP32 Dev Module` target for the HUZZAH32 build.
- Avoids TinyPICO-specific initialization that is not applicable to the HUZZAH32.
- Uses existing dummy status-indicator/touch implementations where TinyPICO-specific hardware is unavailable.
- Corrects the global Adapter instance/reference used by the bridge.
- Provides a HUZZAH32 identifier in the serial startup output.

The intent is to change as little of the upstream B.B. Link protocol and application logic as possible.

## Known-working build environment

- Arduino IDE 2.x
- Board target: ESP32 Dev Module
- ESP32 Arduino core: 2.0.15
- ArduinoLog: 1.1.1
- ArduinoQueue: 1.2.5

Additional upstream dependencies may include:

- TinyPICO Helper Library 1.4.0
- FreeRTOS 11.0.1-5

## ESP32 core compatibility

ESP32 Arduino core 3.x changes several Bluetooth/BLE APIs used by B.B. Link.

Symptoms of using an incompatible 3.x core can include errors involving:

- `BLECharacteristic::getValue()`
- conversion between Arduino `String` and `std::string`
- `BluetoothSerial::setPin()`

For this port, ESP32 core **2.0.15 is the known-working baseline**.

## Current scope

The current priority is reliable RadioMail-to-TH-D75 communications.

TinyPICO-specific convenience features are not part of the initial HUZZAH32 port, including:

- TinyPICO RGB status indication
- TinyPICO capacitive touch controls
- TinyPICO-specific battery monitoring
- TinyPICO-specific automatic battery shutdown behavior

These can be revisited after the core bridge is fully validated.

## Hardware publication status

Mechanical hardware development is intentionally excluded from the repository at this stage.

Do not publish enclosure CAD, STL files, battery packaging details, mounting dimensions, mechanical BOM information, or prototype renders until the enclosure design is approved.
