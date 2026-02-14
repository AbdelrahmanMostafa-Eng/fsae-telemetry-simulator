# Modeling Assumptions
Key simplifications used in the FSAE Telemetry Simulator.

The goal of this simulator is to provide realistic‑looking telemetry data without requiring a full physics engine.  
To achieve this, several assumptions and simplifications are made.

---

## 1. Track & Environment
- Track length is constant for all laps.
- No elevation changes, weather effects, or temperature variation.
- Grip level is assumed constant except for tire wear.
- No traffic, overtakes, or yellow flags.

---

## 2. Speed Model
- Driver speed varies around a target value with Gaussian noise.
- No aerodynamic drag model is applied.
- No throttle/brake simulation — speed is treated as an average per lap.
- Maximum speed is capped and does not depend on fuel load or tire wear.

---

## 3. Fuel Model
- Fuel burn rate is constant per lap.
- Fuel mass affects lap time linearly (lighter car = slightly faster).
- No fuel mixture modes or engine maps.
- Fuel density is constant.

---

## 4. Tire Wear Model
- Tire wear increases linearly per lap.
- Wear rate may scale with speed but not with temperature or load.
- No tire compound differences (soft/medium/hard).
- No tire degradation recovery (cooling laps).

---

## 5. Lap Time Model
- Lap time is based on average speed, fuel load, and tire wear.
- No sector‑by‑sector simulation.
- No dynamic events (lockups, mistakes, traffic).
- No aerodynamic or mechanical grip modeling.

---

## 6. Pit Stops
- Pit stop time is fixed.
- No variation for tire changes, refueling, or driver errors.
- No pit entry/exit time loss modeled.

---

## 7. Randomness & Noise
- Random variation is applied to speed and lap time to simulate driver inconsistency.
- Noise is Gaussian and independent per lap.
- No correlation between laps (e.g., momentum, confidence, overheating).

---

## 8. Stint Comparison
- Stints are compared only by average lap time.
- No strategy modeling (undercut, overcut, tire offset).
- No degradation curves or fuel‑corrected lap times.

---

## Purpose of These Assumptions
These simplifications allow the simulator to:
- Generate realistic‑looking telemetry quickly  
- Remain easy to understand and modify  
- Serve as a teaching, testing, or visualization tool  

As the project grows, these assumptions can be replaced with more advanced physics or data‑driven models.
