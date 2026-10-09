# PROJECT REPORT
## Simulation of Projectile Motion with Air Resistance

**Submitted by:** Your Name  
**Roll Number:** Your Roll Number  
**Department:** Your Department  
**Institution:** Your College/University  
**Academic Session:** 20__–20__

---

## Abstract
This project develops a computational model to study projectile motion under gravity and air resistance. A Python program uses NumPy for numerical calculations and Matplotlib to generate graphs. The ideal trajectory is compared with a trajectory affected by linear air resistance. The program calculates horizontal range, maximum height, and total flight time. It also examines how launch angle changes the horizontal range. The simulation demonstrates why a real projectile generally follows a different path from the ideal parabolic trajectory.

## 1. Introduction
Projectile motion is the motion of an object launched into the air and then moving under external forces. In an ideal model, only gravity is considered. In real situations, air exerts a resistive force opposite to the direction of motion. This force reduces the projectile's speed and changes its trajectory. Computer simulation allows us to explore these effects by solving the equations of motion step by step.

## 2. Objectives
1. Simulate projectile motion using Python.
2. Compare trajectories with and without air resistance.
3. Calculate horizontal range, maximum height, and flight time.
4. Study the relationship between launch angle and horizontal range.
5. Use numerical methods to approximate the equations of motion.

## 3. Software and Tools
- Python: main programming language
- NumPy: arrays and numerical calculations
- Matplotlib: graphs and visual comparison
- Numerical method: explicit Euler integration

## 4. Theory
Let the initial speed be u and launch angle be θ. The initial velocity components are:
- vx(0) = u cos θ
- vy(0) = u sin θ

The acceleration due to gravity is g = 9.81 m/s².

### 4.1 Ideal projectile
When air resistance is ignored:
- ax = 0
- ay = -g

For a projectile launched and landing at the same height, the theoretical flight time is T = 2u sin θ / g, the maximum height is H = u² sin² θ / (2g), and the horizontal range is R = u² sin(2θ) / g.

### 4.2 Linear air resistance
This project uses a simplified linear drag law:
- Fdx = -k vx
- Fdy = -k vy

By Newton's second law:
- ax = -(k/m) vx
- ay = -g - (k/m) vy

Here m is projectile mass and k is the linear drag coefficient. The minus signs show that drag acts opposite to velocity.

### 4.3 Euler numerical method
For a small time interval Δt:
- vx(next) = vx + ax Δt
- vy(next) = vy + ay Δt
- x(next) = x + vx Δt
- y(next) = y + vy Δt

The calculation repeats until the projectile reaches ground level. Euler's method is easy to understand but introduces numerical error, so the time step should be sufficiently small.

## 5. Methodology
1. Set initial speed, launch angle, mass, drag coefficient, and time step.
2. Split the initial speed into horizontal and vertical components.
3. Calculate acceleration from gravity and, when enabled, drag.
4. Update velocity and position at each time step.
5. Stop the simulation at ground impact.
6. Repeat the calculation without drag for comparison.
7. Plot the trajectories, speed over time, and range versus launch angle.
8. Print the calculated range, flight time, and maximum height.

## 6. Implementation
The main program is contained in `main.py`. The function `simulate_projectile()` carries out the numerical simulation and returns arrays for time, position, and velocity. The function `make_plots()` generates three graphs:
- `trajectory_comparison.png`
- `speed_comparison.png`
- `range_vs_angle.png`

## 7. Results and Discussion
Run `python main.py` to generate the numerical results and figures. With the same initial speed and angle, the ideal model generally predicts a longer range than the model with drag. Drag removes mechanical energy, reduces speed, and makes the path non-parabolic. The launch angle that produces the greatest range in the drag model may differ from 45 degrees. Exact values depend on the chosen mass, drag coefficient, initial speed, and time step.

**Insert your program's actual output and generated graphs here after running the code.** Do not report example values as measured results.

## 8. Applications
- Understanding basic mechanics and projectile trajectories
- Introductory sports physics
- Educational simulations
- Preliminary modelling in engineering and computational physics

## 9. Limitations
1. Linear drag is a simplified model; real aerodynamic drag often depends approximately on speed squared.
2. Wind and air-density variation are ignored.
3. Spin and lift forces are not modelled.
4. Euler integration is approximate.
5. The selected drag coefficient is illustrative and should not be treated as a measured value for a real object.

## 10. Future Scope
- Add quadratic drag: Fd = -(1/2) ρ Cd A |v| v.
- Add a user interface with sliders for speed and angle.
- Compare Euler integration with the Runge–Kutta method.
- Include wind, spin, and different projectile shapes.
- Export simulation results to CSV.

## 11. Conclusion
The project demonstrates how numerical simulation can be used to investigate projectile motion. Comparing ideal motion with a model that includes air resistance shows that drag changes the projectile's speed, height, flight time, and range. Python, NumPy, and Matplotlib provide a simple and effective environment for modelling the system and visualizing its behaviour.

## References
1. Halliday, Resnick and Walker, *Fundamentals of Physics*, sections on projectile motion and Newton's laws.
2. NumPy documentation: https://numpy.org/doc/
3. Matplotlib documentation: https://matplotlib.org/stable/
4. Python documentation: https://docs.python.org/3/
