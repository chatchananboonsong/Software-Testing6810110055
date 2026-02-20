def staircase(n, display):
    if not (0 < n <= 30):
        return ""
    
    result = ""
    for i in range(1, n + 1):
        line = " " * (n - i) + display * i
        result += line + ("\n" if i < n else "")
    return result