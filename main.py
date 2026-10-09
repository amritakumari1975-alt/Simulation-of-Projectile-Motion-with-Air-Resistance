"""
Simulation of Projectile Motion with Air Resistance
Author: Your Name
Description:
Compare ideal projectile motion with motion under linear air resistance.
Dependencies: numpy, matplotlib
Run: python main.py
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

G = 9.81  # gravitational acceleration (m/s^2)


def simulate_projectile(speed, angle_deg, mass=0.145, drag_k=0.02,
                        dt=0.001, include_drag=True, max_time=30.0):
    """Simulate a projectile using explicit Euler integration.

    Linear drag model: F_drag = -k * velocity.
    Returns arrays for time, x, y, vx, vy. Simulation stops at ground impact.
    """
    angle = np.radians(angle_deg)
    vx = speed * np.cos(angle)
    vy = speed * np.sin(angle)
    x, y, t = 0.0, 0.0, 0.0

    times, xs, ys, vxs, vys = [t], [x], [y], [vx], [vy]
    while t < max_time:
        ax = -(drag_k / mass) * vx if include_drag else 0.0
        ay = -G - (drag_k / mass) * vy if include_drag else -G

        # Explicit Euler update
        vx_new = vx + ax * dt
        vy_new = vy + ay * dt
        x_new = x + vx * dt
        y_new = y + vy * dt
        t_new = t + dt

        # Interpolate final segment to y=0 for a cleaner landing point
        if y_new < 0 and t_new > dt:
            frac = y / (y - y_new) if y != y_new else 0.0
            x_land = x + frac * (x_new - x)
            t_land = t + frac * dt
            times.append(t_land)
            xs.append(x_land)
            ys.append(0.0)
            vxs.append(vx + frac * (vx_new - vx))
            vys.append(vy + frac * (vy_new - vy))
            break

        t, x, y, vx, vy = t_new, x_new, y_new, vx_new, vy_new
        times.append(t)
        xs.append(x)
        ys.append(y)
        vxs.append(vx)
        vys.append(vy)
        if y == 0 and t > 0:
            break

    return {
        "time": np.array(times), "x": np.array(xs), "y": np.array(ys),
        "vx": np.array(vxs), "vy": np.array(vys),
        "range": float(xs[-1]), "flight_time": float(times[-1]),
        "max_height": float(max(ys))
    }


def make_plots(ideal, drag, speed, angle, drag_k):
    """Create trajectory and speed plots and save them to outputs/."""
    out = Path("outputs")
    out.mkdir(exist_ok=True)

    plt.figure(figsize=(9, 5.5))
    plt.plot(ideal["x"], ideal["y"], label="Ideal (no air resistance)", linewidth=2)
    plt.plot(drag["x"], drag["y"], label=f"With linear drag (k={drag_k:g} kg/s)", linewidth=2)
    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Height (m)")
    plt.title(f"Projectile Trajectory: speed={speed:g} m/s, angle={angle:g}°")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "trajectory_comparison.png", dpi=160)
    plt.close()

    ideal_speed = np.hypot(ideal["vx"], ideal["vy"])
    drag_speed = np.hypot(drag["vx"], drag["vy"])
    plt.figure(figsize=(9, 5.5))
    plt.plot(ideal["time"], ideal_speed, label="Ideal", linewidth=2)
    plt.plot(drag["time"], drag_speed, label="With linear drag", linewidth=2)
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.title("Speed vs Time")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "speed_comparison.png", dpi=160)
    plt.close()

    # Compare the range for different launch angles
    angles = np.arange(10, 81, 5)
    ideal_ranges, drag_ranges = [], []
    for a in angles:
        ideal_a = simulate_projectile(speed, a, include_drag=False)
        drag_a = simulate_projectile(speed, a, drag_k=drag_k, include_drag=True)
        ideal_ranges.append(ideal_a["range"])
        drag_ranges.append(drag_a["range"])

    plt.figure(figsize=(9, 5.5))
    plt.plot(angles, ideal_ranges, "o-", label="Ideal", linewidth=2)
    plt.plot(angles, drag_ranges, "s-", label="With linear drag", linewidth=2)
    plt.xlabel("Launch angle (degrees)")
    plt.ylabel("Horizontal range (m)")
    plt.title("Effect of Launch Angle on Range")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "range_vs_angle.png", dpi=160)
    plt.close()


def main():
    print("=" * 58)
    print("SIMULATION OF PROJECTILE MOTION WITH AIR RESISTANCE")
    print("=" * 58)

    # Default values can be changed for experiments
    speed = 30.0       # m/s
    angle = 45.0       # degrees
    mass = 0.145       # kg (approximate baseball mass)
    drag_k = 0.02      # kg/s (illustrative linear-drag coefficient)
    dt = 0.001         # s

    ideal = simulate_projectile(speed, angle, mass, drag_k, dt, False)
    drag = simulate_projectile(speed, angle, mass, drag_k, dt, True)

    print(f"\nInput parameters")
    print(f"Initial speed       : {speed:.2f} m/s")
    print(f"Launch angle        : {angle:.2f} degrees")
    print(f"Projectile mass     : {mass:.3f} kg")
    print(f"Linear drag k       : {drag_k:.4f} kg/s")
    print(f"Time step           : {dt:.4f} s")

    print("\nResults")
    print("-" * 58)
    print(f"{'Measurement':<24}{'Ideal':>15}{'With drag':>17}")
    print("-" * 58)
    print(f"{'Horizontal range (m)':<24}{ideal['range']:>15.3f}{drag['range']:>17.3f}")
    print(f"{'Flight time (s)':<24}{ideal['flight_time']:>15.3f}{drag['flight_time']:>17.3f}")
    print(f"{'Maximum height (m)':<24}{ideal['max_height']:>15.3f}{drag['max_height']:>17.3f}")
    print("-" * 58)

    make_plots(ideal, drag, speed, angle, drag_k)
    print("\nPlots saved in the 'outputs' folder:")
    print("  - trajectory_comparison.png")
    print("  - speed_comparison.png")
    print("  - range_vs_angle.png")


if __name__ == "__main__":
    main()
