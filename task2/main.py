from integrals import monte_carlo_integral, f_integral, f, scipyquad_integral
from visualize import visualize

# bounds
a, b = 0, 2

# points
N = 1000000




# integrated
integral_analytical = f_integral(a, b)

integral_monte_carlo = monte_carlo_integral(a, b, f, N)

result, error = scipyquad_integral(f, a, b)



print("Integrated manually:", integral_analytical)
print("Monte-Carlo method:", integral_monte_carlo)
print(f"Scipy quad: {result}; error: {error}")


print("\nMC and quad delta:", abs(integral_monte_carlo - result))
print("MC and manual delta:", abs(integral_monte_carlo - integral_analytical))


visualize(f, a, b)