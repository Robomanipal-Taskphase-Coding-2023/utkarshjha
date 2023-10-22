def compress_string(s):
    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed += f"({count}, {s[i - 1]})"
            else:
                compressed += s[i - 1]
            count = 1

    if count > 1:
        compressed += f"({count}, {s[-1]})"
    else:
        compressed += s[-1]

    return compressed