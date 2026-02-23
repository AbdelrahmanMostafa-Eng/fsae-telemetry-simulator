# Track Data

This folder stores track‑related datasets used by the simulator and analysis
modules. Track data defines the physical layout of a circuit and provides
the geometric information required for lap simulation, speed estimation,
and visualization.

## Purpose

Track datasets typically include:
- Track centerline coordinates  
- Radius map (curvature vs distance)  
- Elevation profile  
- Sector definitions  
- Corner names and metadata  

These files allow the simulator to:
- Compute optimal speed profiles  
- Estimate braking and acceleration zones  
- Visualize track geometry  
- Compare laps across different tracks  

## Expected Formats

Track files may be stored in:

### ✔ CSV  
Simple and easy to parse.  
Example columns:
s, x, y, z, radius, sector

### ✔ JSON  
Useful for structured metadata (corner names, sectors, flags).

### ✔ YAML  
Readable format for track configuration files.

### ✔ GPX / KML  
For GPS‑based track maps.

## Notes

- Keep raw GPS data separate from processed radius maps.  
- Large or high‑resolution track maps should be added to `.gitignore`.  
- Demo tracks for tutorials should go in `data/samples/`.
