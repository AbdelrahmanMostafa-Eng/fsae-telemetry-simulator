# Telemetry Formulas
Mathematical foundations used in the FSAE Telemetry Simulator.

---

## 1. Lap Time Model
Lap time is influenced by speed, tire wear, and fuel load.

### Base Formula
$$
\text{Lap Time} = \frac{\text{Lap Length}}{\text{Average Speed}}
$$

### Adjusted for Tire Wear
$$
\text{Lap Time}_{\text{wear}} = \text{Lap Time} \times (1 + k_{\text{wear}} \cdot \text{Tire Wear})
$$

### Adjusted for Fuel Load
$$
\text{Lap Time}_{\text{fuel}} = \text{Lap Time}_{\text{wear}} - k_{\text{fuel}} \cdot \text{Fuel Burned}
$$

---

## 2. Fuel Consumption

### Base Fuel Burn
$$
\text{Fuel Used} = \text{Fuel Rate} \times \text{Lap Time}
$$

### Fuel Mass
$$
\text{Fuel Mass} = \text{Fuel Volume} \times \rho_{\text{fuel}}
$$

---

## 3. Tire Wear Model

### Linear Wear Model
$$
\text{Tire Wear}_{n} = \text{Tire Wear}_{n-1} + k_{\text{wear}}
$$

### Speed‑Adjusted Wear
$$
k_{\text{wear}} = k_0 \times \left(1 + \frac{v}{v_{\text{max}}}\right)
$$

---

## 4. Speed Model
$$
v = v_{\text{target}} + \mathcal{N}(0, \sigma)
$$

---

## 5. Stint Comparison
$$
\bar{t} = \frac{1}{N} \sum_{i=1}^{N} t_i
$$

Lower average lap time → faster stint.

---

## 6. Pit Stop Time
$$
T_{\text{total}} = \sum \text{Lap Times} + N_{\text{stops}} \cdot T_{\text{pit}}
$$

---

These formulas define the core behavior of the telemetry simulator and can be expanded as the project grows.
