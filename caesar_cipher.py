def caesarCipher(s, k):
    result = []
    shift = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
            
    return "".join(result)