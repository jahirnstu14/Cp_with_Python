from math import sqrt, pi

def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def parameter(points):
    total_length = 0.0
    for i in range(len(points)):
        total_length += distance(points[i], points[(i + 1) % len(points)])
    return total_length

N, R = map(int, input("Enter nails number and radius of each nails with spaces: ").split())

nails = []
for i in range(N):
    x, y = map(float, input().split()) 
    nails.append((x, y))

convex_parameter_length = parameter(nails)

overall_length = convex_parameter_length + 2 * pi * R

print(f"The overall length of the rope is {overall_length:.2f}")

# for taking input as list 

# groubs = list(map(int,input().split()))
# print(*groubs)
