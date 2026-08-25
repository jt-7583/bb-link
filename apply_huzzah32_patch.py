#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path.cwd()
SRC = ROOT / "src" / "bb-link"

required = [SRC/"Adapter.h", SRC/"Adapter.cpp", SRC/"Bridge.cpp", SRC/"bb-link.ino"]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print("ERROR: Run this from the root of the official islandmagic/bb-link source folder.")
    for p in missing:
        print("Missing:", p)
    sys.exit(1)

def replace_once(path, old, new, desc):
    s = path.read_text()
    if new in s:
        print("Already patched:", desc)
        return
    if old not in s:
        print("ERROR: expected text not found:", desc)
        print("File:", path)
        sys.exit(2)
    path.write_text(s.replace(old, new, 1))
    print("Patched:", desc)

p = SRC/"Adapter.h"
replace_once(
    p,
    "enum hardware_board_t {\n  hardware_board_unknown = 0,\n  hardware_board_tinypico = 1,\n  hardware_board_pico32 = 2\n};",
    "enum hardware_board_t {\n  hardware_board_unknown = 0,\n  hardware_board_tinypico = 1,\n  hardware_board_pico32 = 2,\n  hardware_board_huzzah32 = 3\n};",
    "Adapter.h add HUZZAH32 board ID"
)

replace_once(
    p,
    "#if defined(ARDUINO_ESP32_PICO)\n#define HARDWARE_BOARD hardware_board_pico32\n#define HARDWARE_VERSION_MAJOR 1\n#define HARDWARE_VERSION_MINOR 0\n#endif\n\n#if !defined(HARDWARE_BOARD)",
    "#if defined(ARDUINO_ESP32_PICO)\n#define HARDWARE_BOARD hardware_board_pico32\n#define HARDWARE_VERSION_MAJOR 1\n#define HARDWARE_VERSION_MINOR 0\n#endif\n\n#if defined(ARDUINO_ESP32_DEV)\n#define HARDWARE_BOARD hardware_board_huzzah32\n#define HARDWARE_VERSION_MAJOR 1\n#define HARDWARE_VERSION_MINOR 0\n#endif\n\n#if !defined(HARDWARE_BOARD)",
    "Adapter.h recognize ESP32 Dev Module"
)

p = SRC/"Adapter.cpp"
replace_once(
    p,
    "  pinMode(VBUS_SENSE_GPIO, INPUT);\n\n  statusIndicator.init();",
    "#if defined(ARDUINO_TINYPICO)\n  pinMode(VBUS_SENSE_GPIO, INPUT);\n#endif\n\n  statusIndicator.init();",
    "Adapter.cpp guard TinyPICO VBUS pin"
)

p = SRC/"bb-link.ino"
replace_once(
    p,
    '#include "Adapter.h"\nAdapter *adapter = nullptr;',
    '#include "Adapter.h"\nAdapter adapter;',
    "bb-link.ino global Adapter object"
)

replace_once(
    p,
    "  adapter = new Adapter();\n\n  Serial.println",
    "  Serial.println",
    "bb-link.ino remove dynamic Adapter allocation"
)

s = p.read_text()
if "adapter->" in s:
    p.write_text(s.replace("adapter->", "adapter."))
    print("Patched: bb-link.ino member access")

p = SRC/"bb-link.ino"
old = '  Serial.printf("Booting up %s v%d.%d.%d on %s v%d.%d\\n\\n", adapter.getAdapterName().c_str(), FIRMWARE_VERSION_MAJOR, FIRMWARE_VERSION_MINOR, FIRMWARE_VERSION_PATCH, HARDWARE_BOARD == hardware_board_tinypico ? "TinyPICO" : "Pico32", HARDWARE_VERSION_MAJOR, HARDWARE_VERSION_MINOR);'
new = '  const char *boardName = HARDWARE_BOARD == hardware_board_tinypico ? "TinyPICO" : HARDWARE_BOARD == hardware_board_pico32 ? "Pico32" : HARDWARE_BOARD == hardware_board_huzzah32 ? "HUZZAH32" : "Unknown";\n  Serial.printf("Booting up %s v%d.%d.%d on %s v%d.%d\\n\\n", adapter.getAdapterName().c_str(), FIRMWARE_VERSION_MAJOR, FIRMWARE_VERSION_MINOR, FIRMWARE_VERSION_PATCH, boardName, HARDWARE_VERSION_MAJOR, HARDWARE_VERSION_MINOR);'
replace_once(p, old, new, "bb-link.ino HUZZAH32 boot banner")

print()
print("HUZZAH32 patch complete.")
print("Use ESP32 Dev Module with ESP32 core 2.0.15.")
