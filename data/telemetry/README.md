# Telemetry Data

This folder stores raw and processed telemetry logs used by the simulator,
analysis tools, and visualization modules.

## Purpose

Telemetry data represents time‑series measurements collected from:
- Real vehicle sensors  
- Simulated laps  
- Synthetic demo datasets  

These logs are used for:
- Telemetry analysis  
- Signal smoothing and filtering  
- Acceleration and derivative calculations  
- Lap comparison  
- Visualization demos  

## Expected Formats

Telemetry files may be stored in any of the following formats:

### ✔ CSV
Recommended for simple time‑series data.

Example columns:
time, speed, throttle, brake, steering, accel_x, accel_y

### ✔ JSON
Useful for structured or hierarchical telemetry.

### ✔ MAT / NPZ
For large datasets or high‑frequency sensor logs.

### ✔ TXT
For lightweight or custom formats.

## Naming Convention

Use clear, descriptive filenames that indicate:

- The session number  
- Whether the data is raw or processed  
- The type of dataset  

## Notes

- Do **not** store code in this directory.  
- Large datasets should be added to `.gitignore` if they exceed repository limits.  
- Synthetic telemetry for demos should go in `data/samples/`.
