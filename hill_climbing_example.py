import time

# HILL CLIMBING EXAMPLE
# Objective function:
# f(x) = -(x - 5)^2 + 25
#
# The maximum value is at x = 5.

def objective(x):
    return -(x - 5) ** 2 + 25


def hill_climbing(start):
    current = start
    steps = 0

    while True:
        steps += 1

        
        neighbours = [current - 1, current + 1]

        # Select the neighbor with the highest objective value
        best = max(neighbours, key=objective)

        # Stop if no neighbor is better
        if objective(best) <= objective(current):
            break

        current = best

    return current, objective(current), steps



#time cal kr 
start = time.time()

solution, value, steps = hill_climbing(2)

execution_time = time.time() - start

print("----- HILL CLIMBING -----")
print("Starting value:", 2)
print("Best value of x:", solution)
print("Maximum objective value:", value)
print("Steps:", steps)
print("Execution time:", execution_time, "seconds")
