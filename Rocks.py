import fractal
import random

def generate_fractal_rock():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    rock = f.generate()
    # Return the fractal shape
    return rock

# Generate 10 fractal rocks
for i in range(10):
    rock = generate_fractal_rock()
    print(rock)
