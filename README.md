# 🏎️ FSAE Telemetry Simulator

A modular Python project for simulating, analyzing, and visualizing Formula SAE (FSAE) telemetry data — including lap times, fuel usage, tire wear, speed traces, and race strategy metrics. Built to demonstrate motorsport‑grade data engineering, simulation, and visualization workflows.

---

## 📦 Features

### 🧪 Simulation
- Synthetic lap and session generation  
- Speed, acceleration, throttle/brake traces  
- Basic physics‑based modeling (planned extensions)  
- Configurable car setups and track definitions  

### 📊 Analysis
- Pace degradation across stints  
- Pit stop impact on race time  
- Lap‑to‑lap comparison utilities  
- Sector‑based performance breakdown  
- Telemetry smoothing and derivative calculations  

### 📈 Visualization
- Speed vs. distance plots  
- Lap comparison overlays  
- Aero maps (drag vs. downforce)  
- Telemetry overlays (raw vs. smoothed)  
- Matplotlib‑based performance dashboards  

### 📁 Data Layer
Organized under `data/`:
- `telemetry/` — raw & processed telemetry logs  
- `tracks/` — track geometry, radius maps, elevation  
- `setups/` — car setup configurations  
- `samples/` — synthetic demo datasets  

Each folder includes its own README and example formats.

### 🧪 Testing
- Full test suite under `tests/`  
- Silent, fast, Matplotlib‑safe tests  
- Covers simulation, analysis, and visualization modules  

---

## 🎯 Why This Project Matters

- Applies real motorsport telemetry concepts  
- Bridges race engineering theory with practical Python tools  
- Supports FSAE workflows (lap analysis, stint planning, strategy)  
- Demonstrates clean architecture and modular design  
- Strong portfolio value for engineering + data roles  

---

## 🚧 Future Improvements

- Real telemetry integration (CSV logs from FSAE cars)  
- Monte Carlo strategy optimizer  
- GUI for interactive telemetry visualization  
- Advanced driver comparison dashboards  
- More physics‑based simulation models
