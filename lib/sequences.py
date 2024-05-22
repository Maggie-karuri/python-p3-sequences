def print_fibonacci(length):
    if length == 0:
        print ([])
    else:
        fibonacci_series = [0]
        if length > 1:
            fibonacci_series.append(1)
        while len(fibonacci_series) < length:
            fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
        print (fibonacci_series)
