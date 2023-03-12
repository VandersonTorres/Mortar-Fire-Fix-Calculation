# Mortar-Shot-Fix-Calculation

This application developed with Python, works to automatically fix mortar grenade launches that suffered any variation, both in direction and range. With an expertise acquired in my last occupation in brazilian army in a command position, i felt this need on the battlefield, and I was able to initialize this prototype.

This is a Object-Oriented code that uses a general class ‘mortar’ and its methods to confirm if there were variations, and fix it fast and safe according to user inputs.

Methods “calculate_direction” and “calculate_range”, contain the inteligence to fix the next launch, and got all exceptions treated to avoid unexpected errors.

The result generates a series of actions to be performed by the shooting team.

Finally, the main method “correct_launch” calls and execute the others methods according to user needs during application execution.
