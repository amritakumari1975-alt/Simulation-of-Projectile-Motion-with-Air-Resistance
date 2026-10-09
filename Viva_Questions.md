# Viva Questions and Answers

1. **What is projectile motion?**  
   It is the motion of an object launched into the air and moving under forces such as gravity and air resistance.

2. **What is the objective of your project?**  
   To simulate projectile motion and compare ideal motion with motion affected by air resistance.

3. **Why did you use Python?**  
   Python is readable and has scientific libraries such as NumPy and Matplotlib.

4. **What is NumPy used for?**  
   It provides numerical operations and arrays for storing simulation data.

5. **What is Matplotlib used for?**  
   It creates graphs of the trajectory, speed, and range.

6. **What is air resistance?**  
   It is a force from air that opposes an object's motion.

7. **What drag model did you use?**  
   A linear drag model, where drag force is proportional to velocity: Fd = -k v.

8. **Is linear drag always realistic?**  
   No. At many ordinary speeds, quadratic drag is more appropriate. Linear drag is a simplified model.

9. **What is Euler's method?**  
   It is a numerical method that estimates the next state using the current derivative and a small time step.

10. **What does the time step mean?**  
    It is the small time interval between successive numerical updates.

11. **What happens when the time step becomes smaller?**  
    The approximation often improves, but the program needs more calculations.

12. **What is horizontal range?**  
    The horizontal distance travelled before the projectile returns to the ground.

13. **What is maximum height?**  
    The highest vertical position reached during the flight.

14. **Why is the ideal trajectory parabolic?**  
    With constant downward acceleration and no horizontal acceleration, horizontal position changes linearly with time while vertical position changes quadratically.

15. **Why does drag change the trajectory?**  
    Drag reduces velocity, so the projectile usually travels a shorter distance and follows a different path.

16. **Why might the best launch angle be below 45 degrees with drag?**  
    A higher angle increases time in the air, allowing drag to act for longer. The exact best angle depends on the model and parameters.

17. **What are the limitations of your project?**  
    It ignores wind, spin, lift, and changing air density, and uses simplified linear drag and Euler integration.

18. **How could you improve the project?**  
    Use quadratic drag, a Runge–Kutta solver, wind effects, and an interactive interface.

19. **What is Newton's second law?**  
    Net force equals mass multiplied by acceleration: F = ma.

20. **What is the conclusion?**  
    Air resistance changes projectile motion, and numerical simulation makes those changes visible and measurable.
