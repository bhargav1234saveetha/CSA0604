def word_break(text, dictionary):
    """
    Returns whether text can be segmented and one valid segmentation.
    dp[i] means text[:i] can be segmented.
    """
    n = len(text)
    words = set(dictionary)
    dp = [False] * (n + 1)
    previous = [-1] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and text[j:i] in words:
                dp[i] = True
                previous[i] = j
                break

    if not dp[n]:
        return False, [], dp

    result = []
    index = n
    while index > 0:
        start = previous[index]
        result.append(text[start:index])
        index = start

    result.reverse()
    return True, result, dp


def run():
    text = "applepie"
    dictionary = {"apple", "pie", "app", "le"}
    possible, parts, states = word_break(text, dictionary)
    print("Text:", text)
    print("Dictionary:", dictionary)
    print("Can be segmented:", possible)
    print("Segmentation:", parts)
    print("DP states:", states)

    print("\nFaulty-algorithm counterexample:")
    bad_text, bad_dictionary = "ab", {"b"}
    print("Text:", bad_text, "Dictionary:", bad_dictionary)
    print("Correct result:", word_break(bad_text, bad_dictionary)[:2])

    print("\nRegression test:")
    print(word_break("cat", {"cat"})[:2])
