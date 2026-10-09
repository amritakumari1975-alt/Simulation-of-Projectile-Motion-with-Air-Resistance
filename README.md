# Simulation of Projectile Motion with Air Resistance

## Overview
A Python project that numerically simulates projectile motion and compares:
1. Ideal motion (gravity only).
2. Motion with linear air resistance, where drag force is proportional to velocity.

## Requirements
- Python 3.9 or newer
- NumPy
- Matplotlib

Install dependencies:
```bash
python -m pip install numpy matplotlib
```

## Run
Open a terminal in this folder and run:
```bash
python main.py
```
On Windows, if `python` is not recognized, try:
```bash
py main.py
```

The program prints a results table and saves three plots in `outputs/`.

## Parameters to experiment with
Open `main.py` and change:
- `speed` (m/s): initial launch speed
- `angle` (degrees): launch angle
- `mass` (kg): projectile mass
- `drag_k` (kg/s): linear drag coefficient
- `dt` (s): numerical time step

For a more accurate numerical result, use a smaller `dt`, while remembering that Euler integration is an approximation.

## Model
With no drag:
- ax = 0
- ay = -g

With linear drag F_drag = -k v:
- ax = -(k/m) vx
- ay = -g - (k/m) vy

The simulation uses explicit Euler integration and stops when the projectile returns to ground level.

## Limitations
- Linear drag is a simplified approximation. Many real projectiles are better modelled with quadratic drag, proportional to speed squared.
- Wind, spin, lift, changing air density, and altitude are ignored.
- The default drag coefficient is illustrative rather than calibrated to a specific projectile.
