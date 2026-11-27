def word_wrap(words, width):
    if width <= 0 or any(len(w) > width for w in words):
        raise ValueError("Invalid width or a word is longer than width")
    n = len(words)
    dp = [float("inf")] * (n + 1)
    choice = [-1] * n
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        length = 0
        for j in range(i, n):
            length += len(words[j]) + (1 if j > i else 0)
            if length > width:
                break
            unused = width - length
            penalty = 0 if j == n - 1 else unused ** 2
            if penalty + dp[j + 1] < dp[i]:
                dp[i], choice[i] = penalty + dp[j + 1], j
    lines, i = [], 0
    while i < n:
        j = choice[i]
        group = words[i:j + 1]
        used = sum(map(len, group)) + len(group) - 1
        unused = width - used
        penalty = 0 if j == n - 1 else unused ** 2
        lines.append((" ".join(group), unused, penalty))
        i = j + 1
    return dp[0], lines, dp

def run():
    words = ["Dynamic", "programming", "helps", "optimise", "document", "layout"]
    for width in (16, 20, 24):
        cost, lines, states = word_wrap(words, width)
        print("Width:", width, "Minimum penalty:", cost)
        for line, unused, penalty in lines:
            print(line, "| unused:", unused, "| penalty:", penalty)
        print("DP states:", states)
    print("Boundary:", word_wrap(["ALGORITHM"], 9))
    try:
        word_wrap(["ALGORITHM"], 5)
    except ValueError as e:
        print("Expected invalid-input test:", e)
