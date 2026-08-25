# RadioMail Setup

## Purpose

RadioMail provides the iPhone/iPad Winlink interface for this project.

The HUZZAH32 allows RadioMail and the Kenwood TH-D75 to communicate despite using different Bluetooth transports.

## Architecture

`RadioMail -> BLE -> B.B. Link on HUZZAH32 -> Bluetooth Classic -> Kenwood TH-D75`

## Initial connection

1. Power on the TH-D75.
2. Power on the HUZZAH32.
3. Allow B.B. Link to establish its radio-side connection.
4. Open RadioMail.
5. Ensure RadioMail has iOS Bluetooth permission.
6. Select/configure the B.B. Link-compatible interface.
7. Connect RadioMail to the HUZZAH32.

## Winlink session

For an initial packet session:

1. Verify the radio and HUZZAH32 are connected.
2. Verify RadioMail is connected to B.B. Link.
3. Select a known reachable Winlink packet gateway.
4. Confirm the gateway frequency.
5. Start the session.
6. Observe Serial Monitor during early testing.
7. Confirm both outgoing and incoming data.

## Troubleshooting — RadioMail cannot find B.B. Link

Check:

- HUZZAH32 is powered.
- Firmware booted successfully.
- BLE initialized.
- RadioMail has Bluetooth permission.
- Close and reopen RadioMail.
- Reboot the HUZZAH32 if necessary.

## Troubleshooting — connects but does not communicate

Separate the problem into two links:

### iPhone side

`RadioMail <-> BLE <-> HUZZAH32`

### Radio side

`HUZZAH32 <-> Bluetooth Classic <-> TH-D75`

Determine which link is failing before changing firmware.

## Version tracking

RadioMail may change over time. Record the RadioMail version alongside each known-good firmware configuration.
