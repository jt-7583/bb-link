# HUZZAH32 B.B. Link Test Plan

The purpose of this test plan is to isolate firmware, BLE, Bluetooth Classic, Kenwood control, KISS, RF, and Winlink problems.

## Phase 1 — Firmware

- [x] HUZZAH32 firmware compiles.
- [x] Firmware uploads to HUZZAH32.
- [ ] Startup banner identifies HUZZAH32.
- [ ] Five consecutive power cycles boot normally.

## Phase 2 — TH-D75 Bluetooth

- [ ] HUZZAH32 discovers TH-D75.
- [ ] Initial Bluetooth pairing completes.
- [ ] Connection remains stable for 10 minutes.
- [ ] Pairing survives HUZZAH32 reboot.
- [ ] Pairing survives TH-D75 reboot.
- [ ] Automatic reconnection works.

## Phase 3 — RadioMail BLE

- [ ] RadioMail discovers B.B. Link.
- [ ] BLE connection completes.
- [ ] BLE reconnects after RadioMail restart.
- [ ] BLE reconnects after HUZZAH32 reboot.
- [ ] Connection remains stable for 10 minutes.

## Phase 4 — Kenwood control

- [ ] B.B. Link communicates with radio control interface.
- [ ] Frequency/QSY operation works.
- [ ] Correct VFO/band behavior is observed.
- [ ] TNC/KISS mode transition works.
- [ ] Radio returns to expected state after session.

## Phase 5 — KISS data

- [ ] RadioMail sends KISS data to HUZZAH32.
- [ ] HUZZAH32 forwards data to TH-D75.
- [ ] TH-D75 received data reaches HUZZAH32.
- [ ] HUZZAH32 forwards received data to RadioMail.

## Phase 6 — RF/Winlink

- [ ] Connect to a known reachable packet gateway.
- [ ] Complete a Winlink connection.
- [ ] Send a test Winlink message.
- [ ] Receive a test Winlink message.
- [ ] Disconnect cleanly.

## Phase 7 — Reliability

- [ ] Ten consecutive complete connection cycles.
- [ ] Thirty-minute idle test.
- [ ] One-hour active/standby test.
- [ ] Battery-powered test.
- [ ] Recovery after TH-D75 goes out of Bluetooth range.
- [ ] Recovery after iPhone BLE interruption.
- [ ] Recovery after RadioMail restart.

## Test record template

For each significant test record:

- Date/time:
- Git commit:
- ESP32 core:
- ArduinoLog:
- ArduinoQueue:
- RadioMail version:
- TH-D75 firmware:
- Frequency:
- Gateway/station:
- Result:
- Serial-log notes:
- Changes made after test:

Change one variable at a time whenever possible.
