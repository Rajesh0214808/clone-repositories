from itertools import permutations

def unique_permutations(lst):
    return [list(perm) for perm in set(permutations(lst))]

# Example usage:
print(unique_permutations([1, 1, 2]))

