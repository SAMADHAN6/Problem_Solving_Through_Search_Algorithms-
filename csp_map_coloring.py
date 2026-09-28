import time

# CONSTRAINT SATISFACTION PROBLEM (CSP)
# Simple Map Coloring Example

regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']


def is_valid(region, color, assignment):
    for neighbour in neighbors[region]:
        if neighbour in assignment and assignment[neighbour] == color:
            return False

    return True


def solve_csp(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:

        if is_valid(region, color, assignment):

            assignment[region] = color

            result = solve_csp(assignment)

            if result:
                return result

            del assignment[region]

    return None


# RUN CSP AND CALCULATE EXECUTION TIME

start = time.time()

solution = solve_csp({})

execution_time = time.time() - start

print("----- CSP MAP COLORING -----")

if solution:
    print("Solution:")
    for region, color in solution.items():
        print(region, "=", color)
else:
    print("No solution found")

print("Execution time:", execution_time, "seconds")
