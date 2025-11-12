def approximate_pi(n_terms):
    pi_over_4_sum = 0.0

    for k in range(n_terms):
        term = ((-1)**k) / (2 * k + 1)
        pi_over_4_sum += term

pi_approximation = 4 * pi_over_4_sum

return pi_approximation
