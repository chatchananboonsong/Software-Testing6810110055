def funnyString(s):
    n = len(s)
    for i in range(1, n):
        left_diff = abs(ord(s[i]) - ord(s[i-1]))
        right_diff = abs(ord(s[n-i-1]) - ord(s[n-i]))
        if left_diff != right_diff:
            return "Not Funny"
    return "Funny"