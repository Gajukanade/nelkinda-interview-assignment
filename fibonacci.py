
def fibonacci(n):
   
    if n < 0:
        raise ValueError("Invalid input: Please enter a non-negative number")
    elif n == 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("Fibonacci sequence:", fibonacci(5))
