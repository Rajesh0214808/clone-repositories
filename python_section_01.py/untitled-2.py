def group_strings_by_length(strings):
    result = {}
    for string in strings:
        length = len(string)
        if length not in result:
            result[length] = []
        result[length].append(string)
    return dict(sorted(result.items()))  # Sort the dictionary by key

# Example usage:
print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group_strings_by_length(["one", "two", "three", "four"]))
