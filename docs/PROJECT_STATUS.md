# Project Status

## Objective

Develop a compact HUZZAH32 implementation of B.B. Link for wireless RadioMail/Winlink operation with a Kenwood TH-D75.

## Software

Completed:

- Forked Island Magic B.B. Link.
- Connected the local working copy to the GitHub fork.
- Added initial Adafruit HUZZAH32 support.
- Identified ESP32 Arduino core 2.0.15 as the known-working baseline.
- Resolved ArduinoLog dependency.
- Resolved ArduinoQueue dependency.
- Successfully compiled firmware.
- Successfully uploaded firmware to the HUZZAH32.
- Preserved the HUZZAH32 changes in Git history.

Current software commit baseline:

`8df355d - Add Adafruit HUZZAH32 support`

In progress:

- End-to-end TH-D75 Bluetooth testing.
- RadioMail BLE validation.
- KISS data validation.
- Winlink session testing.
- Reconnection/reliability testing.

Future software work may include:

- HUZZAH32-specific status indication.
- Battery monitoring.
- Power-management behavior.
- Improved diagnostics/logging.
- Additional recovery logic if field testing identifies a need.

## Hardware

**HARDWARE DESIGN IS NOT READY FOR PUBLICATION.**

No prototype mechanical design should be committed at this stage.

Specifically hold:

- enclosure CAD
- OpenSCAD source
- STL files
- renders
- enclosure dimensions
- PCB mounting geometry
- battery packaging geometry
- MagSafe geometry
- mechanical BOM
- prototype photographs that reveal unfinished mechanical design

A `hardware/` directory should be added only after the enclosure design is approved.

## Documentation

Software/build/setup/test documentation may be published now.

Documentation should distinguish between:

- confirmed working behavior
- configuration known to compile/upload
- items still awaiting functional testing

## Upstream strategy

Keep:

- `origin` = this HUZZAH32 fork
- `upstream` = Island Magic B.B. Link

Review upstream changes before merging them into the HUZZAH32 branch, especially changes affecting Bluetooth, BLE, board abstraction, Arduino dependencies, or ESP32 core versions.
