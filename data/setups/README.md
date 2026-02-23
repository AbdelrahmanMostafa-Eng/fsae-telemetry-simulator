# Car Setup Data

This folder stores car setup configuration files used by the simulator,
aerodynamic models, and analysis tools. These files define the mechanical
and aerodynamic parameters of the vehicle for a given session or simulation.

## Purpose

Setup files typically include:
- Aerodynamic parameters (Cd, Cl, wing angles)
- Suspension settings (spring rates, damping, ARBs)
- Tire pressures and compounds
- Gear ratios
- Weight distribution
- Ride heights

These configurations allow the simulator to:
- Compute drag and downforce
- Estimate acceleration and braking performance
- Compare different setups
- Reproduce simulation scenarios

## Expected Formats

Setup files may be stored in:

### ✔ JSON  
Clear structure, ideal for hierarchical parameters.

### ✔ YAML  
Human‑readable and commonly used for configuration files.

### ✔ CSV  
Useful for simple key‑value setups.

## Notes

- Keep real setups separate from demo setups.
- Large collections of setups should be versioned carefully.
- Example setups for tutorials should go in `data/samples/`.
