def is_prime_list(numbers):
    if not numbers:
        return False 
    results = []
    for num in numbers:
        if num < 2:
            results.append(False)
            continue  
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        results.append(is_prime)
    return all(results) if isinstance(results, list) and results else False