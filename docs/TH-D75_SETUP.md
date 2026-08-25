# Kenwood TH-D75 Setup

## Purpose

The Kenwood TH-D75 is the radio side of the HUZZAH32 B.B. Link system.

The intended path is:

`RadioMail -> BLE -> HUZZAH32 -> Bluetooth Classic SPP -> TH-D75`

## Bluetooth preparation

Before first testing:

1. Power on the TH-D75.
2. Enable Bluetooth.
3. Put the radio into the appropriate discoverable/pairing state.
4. Keep the HUZZAH32 close to the radio for initial pairing.
5. Avoid having another computer or phone simultaneously connected to the radio's Bluetooth serial service.

## Pairing

B.B. Link scans for and communicates with the Kenwood using Bluetooth Classic Serial Port Profile.

The upstream software uses Bluetooth pairing logic internally. Unless intentionally changed in source, use the pairing behavior provided by B.B. Link rather than trying to create an unrelated iOS Bluetooth connection directly to the radio.

## Packet operation

B.B. Link contains Kenwood-specific radio control and KISS/TNC handling.

During initial testing, avoid manually changing radio modes or TNC state while B.B. Link is performing a session. This makes failures easier to isolate.

## Troubleshooting — radio not discovered

Check:

- TH-D75 Bluetooth is enabled.
- Radio is discoverable.
- Another device is not occupying the connection.
- HUZZAH32 firmware booted correctly.
- Serial Monitor shows Bluetooth initialization.
- Radio and HUZZAH32 are physically close during first pairing.

## Troubleshooting — paired but no packet traffic

Check:

- Correct packet frequency.
- Correct active band/VFO.
- B.B. Link radio-control messages in Serial Monitor.
- TNC/KISS transitions.
- Reachability of the packet/Winlink gateway.

Test against a known reachable station before assuming the bridge is defective.

## Known-good configuration record

As testing progresses, record:

- TH-D75 firmware version
- relevant Bluetooth settings
- packet baud rate
- frequencies tested
- Winlink gateways tested
- successful B.B. Link firmware commit
