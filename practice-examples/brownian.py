"""
This script draws a Brownian bride across the middle of the window, by adding a small random
number (drawn from the Gaussian distribution) to a recursive function that would otherwise
plot a straight line. The command-line argument, known as the Hurst exponent, controls
the smoothness of the curves - the recursive function uses it to compute a factor beta that 
adjusts the variance of the Gaussian distribution.
"""

# Import necessary libraries
import math  # Provides access to basic mathematical functions
import sys  # Access to system-specific parameters and functions
import stddraw  # Custom library for basic drawing utilities
import stdrandom  # Custom library for generating random numbers

# Define the curve function for drawing the Brownian bridge
def curve(x0, y0, x1, y1, var, beta, n=7):
    # Base case: if recursion depth n reaches 0, draw a line and return
    if n == 0:
        stddraw.line(x0, y0, x1, y1)  # Draws a line from (x0, y0) to (x1, y1)
        return
    
    # Calculate midpoint coordinates of the line segment
    xm = (x0 + x1) / 2.0  # Midpoint x-coordinate
    ym = (y0 + y1) / 2.0  # Midpoint y-coordinate, corrected to be (y0 + y1) / 2.0 for actual midpoint
    
    # Generate a random deviation for the y-coordinate of the midpoint
    delta = stdrandom.gaussian(0.0, math.sqrt(var))  # Random deviation from a Gaussian distribution
    
    # Recursive calls to draw the two halves of the curve with added randomness
    curve(x0, y0, xm, ym + delta, var / beta, beta, n - 1)  # First half, with adjusted variance and midpoint
    curve(xm, ym + delta, x1, y1, var / beta, beta, n - 1)  # Second half, with the same adjustments

# Read the Hurst exponent from command-line arguments, controlling curve smoothness
hurstExponent = float(sys.argv[1])

# Set up drawing parameters
stddraw.setPenRadius(0.0)  # Set the pen radius to 0 for fine lines

# Calculate the beta factor from the Hurst exponent, affecting curve variance
beta = 2.0 ** (2.0 * hurstExponent)  # Variance adjustment factor

# Draw the curve across the middle of the window with initial parameters
curve(0.0, 0.5, 1.0, 0.5, 0.01, beta)  # Starting points, variance, beta

# Display the drawing
stddraw.show()  # Render the completed drawing to the screen
