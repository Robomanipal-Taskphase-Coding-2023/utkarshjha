import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())

distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the two points is: {distance}")