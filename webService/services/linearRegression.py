def simpleLinearRegression(data):
    # Extract x and y values
    x_vals = [point[0] for point in data]
    y_vals = [point[1] for point in data]

    n = len(data)

    # Compute means
    x_mean = sum(x_vals) / n
    y_mean = sum(y_vals) / n

    # Compute coefficients
    numerator = sum((x_vals[i] - x_mean) * (y_vals[i] - y_mean) for i in range(n))
    denominator = sum((x_vals[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        raise ValueError("All x values are the same. Cannot perform linear regression.")

    a = numerator / denominator  # slope
    b = y_mean - a * x_mean  # intercept

    return [a, b]

def simpleLinearPredict(x_intercept, y_slope, x_values):
    a = x_intercept
    b = y_slope

    # Return predicted y values
    y_estimates = [a * x + b for x in x_values]

    return y_estimates
