from itertools import combinations

def alternate(s):
    max_len = 0
    unique_chars = list(set(s))
    for char1, char2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == char1 or c == char2]
        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i+1]:
                is_valid = False
                break
        if is_valid:
            max_len = max(max_len, len(filtered))
            
    return max_len