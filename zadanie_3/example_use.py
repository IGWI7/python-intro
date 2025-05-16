from my_awesome_lib.math_tools import calculate_mean, solve_quadratic

# Przykład 1: obliczanie średniej
numbers = [10, 20, 30, 40]
mean = calculate_mean(numbers)
print(f"Średnia liczb {numbers} to {mean}")

# Przykład 2: rozwiązywanie równania kwadratowego
a, b, c = 1, -3, 2
roots = solve_quadratic(a, b, c)
print(f"Pierwiastki równania {a}x² + {b}x + {c} = 0 to: {roots}")